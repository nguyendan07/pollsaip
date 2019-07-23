from django.urls import path

from . import apiviews


urlpatterns = [
    # api
    path('', apiviews.QuestionList.as_view(), name='question_list'),
    path('<int:pk>/', apiviews.QuestionDetail.as_view(), name='question_detail')
]