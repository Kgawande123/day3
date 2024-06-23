from django.http import HttpResponse
from django.shortcuts import render
from .forms import CalculatorForm
from .models import Calculator

# Create your views here.
def cview(request):
    form = CalculatorForm()
    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data.get("num1")
            num2 = form.cleaned_data.get("num2")
            choice = form.cleaned_data.get("choice")
            obj = Calculator(num1=num1,num2=num2)

            obj.save()
            if choice == "addition":
                res = num1+num2
                return HttpResponse(f"addition is{res}")
            elif choice == "substraction":
                res = num1-num2
                return HttpResponse(f"substaction is{res}")
            elif choice == "multiplication":
                res = num1*num2
                return HttpResponse(f"multiplication is{res}")
            elif choice == "division":
                res = num1/num2
                return HttpResponse(f"division is{res}")
            elif choice == "modulas":
                res = num1%num2
                return HttpResponse(f"modulas is{res}")
            elif choice == "fdivision":
                res = num1//num2
                return HttpResponse(f"fdivision is{res}")
            elif choice == "exponent":
                res = num1**2 or num2**2
                return HttpResponse(f"exponent is{res}")





    return render(request,"form.html",{"form":form})