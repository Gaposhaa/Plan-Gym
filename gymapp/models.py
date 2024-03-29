from django.db import models


class Coaches(models.Model):
    name = models.CharField("Имя", max_length=15,)
    coach_information = models.TextField("Описание")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/coaches/{self.id}"

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
    number_of_training = models.IntegerField("Количество тренировок")
    price = models.IntegerField("Цена(бел/руб)")
    coach = models.ForeignKey(Coaches, on_delete=models.CASCADE, null=True)
    sport_style = models.ForeignKey(SportStyle, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.number_of_training} трен. {self.sport_style}"

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Прайс-лист"


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email
