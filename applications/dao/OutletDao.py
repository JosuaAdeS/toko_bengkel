from applications.lib import PostgresDatabase

def dt_data_outlet(search, offset):
    db = PostgresDatabase()
    query = """
        SELECT
            *
        FROM
            ms_outlet
        WHERE
            phone ILIKE %(search)s OR
            outlet_name ILIKE %(search)s OR
            address ILIKE %(search)s
    """
    param = {
        "search": f"%{search}%",
        "offset": offset
    }

    return db.execute_dt(query, param, limit=25)

def get_data_outlet_filter(search):
    db = PostgresDatabase()
    query = """
        SELECT
            outlet_id as "ID Outlet", 
            outlet_name as "Nama Outlet", 
            address as "Alamat", 
            phone as "Nomor Telepon"
        FROM
            ms_outlet
        WHERE
            phone ILIKE %(search)s OR
            outlet_name ILIKE %(search)s OR
            address ILIKE %(search)s
    """
    param = {
        "search": f"%{search}%"
    }

    return db.execute(query, param)


def update_data_outlet(data):
    db = PostgresDatabase()
    query = """
        UPDATE 
            ms_outlet
        SET
            outlet_name = %(outlet_name)s,
            address = %(address)s,
            phone = %(phone)s
        WHERE
            outlet_id = %(outlet_id)s
    """
    param = data

    return db.execute(query, param)

def delete_data_outlet(id):
    db = PostgresDatabase()
    query = """
        DELETE
        FROM 
            ms_outlet
        WHERE
            outlet_id = %(id)s
    """
    param = {
        "id" : id
    }

    return db.execute(query, param)

def add_data_outlet(data):
    db = PostgresDatabase()
    query = """
        INSERT INTO 
            ms_outlet 
                (outlet_id, outlet_name, phone, address) 
        VALUES 
                (%(outlet_id)s, %(outlet_name)s, %(phone)s, %(address)s);
    """
    param = data

    return db.execute(query, param)

def check_id_outlet(id):
    db = PostgresDatabase()
    query = """
        SELECT
            outlet_id
        FROM
            ms_outlet
        WHERE
            outlet_id = %(id)s
    """
    param = {'id': id }
    return db.execute(query, param)


def get_all_outlet():
    db = PostgresDatabase()
    query = """
        SELECT
            *
        FROM
            ms_outlet
        ORDER BY
            outlet_name
    """
    return db.execute(query)