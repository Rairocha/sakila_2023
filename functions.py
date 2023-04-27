import pandas as pd
from sqlalchemy import text

#Data gathering step: Extracting the data 
def get_daily_rentals(engine):

    query = '''SELECT 
    inventory.store_id,
    DATE(rental_date) as data,
    COUNT(rental_id) as qtd_alugueis
    FROM inventory 
    JOIN rental ON inventory.inventory_id = rental.inventory_id
    WHERE YEAR(rental_date) = 2005
    GROUP BY store_id, data;'''
 
    data = pd.read_sql(text(query), engine)
    return data

def get_benefits(engine):
 
    query = '''SELECT 
	store_id,
    SUM(amount)
    FROM payment
    JOIN staff ON staff.staff_id = payment.staff_id
    GROUP BY store_id;
    '''
 
    data = pd.read_sql(text(query), engine)
    return data

def get_movies(engine):
    query_primeira_possibilidade="""WITH store_1 AS
(SELECT 
	title,
    store_id
FROM film 
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.rental_id
WHERE store_id = 1
GROUP BY title,store_id
ORDER BY COUNT(*) DESC
LIMIT 5),
store_2 AS
(SELECT 
	title,
    store_id
FROM film 
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.rental_id
WHERE store_id = 2
GROUP BY title,store_id
ORDER BY COUNT(*) DESC
LIMIT 5)

SELECT * FROM store_1
UNION
SELECT * FROM store_2;"""
    query = '''WITH tabela_agrupada AS
(SELECT 
	title,
    store_id,
    COUNT(*) contagem
FROM film 
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.rental_id
GROUP BY title,store_id)

,tabela_numerada AS
(SELECT 
*, 
ROW_NUMBER() OVER(PARTITION BY store_id ORDER BY store_id, contagem DESC) as numero
FROM tabela_agrupada)

SELECT title,store_id FROM tabela_numerada WHERE numero<=5
;'''
    data = pd.read_sql(text(query), engine)
    return data

