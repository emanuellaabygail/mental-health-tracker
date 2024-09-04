from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152185',
        'name': 'Emanuella Abygail',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)