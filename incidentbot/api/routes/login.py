from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from incidentbot.api import crud
from incidentbot.api.deps import (
    CurrentUser,
    SessionDep,
)
from incidentbot.configuration.settings import settings
from incidentbot.models.database import Token, UserPublic
from incidentbot.util.security import create_access_token
from typing import Annotated, Any

router = APIRouter()


@router.post("/login/access-token")
def login_access_token(
    session: SessionDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    """
    OAuth2 compatible token login, get an access token for future requests
    """

    user = crud.authenticate(
        session=session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect email or password"
        )
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return Token(
        access_token=create_access_token(
            user.id, expires_delta=access_token_expires
        )
    )


@router.post("/login/test-token", response_model=UserPublic)
def test_token(current_user: CurrentUser) -> Any:
    """
    Test access token
    """

    return current_user
