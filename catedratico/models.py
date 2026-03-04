from django.db import models

class Catedratico(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'catedraticos'