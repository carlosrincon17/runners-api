import unittest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
import main


class TestUsers(unittest.TestCase):

    def setUp(self) -> None:
        SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

        engine = create_engine(
            SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )
        Base.metadata.create_all(bind=engine)
        main.SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)
        self.client = TestClient(main.app)

    def test_create_user(self):
        """Test the user is created successfully"""
        mock_user_data = {
            "email": "deadpool@example.com",
            "password": "chimichangas4life",
            "first_name": "Bruno",
            "last_name": "Diaz"
        }
        response = self.client.post(
            "/user/",
            json=mock_user_data,
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["email"] == "deadpool@example.com"
        assert "id" in data

    def test_existing_user_validation(self):
        """Test the unique email validation in user creation"""
        mock_user_data = {
            "email": "deadpool@example.com",
            "password": "chimichangas4life",
            "first_name": "Bruno",
            "last_name": "Diaz"
        }
        response = self.client.post(
            "/user/",
            json=mock_user_data,
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["email"] == "deadpool@example.com"
        response = self.client.post(
            "/user/",
            json=mock_user_data,
        )
        assert response.status_code == 409


if __name__ == '__main__':
    unittest.main()
