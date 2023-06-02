from django.db import migrations 
import os

def seed_type_categories(apps, schema_editor):
    TypeCategory = apps.get_model("type", "TypeCategory")

    type_categories_seed = [
        {
            "categoryName": "AccountType",
            "categoryDescription": "Account Type",
        },
        {
            "categoryName": "ItemType",
            "categoryDescription": "Item Type",
        },
    ]

    for current_type_category in type_categories_seed:
        type = TypeCategory.objects.create(**current_type_category)
        type.save()

class Migration(migrations.Migration):

    dependencies = [
        ('type', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_type_categories),
    ]
