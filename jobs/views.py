from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import JobForm

def job_list(request):
    #Pega todas as vagas do banco de dados da mais nova para a mais antiga
    jobs = Job.objects.all().order_by('-applied_date')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list') # Volta para a home depois de salvar
    else:
        form = JobForm() # Se for GET, mostra o formulário vazio
    return render(request, 'jobs/job_form.html', {'form': form})

def job_edit(request, id):
    job = get_object_or_404(Job, id=id) # Pega a vaga pelo ID ou dá erro 404 se não existir

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job) # 'instance=job' preenche o formulário com os dados existentes
        if form.is_valid():
            form.save()
            return redirect('job_list') # Volta para a home depois de salvar
    else:
        form = JobForm(instance=job) # Se for GET, mostra o formulário preenchido com os dados da vaga
    return render(request, 'jobs/job_form.html', {'form': form})

def job_delete(request, id):
    job = get_object_or_404(Job, id=id) # Pega a vaga pelo ID ou dá erro 404 se não existir
    if request.method == 'POST':
        job.delete()
        return redirect('job_list') # Volta para a home depois de deletar
    return render(request, 'jobs/job_confirm_delete.html', {'job': job})

