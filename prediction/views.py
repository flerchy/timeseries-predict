from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Document
from forms import DocumentForm



def result(request, filename):
    template = loader.get_template('prediction/result.html')
    print filename
    f = open(str("files/"+filename), "r")
    str_f = f.read()
    print str_f
    f.close()
    context = {'file_name': filename, 'file': str_f}
    return HttpResponse(template.render(context, request))

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('prediction.views.index'))
    else:
        form = DocumentForm() # A empty, unbound form

    documents = Document.objects.all()

    template = loader.get_template('prediction/index.html')
    return render( request, 'prediction/index.html', {'documents': documents, 'form' : form}, 
                            context_instance=RequestContext(request)
                          )

