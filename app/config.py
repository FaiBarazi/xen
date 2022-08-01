import os
DB = {
    'name': os.environ['POSTGRES_DB'],
    'user': os.environ['POSTGRES_USER'],
    'host': 'database',
    'password': os.environ['POSTGRES_PASSWORD']
}
