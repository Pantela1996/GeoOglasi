# Generated by Django 4.0.1 on 2022-03-10 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instrumenti', '0005_instrument_kontakt'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='mesto',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]