from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView

from bms_overview.models import Question


class HomePageView(TemplateView):
    template_name = "bms_overview/index.html"


class QuestionList(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
