from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, Any

from ..database import get_db as get_session
from ..models.user_profile import UserProfile, UserProfileUpdate
from ..services.auth_service import get_current_active_user # Assuming this function exists or will be created

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get("/me", response_model=UserProfile)
async def read_users_me(current_user: UserProfile = Depends(get_current_active_user)):
    return current_user


@users_router.put("/me", response_model=UserProfile)
async def update_users_me(
    user_update: UserProfileUpdate,
    current_user: UserProfile = Depends(get_current_active_user),
    session: AsyncSession = Depends(get_session),
):
    for key, value in user_update.dict(exclude_unset=True).items():
        if key == "profile_data" and value is not None:
            # Merge profile_data instead of overwriting
            current_user.profile_data.update(value)
        else:
            setattr(current_user, key, value)

    session.add(current_user)
    await session.commit()
    await session.refresh(current_user)
    return current_user
