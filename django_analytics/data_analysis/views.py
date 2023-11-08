from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def test(request):
    return HttpResponse("<h1>Тестирование модели</h1>")

def train(request):
    return HttpResponse("<h1>Тренировка модели</h1>")