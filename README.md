# Star Wars Planets API

This Django project provides a RESTful API for interacting with data about planets from the Star Wars universe. It fetches data from a GraphQL API, stores it in a database, and allows CRUD operations via REST endpoints. Additionally, I provided a search feature to search and filter the planets.

## Usage

You can interact with the API through the following endpoints:

/planets/ - GET (list planets), POST (add a new planet).
/planets/<int:id>/ - GET (retrieve a planet), PUT (update a planet), PATCH (partially update a planet), DELETE (delete a planet).

## Filtering and Search

To filter planets by name, use /planets/?name=[name].
To filter by population range, use /planets/?min_population=[min]&max_population=[max].
To search by terrain or climate, use /planets/?terrains=[terrain_name] or /planets/?climates=[climate_name].
