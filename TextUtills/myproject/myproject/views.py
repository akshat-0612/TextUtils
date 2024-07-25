from django.shortcuts import render
from django.http import HttpResponse
# def about(request):
#     # return HttpResponse('''hello Akshat <a href="https://www.youtube.com/" target=_blank>tap me</a>''')
#
def about(request):
    return render(request,"about.html")
def index(request):
    # return HttpResponse('''<button ><a href="http://127.0.0.1:8000/about">press</a></button>''')
    return render(request, "index.html")

def analyze(request):
    if(request.method=="POST"):
        djtext = request.POST['text']
        calculator=request.POST.get("calculator","off")
        removepunc = request.POST.get("removepunc","off")
        inline_text=request.POST.get("Inline_text","off")
        capitalize=request.POST.get("capitalize","off")
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~+'''
        analyzed = ""
        signs='''+-/*'''
        f=0
        result=""

        if (removepunc != "off" or inline_text!="off" or capitalize!="off" or calculator!="off"):
            if (calculator != "off"):
                for i in djtext:
                    if i in signs:
                        sine = i
                        f = 1
                if (f == 1):
                    arr = djtext.split(sine)

                    if(sine=='+'):
                        sum = 0
                        for i in arr:
                            sum+=int(i)
                            analyzed=str(sum)
                    elif(sine == '-'):
                        sum = 0
                        for i in arr:
                            sum -= int(i)
                            analyzed = str(sum)
                    elif(sine == '*'):
                        sum = 1
                        for i in arr:
                            sum *= int(i)
                            analyzed = str(sum)
                    elif(sine == '/'):
                        sum = 1
                        for i in arr:
                            sum /= int(i)
                            analyzed = str(sum)
                result="Calculated"
            elif(removepunc=="on" and inline_text=="on"):
                for ch in djtext:
                    if ch not in punctuations and ch!="\n":
                        analyzed += ch
                if capitalize=="on":
                    analyzed=[x.upper() for x in analyzed]
                    analyzed = ' '.join([str(elem) for elem in analyzed])
                result="Punchuation Removed and Inlined"
            elif(inline_text=="on"):
                for ch in djtext:
                    if ch!="\n":
                        analyzed+=ch
                if capitalize=="on":
                    analyzed=([x.upper() for x in analyzed])
                    analyzed = ' '.join([str(elem) for elem in analyzed])
                result="Text Inlined"
            elif(removepunc=="on"):
                for ch in djtext:
                    if ch not in punctuations:
                        analyzed += ch
                if capitalize=="on":
                    analyzed=[x.upper() for x in analyzed]
                    analyzed = ' '.join([str(elem) for elem in analyzed])
                result="Punchuation Removed"
            else:
                for ch in djtext:
                    analyzed+=ch
                analyzed=[x.upper() for x in analyzed]
                analyzed = ''.join([str(elem) for elem in analyzed])
                result="Capitalized"

        else:
            return render(request, "error.html")

        params = {"aim": result, "analyzed_text": analyzed}
        return render(request, "analyze.html", params)
    else:
        return render(request, "error.html")


