from django.shortcuts import render

def index(request):
    lista_atividades = [
        {
            "nome": "estudar html", 
            "status": "em andamento",
            "prazo": "30/06",
        },
        {
            "nome": "estudar html", 
            "status": "em andamento",
            "prazo": "30/06",
        },
    ]

    context = {
        "atividades": lista_atividades,
    }

    return render(request, "app/index.html", context)


