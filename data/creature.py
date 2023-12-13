import sqlite3
from .init import conn, curs
from model.creature import Creature

curs.execute('''
    create table if not exists creature(
        name text primary key,
        description text,
        country text,
        area text,
        aka text)
''')


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(name, description, country, area, aka)


def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()


def get_one(name: str) -> Creature:
    qry = 'select * from creature where name=:name'
    params = {'name': name}
    curs.execute(qry, params)
    return row_to_model(curs.fetchone())


def get_all(name: str) -> list[Creature]:
    qry = 'select * from creature'
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


def create(creature: Creature) -> Creature:
    query = 'insert into creature values(:name, :description, :country, :area, :aka)'
    params = model_to_dict(creature)
    curs.execute(query, params)
    return get_one(creature.name)


def modify(creature: Creature):
    query = '''
        update creature 
        set country = :country, name = :name, area = :area, aka = :aka
        where name = :name_original
    '''
    params = model_to_dict(creature)
    params['name_original'] = creature.name
    _ = curs.execute(query, params)
    return get_one(creature.name)


def replace(creature: Creature):
    return creature


def delete(creature: Creature) -> bool:
    query = 'delete from creature where name = :name'
    params = {'name': creature.name}
    result = curs.execute(query, params)
    return bool(result)

