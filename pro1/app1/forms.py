from django import forms

op=[("addition","Addition"),("substraction","Substraction"),("multiplicqation","Multiplication"),("division","Division"),("modulas","Modulas"),("fdivision","Fdivision"),("exponent","Exponent")]


class CalculatorForm(forms.Form):
    num1 = forms.IntegerField(label="Number1",widget=forms.NumberInput(
        attrs={"class":"form_control"}
    ))
    num2 = forms.IntegerField(label="Number2",widget=forms.NumberInput(
        attrs={"class":"form_control"}
    ))
    choice = forms.ChoiceField(choices=op)
