# Generated by Django 2.1 on 2019-08-07 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20190803_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(max_length=20)),
            ],
            options={
                'db_table': 'EmailVerify',
            },
        ),
        migrations.DeleteModel(
            name='Subcription_type_quarterly',
        ),
        migrations.DeleteModel(
            name='Subscription_type_annual',
        ),
        migrations.DeleteModel(
            name='Subscription_type_halfyearly',
        ),
        migrations.DeleteModel(
            name='Subscription_type_monthly',
        ),
    ]
