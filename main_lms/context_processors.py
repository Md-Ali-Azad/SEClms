from main_lms.models import *
def hcolor(request):
    hcolor=HeaderColor.objects.all()[:1].get()
    return {'hcolor':hcolor}