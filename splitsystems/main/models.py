from django.db import models
from django.contrib.auth.models import User


class Postavshiki (models.Model):
    kod_postavshika = models.IntegerField(primary_key=True, verbose_name="Код поставщика")
    naimenovanie_postavshika = models.CharField(max_length=100, verbose_name="Наименование поставщика")
    uridicheski_adress = models.CharField(max_length=100, verbose_name="Юридический адрес")
    phone = models.CharField(max_length=15, verbose_name="Телефон")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.naimenovanie_postavshika


class Postavki(models.Model):
    nomer_partii = models.IntegerField(primary_key=True, verbose_name="Номер партии")
    kod_postavshika = models.ForeignKey(Postavshiki, on_delete=models.CASCADE, verbose_name="Код поставщика")
    data_postavki = models.DateField(verbose_name="Дата поставки")
    price_zakupki = models.PositiveIntegerField(verbose_name="Цена закупки")

    class Meta:
        verbose_name = "Поставка"
        verbose_name_plural = "Постравки"

    def __str__(self):
        return {"Партия номер":  self.nomer_partii}


class Proizvoditeli (models.Model):
    kod_proizvoditelya = models.IntegerField(primary_key=True, verbose_name="Код производителя")
    naimenovanie_proizvoditelya = models.CharField(max_length=100, verbose_name="Наименование производителя")
    uridicheskiy_adress = models.CharField(max_length=150, verbose_name="Юридический адрес")

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return self.naimenovanie_proizvoditelya


class Condicioneri (models.Model):
    seriyni_nomer = models.IntegerField(primary_key=True, verbose_name="Серийный номер")
    kod_proizvoditelya = models.ForeignKey(Proizvoditeli, on_delete=models.CASCADE, verbose_name="Код производителя")
    kod_prostavshika = models.ManyToManyField(Postavshiki, verbose_name="Код поставщика")
    nomer_partii = models.ForeignKey(Postavki, on_delete=models.CASCADE, verbose_name="Номер партии")
    naimenovanie = models.CharField(max_length=100, verbose_name="Наименование")
    price = models.CharField(max_length=100, verbose_name="Цена")
    nalichie = models.BooleanField(default=True, verbose_name="Наличие")
    garantia = models.IntegerField(verbose_name="Гарантия")
    data_proizvodstva = models. DateField(verbose_name="Дата производства")

    class Meta:
        verbose_name = "Кондиционер"
        verbose_name_plural = "Кондиционеры"

    def __str__(self):
        return self.naimenovanie


class Zavoz (models.Model):
    seriyni_nomer = models.ForeignKey(Condicioneri, on_delete=models.CASCADE, verbose_name="Серийный номер")
    kod_postavshika =  models.ForeignKey(Postavshiki, on_delete=models.CASCADE, verbose_name="Код поставщика")
    nomer_partii = models.ForeignKey(Postavki, on_delete=models.CASCADE, verbose_name="Номер партии")

    class Meta:
        verbose_name = "Завоз"
        verbose_name_plural = "Завозы"


class Privoz (models.Model):
    seriyni_nomer = models.ForeignKey(Condicioneri, on_delete=models.CASCADE,verbose_name="Серийный номер")
    nomer_partii = models.ForeignKey(Postavki, on_delete=models.CASCADE, verbose_name="Номер партии")
    kolichestvo = models.PositiveIntegerField(verbose_name="Количество")

    class Meta:
        verbose_name = "Привоз"
        verbose_name_plural = "Привозы"


class Sotrudniki (models.Model):
    tabelniy_nomer = models.IntegerField(primary_key=True, verbose_name="Табельный номер")
    FIO = models.CharField(max_length=100, verbose_name="ФИО")
    doljnost = models.CharField(max_length=150, verbose_name="Должность")

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.FIO


class Prodaji (models.Model):
    nomer_cheka = models.IntegerField(primary_key=True, verbose_name="Номер чека")
    tabelniy_nomer = models.ForeignKey(Sotrudniki, on_delete=models.CASCADE, verbose_name="Табельный номер")
    data = models.DateField(verbose_name="Дата")

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"

    def __str__(self):
        return {"Чек номер":  self.nomer_cheka}



class Realizacia (models.Model):
    seriyni_nomer = models.ForeignKey(Condicioneri, on_delete=models.CASCADE, verbose_name="Серийный номер")
    nomer_cheka = models.ForeignKey(Prodaji, on_delete=models.CASCADE, verbose_name="Номер чека")
    kolichestvo = models.PositiveIntegerField(verbose_name="Количество")

    class Meta:
        verbose_name = "Реализация"
        verbose_name_plural = "Реализации"


class Pokupatel (models.Model):
    nomer_pokupatelya = models.IntegerField(primary_key=True, verbose_name="Номер покупателя")
    FIO_pokupatelya = models.CharField(max_length=150, verbose_name="ФИО покупателя")

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"

    def __str__(self):
        return self.FIO_pokupatelya


class Schet_pokupatelya (models.Model):
    nomer_scheta = models.IntegerField(primary_key=True, verbose_name="Номер счета")
    nomer_pokupatelya = models.ForeignKey(Pokupatel, on_delete=models.CASCADE, verbose_name="Номер покупателя")
    sostoyanie_scheta = models.PositiveIntegerField(verbose_name="Состояние счета")

    class Meta:
        verbose_name = "Счет покупателя"
        verbose_name_plural = "Счета покупателей"

    def __str__(self):
        return {"Счет номер":  self.nomer_scheta}


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField(verbose_name="id Кондиционера");
    def __str__(self):
        return {"Кондиционера":  self.product_id}


