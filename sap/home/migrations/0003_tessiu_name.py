# Generated by Django 3.2.8 on 2021-11-04 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='tessiu',
            name='name',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='home.paciente'),
            preserve_default=False,
        ),
    ]