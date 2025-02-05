# Generated by Django 5.0.6 on 2024-07-08 07:06

from django.db import migrations


def create_admin(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.create_superuser(username='admin', password='admin')


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0002_alter_orderitem_order'),
    ]

    operations = [
        migrations.RunPython(create_admin, lambda apps, schema_editor: None)
    ]
