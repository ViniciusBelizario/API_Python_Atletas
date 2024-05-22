from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workout_api.contrib.dependecies import DatabaseDependency
from sqlalchemy.future import select

router = APIRouter()

@router.post(
        path='/', 
        summary='Criar um novo centro de treinamento',
        status_code=status.HTTP_201_CREATED,
        response_model=CentroTreinamentoOut,
        )
        
async def post(
    db_session: DatabaseDependency,
    categoria_in: CentroTreinamentoIn= Body(...)
) -> CentroTreinamentoIn:
    
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **categoria_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())
    
    db_session.add(centro_treinamento_model)
    await db_session.commit()
    
    return centro_treinamento_model

@router.get(
        path='/', 
        summary='Consultar todas as centro treinamento',
        status_code=status.HTTP_200_OK,
        response_model=list[CentroTreinamentoOut],
        )
        
async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:
    centro_treinamentos: list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    return centro_treinamentos

@router.get(
        path='/{id}', 
        summary='Consulta uma centro treinamento pelo id',
        status_code=status.HTTP_200_OK,
        response_model=CentroTreinamentoOut,
        )
        
async def query(id: UUID4, db_session: DatabaseDependency) ->CentroTreinamentoOut:
    centro_treinamento: CentroTreinamentoOut = (
        await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))
        ).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Centro de treinamento não encontrada no id {id}')

    return centro_treinamento