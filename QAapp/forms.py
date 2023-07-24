from .models import Question,Answer
from django.forms import ModelForm


class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields= '__all__' #('title','detail','tags')


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)

