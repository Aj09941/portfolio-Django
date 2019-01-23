from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Jop
# Create your views here.
def home(request):
	jops = Jop.objects
	return render(request, 'jops/home.html', {'jops':jops})

def detail(request, job_id):
	job_detail = get_object_or_404(Jop, pk=job_id)
	return render(request, 'jops/detail.html', {'jops':job_detail})