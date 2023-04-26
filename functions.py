import pandas as pd
from sqlalchemy import text

#Data gathering step: Extracting the data 
def get_daily_rentals(engine):

    query = '''escrever a query adequada'''
 
    data = pd.read_sql(text(query), engine)
    return data

def get_benefits(engine):
 
    query = '''escrever a query adequada'''
 
    data = pd.read_sql(text(query), engine)
    return data

def get_movies(engine):

    query = '''escrever a query adequada'''
    data = pd.read_sql(text(query), engine)
    return data

