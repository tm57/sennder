from django.http import HttpResponse
from django.shortcuts import render


def movies(request):
    response = "Here is a list of mivies and the people in them"
    # return render(request, 'polls/index.html', context)
    return HttpResponse(response)
