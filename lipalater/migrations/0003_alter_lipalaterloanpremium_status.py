# Generated by Django 4.1.7 on 2023-09-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lipalater", "0002_alter_lipalaterloan_amount_paid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lipalaterloanpremium",
            name="status",
            field=models.CharField(
                choices=[
                    ("unpaid", "Unpaid"),
                    ("pending", "Pending"),
                    ("paid", "Paid"),
                    ("paying", "Paying"),
                    ("reviewing", "Reviewing"),
                ],
                max_length=255,
            ),
        ),
    ]