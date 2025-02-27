# Generated by Django 2.2.24 on 2022-05-22 10:54

from django.db import migrations


def copy_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flat_set = Flat.objects.all()
    flat_iterator = flat_set.iterator()
    for flat in flat_iterator:
        Owner.objects.get_or_create(owner=flat.owner,
                                    owner_pure_phone=flat.owner_pure_phone,
                                    owners_phonenumber=flat.owners_phonenumber)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0011_auto_20220520_1958'),
    ]

    operations = [
        migrations.RunPython(copy_owners),
    ]
