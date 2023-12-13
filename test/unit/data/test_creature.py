import os
import pytest
from model.creature import Creature
from errors import Missing, Duplicate

os.environ['CRYPTID_SQLITE_DB'] = ':memory:'
from data import creature


@pytest.fixture
def sample() -> Creature:
    return Creature(name='yeti', country='CN', area='Himalaya', description='Abominable Snowman', aka='what else')


def test_model():
    data = Creature(name='yeti', country='CN', description='Abominable Snowman', aka='what else', area='Himalaya')
    assert data is not None


def test_create(sample):
    response = creature.create(sample)
    assert response == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        creature.create(sample)


def test_modify_missing():
    non_existent = Creature(name='snurf', country='CN', area='', description='some thing', aka='what else')
    with pytest.raises(Missing):
        creature.modify(non_existent.name, non_existent)
