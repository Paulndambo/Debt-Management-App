# Generated by Django 4.2.4 on 2023-08-19 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_inventory_brand_alter_inventory_unit'),
        ('debts', '0012_remove_customeritemloan_month_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemborrowed',
            old_name='unit_price',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='itemborrowed',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.inventory'),
        ),
    ]
