from django.db import models


class Couches(models.Model):
    name = models.CharField("Имя", max_length=15)
    coach_information = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"


class SportStyle(models.Model):
    name = models.CharField("Название", max_length=20)
    direction_information = models.TextField("Описание направления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class PriceList(models.Model):
    number_of_training = models.CharField("Количество тренировок", max_length=15)
    price = models.CharField("Цена(бел/руб)", max_length=5)
    coach = models.ForeignKey(Couches, on_delete=models.CASCADE, null=True)
    sport_style = models.ForeignKey(SportStyle, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.number_of_training} трен. {self.sport_style}"

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Прайс-лист"
