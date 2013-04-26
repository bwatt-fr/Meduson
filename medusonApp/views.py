# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from medusonApp.models import Client
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	return render_to_response('meduson/index.html')

def clients(request):
	clients_list = Client.objects.all().order_by('abreviation')
	return render_to_response('meduson/clients.html',{'clients_list' : clients_list})

def clientDetail(request,client_id):
	client = Client.objects.get(id_spec=client_id)
	return render_to_response('meduson/detailClient.html',{'client' : client})

def addClient(request):
	if request.method == 'GET' : 
		return render_to_response('meduson/addClient.html')
	else :
		c = Client(id_lettre=request.POST['identifiant'],societe=request.POST['societe'],abreviation=request.POST['abreviation'],nom=request.POST['nom'],prenom=request.POST['prenom'],adresse_postale=request.POST['adresse_postale'],ville=request.POST['ville'],code_postal=request.POST['code_postal'],pays=request.POST['pays'],telephone1=request.POST['telephone1'],telephone2=request.POST['telephone2'],mail=request.POST['mail'])
		c.save()
		return HttpResponseRedirect(reverse('medusonApp.views.clients'))
