from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Account, UserSelectedAccount

@api_view(['POST'])
def select_account(request):
    user = request.user
    account_id = request.data.get('account_id')

    try:
        account = Account.objects.filter(user=user).get(id=account_id)
    except Account.DoesNotExist:
        return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        user_account = UserSelectedAccount.objects.get(user=user)
        user_account.account = account
        user_account.save()
    except UserSelectedAccount.DoesNotExist:
        UserSelectedAccount.objects.create(user=user, account=account)

    return Response({'success': 'Account selected'})
