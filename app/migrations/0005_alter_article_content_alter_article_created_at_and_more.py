# Generated by Django 5.0.7 on 2025-01-24 11:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_article_creator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.TextField(blank=True, default="", verbose_name="content"),
        ),
        migrations.AlterField(
            model_name="article",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
        ),
        migrations.AlterField(
            model_name="article",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="articles",
                to=settings.AUTH_USER_MODEL,
                verbose_name="creator",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="status",
            field=models.CharField(
                choices=[("draft", "Draft"), ("inprogress", "In Progress"), ("published", "Published")],
                default="draft",
                max_length=20,
                verbose_name="status",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=100, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="article",
            name="twitter_post",
            field=models.TextField(blank=True, default="", verbose_name="twitter_post"),
        ),
        migrations.AlterField(
            model_name="article",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="updated_at"),
        ),
        migrations.AlterField(
            model_name="article",
            name="word_count",
            field=models.IntegerField(blank=True, default="", verbose_name="word_count"),
        ),
    ]
