from django.db import models


class Book(models.Model):
    autor = models.CharField(max_length=64, blank=False)
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    kategoria = models.CharField(max_length=64, blank=False)
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default="")
    zdjecie = models.ImageField(upload_to="zdjecia", null=True, blank=True)

    def __str__(self):
        return self.autorTytulKategoria()

    def autorTytulKategoria(self):
        return "{} ({})".format(self.tytul, self.autor, self.kategoria)
