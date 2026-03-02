from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 

class Participant(models.Model):
    """Модель для участника олимпиады"""
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email', unique=True)
    university = models.CharField('Вуз', max_length=200)
    course = models.PositiveIntegerField(
        'Курс',
        validators=[MinValueValidator(1), MaxValueValidator(5)]  
    )
    registered_at = models.DateTimeField('Дата регистрации', auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'