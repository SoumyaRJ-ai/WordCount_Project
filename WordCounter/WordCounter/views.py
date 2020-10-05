import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    string = request.GET['fulltext']
    wordlist = string.split()
    dict_obj = {}
    for word in wordlist:
        if word in dict_obj:
            dict_obj[word] += 1
        else:
            dict_obj[word] = 1

    sortedwords = sorted(dict_obj.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'count': len(wordlist), 'text': string, 'sortedwords': sortedwords})


def about(request):
    return render(request, 'about.html')