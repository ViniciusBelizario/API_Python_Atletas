from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from workout_api.contrib.models import BaseModel

class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamento'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(255), nullable=False)
    proprietario: Mapped[str]= mapped_column(String(30), nullable=False)
    atletas: Mapped[list['AtletaModel']] = relationship("AtletaModel", back_populates='centro_treinamento')


