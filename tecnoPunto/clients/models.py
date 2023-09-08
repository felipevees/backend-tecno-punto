from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cc = models.CharField(max_length=20)
    payment_value = models.DecimalField(max_digits=6, decimal_places=3)
    payments = models.IntegerField(verbose_name="Cuotas pagadas")
    asesor = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.cc + ' ' + self.first_name + ' ' + self.last_name
