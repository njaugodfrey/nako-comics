from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import redirect
from userprofile.models import Profile

def user_check(allowed_roles=[]):
    pass
