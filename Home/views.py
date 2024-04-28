from django.http import HttpResponse
from django.template import loader

def home(request):
    # Logic for rendering the home page
    template = loader.get_template('homepage/home.html')
    return HttpResponse(template.render(request=request))
