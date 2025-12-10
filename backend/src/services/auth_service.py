from typing import Optional, Tuple
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlmodel import Session, select
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from backend.src.models.user_profile import UserProfile, UserProfileCreate
from backend.src.config import settings
from backend.src.database import get_db as get_session

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT settings
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signin")

async def get_current_user(session: Session = Depends(get_session), token: str = Depends(oauth2_scheme)) -> UserProfile:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await AuthService(session).get_user_by_email(email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: UserProfile = Depends(get_current_user)):
    return current_user


class AuthService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def get_user_by_email(self, email: str) -> Optional[UserProfile]:
        statement = select(UserProfile).where(UserProfile.email == email)
        result = await self.db_session.execute(statement)
        return result.scalar_one_or_none()

    async def signup(self, user_data: UserProfileCreate) -> Optional[UserProfile]:
        existing_user = await self.get_user_by_email(user_data.email)
        if existing_user:
            return None  # User with this email already exists

        hashed_password = get_password_hash(user_data.password)

        user_profile = UserProfile(
            email=user_data.email,
            auth_provider_id="betterauth_default",  # Placeholder
            full_name=user_data.full_name,
            password_hash=hashed_password,
            profile_data=user_data.profile_data if user_data.profile_data else {},
        )
        self.db_session.add(user_profile)
        await self.db_session.commit()
        await self.db_session.refresh(user_profile)
        return user_profile

    async def signin(self, email: str, password: str) -> Optional[Tuple[str, str]]:
        user = await self.get_user_by_email(email)
        if not user or not self.verify_password(password, user.password_hash):
            return None

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return access_token, "bearer"
