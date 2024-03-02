from django.shortcuts import render

def blog(requets):
  return render(requets, 'blog.html')

def contactanos(requets):
  return render(requets, 'contactanos.html')

def index(requets):
  return render(requets, 'index.html')

def nosotros(requets):
  return render(requets, 'nosotros.html')

def servicios(requets):
  return render(requets, 'servicios.html')