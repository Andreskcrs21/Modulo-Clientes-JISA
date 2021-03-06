# Generated by Django 3.2.7 on 2021-09-10 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marca', models.CharField(max_length=200)),
                ('Modelo', models.CharField(max_length=200)),
                ('Año', models.IntegerField(max_length=4)),
                ('Color', models.CharField(max_length=30)),
                ('Placa', models.CharField(max_length=15)),
                ('Cilindrada', models.IntegerField(max_length=10)),
                ('Transmision', models.CharField(choices=[('manual', 'Manual'), ('automatico', 'Automatico')], max_length=10)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Foto', models.ImageField(upload_to='fotos')),
            ],
        ),
    ]
