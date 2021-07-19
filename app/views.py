from django.shortcuts import render
import time
from django.http import HttpResponse

# Create your views here.


def index(request):
        return render(request, "index.html")



def posts(request):
    start = int(request.GET.get('start') or 0)
    end = int(request.GET.get('end') or (start+9))

    data = []
    for i in range(start, end+1):
        data.append(f'Post#{i} ')

    #print(data)

    time.sleep(1)

    return HttpResponse(data)
