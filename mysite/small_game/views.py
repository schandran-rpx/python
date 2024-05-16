from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index_v.html')

