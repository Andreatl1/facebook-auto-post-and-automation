# Generated by Django 4.2 on 2023-05-02 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_category_remove_post_category_post_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='marketplace.category'),
        ),
    ]
