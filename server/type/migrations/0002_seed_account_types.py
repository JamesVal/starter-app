from django.db import migrations 
import os

def seed_account_types(apps, schema_editor):
    Type = apps.get_model("type", "Type")

    types_seed = [
        {
            "typeName": "AdminAccount",
            "typeDescription": "Admin Account",
        },
        {
            "typeName": "CustomerAccount",
            "typeDescription": "Customer Account",
        },
        {
            "typeName": "VendorAccount",
            "typeDescription": "Vendor Account",
        },
    ]

    for current_type in types_seed:
        type = Type.objects.create(**current_type)
        type.save()

class Migration(migrations.Migration):

    dependencies = [
        ('type', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_account_types),
    ]
