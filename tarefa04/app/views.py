from django.shortcuts import render

def index(request):
    return render(request,  "app/index.html")


def atividades(request):

    lista_atividades = [
        {
            "nome": "estudar html", 
            "status": "em andamento",
            "parzo": "30/06",
        },
    ]

    context = {
        "atividades": lista_atividades,
    }

    return render(request, "app/index.html", context)