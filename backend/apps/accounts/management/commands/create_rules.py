from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Cria as permissões de usuário"

    def handle(self, *args, **options):
        groups_name = ["Admin", "Manager", "Developer"]
        bulk_list = []
        for group_name in groups_name:
            bulk_list.append(Group(name=group_name))

        Group.objects.bulk_create(bulk_list, ignore_conflicts=True)
