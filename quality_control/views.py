from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import View, DetailView

from quality_control.models import BugReport, FeatureRequest


def index(request):
    bugs_page_url = reverse('quality_control:bugs')
    feature_list_url = reverse('quality_control:features')

    html = (f"<h1>Система контроля качества</h1>"
            f"<a href='{bugs_page_url}'>Список всех багов</a><br>"
            f"<a href='{feature_list_url}'>Запросы на улучшение</a>")
    return HttpResponse(html)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        bugs_page_url = reverse('quality_control:bugs')
        feature_list_url = reverse('quality_control:features')

        html = (f"<h1>Система контроля качества</h1>"
                f"<a href='{bugs_page_url}'>Список всех багов</a><br>"
                f"<a href='{feature_list_url}'>Запросы на улучшение</a>")
        return HttpResponse(html)


def bug_list(request):
    html = '<h1>Список отчетов об ошибках</h1>'
    for i in BugReport.objects.all():
        url = reverse('quality_control:bug_detail', args=[i.id])

        html += f'<li><a href={url}>{i}</a></li>'
    return HttpResponse(html)


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object

        html = (f'<h1>Title: {bug.title}<br>Description: {bug.description}<br>Status: {bug.status}'
                f'<br>Priority: {bug.priority}</h1>')
        return HttpResponse(html)


def feature_list(request):
    html = '<h1>Список запросов на улучшение</h1>'
    for i in FeatureRequest.objects.all():
        url = reverse('quality_control:feature_id_detail', args=[i.id])

        html += f'<li><a href={url}>{i}</a></li>'
    return HttpResponse(html)


# def bug_detail(request, bug_id):
#     html = (f"<h1>Детали бага {bug_id}</h1>")
#     return HttpResponse(html)


# def feature_id_detail(request, feature_id):
#     html = (f"<h1>Детали улучшения {feature_id}</h1>")
#     return HttpResponse(html)


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object

        html = (f'<h1>Title: {feature.title}<br>Description: {feature.description}<br>Status: {feature.status}'
                f'<br>Priority: {feature.priority}<br>Project: {feature.project}<br>Task: {feature.task}</h1>')
        return HttpResponse(html)
