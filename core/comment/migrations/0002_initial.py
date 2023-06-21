# Generated by Django 4.2.2 on 2023-06-19 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core_post", "0001_initial"),
        ("core_comment", "0001_initial"),
        ("core_user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core_user.user"
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core_post.post"
            ),
        ),
    ]