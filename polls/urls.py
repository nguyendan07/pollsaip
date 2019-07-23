from django.urls import path

from . import apiviews


urlpatterns = [
    # api
    path('polls', apiviews.QuestionList.as_view(), name='question_list'),
    path('poll/<int:pk>/', apiviews.QuestionDetail.as_view(), name='question_detail'),
    path('choices/', apiviews.ChoiceList.as_view(), name='choice_list'),
    path('vote/', apiviews.CreateVote.as_view(), name='create_vote')
]