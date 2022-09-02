from django import forms

class LoanForm(forms.Form):
    moneyAmount = forms.IntegerField(label='Cantidad de dinero a pedir', required=True)
    monthsAmount = forms.IntegerField(label='Plazo en meses a pagar', required=True)
    customerSalary = forms.IntegerField(label='Ingreso mensual total', required=True)
    LOAN_TYPE_CHOICES = (
        ('hipotecario', 'Hipotecario'),
        ('prendario', 'Prendario'),
        ('personales', 'Personales'),
        ('con garantia', 'Con garantia'),
        ('sin garantia', 'Sin garantia'),
    
    )
    loanType = forms.ChoiceField(label='Seleccione tipo de prestamo a solititar', choices=LOAN_TYPE_CHOICES)
    termsAndConds = forms.BooleanField(label='Terminos y condiciones', required=True)