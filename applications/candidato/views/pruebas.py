from django.shortcuts import render, redirect, get_object_or_404

def pruebas(request):
    
    return render(request, 'candidato/prueba.html')