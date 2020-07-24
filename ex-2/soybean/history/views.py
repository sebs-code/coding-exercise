from django.views.generic import ListView

from .models import SoybeanCondition


class SoybeanConditionListView(ListView):
    queryset = SoybeanCondition.objects.all()
