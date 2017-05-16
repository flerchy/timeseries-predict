from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Document
from forms import DocumentForm

import analyze
import os

def result(request, filename):
    analyze.draw_plot("files/" + filename)
    analyze.linreg("files/" + filename)
    analyze.isoreg("files/" + filename)
    template = loader.get_template('prediction/result.html')
    print filename
    f = open(str("files/" + filename), "r")
    str_f = f.read()
    print str_f
    f.close()
    filename = os.path.splitext(os.path.basename(filename))[0]
    context = {'file_name': filename, 'file': str_f, 'pic_name': "/files/"+filename }
    return HttpResponse(template.render(context, request))

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            # Redirect to the document list after POST

            
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        form = DocumentForm() # A empty, unbound form

    documents = Document.objects.all()

    template = loader.get_template('prediction/index.html')
    return render( request, 'prediction/index.html', {'documents': documents, 'form' : form})

