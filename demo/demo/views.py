from ast import Pass
import imp
import nturl2path
import re
from tkinter import N
from tkinter.tix import Tree
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from pkg_resources import require


def index(request):
    res1=0
    data={}
    try:
        if request.method == 'GET':
            n=int(request.GET.get('num1'))
            n1=int(request.GET.get('num2'))
            res1=n+n1
            data={
                'n':n,
                'n1':n1,
                'res1':res1
            }
            url="/blog/?output={}".format(res1)
            return HttpResponseRedirect(url)    
            
        
        
    except:
        Pass
    return render(request,"index.html",data)
    
def about(request):
    return render(request,"about.html")
    
def blog(request):
    if request.method == "GET":
        output=request.GET.get('output')
    return render(request,"blog.html",{'output':output})


def calculator(request):
    res=''
    try:
        if request.method=="POST":
            
            no1=eval(request.POST.get("no1"))
            no2=eval(request.POST.get("no2"))
            opr=request.POST.get("opr")

            if opr=='+':
                res=no1+no2
            elif opr=='-':
                res=no1-no2
            elif opr=='*':
                res=no1*no2
            elif opr=='/':
                res=no1/no2
    except:
        res='Invalid Operation'
    return render(request,"calculator.html",{'res':res})

def studentsheet(request): 
       
    if request.method=="POST":        
        subject1=eval(request.POST.get("sub1"))
        subject2=eval(request.POST.get("sub2"))
        subject3=eval(request.POST.get("sub3"))
        subject4=eval(request.POST.get("sub4"))
        subject5=eval(request.POST.get("sub5"))
        tot=subject1+subject2+subject3+subject4+subject5
        avg=tot*100/500
        if avg>60:
            g='First class'
        elif avg>50:
            g='Second class'
        elif avg>35:
            g='Third class'
        elif avg>0:
            g='Faild'
        data11={
            'total':tot,
            'average':avg,
            'grade':g
                
        }
        return render(request,"studentsheet.html",data11)
    


    return render(request,"studentsheet.html")




def evenorodd(request):
    datares={}
    if request.method=="POST":
        if request.POST.get("no")=="":
            return render(request,"evenorodd.html",{'error':True})
        n1=eval(request.POST.get("no"))
        if(n1%2==0):
            res12='Even Number'
        else:
            res12='Odd Number'
        datares={
            'check':res12,
        }
    return render(request,"evenorodd.html",datares)

def Formval(request):
    formdata1={}
    
    if request.method=="POST":
       
        
        if request.POST.get("name")=="":
            return render(request,"Formval.html",{'nameerror':True})
        if request.POST.get("email")=="":
            return render(request,"Formval.html",{'emailerror':True})
        if request.POST.get("password")=="":
            return render(request,"Formval.html",{'passworderror':True})
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        formdata1={
            'name1':name,
            'email1':email,
            'password1':password,
       }

    return render(request,"Formval.html",formdata1)

