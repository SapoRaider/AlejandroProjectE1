from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        "nombre":"Alejandro",
        "apellido":"Troncoso",
        "telefono":"+56 9 3372 5662",
        "profesion":"Estudiante",
        "edad":"21",
        "ciudad":"Talca",
        "foto":"images/foto.jpg"
    }

    return render(request,'firstAPP1/indextem.html',data)


def projects(request):
    data = {
        "project1":"images/fb.jpg",
        "project2":"images/instagram.jpg",
        "project3":"images/twitter.jpg",
        "nombre1":"Facebook",
        "nombre2":"Instagram",
        "nombre3":"Twitter",
        "link1":"https://www.facebook.com",
        "link2":"https://www.instagram.com",
        "link3":"https://twitter.com",
        "año1":"2020",
        "año2":"2019",
        "año3":"2022",
        "cliente":"Mark Zuckerberg",
        "cliente2":"Mark Zuckerberg",
        "cliente3":"Elon Musk",
        "detalle1":"Proyecto de rediseño Front-End",
        "detalle2":"Proyecto de mejora",
        "detalle3":"Diseño grafico de la ultima update",
        "fondo":"images/blob-scene-haikei.svg",
        "duracion1":"3 meses",
        "duracion2":"4 meses",
        "duracion3":"10 meses"
    }

    return render(request,'firstAPP1/websites.html',data)