from django.db import models
from django.core.exceptions import ValidationError


class Pizza(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()

    def clean(self):
        if self.price is not None and self.price <= 0:
            raise ValidationError({'price': f'Nieprawidłowa cena: {self.price} (musi być > 0)'})
        if not self.name:
            raise ValidationError({'name': 'Nazwa pizzy nie może być pusta!'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}: {self.price} zł"

    class Meta:
        ordering = ['name']