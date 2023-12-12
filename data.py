from model import Creature


creatures: list[Creature] = [
    Creature(name='yeti',
             country='CN',
             area='Himalayas',
             description='Hirsute',
             aka='Abominable Snowman'),
    Creature(name='sasquatch',
             country='US',
             area='*',
             description="Yeti's Cousin Eddie",
             aka='BigFoot')
]


def get_creatures() -> list[Creature]:
    return creatures
