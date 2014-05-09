from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("""Hello world: Probando que funciona django
    					con url /hello/ pero que al dejarlo sin esta ultima,
    					bota un error 404 porque no hay una pagina inicial
    					""")

def home_page(request):
	return HttpResponse("Esta es la pagina de inicio (asi no parezca)")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
        assert False
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    #return HttpResponse(html)
    return render(request, 'hours_ahead.html',{'hour_offset': offset, 'next_time': dt})
