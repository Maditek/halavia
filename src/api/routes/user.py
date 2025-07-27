from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.api.scehmas.user import UserCreate, UserResponse
from src.db.session import get_session
from src.services.user import UserService


router = APIRouter(prefix="/user")


def get_user_service(session: Session = Depends(get_session)) -> UserService:
    return UserService(session)


@router.get("/id", response_model=UserResponse)
async def get_by_id(id: int, service: UserService = Depends(get_user_service)):
    return service.get_by_id(id=id)


@router.post("/", response_model=UserResponse)
async def create(
    user_create: UserCreate, service: UserService = Depends(get_user_service)
):
    return service.create(user_create=user_create)


@router.get("/name", response_model=UserResponse)
async def get_by_name(name: str, service: UserService = Depends(get_user_service)):
    return service.get_by_name(name=name)
