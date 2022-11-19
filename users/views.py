from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

@login_required #Suddenly you need to be logged in before you can view this page.  With class based views it will be a lot more difficult. Whatever that means.  
#A cool feature of the loign_required, is that after being redirected to the login page, the next page will be the page you couldn't login to. 
def profile(request):
    if request.method =='POST': #Is request Post
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, 
            instance =request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')

    
    else: 
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance =request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context) #However, without checks we can always go there even without login. 

def register(request):
    if request.method =='POST': #Is request Post
        form = UserRegisterForm(request.POST) #Use data in form
        if form.is_valid(): #Is the form valid? Already existing user, etc. 
            form.save() #This runs everything in the background 
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are able to login as {username}!')
            return redirect('login')

    else:
        form= UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


#Different messages:
# message.debug
# message.info
# message.success
# message.warning
# message.error

