from django.http import HttpResponse

def test(request):
    return HttpResponse('<center><h1>Hello</h1></center>')