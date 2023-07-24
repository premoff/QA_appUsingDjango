from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Question model
class Question(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# Answer model
class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    answer = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer

# UpVotes
class UpVote(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='upvote_user')
    