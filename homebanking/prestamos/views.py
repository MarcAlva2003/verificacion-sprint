from cgi import print_exception
import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import LoanForm
from .models import prestamos as Prestamos
from datetime import datetime
from Cuentas.models import cuenta as Cuenta
from Clientes.models import clientes

# Create your views here.

@login_required
def prestamos(request):

    prestamos_db = Prestamos.objects.filter(id_cliente__icontains = request.user.id)
    helper = clientes.objects.filter(id__icontains = request.user.id)
    user_client_type = helper[0].tipo_cliente
    loan_form = LoanForm()

    if request.method == "POST":
        loan_form = LoanForm(data=request.POST)
        
        if loan_form.is_valid():
            money_amount = int(request.POST.get('moneyAmount'))
            
            if (user_client_type == 'classic') and (money_amount > 100000):
                print('CLASSIC MAYOR')
                return redirect(reverse('prestamos') + "?amounterror")
            elif (user_client_type == 'gold') and (money_amount > 300000):
                print('GOLD MAYOR')
                return redirect(reverse('prestamos') + "?amounterror")
            elif money_amount > 500000:
                print('BLACK MAYOR')
                return redirect(reverse('prestamos') + "?errorblack")
            else:
                money_amount = float(request.POST.get('moneyAmount'))
                monthsAmount_received = int(request.POST.get('monthsAmount'))
                loanType_received = request.POST.get('loanType')
                id_cliente_received = request.user.id
                prestamo = Prestamos(loan_approved_date=datetime.now(),loan_month = monthsAmount_received,loan_total=money_amount,loanType = loanType_received,id_cliente = id_cliente_received)
                monto_anterior = consultar(id_cliente_received)
                monto_actualizado = monto_anterior + money_amount
                modificar(id_cliente_received,monto_actualizado)
                prestamo.save()

    return render(request,'prestamos/prestamos.html', {'prestamos_db':prestamos_db,'form':loan_form, 'client_type':user_client_type})

def conectar():
    conexion = sqlite3.connect('db.sqlite3')
    cursor = conexion.cursor()
    return conexion, cursor

def consultar(id_cliente):
    conexion,cursor = conectar()
    cursor.execute("SELECT id,account_id,balance,tipo_de_cuenta_id from Cuentas_cuenta")

    for fila in cursor:
        if fila[1] == id_cliente:
            monto = fila[2]
    conexion.close()

    return monto


def modificar(id,nuevo_balance):
    conexion,cursor = conectar()
    sql = "UPDATE Cuentas_cuenta SET balance="+str(nuevo_balance)+" WHERE account_id="+str(id)
    print(sql)
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()
