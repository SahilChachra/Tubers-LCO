from .models import BaseAppModel

def basedata(request):
    x = BaseAppModel.objects.all().order_by('-created_date')
    print(x[0])
    return {'data' : x[0] }