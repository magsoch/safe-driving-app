from rest_framework import serializers
from .models import Hint, Quiz, Question


class HintSerializer(serializers.HyperlinkedModelSerializer):
    publish_date = serializers.DateTimeField(format='%d-%B-%Y %H:%M', required=False)
    hint_detail = serializers.HyperlinkedIdentityField(view_name='hint-detail', read_only=True)

    class Meta:
        model = Hint
        fields = ('id', 'hint_detail', 'title', 'content', 'tags', 'publish_date', 'quiz')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'url', 'question', 'positive_answer', 'negative_answer1', 'negative_answer2', 'hint', 'quiz')


class QuizSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Quiz
        fields = ('id', 'url', 'hint', 'question')
