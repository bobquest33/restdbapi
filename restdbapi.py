import sys
from decimal import Decimal
from flask.json import JSONEncoder
from flask import Flask,url_for
from flask_restless import APIManager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeferredReflection
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.inspection import inspect
from sqlalchemy_utils import get_primary_keys
import sqlalchemy as sqla
import traceback


class CustomDecimalJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, Decimal):
              return str(obj)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


def list_routes(app):
  import urllib
  output = []
  with app.test_request_context():
    for rule in app.url_map.iter_rules():

      options = {}
      for arg in rule.arguments:
        options[arg] = "[{0}]".format(arg)

      methods = ','.join(rule.methods)
      url = url_for(rule.endpoint, **options)
      line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
      output.append(line)

      for line in sorted(output):
        print line

if len(sys.argv) < 2:
	print "Please provide the connection url for DB"
	exit()

conn = sys.argv[1]


app = Flask(__name__)
app.json_encoder = CustomDecimalJSONEncoder
mclasses = []
tab_ignored = []

try:
  print "setting connection"
  engine = create_engine(conn,echo=False)
  Base = declarative_base()
  print "reflect the tables"
  # reflect the tables
  Base.metadata.reflect(engine)
  metadata = Base.metadata
  #print dir(metadata)
  #print metadata.tables.keys()
  #print metadata.tables.values()

  for name,mtable in metadata.tables.items():
    print str(name)
    if len(get_primary_keys(mtable).keys()) > 0:
      clsl = type(str(name).title(), (DeferredReflection,Base),
                  {'__tablename__': str(name)})
      mclasses.append(clsl)
    else:
      tab_ignored.append(str(name))
  DeferredReflection.prepare(engine)
  print "setting session"
  session = sessionmaker(bind=engine)
  mysession = session()
  apimanager = APIManager(app, session=mysession)

  for clsl in mclasses:
    apimanager.create_api(clsl)

  #apimanager.init_app(app)
except:
    traceback.print_exc()
list_routes(app)
print tab_ignored
app.run()