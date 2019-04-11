from django.db import connection


def execute_select_query(query, fetch=None):
    data = None
    with connection.cursor() as cursor:
        cursor.execute(query)
        if fetch and fetch == 'one':
            data = cursor.fetchone()
        else:
            data = cursor.fetchall()

    return data


def execute_update_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)