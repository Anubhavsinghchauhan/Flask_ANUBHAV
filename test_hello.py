import pytest
from hello import app

@pytest.fixture
def client():
    return app.test_client() 
        

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.text=="<h1>Loan Approval Application V2!!!</h1>"


def test_predict(client):
    test_data={
    "ApplicantIncome": 100,
    "Credit_History": 1.0,
    "Gender": "Male",
    "LoanAmount": 12,
    "Married": "No"}
    response = client.post('/predict', json=test_data)
    assert response.status_code == 200
    assert response.json == {"loan_approval_status": "Approved"}


