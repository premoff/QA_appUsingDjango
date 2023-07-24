from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Question,Answer,UpVote
from .forms import AnswerForm,QuestionForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.


def home(request):
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request,'QAapp/home.html',context)


@login_required(login_url='login')
def detail(request,pk):
    quest = Question.objects.get(id=pk)
    answer = Answer.objects.filter(question=quest)
    form = AnswerForm()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.question= quest
            ans.user=request.user
            ans.save()
    context = {'question':quest,'answers':answer,'form':form}
    return render(request,'QAapp/answer.html',context)


@login_required(login_url='login')
def ask(request):
    form = QuestionForm()
    if request.method=='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ask')
    context = {'form':form}
    return render(request,'QAapp/ask.html',context)

def register(request):
    form = UserCreationForm()
    if request.method=='POST':
        form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    context = {'form':form}
    return render(request,'registration/register.html',context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
                login(request,user)
                return redirect('home')
    context = {}                    
    return render(request,'registration/login.html',context)

def signout(request):
    logout(request)
    return redirect('login')


def save_upvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=UpVote.objects.filter(answer=answer,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            UpVote.objects.create(
                answer=answer,
                user=user
            )
            return JsonResponse({'bool':True})