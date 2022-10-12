# # I have created this website Name : Mohammed Ubaid
# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     #return HttpResponse('''<h1>Hello World, Welcome to my new site</h1> <a href= https://www.linkedin.com/in/ubaid-mohammed-588a06245/> Visit on my LinkedIn</a>''')
#     params = {'name': 'Ubaid', 'django': 'developer'}
#     return render(request, 'index.html',params)

# def about(request):
#     return HttpResponse("About me")

# def contact(request):
#     return HttpResponse('''Contact me at <a href=https://www.instagram.com> Please Sign Up </a>''')


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def ex1(request):
    s = '''<h1>navigation bar<br></h1>
    <a href= 'www.facebook.com'>Facebbok<br></a>
    <a href= 'www.instagram.com'>Instagram</a>'''
    return HttpResponse(s)

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    removeextraspace = request.POST.get('removeextraspace', 'off')
    
    if removepunc == 'on':
        punctuation = '''-+?.,/';:"{}[]()_&@#$'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char#Analyze the text
                
                params = {'purpose':'Remove punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if(capitalize == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            
            params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
            
        # return render(request, 'analyze.html', params)
        djtext = analyzed
        
    elif(newlineremove == 'on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char!= '\r':
                analyzed = analyzed + char
            
            else:
                print('No')
            print("pre", analyzed)
            params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
        
    if(removeextraspace == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzed = analyzed + char

                params = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
    
    if(removepunc != 'on' and capitalize != 'on' and newlineremove != 'on' and removeextraspace != 'on'):
        return HttpResponse('Please Select Operations to be performed')
    
    return render (request, 'analyze.html', params)
    
    
# def capfirst(request):
#     return HttpResponse('capitalizefirst')

# def newlineremove(request):
#     return HttpResponse('newlineremove')

# def spaceremove(request):
#     return HttpResponse('spaceremove')

# def charcount(request):
#     return HttpResponse('charcount')