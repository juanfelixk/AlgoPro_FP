import django_filters
from job.models import Job

class JobFilter(django_filters.FilterSet): #inheritance from FilterSet class in django_filters module
    title = django_filters.CharFilter(lookup_expr = 'icontains') #filter the title field if it contains the substring submitted (case-insensitive)
    class Meta:
        model = Job
        fields = ['title', 'job_type', 'industry'] #define fields to be filtered