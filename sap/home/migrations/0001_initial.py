# Generated by Django 3.2.8 on 2021-11-04 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tessiu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(verbose_name='Temperatura')),
                ('color', models.FloatField()),
                ('inflamation', models.FloatField(verbose_name='inflamación')),
            ],
            options={
                'verbose_name': 'Tejido',
                'verbose_name_plural': 'Tejidos',
            },
        ),
    ]