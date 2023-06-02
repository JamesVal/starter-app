from django.db import migrations 
import os

def seed_account_types(apps, schema_editor):
    Type = apps.get_model("type", "Type")
    TypeCategory = apps.get_model("type", "TypeCategory")

    type_category = TypeCategory.objects.get(categoryName="AccountType")

    types_seed = [
        {
            "typeName": "AdminAccount",
            "typeDescription": "Admin Account",
            "category": type_category
        },
        {
            "typeName": "CustomerAccount",
            "typeDescription": "Customer Account",
            "category": type_category
        },
        {
            "typeName": "VendorAccount",
            "typeDescription": "Vendor Account",
            "category": type_category
        },
    ]

    for current_type in types_seed:
        type = Type.objects.create(**current_type)
        type.save()

class Migration(migrations.Migration):

    dependencies = [
        ('type', '0002_seed_type_categories'),
    ]

    operations = [
        migrations.RunPython(seed_account_types),
    ]
