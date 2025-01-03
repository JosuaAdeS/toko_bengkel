from applications.lib import PostgresDatabase

def dt_data_member(search, offset):
    db = PostgresDatabase()
    query = """
        SELECT
            member_id,
            member_name,
            phone,
            address
        FROM
            ms_member
        WHERE
            CAST(member_id AS TEXT) ILIKE %(search)s OR
            member_name ILIKE %(search)s OR
            phone ILIKE %(search)s 
        ORDER BY
            member_name;
    """
    param = {
        "search": f"%{search}%",
        "offset": offset
    }

    return db.execute_dt(query, param, limit=25)

def get_data_member_filter(search):
    db = PostgresDatabase()
    query = """
        SELECT
            member_id as "ID Pelanggan",
            member_name "Nama Pelanggan",
            phone "Nomor Telepon",
            address "Alamat"
        FROM
            ms_member
        WHERE
            CAST(member_id AS TEXT) ILIKE %(search)s OR
            member_name ILIKE %(search)s OR
            phone ILIKE %(search)s 
        ORDER BY
            member_name;
    """
    param = {
        "search": f"%{search}%"
    }

    return db.execute(query, param)

def update_data_member(data):
    db = PostgresDatabase()
    query = """
        UPDATE 
            ms_member
        SET
            member_name = %(name)s,
            phone = %(phone)s,
            address = %(addr)s
        WHERE
            member_id = %(id)s
    """
    param = {
        "name" : data['name'],
        "phone" : data['phone'],
        "addr" : data['addr'],
        "id" : data['id']
    }

    return db.execute(query, param)

def delete_data_member(id):
    db = PostgresDatabase()
    query = """
        DELETE
        FROM 
            ms_member
        WHERE
            member_id = %(id)s
    """
    param = {
        "id" : id
    }

    return db.execute(query, param)

def add_data_member(data):
    db = PostgresDatabase()
    query = """
        INSERT INTO 
            ms_member 
                (member_name, phone, address) 
        VALUES 
                (%(member_name)s, %(phone)s, %(address)s);

    """
    param = data

    return db.execute(query, param)

def check_id_member(id):
    db = PostgresDatabase()
    query = """
        SELECT
            member_id
        FROM
            ms_member
        WHERE
            member_id = %(id)s
    """
    param = {'id': id }
    return db.execute(query, param)

def get_all_member():
    db = PostgresDatabase()
    query = """
        SELECT
            member_name nama_member,
            phone telepon,
            address alamat
        FROM
            ms_member
        ORDER BY
            member_name;
    """
    return db.execute(query)