from django.shortcuts import render, get_object_or_404
from .models import Usuario
from .forms import AgendarForm

def agendar_usuario(request, id=None):
	form = AgendarForm(request.POST or None)
	queryset = get_object_or_404(Usuario, idDatosPer=id)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect("agendar")

	context = {

		"form": form,
		"object_list": queryset,
	}
	return render(request,"agendar.html",context)
