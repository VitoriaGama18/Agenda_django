from django.shortcuts import render

def add_contato(request):
    return render(request,'core/add_contato.html')
