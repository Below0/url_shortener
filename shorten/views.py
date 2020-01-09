from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import LinkForm
from django.shortcuts import render, redirect, get_object_or_404
from .constants import *


# Create your views here.
def main(request):
    shorten_url = ''
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_link = Link().transform(cd['og'])
            if new_link is not None:
                shorten_url = '/'.join([request.get_host(), new_link])
            else:
                return render(request, 'shorten/error.html', {'content': ERROR_MESSAGE_2})

    return render(request, 'shorten/index.html', {'value': shorten_url})


def mapping(request, key):
    try:
        mapping_url = Link.objects.get(id=fromBase62(key))
        mapping_url.last_accessed = timezone.now()
        mapping_url.save()
        return HttpResponseRedirect(mapping_url.og)
    except Link.DoesNotExist:
        return render(request, 'shorten/error.html', {'content': ERROR_MESSAGE_1})
