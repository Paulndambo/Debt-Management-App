# Generated by Django 4.2.1 on 2023-08-18 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debts', '0010_alter_customermoneyloan_expected_repay_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeritemloan',
            name='year',
            field=models.CharField(choices=[('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029')], max_length=255, null=True),
        ),
    ]
