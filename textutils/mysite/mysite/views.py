# i have created this file - bijayata
from django.http import HttpResponse
from django.shortcuts import render

#code for video 6
#def index(request):
 #   return HttpResponse('''<a href =' https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'<h1>django tutorial<h1> </a>''')

#def about(request):
 #   return HttpResponse('<h1>welcome to home page</h1>')

#code for video 7,8 & 9

#def index(request):
 #   return render(request,'index.html',)
   # return HttpResponse('home')

#def removepunc(request):
    #get the text
  #  djtext=request.GET.get('text','default')
   # print(djtext)
    #analyze the text
   # return HttpResponse('removepunc')

#def capfirst(request):
 #   return HttpResponse('capitalizefirst')

#def newlineremove(request):
 #   return HttpResponse('nelineremove')

#def spaceremove(request):
  #  return HttpResponse('''spaceremove<a href='/'>back</a>''')

#def charcount(request):
 #   return HttpResponse('charcount')

#  code for video 10
def index(request):
   return render(request,'index.html')
  #return HttpResponse('home')

def analyze(request):
    #get the text
     djtext=request.POST.get('text','default')
     
     
     removepunc=request.POST.get('removepunc','off')
     fullcaps=request.POST.get('fullcaps','off')
     newlineremover=request.POST.get('newlineremover','off')
     extraspaceremover=request.POST.get('extraspaceremover','off')

     if (removepunc == "on"):
           punctuations = '''. , ? ! : ; " ' () [] {} - – — ... / \ | < > ~ @ # $ % ^ & * _ + ='''
           analyzed = ""
           for char in djtext:
              if char not in punctuations:
               analyzed = analyzed + char
           params={'purpose':'remove punctuations','analyzed_text':analyzed}
      #analyze the text
      #return HttpResponse('removepunc')
           djtext = analyzed
           #return render(request,'analyze.html',params) 

     if(fullcaps=="on"):
           analyzed=""
           for char in djtext:
            analyzed=analyzed + char.upper()  
           params={'purpose':'changed to uppercase','analyzed_text':analyzed}
           djtext = analyzed
           #return render(request,'analyze.html',params)

     if(extraspaceremover=="on"):
           analyzed=""
           for index,char in enumerate(djtext):
              if not (djtext[index] ==" " and djtext[index+1]==" "):   
                analyzed=analyzed + char 
           params={'purpose':'extra space remove ','analyzed_text':analyzed}
           djtext = analyzed     
 
     if(newlineremover=="on"):
           analyzed=""
           for char in djtext:
            if char !="\n"and char != "\r":   
             analyzed=analyzed + char  
            else:
             print("no")
             print("pre",analyze)
           params={'purpose':'new line remove ','analyzed_text':analyzed}
     if(removepunc != "on" and fullcaps!="on" and extraspaceremover!="on" and newlineremover!="on"):
           return HttpResponse("Choose the button option and try again")
           
           #return render(request,'analyze.html',params)
     
     return render(request,'analyze.html',params)


def ex1(request):
    s ="""<h1> Navigation Bar<br></h1> <a href="https://www.youtube.com/">youtube</a><br>
          <a href="https://www.instagram.com/">instagram</a><br>
          <a href="https://www.facebook.com/">facebook</a><br>
          <a href="https://www.linkdein.com/">linkdein</a>""" 
    return HttpResponse(s)                                  
    
      

