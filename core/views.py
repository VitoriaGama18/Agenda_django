from django.shortcuts import render
from core.models import Contato

def add_contato(request):
    if request.method != 'POST':
        return render(request,'core/add_contato.html')
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    telefone = request.POST['telefone']
    email = request.POST['email']
    descricao = request.POST['descricao']
    imagem =request.FILES['imagem']

    if not nome or not sobrenome:
        return render(request, 'core/add_contato.html')
    salvarContato = Contato.objects.create(nome=nome,
                                           sobrenome=sobrenome,
                                           telefone=telefone,
                                           email=email,
                                           descricao=descricao,
                                           imagem=imagem)
    salvarContato.save()
    return render(request, 'core/add_contato.html')

def listar_contato(request):
    contato = Contato.objects.all()
    return  render( request, 'core/listar_contato.html',
                    {'contato':contato})

