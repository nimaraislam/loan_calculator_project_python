from app.services.database import Database
from app.services.file_service import TEST_DB_PATH, write_db
from starlette.testclient import TestClient
from app.routers.loans import router
from fastapi import FastAPI

test_app = FastAPI()
router.database = Database(db_path=TEST_DB_PATH)
test_app.include_router(router)
client = TestClient(test_app)

def test_save_loan_api():
    response = client.post("/loans", json={
        "principal_amount": 123456,
        "interest_rate": 3,
        "term": 2,
        "month_or_year": "Y"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 2
    assert data["principal_amount"] == 123456

def test_get_a_loan_details_by_id_api():
   response= client.get("/loans/1")
   assert response.status_code == 200
   data = response.json()
   assert data["id"] == 1

def test_update_api():
     reponse = client.put("/loans/2",json={
        "principal_amount": 10000,
        "interest_rate": 3,
        "term": 2,
        "month_or_year": "Y"
    })
     assert reponse.status_code == 200
     data = reponse.json()
     assert data["id"] == 2
     assert data["principal_amount"] ==  10000

def test_save_loan_dlt_api():
    response = client.post("/loans", json={
        "principal_amount": 3000,
        "interest_rate": 3,
        "term": 2,
        "month_or_year": "M"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 3

def test_delete_api():
    response= client.delete("/loans/3")
    assert response.status_code == 200