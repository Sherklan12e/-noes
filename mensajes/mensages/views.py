from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def images(request):
    return render(request, 'images.html')
def usuarios(request):
    return render(request, 'usuarios.html')
