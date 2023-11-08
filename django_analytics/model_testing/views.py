from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("<h1>Тестирование модели</h1>")

def train(request):
    return HttpResponse("<h1>Тренировка модели</h1>")
