from django.views.generic import ListView
from django.views.generic import TemplateView

from bms_overview.models import Question


class HomePageView(TemplateView):
    template_name = "bms_overview/index.html"


class QuestionList(ListView):
    model = Question
