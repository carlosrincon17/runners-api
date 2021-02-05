from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(secret: str):
    return pwd_context.hash(secret=secret)


def verify_password(plain_password: str, hashed_password: str):
    print(hashed_password)
    return pwd_context.verify(plain_password, hashed_password)
