from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer, VoteSerializer, UserSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(question_id=self.kwargs['pk'])
        return queryset
    serializer_class = ChoiceSerializer


class CreateVote(APIView):
    def post(self, request, pk, choice_pk):
        voted_by = request.data.get('voted_by')
        data = {'choice': choice_pk, 'question': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUser(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
