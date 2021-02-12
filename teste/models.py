from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Consumer(BaseModel):
    consumer_id = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumers'
        ordering = ['id']


class Service(BaseModel):
    service_id = models.CharField(max_length=64)
    latency_proxy = models.IntegerField(blank=False, null=False)
    latency_gateway = models.IntegerField(blank=False, null=False)
    latency_request = models.IntegerField(blank=False, null=False)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Service'
        ordering = ['id']
