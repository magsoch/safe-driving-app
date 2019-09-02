from django.urls import path
from core.views import *


urlpatterns = [
    path('hint/', HintList.as_view(), name='hint-list'),
    path('hint/<int:pk>/', HintDetail.as_view(), name='hint-detail'),
    path('question/', QuestionList.as_view(), name='question-list'),
    path('question/<int:pk>', QuestionDetail.as_view(), name='question-detail'),
    path('quiz/', QuizList.as_view(), name='quiz-list'),
    path('quiz/<int:pk>/', QuizDetail.as_view(), name='quiz-detail'),
]
