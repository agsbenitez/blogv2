from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model): 
    #autor = models.ForeignKey('autor.User', on_delete=models.CASCADE)
    autor = models.CharField(max_length = 250)
    titulo = models.CharField(max_length = 250)
    texto = models.TextField()
    fCreado = models.DateTimeField(default = timezone.now)
    fPublicacion = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.fPublicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo