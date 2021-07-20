from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
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
            user.is_superuser = False
            user.is_staff = False
            user.save()
            return redirect(
                'userprofile:view-profile',
                pk=user.pk, slug=user.username
            )
    else:
        form = SignUpForm()
        return render(request, 'userprofile/signup.html', {'form': form})

@login_required
def view_profile(request, pk, slug):
    user = get_object_or_404(
        User, pk=pk
    )

    profile = get_object_or_404(
        Profile, user=user
    )

    if profile.birth_date == None:
        return redirect(
            'userprofile:update-profile',
            pk=user.pk, slug=user.username
        )

    else:
        context = {
            'usr': user
        }

        return render(
            request, template_name='userprofile/view_profile.html',
            context=context
        )

@login_required
def update_profile(request, pk, slug):
    current_user = request.user
    profile = get_object_or_404(
        User, pk=pk
    )
    if profile.pk == current_user.pk:
        profileform = UserProfileForm(
            request.POST or None, instance=profile
        )
        userform = SignUpForm(
            request.POST or None, instance=profile
        )

        if request.method == 'POST':
            #user_form = SignUpForm(request.POST)
            profile_form = UserProfileForm(request.POST)

            if profile_form.is_valid():
                this_profile_form = profile_form.save(commit=False)
                this_profile = get_object_or_404(
                    Profile, user=profile
                )
                this_profile.birth_date = profile_form.cleaned_data.get('date_birth')
                this_profile.avatar = profile_form.cleaned_data.get('avatar')
                this_profile.bio = profile_form.cleaned_data.get('bio')
                this_profile.location = profile_form.cleaned_data.get('location')
                this_profile.website = profile_form.cleaned_data.get('website')
                this_profile.save()
                return redirect(
                    'userprofile:view-profile',
                    pk=profile.pk, slug=profile.username
                )
            else:
                return HttpResponse('Invalid form')
        
        context = {
            'profileform': profileform,
            'userform': userform
        }

        return render(
            request, template_name='userprofile/edit_profile.html',
            context=context
        )
    else:
        return HttpResponse('Not your profile')

@login_required
def update_account(request, pk, slug):
    pass

@login_required
def delete_profile(request):
    pass
