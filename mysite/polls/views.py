from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Sivanm. You're at the polls inde .")

# from django.shortcuts import render

# def index(request):
#     return render(request, 'myapp/index.html')
