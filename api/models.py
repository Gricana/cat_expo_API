from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Breed(models.Model):
    """
    Модель для представления породы кошек.
    """
    name: str = models.CharField(max_length=100, unique=True,
                                 help_text="Порода кошки")

    def __str__(self) -> str:
        return self.name


class Color(models.Model):
    """
    Модель для представления окраса кошки.
    """
    name: str = models.CharField(max_length=30, unique=True,
                                 verbose_name="Цвет")

    def __str__(self) -> str:
        return self.name


class Cat(models.Model):
    """
    Модель для представления кота, его породы, окраса и владельца.
    """
    owner: User = models.ForeignKey(
        verbose_name="Владелец кошки",
        to=User,
        on_delete=models.CASCADE,
        related_name='cats'
    )
    breed: Breed = models.ForeignKey(
        verbose_name="Порода кошки",
        to=Breed,
        on_delete=models.SET_DEFAULT,
        default=0,
        related_name='cats'
    )
    color: Color = models.ForeignKey(
        Color,
        on_delete=models.SET_DEFAULT,
        default='',
        max_length=30,
        help_text="Цвет кошки"
    )
    age: int = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(325)],
        help_text="Возраст (в полных месяцах)"
    )
    description: str = models.TextField(
        max_length=500,
        help_text="Описание кошки"
    )

    def __str__(self) -> str:
        return f"{self.breed} - {self.age}"


class Rating(models.Model):
    """
    Модель для оценки кота пользователями.
    """
    cat: Cat = models.ForeignKey(
        Cat,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    user: User = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating: int = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)],
        help_text="Оценка от 1 до 5"
    )

    class Meta:
        unique_together = ('cat', 'user',)

    def __str__(self) -> str:
        return f"Оценка {self.rating} от {self.user.username} для {self.cat}"
