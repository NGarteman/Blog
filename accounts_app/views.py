from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    form = RegisterForm()
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = form.save(commit=False)
            new_user.set_password(cd['password2'])
            new_user.save()
            return redirect('login')
    return render(request, 'register.html', {'form': form})