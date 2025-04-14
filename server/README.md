#Late Show Code Challenge
This code challenge was all about creating an API to retrieve data specific to the data pertaining to the 3 models. 

##models.py
Models.py consists of 3 classes or models that will make up the tables within the database, `Episode`, `Guest` and `Appearance`. Within the models are attributes which define the table columns as well as serialising rules. The models all inherit from db.Model which enables querying and Serializer_Mixin which provides the to_dict() method allowing easy conversion of table data into python dictionaries then subsequently into JSON data. Within the models are also representations of how the data will be outputtes when querying from the terminal.

##app.py
App.py is where all the code to create the database is. The database `app.db` is created and the tables based off the models populate it. Another functionality of this module is to handle the routing. App.py contains all the routes which are functions that retrieve data from the tables and represent it as `JSON data` on a browser when the user visits one of these routes.

##seed.py
Seed.py is the seed data for the tables. Running this file populated the cells of the tables with sample data allowing for testing and viewing of the routes.

##app.db
This is the database where the tables are stored.

##Prerequisites
- **Python 3.9+**
- **pip** (Python package manager)
- **Virtual environment tool** (`venv` or `virtualenv`)
- **SQLite** 
- **Postman** (optional, for API testing)

###Author: Tamara Kaka