# Generated by Django 4.1 on 2023-09-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_operaciones_idfabricacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionorders1_sap',
            name='duedate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='DueDate'),
        ),
    ]
