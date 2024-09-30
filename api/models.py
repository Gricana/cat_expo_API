from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Cat(models.Model):
    owner = models.ForeignKey(verbose_name="Владелец кошки", to=User,
                              on_delete=models.CASCADE, related_name='cats')
    breed = models.ForeignKey(verbose_name="Порода кошки", to=Breed,
                              on_delete=models.SET_DEFAULT,
                              default=0,
                              related_name='cats')
    color = models.CharField(max_length=30)
    age = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                  MaxValueValidator(325)],
                                      help_text="Возраст в полных месяцах")
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.breed} - {self.age}"


class Rating(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='cats')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)],
                                         help_text="Оценка от 1 до 5")

    class Meta:
        unique_together = ('cat', 'user', )

    def __str__(self):
        return f"Оценка {self.rating} от {self.user.username} для {self.cat}"
