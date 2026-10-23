from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split






def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and Confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')




def getPredictions(a,b,c,d,e,f,g,h,i,j,k,l,m,n):
    model = pickle.load(open('KNN.pkl', 'rb'))
    prediction = model.predict(np.array([[a,b,c,d,e,f,g,h,i,j,k,l,m,n]]))
    return prediction[0]



def result(request):
    a = int(request.GET['YEAR'])
    b = float(request.GET['JAN'])
    c = float(request.GET['FEB'])
    d = float(request.GET['MAR'])
    e = float(request.GET['APR'])
    f = float(request.GET['MAY'])
    g = float(request.GET['JUN'])
    h = float(request.GET['JUL'])
    i = float(request.GET['AUG'])
    j = float(request.GET['SEP'])
    k = float(request.GET['OCT'])
    l = float(request.GET['NOV'])
    m = float(request.GET['DEC'])
    n = float(request.GET['ANNUAL_RAINFALL'])

        
    result= getPredictions(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
    return render(request, 'result.html', {'result': result})