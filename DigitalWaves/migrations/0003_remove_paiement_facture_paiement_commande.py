# Generated by Django 4.0 on 2024-07-09 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalWaves', '0002_panier_produit_panier_quantite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paiement',
            name='facture',
        ),
        migrations.AddField(
            model_name='paiement',
            name='commande',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='DigitalWaves.commande'),
            preserve_default=False,
        ),
    ]
