from django.shortcuts import redirect
from django.urls import reverse

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Check if the session has expired
            if request.session.get_expiry_age() <= 0:
                # Redirect to the login page
                return redirect(reverse('login'))  # Assuming 'login' is the login URL name

        response = self.get_response(request)
        return response
