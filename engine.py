from sqlalchemy import create_engine

def get_engine(password):  
    #from sqlalchemy import create_engine
    # We create the connection
    connection_string = 'mysql+pymysql://root:' + password + '@localhost/sakila'
    engine = create_engine(connection_string)
    return engine
