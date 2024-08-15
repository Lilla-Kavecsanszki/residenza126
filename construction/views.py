from django.shortcuts import render

def construction(request):
    return render(request, 'construction/construction.html')
