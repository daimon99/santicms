from django.shortcuts import render
import models as m

# Create your views here.

def hello(request):
    name = request.GET.get('name', 'santi')
    return render(request, 'mycms/hello.html', dict(msg=name))

def home(request):
    pass


def article(request, art_id):
    return render(request, 'mycms/hello.html', dict(msg=art_id))


def tag(request, tag_name):
    return render(request, 'mycms/hello.html', dict(msg=tag_name))


def question(request, q_id):
    return render(request, 'mycms/hello.html', dict(msg=q_id))


def questions(request):
    return render(request, 'mycms/hello.html', dict(msg='questions'))


def questions_hottest(request):
    return render(request, 'mycms/hello.html', dict(msg='questions_hottest'))


def questions_unanswered(request):
    return render(request, 'mycms/hello.html', dict(msg='questions_unanswered'))


def blogs(request):
    articles = m.get_blogs_recommended(page=1)
    return render(request, 'mycms/blogs_index.html', dict(blogs=articles))


def user(request, username):
    return render(request, 'mycms/hello.html', dict(msg=username))


def ask(request):
    return render(request, 'mycms/hello.html', dict(msg='ask'))


def write(request):
    return render(request, 'mycms/hello.html', dict(msg='write'))


def draft(request):
    return render(request, 'mycms/hello.html', dict(msg='draft'))


def login_register(request):
    return render(request, 'mycms/hello.html', dict(msg='login_register'))