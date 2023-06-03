import time
import os
from django.core import management
from user.models import User, Account
from type.models import Type
from item.models import Item
from comment.models import Comment
import random
from django.db import transaction

DEFAULT_PASSWORD = os.environ.get("DEFAULT_PASSWORD")
NUM_USERS = 5
MAX_ITEMS_PER_USER = 10
MAX_COMMENTS_PER_ITEM = 10

DUMMY_COMMENT_CONTENT = [
    'The cat jumped over the lazy dog.',
    'The sun was shining brightly on the beach.',
    'She opened the door and found a surprise waiting inside.',
    'The raindrops danced on the windowpane.',
    'The children laughed and played in the park.',
    'He tasted the delicious cake and couldn\'t help but smile.',
    'The old oak tree stood tall and proud in the middle of the field.',
    'The book was filled with intriguing mysteries and captivating characters.',
    'The sound of music filled the air, creating a magical atmosphere.',
    'As the sun set, the sky transformed into a stunning palette of colors.'
]

class Command(management.base.BaseCommand):
    help = 'Create dummy users and items'

    def create_dummy_data(self):
        try:
            with transaction.atomic():
                for i in range(NUM_USERS):
                      user = User.objects.create(username=f'DUMMY_USER {i}', password=DEFAULT_PASSWORD, email=f'DUMMY_USER{i}@test.com')
                      user.save()

                      account = Account.objects.create(accountName=f'Test Account {i}', user=user)
                      account_type = Type.objects.get(typeName="VendorAccount")
                      account.type = account_type
                      account.save()

                num_items = random.randint(1, MAX_ITEMS_PER_USER)

                for item_index in range(num_items):
                    item_owner = random.choice(Account.objects.all())
                    item_types = Type.objects.filter(category__categoryName="ItemType")
                    item = Item.objects.create(
                        itemName=f'{item_owner.accountName} - Test Item {item_index}',
                        itemDescription=f'{item_owner.accountName} - Test Item {item_index} Description',
                        owner=item_owner,
                        type=random.choice(item_types),
                    )
                    item.save()
                    num_comments = random.randint(1, MAX_COMMENTS_PER_ITEM)
                    for comment_index in range(num_comments):
                        comment_account = random.choice(Account.objects.all())
                        comment = Comment.objects.create(
                            content=random.choice(DUMMY_COMMENT_CONTENT),
                            item=item,
                            owner=comment_account
                        )
                        comment.save()

        except Exception as e:
            print(e)
            print(f'Error creating dummy data', flush=True)

    def handle(self, *args, **options):
        self.create_dummy_data()