# Generated by Django 4.1 on 2024-01-12 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("learn", "0003_authordetail"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="learn.author",
            ),
        ),
    ]
