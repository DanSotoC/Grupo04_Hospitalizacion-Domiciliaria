from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from usuarios.models import Paciente, Personal
from usuarios.models import Tutor
from usuarios.models import Perfil
from visita.models import Visita
from django.contrib.auth.models import User
from registrar.forms import formulario_visita_esp
from especialista.views import visitas_programadas_esp
from visita.forms import  asignar_equipo
from datetime import date, time,datetime

def formulario(request, id=None):

	now = datetime. now()
	current_time = now. strftime("%H:%M:%S")
	now=datetime.today()
	current_user = request.user
	personal=Personal.objects.get(id_perfil=current_user.id)
	visita =  get_object_or_404(Visita, id=id)
	px = get_object_or_404(Paciente, id=visita.id_paciente)
	form=formulario_visita_esp(request.POST)
	if request.method=='POST':
		form=formulario_visita_esp(request.POST)




		if form.is_valid():
			form.save()

			return redirect(visitas_programadas_esp)
	context = {

		"id_visita": visita.id,
		"id_especialista": personal.id,
		"actual":current_user,
		"px":px,
		"form":form,
		"h_inicio":current_time
	}
		
	return render(request,'formulario_visita_esp.html',context)