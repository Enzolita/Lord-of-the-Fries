# Generated by Django 4.2.14 on 2024-08-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_alter_recipe_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Pending"), (1, "Approved")], default=0
            ),
        ),
    ]
