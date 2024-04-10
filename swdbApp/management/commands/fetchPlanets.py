from django.core.management.base import BaseCommand
import requests
from swdbApp.models import Planet

class Command(BaseCommand):
    help = 'Fetch and store planet data from the Star Wars API'

    def handle(self, *args, **kwargs):
        self.stdout.write("Fetching planet data from the Star Wars API...")

        query = '''
        query Query {
            allPlanets {
                planets {
                    name 
                    population 
                    terrains 
                    climates
                }
            }
        }
        '''

        url = 'https://swapi-graphql.netlify.app/.netlify/functions/index'
        response = requests.post(url, json={'query': query})
        data = response.json()

        for planet in data['data']['allPlanets']['planets']:            
            Planet.objects.create(
                name=planet['name'],
                population = planet['population'] if planet['population'] is not None else None,
                terrains=','.join(planet['terrains']),
                climates=','.join(planet['climates'])
            )
            self.stdout.write(f"Added planet: {planet['name']}")

        self.stdout.write("Planet data fetching and storing complete.")
