from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, DetailView

from quality_control.forms import BugReportForm, FeatureRequestForm
from quality_control.models import BugReport, FeatureRequest


# def index(request):
#     bugs_page_url = reverse('quality_control:bugs')
#     feature_list_url = reverse('quality_control:features')
#
#     html = (f"<h1>Система контроля качества</h1>"
#             f"<a href='{bugs_page_url}'>Список всех багов</a><br>"
#             f"<a href='{feature_list_url}'>Запросы на улучшение</a>")
#     return HttpResponse(html)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


def bug_list(request):
    return render(request, 'quality_control/bug_list.html', {'bug_reports': BugReport.objects.all()})


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object

        return render(request, 'quality_control/bug_detail.html', {'bug': bug})


def feature_list(request):
    return render(request, 'quality_control/feature_list.html',
                  {'feature_list': FeatureRequest.objects.all()})


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

        return render(request, 'quality_control/feature_detail.html', {'feature': feature})


def create_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})


def create_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})