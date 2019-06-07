# Generated by Django 2.2 on 2019-06-06 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dteEmision', models.CharField(max_length=50)),
                ('dteTipo', models.CharField(max_length=50)),
                ('dteFolio', models.IntegerField()),
                ('emisorRut', models.CharField(max_length=50)),
                ('emisorRazonSocial', models.CharField(max_length=50)),
                ('receptorRut', models.CharField(max_length=50)),
                ('receptorRazonSocial', models.CharField(max_length=50)),
                ('detalle1Monto', models.IntegerField()),
                ('detalle1Iva', models.IntegerField()),
                ('detalle1Txt', models.CharField(max_length=50)),
                ('detalle2Monto', models.IntegerField(blank=True, null=True)),
                ('detalle2Iva', models.IntegerField(blank=True, null=True)),
                ('detalle2Txt', models.CharField(blank=True, max_length=50, null=True)),
                ('detalle3Monto', models.IntegerField(blank=True, null=True)),
                ('detalle3Iva', models.IntegerField(blank=True, null=True)),
                ('detalle3Txt', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
