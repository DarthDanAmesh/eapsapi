# Generated by Django 4.0.4 on 2022-05-15 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_rename_first_name_foo_country_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Foo',
            new_name='FooModel',
        ),
    ]
