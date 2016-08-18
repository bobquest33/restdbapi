##Rest DB API##

This is a python inspiered by sandman2 to help convert tables in any database supported by SQlAlchemy to a fully functional API with support for read, write and delete.

### Current Version ###
0.01 pre-Alpha-1 as I have just completed development and will need time to structure it to a proper python project structure.


### How to install ###

1. Copy the git repo to your local or the server.
2. Setup a virtual environment (Optional)
  virtualenv venv
  venv\Scripts\activate (For windows)
3. Install dependencies
  pip install -r requirements.txt
4. Connect to any database
  python restdbapi.py <DB connection url>

  Refer http://docs.sqlalchemy.org/en/latest/core/engines.html for the probable format of DB connection url.
  Url e.g dialect+driver://username:password@host:port/database

  Sample command:
  python restdbapi.py "postgresql://scott:tiger@localhost/mydatabase"
  python restdbapi.py "mysql://scott:tiger@localhost/foo"
  python restdbapi.py  "sqlite:///foo.db"

This will get you started. For any issues please raise an issue in github.

### Roadmap ###
1. This has only been tested for Sqlite3 , MySQL & postgresql. Need to test for other DBs as well.
2. Create a reusable api structure and make options more configurable.
3. Add a UI admin
4. Add authentication support
5. Add documentation
6. Adding comprehensive unit & api testing
7. Right now API for only those tables are created that do have a primary key and other tables are ignored. Need to fix it.
8. Need to add support to list, schemas, databases and views.

Note: This software has not even gone through the full cycle of testing and was a qucik hack hence use it at your own risk.

### License ###

The MIT License (MIT)

Copyright (c) <2016> <Priyabrata Dash>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
