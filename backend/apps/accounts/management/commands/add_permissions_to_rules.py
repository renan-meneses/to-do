from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Cria as permissões de usuário"

    def handle(self, *args, **options):
        # Creation user can't inactivate objects and can
        # not interact with users objects
        creation_no_permissions = [
            "Create trask",
            "Update trask",
            "Delete trask",
        ]

        # Client user can only list objects of his brand

        # Admin or Atendimento just can't approve or reprove job
        adm_and_answering_no_permissions = [ ]

        groups_n_permissions = [
            {
                "Admin": Permission.objects.exclude(
                    name__in=adm_and_answering_no_permissions
                )
            },
            {
                "Developer": Permission.objects.exclude(
                    name__in=adm_and_answering_no_permissions
                )
            },
            {
                "Manager": Permission.objects.exclude(
                    name__in=creation_no_permissions
                )
            },
        ]

        for data in groups_n_permissions:
            for group, permissions in data.items():
                Group.objects.get(name=group).permissions.set(permissions)
