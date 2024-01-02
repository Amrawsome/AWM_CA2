# load_data.py
import json
from CA2.staticfiles.Routing.models import Location  # Replace 'myapp' with the name of your Django app


def run():
    with open('CA2/staticfiles/Routing/Location.json') as f:  # Replace 'your_json_file.json' with the path to your JSON file
        data = json.load(f)
        locations = data['locations']

        for location_data in locations:
            Location.objects.create(
                id=location_data['id'],
                category=location_data['category'],
                name=location_data['name'],
                desc=location_data['desc'],
                lat=location_data['lat'],
                long=location_data['long']
            )

