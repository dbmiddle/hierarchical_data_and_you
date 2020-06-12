from django.shortcuts import render

from mpttfun.models import Filesystem

# Create your views here.


def homepage(request):
    files = Filesystem.objects.all()
    return render(request, 'index.html', {'files': files})
