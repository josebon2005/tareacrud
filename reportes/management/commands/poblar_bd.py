from django.core.management.base import BaseCommand
from universidad.Models.Alumno.models import Alumno
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Poblar la base de datos con 10,000 alumnos falsos'

    def handle(self, *args, **kwargs):
        fake = Faker('es_ES')

        total = 10000
        inicio = Alumno.objects.count() + 1

        self.stdout.write(self.style.WARNING(f'Creando {total} alumnos...'))

        for i in range(inicio, inicio + total):
            Alumno.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=f'alumno{i}@correo.com',
                phone=str(50000000 + i),
                gender=random.choice(['M', 'F']),
                birth_date=fake.date_of_birth(minimum_age=18, maximum_age=30),
                is_active=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('✔ Base de datos poblada correctamente'))