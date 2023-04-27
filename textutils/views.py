from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'index.html')
def capatilized(text):
    output = ""
    
    return output

def textmodify(request):
    userinput = request.POST.get('text' , 'hello')

    removepun = request.POST.get('removepunc' , 'off')
    capital = request.POST.get('capital' , 'off')
    newlinerem = request.POST.get('newline' , 'off')
    extraspace = request.POST.get('extraspace' , 'off')
    charcount = request.POST.get('charcount' , 'off')
    analyser = ""
    if removepun == "on":
        punctuations = '''!@#$%^&*()_+-+*/\}{[]:="?'';><.,`~'''
        for char in userinput:
            if char not in punctuations:
                analyser = analyser + char
        params = {'purpose' : 'Puntuation Remove' , 'analyse_text' : analyser}
        return render(request,'textmodify.html',params)
        
    elif capital == "on":
        for char in userinput:
            analyser = analyser + char.upper()
       
        params =  {'purpose' : 'UPPERCASE in Characters' , 'analyse_text' : analyser}
        return render(request,'textmodify.html',params)
    elif newlinerem == "on":
        for char in userinput:
            if char != '\n' and char !='\r':
                analyser = analyser + char
        
        params =  {'purpose' : 'New Line Remover' , 'analyse_text' : analyser}
        return render(request,'textmodify.html',params)
    elif extraspace == "on":
        for index,char in enumerate(userinput):
            if not(userinput[index] == " " and userinput[index+1] == " "):
                analyser = analyser + char
        
        params =  {'purpose' : 'Remove Extra Spaces' , 'analyse_text' : analyser}
        return render(request,'textmodify.html',params)
    elif charcount == "on":
        analyser = str(len(userinput))
        params =  {'purpose' : 'New Line Remover' , 'analyse_text' : analyser}
        return render(request,'textmodify.html',params)
    else:
        params =  {'purpose' : 'Error' , 'analyse_text' : 'Error'}
        return render(request,'textmodify.html',params)
        
def contact(request):
    return render(request,'contact.html',None)

# def spacerem(request):
#     return HttpResponse('''<h1>Hello This is <b>Space Remove</b> page.</h1> <a href="http://127.0.0.1:8000/">Click Home</a> <br> <a href="http://127.0.0.1:8000/removePuncuation">Click Rem Punc</a> <br> <a href="http://127.0.0.1:8000/capitalFirst">Click Cap First</a> <br> <a href="http://127.0.0.1:8000/newLineRemove">Click New Line Rem</a> <br> <a href="http://127.0.0.1:8000/spaceRemove">Click Space Rem</a> <br> <a href="http://127.0.0.1:8000/charCount">Click Char Count</a> <br> 
# ''')

# def charcnt(request):
#     return HttpResponse('''<h1>Hello This is <b>Char count</b> page.</h1> <a href="http://127.0.0.1:8000/">Click Home</a> <br> <a href="http://127.0.0.1:8000/removePuncuation">Click Rem Punc</a> <br> <a href="http://127.0.0.1:8000/capitalFirst">Click Cap First</a> <br> <a href="http://127.0.0.1:8000/newLineRemove">Click New Line Rem</a> <br> <a href="http://127.0.0.1:8000/spaceRemove">Click Space Rem</a> <br> <a href="http://127.0.0.1:8000/charCount">Click Char Count</a> <br> 
# ''')
