from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Command to create a user to be used in django admin
    """

    help = "Seed the database informations"

    def create_super_user(self):
        if User.objects.filter(username="admin").count() == 0:
            self.stdout.write(
                self.style.WARNING("Iniciando o processo de Inserção de Super User")
            )
            User.objects.create_superuser("admin", "admin@example.com", "admin")
            self.stdout.write(
                self.style.SUCCESS("processo de criação de Super User Finalizado")
            )

    def handle(self, *args, **options):
        self.create_super_user()
