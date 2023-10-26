# Generated by Django 3.2.5 on 2023-10-26 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('satellites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('createdAt', models.DateTimeField()),
                ('satellite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='satellites.satellitemodel')),
            ],
        ),
    ]