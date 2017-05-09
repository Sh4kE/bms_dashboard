from django.conf.urls import url
from django.contrib import admin

from bms_overview.views import QuestionList, HomePageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^questions/$', QuestionList.as_view()),
    url(r'^$', HomePageView.as_view()),
]
