# Generated by Django 4.0.4 on 2022-05-05 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condicioneri',
            fields=[
                ('seriyni_nomer', models.IntegerField(primary_key=True, serialize=False)),
                ('naimenovanie', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('nalichie', models.BooleanField(default=True)),
                ('garantia', models.IntegerField()),
                ('data_proizvodstva', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pokupatel',
            fields=[
                ('nomer_pokupatelya', models.IntegerField(primary_key=True, serialize=False)),
                ('FIO_pokupatelya', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Postavki',
            fields=[
                ('nomer_partii', models.IntegerField(primary_key=True, serialize=False)),
                ('data_postavki', models.DateField()),
                ('price_zakupki', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Postavshiki',
            fields=[
                ('kod_postavshika', models.IntegerField(primary_key=True, serialize=False)),
                ('naimenovanie_postavshika', models.CharField(max_length=100)),
                ('uridicheski_adress', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Prodaji',
            fields=[
                ('nomer_cheka', models.IntegerField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proizvoditeli',
            fields=[
                ('kod_proizvoditelya', models.IntegerField(primary_key=True, serialize=False)),
                ('naimenovanie_proizvoditelya', models.CharField(max_length=100)),
                ('uridicheskiy_adress', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Sotrudniki',
            fields=[
                ('tabelniy_nomer', models.IntegerField(primary_key=True, serialize=False)),
                ('FIO', models.CharField(max_length=100)),
                ('doljnost', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Zavoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod_postavshika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.postavshiki')),
                ('nomer_partii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.postavki')),
                ('seriyni_nomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.condicioneri')),
            ],
        ),
        migrations.CreateModel(
            name='Schet_pokupatelya',
            fields=[
                ('nomer_scheta', models.IntegerField(primary_key=True, serialize=False)),
                ('sostoyanie_scheta', models.PositiveIntegerField()),
                ('nomer_pokupatelya', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pokupatel')),
            ],
        ),
        migrations.CreateModel(
            name='Realizacia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kolichestvo', models.PositiveIntegerField()),
                ('nomer_cheka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.prodaji')),
                ('seriyni_nomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.condicioneri')),
            ],
        ),
        migrations.AddField(
            model_name='prodaji',
            name='tabelniy_nomer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sotrudniki'),
        ),
        migrations.CreateModel(
            name='Privoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kolichestvo', models.PositiveIntegerField()),
                ('nomer_partii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.postavki')),
                ('seriyni_nomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.condicioneri')),
            ],
        ),
        migrations.AddField(
            model_name='postavki',
            name='kod_postavshika',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.postavshiki'),
        ),
        migrations.AddField(
            model_name='condicioneri',
            name='kod_proizvoditelya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.proizvoditeli'),
        ),
        migrations.AddField(
            model_name='condicioneri',
            name='kod_prostavshika',
            field=models.ManyToManyField(to='main.postavshiki'),
        ),
        migrations.AddField(
            model_name='condicioneri',
            name='nomer_partii',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.postavki'),
        ),
    ]