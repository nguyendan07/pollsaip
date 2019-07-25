from django.urls import path
from rest_framework.routers import DefaultRouter

from . import apiviews

router = DefaultRouter()
router.register('polls', apiviews.QuestionViewSet, base_name='polls')


urlpatterns = [
    # api
    path('login/', apiviews.LoginView.as_view(), name='login'),
    path('polls/<int:pk>/choices/', apiviews.ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', apiviews.CreateVote.as_view(), name='create_vote'),
    path('users/', apiviews.CreateUser.as_view(), name='create_user'),
]

urlpatterns += router.urls
