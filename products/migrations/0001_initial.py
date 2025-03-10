# Generated by Django 5.1.3 on 2025-02-22 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categorie', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_prod', models.CharField(max_length=255)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=15)),
                ('statut', models.CharField(choices=[('disponible', 'Disponible'), ('indisponible', 'Indisponible')], default='indisponible', max_length=14)),
                ('quantite_en_stock', models.IntegerField()),
                ('boutiquier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.boutiquier')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categorie')),
            ],
        ),
    ]
