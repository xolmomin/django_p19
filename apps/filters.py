from django_filters import FilterSet, CharFilter

from apps.models import Course


class CourseFilterSet(FilterSet):
    category = CharFilter('category__name', lookup_expr='exact')

    class Meta:
        model = Course
        fields = 'title', 'category'
