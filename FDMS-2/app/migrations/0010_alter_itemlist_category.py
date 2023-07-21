# Generated by Django 4.1.3 on 2023-02-28 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_itemlist_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlist',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app.categorylist'),
        ),
    ]
