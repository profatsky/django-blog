from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, "errors/404.html")
