from django.shortcuts import render

# Create your views here.
def vista(request):
    return render(request,"index.html")

def chat(request,pk):
    return render(request,"chat.html",context  ={"pk":pk})