from django.db import models

class Job(models.Model):
    #Opções para o campo de status (Fica um menu suspenso bonito depois)
    STATUS_CHOICES = [
        ('enviado', 'Currículo Enviado'),
        ('entrevista', 'Entrevista Agendada'),
        ('teste', 'Teste Técnico'),
        ('aguardando', 'Aguardando Resposta'),
        ('rejeitado', 'Rejeitado'),
    ]

    title = models.CharField(max_length=100, verbose_name="Cargo")
    company = models.CharField(max_length=100, verbose_name="Empresa")
    location = models.CharField(max_length=100, verbose_name="Localização", blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='enviado')
    applied_date = models.DateField(auto_now_add=True, verbose_name="Data de Aplicação")
    notes = models.TextField(blank=True, verbose_name="Anotações")

    #Isso faz aparecer o nome da vaga em vez de "Job object (1)" na tela
    def __str__(self):
        return f"{self.company} - {self.title}"