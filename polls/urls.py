from django.urls import path
from rest_framework.routers import DefaultRouter

from . import apiviews

router = DefaultRouter()
router.register('polls', apiviews.QuestionViewSet, base_name='polls')


urlpatterns = [
    # api
    path('polls/<int:pk>/choices/', apiviews.ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', apiviews.CreateVote.as_view(), name='create_vote')
]

urlpatterns += router.urls
