from django.db import models

class Posts(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to="app/static/imgs")
    data_publi = models.DateField()
    
    def __str__(self):
        return self.titulo
