from django.core.management.base import BaseCommand
from app1.models import ServiciosExtras

class Command(BaseCommand):
    help = 'Crea 5 registros de servicios extras'

    def handle(self, *args, **kwargs):
        # Crear una lista de datos para los hoteles
        servicios_datos = [
            {'titulo': 'piscina','precio':5000, 'imagen' : 'https://i.ibb.co/n6r3b4F/piscina.jpg'},
            {'titulo': 'gimnasio','precio':7000, 'imagen' : 'https://i.ibb.co/qRVgpKF/gym.webp'},
            {'titulo': 'jacuzzi','precio':8000, 'imagen' : 'https://i.ibb.co/pnfjRKL/jacuzzi.jpg'},
        ]
        
        # Iterar sobre los datos y crear registros en la base de datos
        for data in servicios_datos:
            ServiciosExtras.objects.create(**data)
        
        self.stdout.write(self.style.SUCCESS('5 registros creados servicios extras'))

