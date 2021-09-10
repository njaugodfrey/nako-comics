from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import redirect
from userprofile.models import Profile

def allowed_user(allowed_roles=[]):
    # decorator that looks for user role
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            role = None
            uid = request.user.id
            profile_type = Profile.objects.get(user=uid)
            role = profile_type.role
            
            if role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Request access denied')
        return wrapper_func
    return decorator

def forbidden_user(forbidden=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            role = None
            uid = request.user.id
            profile_type = Profile.objects.get(user=uid)
            role = profile_type.role
            
            if role in forbidden:
                return HttpResponse('Request access denied')
            else:
                return view_func(request, *args, **kwargs)
                
        return wrapper_func
    return decorator
