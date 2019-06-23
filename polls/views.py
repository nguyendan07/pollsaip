from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.conf import settings

from .models import Choice, Question


def index(request):
    question = Question.objects.all()[:settings.MAX_OBJECTS]
    data = {
        'results': list(question.values('question_text', 'created_by__username', 'pub_date'))
    }
    return JsonResponse(data)


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    data = {
        'results': {
            'question': question.question_text,
            'created_by': question.created_by.username,
            'pub_date': question.pub_date
        }
    }
    return JsonResponse(data)
