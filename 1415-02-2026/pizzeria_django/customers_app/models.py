from django.db import models
from django.core.exceptions import ValidationError

class Customer(models.Model):
    CUSTOMER_TYPES = [
        ('regular', 'Zwykły klient'),
        ('vip', 'VIP'),
    ]

    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=20)
    customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPES, default='regular')
    discount_percent = models.FloatField(default=0)
    loyalty_points = models.IntegerField(default=0)

    def clean(self):
        if self.customer_type == 'vip' and (self.discount_percent < 0 or self.discount_percent > 100):
            raise ValidationError({'discount_percent': 'Rabat musi być w zakresie 0-100%.'})
        if not self.first_name or not self.last_name:
            raise ValidationError('Imię i nazwisko klienta nie mogą być puste!')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def is_vip(self):
        return self.customer_type == 'vip'

    def __str__(self):
        vip_tag = " (VIP)" if self.is_vip else ""
        return f"{self.first_name} {self.last_name}{vip_tag}"

    class Meta:
        ordering = ['first_name', 'last_name']