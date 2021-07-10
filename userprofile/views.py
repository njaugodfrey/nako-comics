from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .forms import SignUpForm, UserProfileForm
from .models import Profile

# Create your views here.

def create_profile(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.is_active = False
            user.save()
            return redirect('home:home')
    else:
        form = SignUpForm()
        return render(request, 'userprofile/signup.html', {'form': form})

@login_required
def view_profile(request, pk, slug):
    profile = get_object_or_404(
        User, pk=pk
    )

    context = {
        'profile': profile
    }

    return render(
        request, template_name='userprofile/view_profile.html',
        context=context
    )

@login_required
def update_profile(request, pk, slug):
    profile = get_object_or_404(
        User, pk=pk
    )
    form = SignUpForm(
        request.POST or None, instance=profile
    )

    if form.is_valid():
        form.save()
        return redirect('home:home')
    
    context = {
        'form': form
    }

    return render(
        request, template_name='userprofile/edit_profile.html',
        context=context
    )

@login_required
def delete_profile(request):
    pass
