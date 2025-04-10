from django.http import HttpResponse

def data_page(request):
    return HttpResponse("<h1>Добро пожаловать на страницу Data!</h1>")

def test_page(request):
    return HttpResponse("<h1>Это тестовая страница! Работает!</h1>")