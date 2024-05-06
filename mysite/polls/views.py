from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Sivanm. You're at the polls inde .")