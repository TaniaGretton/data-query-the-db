# pylint:disable=C0111,C0103

def query_orders(db):
    query = """
    SELECT *
    FROM Orders
    ORDER BY OrderID"""
    db.execute(query)
    orders = db.fetchall()
    return orders

def get_orders_range(db, date_from, date_to):
    query = """
    SELECT *
    FROM Orders
    WHERE OrderDate > ? AND OrderDate <= ?
    """
    db.execute(query, (f'{date_from}', f'{date_to}'))
    orders_range = db.fetchall()
    return orders_range
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)


def get_waiting_time(db):
    query = """
    SELECT *, (julianday(ShippedDate) - julianday(OrderDate)) AS TimeDelta
    FROM Orders
    ORDER BY TimeDelta
    """
    db.execute(query)
    orders_time = db.fetchall()
    return orders_time
