import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class FileCnab(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    type_number = models.IntegerField(validators=[
        MaxValueValidator(9),
        MinValueValidator(1)
    ])
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.TextField(max_length=11)
    card = models.TextField(max_length=12)
    time = models.TimeField()
    owner = models.TextField()
    store = models.TextField()
