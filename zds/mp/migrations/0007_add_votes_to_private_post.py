# Generated by Django 3.2.12 on 2022-05-22 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mp", "0006_auto_20190114_1301"),
    ]

    operations = [
        migrations.AddField(
            model_name="privatepost",
            name="dislike",
            field=models.IntegerField(default=0, verbose_name="Dislikes"),
        ),
        migrations.AddField(
            model_name="privatepost",
            name="like",
            field=models.IntegerField(default=0, verbose_name="Likes"),
        ),
        migrations.CreateModel(
            name="PrivatePostVote",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("positive", models.BooleanField(default=True, verbose_name="Est un vote positif")),
                ("private_post", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="mp.privatepost")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "Vote",
                "verbose_name_plural": "Votes",
                "unique_together": {("user", "private_post")},
            },
        ),
    ]