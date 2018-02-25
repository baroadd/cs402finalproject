from django.shortcuts import render
from sql_checkingapp import findsomethinglikejs

#from django.http import HttpResponse
#from django.template import loader
'''
def index(request):
    header_str = 'Hello, Python variable'
    template = loader.get_template('index.html')
    context = {
        'var1':header_str
    }
    return HttpResponse(template.render(context,request))
'''
def index(request):
    url = 'http://localhost/testHtml.html'
    #functionName = findsomethinglikejs.findMethod(url)
    functionName = "loadDocVar()"
    scriptAll = findsomethinglikejs.findAllScript(url)

    
    context = {
        'var1':functionName ,
        'var2':scriptAll   
    }
    return render(request, 'index.html',context)