import time
import os
from django.core import management
from user.models import User, Account
from type.models import Type
from item.models import Item
import random
from django.db import transaction

DEFAULT_PASSWORD = os.environ.get("DEFAULT_PASSWORD")
NUM_USERS = 5
MAX_ITEMS_PER_USER = 10

class Command(management.base.BaseCommand):
    help = 'Create dummy users and items'

    def create_dummy_data(self):
        for i in range(NUM_USERS):
            try:
                with transaction.atomic():
                    user = User.objects.create(username=f'DUMMY_USER {i}', password=DEFAULT_PASSWORD, email=f'DUMMY_USER{i}@test.com')
                    user.save()

                    account = Account.objects.create(accountName=f'Test Account {i}', user=user)
                    account_type = Type.objects.get(typeName="VendorAccount")
                    account.type = account_type
                    account.save()

                    num_items = random.randint(1, MAX_ITEMS_PER_USER)

                    for item_index in range(num_items):
                        item_types = Type.objects.filter(category__categoryName="ItemType")
                        item = Item.objects.create(itemName=f'{account.accountName} - Test Item {item_index}', itemDescription=f'{account.accountName} - Test Item {item_index} Description', owner=account, type=random.choice(item_types))
                        item.save()

            except Exception as e:
                print(e)
                print(f'Error creating dummy data for user {i}', flush=True)

    def handle(self, *args, **options):
        self.create_dummy_data()