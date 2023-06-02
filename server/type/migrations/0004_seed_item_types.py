from django.db import migrations 
import os

def seed_item_types(apps, schema_editor):
    Type = apps.get_model("type", "Type")
    TypeCategory = apps.get_model("type", "TypeCategory")

    type_category = TypeCategory.objects.get(categoryName="ItemType")

    types_seed = [
        {
            "typeName": "ExampleItemType1",
            "typeDescription": "Example Item Type 1",
            "category": type_category
        },
        {
            "typeName": "ExampleItemType2",
            "typeDescription": "Example Item Type 2",
            "category": type_category
        }
    ]

    for current_type in types_seed:
        type = Type.objects.create(**current_type)
        type.save()

class Migration(migrations.Migration):

    dependencies = [
        ('type', '0003_seed_account_types'),
    ]

    operations = [
        migrations.RunPython(seed_item_types),
    ]
