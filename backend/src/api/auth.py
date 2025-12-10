from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta

from backend.src.database import get_db as get_session
from backend.src.services.auth_service import AuthService, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from backend.src.models.user_profile import UserProfileCreate, UserProfile
from backend.src.config import settings

auth_router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signin") # Updated tokenUrl


@auth_router.post("/signup", response_model=UserProfile)
async def signup(user_data: UserProfileCreate, session: AsyncSession = Depends(get_session)):
    auth_service = AuthService(session)
    user = await auth_service.signup(user_data)
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")


@auth_router.post("/signin")
async def signin(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)):
    auth_service = AuthService(session)
    token_data = await auth_service.signin(form_data.username, form_data.password)

    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token, token_type = token_data
    return {"access_token": access_token, "token_type": token_type}
