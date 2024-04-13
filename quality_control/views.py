from django.http import HttpResponse
from django.urls import reverse


def index(request):
    bugs_page_url = reverse('quality_control:bugs')
    feature_list_url = reverse('quality_control:features')

    html = (f"<h1>Система контроля качества</h1>"
            f"<a href='{bugs_page_url}'>Список всех багов</a><br>"
            f"<a href='{feature_list_url}'>Запросы на улучшение</a>")
    return HttpResponse(html)


def bug_list(request):
    return HttpResponse("Cписок отчетов об ошибках")


def feature_list(request):
    return HttpResponse("Список запросов на улучшение")


def bug_detail(request, bug_id):
    html = (f"<h1>Детали бага {bug_id}</h1>")
    return HttpResponse(html)


def feature_id_detail(request, feature_id):
    html = (f"<h1>Детали улучшения {feature_id}</h1>")
    return HttpResponse(html)
