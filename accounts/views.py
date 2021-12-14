from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def Profile(request):
    """
    View for profile page
    """
    return render(request, 'registration/profile.html', {'section': 'profile'})


