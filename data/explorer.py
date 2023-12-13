from .init import curs
from model.explorer import Explorer

curs.execute('''
    create table if not exists explorer(
        name text primary key,
        country text,
        description text)
''')


def row_to_model(row: tuple) -> Explorer:
    return Explorer(name=row[0], country=row[1], description=row[2])


def model_to_dict(explorer: Explorer) -> dict:
    return explorer.model_dump() if explorer else None


def get_one(name: str) -> Explorer:
    query = 'select * from explorer where name = :name'
    params = {'name': name}
    curs.execute(query, params)
    return row_to_model(curs.fetchone())


def get_all() -> list[Explorer]:
    query = 'select * from explorer'
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def create(explorer: Explorer) -> Explorer:
    query = '''
        insert into explorer (name, country, description)
        values (:name, :country, :description)
    '''
    params = model_to_dict(explorer)
    _ = curs.execute(query, params)
    return get_one(explorer.name)


def modify(name: str, explorer: Explorer) -> Explorer:
    query = '''
        update explorer
        set country = :country, description = :description, name = :name
        where name = :name_original
    '''
    params = model_to_dict(explorer)
    params['name_original'] = name
    _ = curs.execute(query.params)
    return get_one(explorer.name)


def delete(explorer: Explorer) -> bool:
    query = 'delete from explorer where name = :name'
    params = {'name': explorer.name}
    result = curs.execute(query, params)
    return bool(result)