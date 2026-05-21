from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")

def usuarios(request):

    lista_usuarios = [
        {
        "nome": "Bruno",
        "matricula": 2024189128,
        "idade": 18,
        "cidade": "São Tomé"
        },
        {
        "nome": "Emilly",
        "matricula": 2024181238,
        "idade": 17,
        "cidade": "Santa Maria"
        },
        {
        "nome": "Nathalia",
        "matricula": 2024198128,
        "idade": 17,
        "cidade": "Santa Maria"
        },
        {
        "nome": "Marquinhos",
        "matricula": 2024859828,
        "idade": 17,
        "cidade": "São Tomé"
        },
        {
        "nome": "José Luís",
        "matricula": 202418348,
        "idade": 18,
        "cidade": "Sitio Novo"
        },
    ]

    context = {
        "usuarios": lista_usuarios,
    }

    return render(request, "app/usuarios.html", context)
