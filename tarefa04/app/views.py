from django.shortcuts import render
from .models import Atividade
from datetime import date

def index(request):

    atividades = Atividade.objects.all()

    context = {
        "atividades": atividades,
        "hoje": date.today(),
    }

    return render(request, "app/index.html", context)


