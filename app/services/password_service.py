from sqlalchemy.orm import Session
from app.db.models.password import Password
from app.core.security import hash_password
from app.schemas.password import PasswordCreate, PasswordUpdate


def create_password(db: Session, user_id: int, password_data: PasswordCreate):
    encrypted_password = hash_password(password_data.password)

    url_as_string = str(password_data.url) if password_data.url else None

    new_password = Password(
        user_id=user_id,
        service_name=password_data.service_name,
        username=password_data.username,
        password_encrypted=encrypted_password,
        notes=password_data.notes,
        url=url_as_string,
    )
    db.add(new_password)
    db.commit()
    db.refresh(new_password)
    return new_password


def list_passwords(db: Session, user_id: int):
    return db.query(Password).filter(Password.user_id == user_id).all()

def edit_password(db: Session, user_id: int, password_id: int, password_data: PasswordUpdate):
    password = db.query(Password).filter(Password.id == password_id, Password.user_id == user_id).first()

    if not password:
        return None
    
    update_data = password_data.model_dump(exclude_unset=True)

    if "password" in update_data:
        update_data["password_encrypted"] = hash_password(update_data.pop("password"))

    if "url" in update_data and update_data["url"] is not None:
        update_data["url"] = str(update_data["url"])

    for key, value in update_data.items():
        setattr(password, key, value)

    db.commit()
    db.refresh(password)
    return password
