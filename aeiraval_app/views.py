# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response


def login_page(request): 
    if request.method == "POST":
        # TODO handle login
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/buttons")
            else:
                return HttpResponse("Disabled account")
        else:
            return HttpResponse("Invalid login")
    elif request.method == "GET":
        c = {}
        c.update(csrf(request))
        return render_to_response('1_login.html', c)


def buttons(request):
    return render_to_response('2_buttons.html')


def fitxes(request):
    return render_to_response('fitxes.html')


def analisi_inicial(request,qtype=None):
    extra_context={}
    extra_context['nou_usuari']=''
    extra_context['antic_usuari']='Palomar'
    extra_context['grup_anterior']='7'
    extra_context['referent_anterior']='EAIA'
    extra_context['antiquitat_a_lentitat']='2007'
    extra_context['altre+entitat']='EAIA'
    extra_context['agent_derivant']='EAIA'
    extra_context['servie_i_professional']='Coperfield'
    extra_context['servie_i_professional_data']='2013'
    extra_context['motius_de_la_derivacio']='Problemes amb la justicia'
    extra_context['pla_de_treball_proposat']='Under review'
    extra_context['possibilitats']='physico'
    extra_context['limitations']='comportament'
    extra_context['valoracio_funcional']='?'
    extra_context['nom']='Rosamunda'
    extra_context['roll']='mere'
    extra_context['mapa_de_relacions_familiar']='?'
    extra_context['sociograma']='?'
    extra_context['hipotest_de_la_situacio']='?'
    extra_context['orientacio_de_la_situacio']='?'
    return render_to_response('analisiinicial.html',extra_context)

def inscripcio(request,qtype=None):
    return render_to_response('inscripio.html',)


def entrevista_inicial(request,qtype=None):
    return render_to_response('entrevistainicial.html',)

def pla_de_treball(request,qtype=None):
    return render_to_response('pladetreball.html',)

def derivacio(request,qtype=None):
    return render_to_response('derivacioserveis.html',)

def valoracio(request,qtype=None):
    return render_to_response('valoracio.html',)

def informe(request,qtype=None):
    return render_to_response('informe.html',)

def acord(request,qtype=None):
    return render_to_response('acord.html',)
