from django.db import models

from tasks.models import Project, Task


class BugReport(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    STATUS_CHOICES = [('N', 'New'), ('I', 'In Progress'), ('C', 'Closed')]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
    PRIORITY_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' [' + self.get_status_display() + ']'


class FeatureRequest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    STATUS_CHOICES = [('C', 'Consideration'), ('A', 'Accepted'), ('R', 'Rejected')]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    PRIORITY_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' [' + self.get_status_display() + ']'
