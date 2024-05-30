from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm, ProfileEditForm, StudentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student


class LoginView(View):
    def get(self, request):
        form=LoginForm
        return render(request, 'user/login.html', context={"form":form})
    def post(self, request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            
            user= authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        form=LoginForm    
        return render(request, 'user/login.html', context={"form":form})      
    
    
    
class RegisterView(View):
    def get(self, request):
        form=RegisterForm()
        return render(request, 'user/register.html', context={"form":form})
   
   
    def post(self, request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('/')
        
        form=RegisterForm()
        return render(request, 'user/register.html', context={"form":form})
    
    
class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'user/profile.html') 
    
    
      

            
class EditProfileView(LoginRequiredMixin,View):
    def get(self, request):
        form=ProfileEditForm(instance=request.user)
        return render(request, 'user/edit.html', context={"form":form})
    
    def post(self, request):
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()  
            return redirect('/')  
        
        form=ProfileEditForm(instance=request.user)
        return render(request, 'user/edit.html', context={"form":form})

        
        
#########################    
    
def student(request):
    student=Student.objects.all()
    return render(request, 'user/student.html', context={"student":student})


def read(request, id):
    student=Student.objects.get(id=id)
    return render(request, 'user/read.html', context={"student":student})

def create(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    return render(request, 'user/create.html', context={"form":form})   


def update(request, id):
    student=get_object_or_404(Student, id=id)
    form=StudentForm(instance=student)
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    return render(request, 'user/create.html', context={"form":form})  


def delete(request, id):
    student=get_object_or_404(Student, id=id)
    student.delete()
    return redirect('users:profile')  

    
    
    