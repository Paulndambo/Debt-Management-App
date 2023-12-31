# Generated by Django 4.2.1 on 2023-08-15 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customer_gender'),
        ('debts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeritemloan',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Defaulted', 'Defaulted'), ('Paying', 'Paying'), ('Reviewing', 'Reviewing')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customermoneyloan',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Defaulted', 'Defaulted'), ('Paying', 'Paying'), ('Reviewing', 'Reviewing')], max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('amount_applied', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Declined', 'Declined')], max_length=255, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loanapplications', to='users.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
