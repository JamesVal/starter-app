from django.contrib.auth import get_user_model
from django.db import migrations
import os
from user.models import Account
from type.models import Type

DEFAULT_USER = os.environ.get("DEFAULT_USER")
DEFAULT_PASSWORD = os.environ.get("DEFAULT_PASSWORD")

def create_superuser(apps, schema_editor):
    User = get_user_model()
    user = User.objects.create_superuser(username=DEFAULT_USER, password=DEFAULT_PASSWORD, email=DEFAULT_USER)
    user.save()
    account = Account.objects.create(accountName="Default Admin", user=user)
    account_type = Type.objects.get(typeName="AdminAccount")
    account.type = account_type
    account.save()


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_account'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
