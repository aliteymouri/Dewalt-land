# Generated by Django 4.2.1 on 2023-05-31 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='درصد تخفیف'),
        ),
    ]
