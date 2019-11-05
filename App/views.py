from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from App.models import Student


def hello(request):
    return HttpResponse("Hello")


def index(request):
    return render(request, 'index.html')


def get_student(request):

    students = Student.objects.all()

    student_dict = {
        "hobby": "encoding",
        "time": "one year"
    }

    code = "<h2>哈哈</h2>"

    data = {
        "students":students,
        "student_dict":student_dict,
        "code": code
    }

    return render(request,'student_list.html',context=data)