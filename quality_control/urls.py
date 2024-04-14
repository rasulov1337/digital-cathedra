from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    # Index
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # Bug Reports
    # FBV
    # path('bugs/', views.bug_list, name='bugs'),
    # path('bugs/new/', views.create_bug_report, name='create_bug_report'),
    # path('bugs/<int:bug_id>', views.bug_report_detail, name='bug_detail'),
    # path('bugs/<int:bug_id>/update/', views.update_bug_report, name='update_bug_report'),
    # path('bugs/<int:bug_id>/delete/', views.delete_bug_report, name='delete_bug_report'),

    # CBV
    path('bugs/', views.BugReportsListView.as_view(), name='bugs'),
    path('bugs/new/', views.BugReportCreateView.as_view(), name='create_bug_report'),
    path('bugs/<int:bug_id>', views.BugDetailView.as_view(), name='bug_detail'),
    path('bugs/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='update_bug_report'),
    path('bugs/<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_bug_report'),

    # Feature Requests
    # FBV
    # path('features/', views.feature_list, name='features'),
    # path('features/new/', views.create_feature_request, name='create_feature_request'),
    # path('features/<int:feature_id>', views.feature_request_detail, name='feature_request_detail'),
    # path('features/<int:feature_id>/update/', views.update_feature_request, name='update_feature_request'),
    # path('features/<int:feature_id>/delete/', views.delete_feature_request, name='delete_feature_request'),

    # CBV
    path('features/', views.FeatureRequestsListView.as_view(), name='features'),
    path('features/new/', views.FeatureRequestCreateView.as_view(), name='create_feature_request'),
    path('features/<int:feature_id>', views.FeatureDetailView.as_view(), name='feature_request_detail'),
    path('features/<int:feature_id>/update/', views.FeatureRequestUpdateView.as_view(), name='update_feature_request'),
    path('features/<int:feature_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='delete_feature_request'),
]
