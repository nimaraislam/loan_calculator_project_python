from app.services.database import Database
from app.services.loan_service import Loan
from app.schemas.loan_schema import LoanSchema,LoanUpdateSchema
from starlette.testclient import TestClient
from app.main import app
from app.routers.loans import router
from fastapi import FastAPI
from app.services.database import Database
from app.services.file_service import TEST_DB_PATH, write_db
test_app = FastAPI()
router.database = Database(db_path=TEST_DB_PATH)
test_app.include_router(router)
client = TestClient(test_app)

#def test_create_loan():
#    new_loan = {
#        "principal_amount": 2000,
#        "interest_rate": 3,
#        "term": 2,
#        "month_or_year": "M"
#    }
#    response = client.post("/loans", json=new_loan)
#    assert response.status_code == 200
#    data = response.json()
#    assert data["id"] == 2  # new loan id should be 2
#    assert data["principal_amount"] == 2000

#def test_get_a_loan_details_by_id_api():
#   response= client.get("/loans/1")
#    assert response.status_code == 200
#    data = response.json()
#    assert data["id"] == 1

#def test_create_todo(client):
#    reponse = client.post("/todos",json={
#        "title": "Learn FastAPI",
#        "description": "Study basics",
#        "completed": False
#    })
#    assert reponse.status_code == 200
#    data = reponse.json()
#    assert data["title"] == "Learn FastAPI"
#    assert data["description"] == "Study basics"
#    assert data["completed"] == False
#    assert "id" in data