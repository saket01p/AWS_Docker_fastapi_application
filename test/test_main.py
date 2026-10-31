from fastapi.testclient import TestClient
from app.main import myapp
import pytest
# import httpx2

get_url='http://127.0.0.1:8005/welcome'
post_url='http://127.0.0.1:8005/data' 


@pytest.fixture
def client():
    client=TestClient(myapp)
    return client



def test_welcome_user(client):
    response=client.get(get_url)
    assert response.status_code==200
@pytest.mark.parametrize(
        "name,result",[('saket','hey saket your resquest has been received successfully...'),
         ('aman',"hey aman your resquest has been received successfully...")]
)
def test_get_user_data(client,name,result):
    response=client.post(post_url,params={'name':name})
    print(response.json())
    assert response.status_code==200
    assert response.json()==result




