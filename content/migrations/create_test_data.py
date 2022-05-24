from django.contrib.auth import get_user_model
from django.db import migrations
from django.db.migrations import RunPython

User = get_user_model()


def create_admin(apps, schema_editor):
    """Create admin"""
    User.objects.create_superuser(
        username="admin", password="admin", email='admin@admin.com'
    )


def create_pages(apps, shcema_editor):
    """Create pages"""
    Page = apps.get_model("content", "Page")
    Page.objects.bulk_create([
        Page(title="Page #1"),
        Page(title="Page #2"),
        Page(title="Page #3")
    ]
    )


def create_content(apps, schema_editor):
    """Create content for first pages"""
    Page = apps.get_model("content", "Page")
    Video = apps.get_model("content", "Video")
    Audio = apps.get_model("content", "Audio")
    Text = apps.get_model("content", "Text")
    page = Page.objects.first()
    Video.objects.bulk_create([
        Video(
            title='Video 1', page=page, order=1, video_url='test.com',
            subtitle_file_url='test.com'
        ),
        Video(
            title='Video 2', page=page, order=3, video_url='test.com',
            subtitle_file_url='test.com'
        ),
    ])
    Audio.objects.bulk_create([
        Audio(
            title='Audio 1', page=page, order=2, bitrate=320,
        ),
        Audio(
            title='Audio 2', page=page, order=5, bitrate=128,
        ),
    ])
    Text.objects.bulk_create([
        Text(
            title='Text 1', page=page, order=4, text='Hello world from Text 1',
        ),
        Text(
            title='Text 2', page=page, order=6, text='Hello world from Text 2',
        ),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_admin),
        migrations.RunPython(create_pages),
        migrations.RunPython(create_content),
    ]
