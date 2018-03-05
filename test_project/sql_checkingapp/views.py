from django.shortcuts import render, redirect
from sql_checkingapp import findsomethinglikejs
from django.http import HttpResponse
from django.template import loader

def index(request):
        url = 'http://localhost/testHtml.html'
        
        #functionName = findsomethinglikejs.findMethod(url)
        functionName = ['loadDoc()','loadDocVar()']
        scriptAll = findsomethinglikejs.findAllScript(url)
        context = {
            'var1':functionName ,
            'var2':scriptAll   
        }
        return render(request, 'index.html',context)
    

def getparams(request,url):
    template=loader.get_template('getparams.html')
    urlName = request.GET.get('url',None)
    data={
        'url':urlName
    }
    return HttpResponse(template.render(data,request))
    
