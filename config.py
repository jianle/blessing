import logging

SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/bless'
SECRET_KEY = 'BLESSING_SECRET_KEY'
CSRF_ENABLED = True
IGNOREPATH = '/static/*'

LOGGING_FORMAT =  '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
LOGGING_LOCATION = 'blessing.log'
LOGGING_LEVEL = logging.DEBUG