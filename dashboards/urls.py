from django.conf.urls import url
from django.contrib import admin

from bms_overview.views import QuestionList, HomePageView, QuestionDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view()),



    url(r'^questions/$', QuestionList.as_view()),
    url(r'^(?P<slug>[-\w]+)/$', QuestionDetailView.as_view(), name='question-detail'),
]
