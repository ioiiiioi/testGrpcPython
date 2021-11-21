from django.core.management.base import BaseCommand
from Version.models import Versions
# from core.logger.views import check_responses
# from core.user.models import User
# from core.user.serializers import UserSerializer
# import asyncio
# from django.db import transaction,IntegrityError
# from core.services.rabbit_connection.connection import celery_publish_msg
# from django.conf import settings

class Command(BaseCommand):
    # def add_arguments(self, parser):
    #     parser.add_argument("-u", "--username", type=str, help="username")

    def handle(self, *args, **options):
        print(Versions.objects.all())