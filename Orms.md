# This file focuses on ORM (Object Relational Mappers)
- [Precursor to Learning](https://www.fullstackpython.com/object-relational-mappers-orms.html)

# What are ORMS
- ORM is a code library that automates the transfer of data stored in relational databases tables into objects 
  - that are more commonly used in application code
    
- ORMs provide a bridge between `relational database tables, relationships and fields and Python objects`
- ORMs provide a high-level abstraction (dealing with ideas rather than events) upon a `relational database`
- So it allows you to write `Python Code` instead of `SQL`
- To `create, read, update, delete` data and schemas in their database
- Imagine  want to get all data for People with `zip_code` values of `###`
- In `SQL` we do : `SELECT * FROM users WHERE zip_code="###"`
- In `Django ORM`: `users = Users.objects.filter(zip_code="###")`

## Benefits Of Using ORMS
    - This can speed up web application development (especially at the beginning of a project)
    - Why: We do not have to switch from Python code into writing declarative paradigm `SQL statements`
    - It is typically easier to start with a single Programming language
    - ORMS also make it theoretically possible to switch an application between various relational databases
    - For example use Sqlite for local dev, MySQL in prod and maybe change to PostgreSQL with minimal code modifications
    - However it is better to use the same db local in prod to prevent unforeseen errors

## Do I have to use an ORM for my web application
- Python ORM libraries are not required for accessing relational databases
- The low level access is typically provided by another library called `database connector`
- For example `psycopg` for PostgreSQL and `MySQL-python` for MySQL
- [ORM examples](https://www.fullstackpython.com/img/visuals/orm-examples.png)

## Downsides of using an ORM
- Impedance mismatch
  - [Link for reference](http://www.agiledata.org/essays/impedanceMismatch.html)
- Potential for reduced performance 
  - ORMs are easy to try but difficult to master
  - `select_related()` improve some queries foreign key relationship performance
  - For 80% - 90% of use cases ORMs are good enough but in 10%-20% improvements can be made by a database admin  
- Shifting complexity from the database into the application code
  -  The addition of data handling logic in the codebase generally isnt an issue
    * But we have more python code instead of separating database from procedures
    
## Python ORM Implementations
1. [SQLAlchemy](https://www.fullstackpython.com/sqlalchemy.html)
2. [Peewee](https://www.fullstackpython.com/peewee.html)
3. [The Django ORM](https://www.fullstackpython.com/django-orm.html)
4. [PonyORM](https://www.fullstackpython.com/pony-orm.html)
5. [SQLObject](http://sqlobject.org/)
6. [Tortoise ORM](https://tortoise-orm.readthedocs.io/en/latest/)

### Django's ORM
- Django's ORM is built in with the `django web framework`
- Works well for `simple-medium complexity` database operations
- Apparently Django ORM makes complex queries much more complicated than writing straight `SQL or using SQLAlchemy` 
- The ORM is couple with Django so replacing it with the SQLAlchemy is a hack workaround

## SCHEMA Migrations
- Adding a column to an existing table in your database are not technically part of ORMs. 
- Schema migrations often go hand in had with Python ORM usage

# General ORM RESOURCE
- Last Picked up on `Jan 5, 2021`
- Go to bottom of site
- [General ORM resources](https://www.fullstackpython.com/object-relational-mappers-orms.html)