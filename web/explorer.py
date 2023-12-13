from fastapi import APIRouter, HTTPException

from errors import Missing, Duplicate
from model.explorer import Explorer
from service import explorer as service

router = APIRouter(prefix='/explorer')


@router.get('')
@router.get('/')
def get_all() -> list[Explorer]:
    return service.get_all()


@router.get('/{name}')
def get_one(name) -> Explorer:
    try:
        return service.get_one(name)
    except Missing as exception:
        raise HTTPException(status_code=404, detail=exception.msg)


@router.post('/')
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as exception:
        raise HTTPException(status_code=404, detail=exception.msg)


@router.patch('/')
def modify(explorer: Explorer) -> Explorer:
    try:
        return service.modify(explorer)
    except Missing as exception:
        raise HTTPException(status_code=404, detail=exception.msg)


@router.delete('/{name}', status_code=204)
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exception:
        raise HTTPException(status_code=404, detail=exception.msg)


@router.put('/{name}')
def replace(explorer: Explorer) -> Explorer:
    return service.replace(explorer)


