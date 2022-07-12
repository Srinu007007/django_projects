from django.http import HttpResponse 
from django.shortcuts import render

def Homepage(request):
    data={
        'title':'Sai ram',
        'friends':['ram','rani','raju'],
        'info':[
            {'name':'srinu','phone':'8712388818'},
            {'name':'Ravi','phone':'9676377687'}
        ]
    }
    return render(request,"index.html",data)

def about(request):
    sum1=0
    try:
        n1=int(request.GET['num1'])
        n2=int(request.GET['num2'])
        sum1=n1+n2
    except:
        pass
    return render(request,"about.html",{'ans':sum1})

def contact(request):
    return render(request,"contact.html")


def aboutUs(request):
    return HttpResponse("Welcome to world")
def course(request):
    return HttpResponse("Hello Course")


def courseDet(request,courseId):
    return HttpResponse(courseId)