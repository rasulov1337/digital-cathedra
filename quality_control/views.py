from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import View, DetailView, UpdateView, DeleteView, ListView, CreateView

from quality_control.forms import BugReportForm, FeatureRequestForm
from quality_control.models import BugReport, FeatureRequest


def index(request):
    return render(request, 'quality_control/index.html')


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


def bug_list(request):
    return render(request, 'quality_control/bug_list.html', {'bugreport_list': BugReport.objects.all()})


class BugReportsListView(ListView):
    model = BugReport
    template_name = 'quality_control/bug_list.html'


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object

        return render(request, 'quality_control/bug_detail.html', {'bug': bug})


def feature_list(request):
    return render(request, 'quality_control/feature_list.html',
                  {'featurerequest_list': FeatureRequest.objects.all()})


class FeatureRequestsListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_list.html'


def bug_report_detail(request, bug_id):
    return render(request, 'quality_control/bug_detail.html', {'bug': get_object_or_404(BugReport, pk=bug_id)})


def feature_request_detail(request, feature_id):
    feature_req = get_object_or_404(FeatureRequest, pk=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature_req})


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


class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bugs')


def create_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})


class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:features')


def update_bug_report(request, bug_id):
    project = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs')
    else:
        form = BugReportForm(instance=project)
    return render(request, 'quality_control/bug_report_update.html', {'form': form, 'project': project})


def update_feature_request(request, feature_id):
    project = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features')
    else:
        form = FeatureRequestForm(instance=project)
    return render(request, 'quality_control/feature_request_update.html', {'form': form, 'project': project})


class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_update.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bugs')


class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_update.html'
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:features')


def delete_bug_report(request, bug_id):
    project = get_object_or_404(BugReport, pk=bug_id)
    project.delete()
    return redirect('quality_control:bugs')


def delete_feature_request(request, feature_id):
    task = get_object_or_404(FeatureRequest, pk=feature_id)
    task.delete()
    return redirect('quality_control:features')


class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bugs')
    template_name = 'quality_control/bug_report_confirm_delete.html'


class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:features')
    template_name = 'quality_control/feature_request_confirm_delete.html'
