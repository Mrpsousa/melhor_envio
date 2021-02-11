from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Teste(BaseModel):
    name = models.CharField(max_length=225)

    class Meta:
        verbose_name = 'Teste'
        verbose_name_plural = 'Testes'
        ordering = ['id']
