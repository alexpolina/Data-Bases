from django.contrib import admin
from .models import Postavshiki, Postavki, Proizvoditeli, Condicioneri, Zavoz, Privoz, Sotrudniki, \
    Prodaji, Realizacia, Pokupatel, Schet_pokupatelya

# Register your models here.

admin.site.register(Postavshiki)
admin.site.register(Postavki)
admin.site.register(Proizvoditeli)
admin.site.register(Condicioneri)
admin.site.register(Zavoz)
admin.site.register(Privoz)
admin.site.register(Sotrudniki)
admin.site.register(Prodaji)
admin.site.register(Realizacia)
admin.site.register(Pokupatel)
admin.site.register(Schet_pokupatelya)