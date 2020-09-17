# BACKEND-CHALLENGE

  

a python backend challenge, you can find the challenge document in this [Link](https://drive.google.com/file/d/1qm_OU73uqzbLGieTZXYb5jPVwVqsXl14/view?usp=sharing)

  

## Getting Started

  

### Prerequisites

  

this project built with python 3.8.5 ,so it's recommended to use this version or better

  

install packages - its preferred to use virtualenv

```

pip install -r requirements.txt

```

  

### Installing

  

you need to have file called ``` .env ``` inside the folder ``` project ```with this values

  

**Get sure you inside the ``` project``` directory**

  

```

SQLALCHEMY_DATABASE_URI = # sqlalchemy connection string

  

DATABASE_NAME_DEVELOPMENT = # development database name

  

DATABASE_NAME_TESTING = # testing database name

  

```

**you can find more about sqlalchemy Database Urls [here](https://docs.sqlalchemy.org/en/13/core/engines.html#supported-databases)**

  

create the models

```

from app import create_app

from app.models import db

app = create_app()

app.app_context().push()

db.create_all()

  

# import the described in the challenge document

from app.models import defaultData

defaultData(app=app, db=db)

  

```

  

## Running the tests

  

**Get sure you inside the ``` project``` directory**

  

you must configure the ```.env``` file before running this - and also get sure your database is ready.

```
python -m unittest
```

## Solved by

* **Mustafa Ahmed** - [LinkedIn](https://www.linkedin.com/in/mustafa-ahmed-8508abb6/)

## Suggested improvements 

* app permissions: critical operations should be limited to specific users
* input validation: all input and filtering operation should be validated first before take action
* update data: this app should have update mechanism to update existing data