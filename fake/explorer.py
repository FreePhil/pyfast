from model.explorer import Explorer

_explorers = [
    Explorer(name='Clade Hande',
             country='fr',
             description='scarce during full moon'),
    Explorer(name='Noah Weiser',
             country='DE',
             description='Myopic machete man'),
]


def get_all() -> list[Explorer]:
    '''return all explorers'''
    return _explorers


def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None


def create(explorer: Explorer) -> Explorer:
    return explorer


def modify(explorer: Explorer) -> Explorer:
    return explorer


def replace(explorer: Explorer) -> Explorer:
    return explorer


def delete(name: str) -> bool:
    return None
