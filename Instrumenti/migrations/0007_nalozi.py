# Generated by Django 4.0.1 on 2022-03-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instrumenti', '0006_instrument_mesto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nalozi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=30)),
                ('prezime', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('brtel', models.CharField(max_length=30)),
            ],
        ),
    ]