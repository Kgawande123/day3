from django.http import HttpResponse
from django.shortcuts import render
from .models import Calculator1


# Create your views here.
def cview(request):
    if request.method == "POST":
        num1=request.POST.get("n1")
        num2=request.POST.get("n2")
        choice = request.POST.get("choice")
        print(f"{num1}----{num2}")
        obj=Calculator1(num1=num1,num2=num2)
        obj.save()
        if choice == "addition":
            res = num1 +num2
            return HttpResponse(f"addition is{res}")


    return render(request,"rawform.html",{})