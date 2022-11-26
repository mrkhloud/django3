from django.shortcuts import render


def google_login(request):
    """
    Представление входа через Google
    """
    template_name = 'oauth/google_login.html'
    return render(request, template_name)