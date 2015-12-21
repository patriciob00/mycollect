from django.db import models

# Create your models here.
class Banda(models.Model):
    nome = models.CharField(max_length=200)
    can_rok = models.BooleanField(default=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'banda'
        verbose_name_plural = 'bandas'

    def __str__(self):
        return self.nome

    def get_members_count(self):
        return self.band.count()

    def get_band_detail_url(self):
        return u"/bands/%i" %self.id

class membro(models.Model):
    nome = models.CharField("Nome do membro", max_length=200)
    instrumento = models.CharField(choices=(
        ('g', "Guitara"),
        ('b', "Baixo"),
        ('d', "Bateria"),
        ('v', "Vocal"),
        ('p' , "piano"),
    ),
         max_length=1
    )

    banda = models.ForeignKey("Banda" , related_name='band')

    class Meta:
        ordering_name = ['nome']
        verbose_name = 'membro'
        verbose_name_plural = 'membros'

    def __str__(self):
        return self.nome