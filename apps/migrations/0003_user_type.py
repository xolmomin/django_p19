# Generated by Django 5.0.6 on 2024-05-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0002_user_image_alter_category_slug_alter_course_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="type",
            field=models.CharField(
                choices=[
                    ("admin", "Admin"),
                    ("moderator", "Moderator"),
                    ("student", "Student"),
                    ("teacher", "Teacher"),
                ],
                default="student",
                max_length=255,
            ),
        ),
    ]