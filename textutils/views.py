# I have created this file - Omar
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'index.html')

def analyze_form(request):

    return render(request, 'analyze_form.html')

##-#-## Buttons Work Together (also single button works) Start ##-#-##
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        analyzed = ""  # Blank String
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):

        return HttpResponse('Please select any operation and try again.')

    return render(request, 'analyze.html', params)
##-#-## Buttons Work Together (also single button works) End ##-#-##

