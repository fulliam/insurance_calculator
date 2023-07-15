from tortoise import fields
from tortoise.models import Model

# Модель тарифа
class InsuranceRate(Model):
    date = fields.DateField()
    cargo_type = fields.CharField(max_length=255)
    rate = fields.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        table = 'insurance_rates'