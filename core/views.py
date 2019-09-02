from rest_framework import generics
from .models import Hint, Question, Quiz
from .serializers import HintSerializer, QuestionSerializer, QuizSerializer


class HintList(generics.ListCreateAPIView):
    """
    List all hints or create new hint
    """
    queryset = Hint.objects.all()
    serializer_class = HintSerializer
    ordering = ('id', )


class HintDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrive, update or delete a hint instance
    """
    queryset = Hint.objects.all()
    serializer_class = HintSerializer


class QuestionList(generics.ListCreateAPIView):
    """
    List or create question instance
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or destroy question instance
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuizList(generics.ListCreateAPIView):
    """
    List or create quiz instance
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List or create quiz instance
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
