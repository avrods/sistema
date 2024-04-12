from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test

def logged_out_required(function=None, redirect_field_name=None, login_url=None):
    actual_decorator = user_passes_test(
        lambda u: not u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
