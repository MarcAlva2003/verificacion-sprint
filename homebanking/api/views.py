from Clientes.models import clientes
from Cuentas.views import Cuentas
from api.serializers import ClienteSerializer,UserSerializer,SucursalSerializer,Sucursal,BalanceCuentaSerializer, AllDataBalanceCuentaSerializer,MontoPrestamosSucursalSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics, authentication
from django.contrib.auth.models import User
from prestamos.models import prestamos as Prestamo
from prestamos.views import consultar, modificar,conectar,consultar
from Cuentas.models import cuenta as Cuenta
from .serializers import PrestamoSerializer, MontoPrestamosDeClienteSerializer
from tarjetas.models import Tarjetas
from tarjetas.serializer import TarjetaSerializer
from Clientes.models import clientes

from rest_framework import permissions

# Validar que un cliente tenga permiso para ver clientes
class UserViewClientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.has_perm('Clientes.view_clientes')
        )
# Validar que un cliente tenga permiso para ver cuentas
class UserViewCuentasPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.has_perm('Cuentas.view_cuenta')
        )
# Validar que un cliente tenga permiso para ver prestamos
class UserViewPrestamosPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.has_perm('prestamos.view_prestamos')
        )

class UserPostPrestamosPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.has_perm('prestamos.add_prestamos')
        )
class UserDeletePrestamosPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.has_perm('prestamos.delete_prestamos')
        )

# Validar que un cliente tenga permiso para modificar clientes
class UserChangeClientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.has_perm('Clientes.chage_clientes')
        )

# Un cliente autenticado puede consultar sus propios datos
# Nota: si el usuario es admin o empleado (is_staff) va a acceder a todos
# los clientes
class Clients(APIView):
    permission_classes = [UserViewClientPermission]
    def get(self, request):
        if not request.user.is_staff:
            cliente =clientes.objects.filter(id=request.user.customer_id).first()
            serializer = ClienteSerializer(cliente, many = False)
        else:
            cliente =clientes.objects.all()
            serializer = ClienteSerializer(cliente, many = True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# Un cliente autenticado puede obtener el tipo de cuenta y su saldo
# Nota: si el usuario es admin o empleado (is_staff) va a acceder a todas
# las cuentas con todos los datos
class ClientBalance(APIView):
    permission_classes = [UserViewCuentasPermission]
    def get(self, request):
        if not request.user.is_staff:
            cuenta = Cuenta.objects.filter(customer_id=request.user.customer_id)
            serializer = BalanceCuentaSerializer(cuenta, many = True)
        else:
            cuenta = Cuenta.objects.all().order_by('customer_id')
            serializer = AllDataBalanceCuentaSerializer(cuenta, many = True)
        if cuenta:
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.error_messages, status = status.HTTP_404_NOT_FOUND)

# OBTENER MONTO DE PRESTAMOS DE UN CLIENTE
# Un empleado autenticado puede obtener el listado de préstamos otorgados de 
# una sucursal determinada.
class MontoPrestamosDeCliente(APIView):
    permission_classes = [UserViewPrestamosPermission]
    def get(self, request):
        if not request.user.is_staff:
            prestamo = Prestamo.objects.filter(id_cliente=request.user.customer_id)
        else:
            prestamo = Prestamo.objects.all()
        serializer = MontoPrestamosDeClienteSerializer(prestamo, many= True)
        if serializer:
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.error_messages, status = status.HTTP_404_NOT_FOUND)


# OBTENER PRESTAMO DE UNA SUCURSAL
# Un empleado autenticado puede obtener el listado de préstamos otorgados de
# una sucursal determinada.
class MontoPrestamoSucursal(APIView):
    permission_classes = [UserViewPrestamosPermission]
    def get(self, request, sucursal_id):
        prestamo = Prestamo.objects.filter(id_sucursal=sucursal_id)
        serializer = MontoPrestamosSucursalSerializer(prestamo, many = True)
        if request.user.is_staff:
            if prestamo:
                return Response(serializer.data, status= status.HTTP_200_OK)
            return Response(serializer.error_messages, status = status.HTTP_404_NOT_FOUND)
        return Response({"Fail": "Usted no tiene permiso para realizar esta acción."}, status = status.HTTP_403_FORBIDDEN)

# OBTENER TARJETAS ASOCIADAS A UN CLIENTE
# Un empleado autenticado puede obtener el listado de tarjetas de crédito de un 
# cliente determinado
class TarjetasCliente(APIView):
    def get(self, request, customer_id):
        tarjeta = Tarjetas.objects.filter(customer_id=customer_id)
        serializer = TarjetaSerializer(tarjeta, many =  True)
        if request.user.is_staff:
            if tarjeta:
                return Response(serializer.data, status= status.HTTP_200_OK)
            return Response(serializer.error_messages, status = status.HTTP_404_NOT_FOUND)
        return Response({"Fail": "Usted no tiene permiso para realizar esta acción."},status = status.HTTP_403_FORBIDDEN)


# GENERAR UNA SOLICITUD DE PRESTAMO PARA UN CLIENTE
# Un empleado autenticado puede solicitar un préstamo para un cliente, registrado 
# el mismo y acreditando el saldo en su cuenta
class SolicitudPrestamo(APIView):
    permission_classes = [UserPostPrestamosPermission]
    def post(self, request, format=None):
        serializer = PrestamoSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ANULAR SOLICITUD DE PRESTAMO DE CLIENTE
# Un empleado autenticado puede anular un préstamo para un cliente, revirtiendo 
# el monto correspondiente
# Nota: se borra el prestamo con el ID que se pase por URL, y se modifica
# el balance del customer_id al que corresponda ese préstamo
# En caso de que el cliente no esté asociado a ningún usuario, se lanzará un error
# y no se eliminará el préstamo.
# En el caso de que no se encuentre el préstamo, se le avisará al usuario
class RechazarPrestamo(APIView):
    permission_classes = [UserDeletePrestamosPermission]
    def delete(self,request, pk):
        prestamo = Prestamo.objects.filter(pk=pk).first()
        if prestamo:
            monto_descuento = prestamo.loan_total
            clienteId = prestamo.id_cliente
            cuenta = Cuenta.objects.get(customer_id = clienteId)
            if cuenta:
                monto_actual = cuenta.balance
                monto_actualizado = monto_actual - monto_descuento
                cuenta.balance = monto_actualizado
                cuenta.save()
                prestamo.delete()
                serializer = PrestamoSerializer(prestamo)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"Fail": "ERROR FATAL: El prestamo seleccionado no se encuentra asociado a ningún cliente"},status = status.HTTP_403_FORBIDDEN)
        return Response({"Fail": "Prestamo no encontrado"},status = status.HTTP_403_FORBIDDEN)

# MODIFICAR DIRECCION DE UN CLIENTE
# El propio cliente autenticado o un empleado puede modificar las direcciones
# NOTA: Creamos dos views, una para el cliente, el cual solo puede modificar su dirección,
# y otra para el empleado, que al no ser un cliente, debe ingresar el ID del cliente en la URL
class DireccionClienteID(APIView):
    def put(self, request, pk):
        if request.user.is_staff:
            cliente = clientes.objects.filter(pk=pk).first()
            serializer = ClienteSerializer(cliente, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Fail": "Usted no tiene permiso para realizar esta acción."},status = status.HTTP_403_FORBIDDEN)

class EditarDireccionCliente(APIView):
    permission_classes = [UserChangeClientPermission]
    def put(self, request):
        if not request.user.is_staff:
            cliente = clientes.objects.filter(pk=request.user.id).first()
            serializer = ClienteSerializer(cliente, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Fail": "ID De cliente no ingresado."},status = status.HTTP_403_FORBIDDEN)

# LISTADO DE TODAS LAS SUCURSALES
# Un endpoint público que devuelve el listado todas las sucursales con la 
# información correspondiente
class ListaSucursales(APIView):
    def get(self, request):
        sucursales = Sucursal.objects.all().order_by('created_at')
        serializer = SucursalSerializer(sucursales, many=True)
        if sucursales:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status = status.HTTP_404_NOT_FOUND)

                # cuenta = Cuenta.objects.get( id = cliente_id).first()
    # def delete(self,request, pk):
    #     prestamo = Prestamo.objects.filter(pk=pk).first()
    #     if prestamo:
    #         serializer = PrestamoSerializer(prestamo)
    #         # prestamo = Prestamo.objects.get(pk = pk)
    #         cliente_id = prestamo.id_cliente
    #         monto_descuento = prestamo.loan_total
    #         monto_actual = cuenta.balance
    #         monto_actualizado = monto_actual - monto_descuento
    #         cuenta.balance = monto_actualizado
    #         cuenta.save()
    #         prestamo.delete()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(status=status.HTTP_404_NOT_FOUND)



# # BALANCE DE CUENTA DE CLIENTE
# class BalanceDeCuentaDeCliente(APIView):
#     def get(self, request):
#         # usuario = User.objects.filter(pk = request.user.id).first()
#         cuenta = Cuenta.objects.filter (user_email=request.user.email)
#         print(request.user.email)
#         # print(request.user.email)
#         serializer = BalanceCuentaSerializer(cuenta, many = True)
#         if cuenta:
#             return Response(serializer.data, status= status.HTTP_200_OK)
#         return Response(serializer.error_messages, status = status.HTTP_404_NOT_FOUND)

# class ClienteLists(APIView):
    # permission_classes = [permissions.IsAuthenticated]
#     def post(self, request, format=None):
#         serializer = ClienteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=self.request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request): # nuevo
#         cliente = clientes.objects.all().order_by('created_at')
#         serializer = ClienteSerializer(cliente, many=True)
#         if(cliente):
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_401_UNAUTHORIZED)

# class GetClientList(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [authentication.BasicAuthentication]
#     def get(self, request): # nuevo
#         cliente = clientes.objects.all().order_by('created_at')
#         serializer = ClienteSerializer(cliente, many=True)
#         if(cliente):
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_401_UNAUTHORIZED)

# class ClienteDetails(APIView):
#     permission_classes = [UserHasViewPermission]
#     def get(self, request, pk):
#         cliente =clientes.objects.filter(pk=pk).first()
        
#         serializer = ClienteSerializer(cliente)
#         if cliente:
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else: 
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


#     def put(self, request, pk):
#         print("Entrando a la actualizacion")
#         cliente = clientes.objects.filter(pk=pk).first()
#         serializer = ClienteSerializer(cliente, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserList(generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# #clase para manejar una única instancia
# class UserDetail(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class SucursalLists(APIView):
#     def post(self, request, format=None):
#         serializer = SucursalSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def get(self, request): # nuevo
#         sucursales = Sucursal.objects.all().order_by('created_at')
#         serializer = SucursalSerializer(sucursales, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# # una sucursal
# class SucursalDetails(APIView):
#     def get(self, request, pk):
#         sucursal = Sucursal.objects.filter(pk=pk).first()
#         serializer = SucursalSerializer(sucursal)
#         if sucursal:
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
# #una sucursal

# class PrestamoList(APIView):
    
#     def post(self, request, format=None):
#         serializer = PrestamoSerializer(data=request.data) 
#         if serializer.is_valid(): 
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # def consultarSaldo(id):
# #     conexion,cursor = conectar()
# #     cursor.execute("SELECT id,account_id,balance,tipo_de_cuenta_id from Cuentas_cuenta")

# #     for fila in cursor:
# #         if fila[0] == id:
# #             monto = fila[2]

# #     conexion.close()

# #     return monto


# class PrestamoDetails(APIView):

#     def delete(self,request, pk):
#         #borra un prestamo con un id determinado
#         prestamo = Prestamo.objects.filter(pk=pk).first()
#         if prestamo:
#             serializer = PrestamoSerializer(prestamo)
            
#             prestamo = Prestamo.objects.get(pk = pk)
#             cliente_id = prestamo.id_cliente
#             cuenta = Cuenta.objects.get( account_id = cliente_id)
#             monto_descuento = prestamo.loan_total
#             monto_actual = cuenta.balance
#             monto_actualizado = monto_actual - monto_descuento
#             cuenta.balance = monto_actualizado
#             cuenta.save()

#             prestamo.delete()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_404_NOT_FOUND)

# # Tarjetas asociadas a un cliente





# # OBTENER PRESTAMO DE UNA SUCURSAL
# class MontoPrestamoSucursal(APIView):
#     def get(self, request, sucursal_id):
#         prestamo = Prestamo.objects.filter(id_sucursal=sucursal_id)
        
#         serializer = MontoPrestamosSucursalSerializer(prestamo, many = True)
#         if prestamo:
#             return Response(serializer.data, status= status.HTTP_200_OK)
#         return Response(serializer.error_messages, status = status.HTTP_404_NOT_FOUND)