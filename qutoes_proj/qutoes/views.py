from django.shortcuts import render
from django.views.generic import ListView

from . models import QutoesCategory
from . models import Qutoes

# Create your views here.
class QutoesView(ListView):
    template_name = "index.html"

    model = Qutoes

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('qutoes_category')