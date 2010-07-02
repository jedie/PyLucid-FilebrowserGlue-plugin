#coding:utf-8

from django.http import HttpResponseRedirect

def url_info(request):
    """ redirect to filebwoser index """
    return HttpResponseRedirect("browse/")
