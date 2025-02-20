import requests
import pytest

URL = "http://0.0.0.0:8080"

test_data = {
    "fixed_acidity": 7.4,
    "volatile_acidity": 0.7,
    "citric_acid": 0.0,
    "residual_sugar": 1.9,
    "chlorides": 0.076,
    "free_sulfur_dioxide": 11.0,
    "total_sulfur_dioxide": 34.0,
    "density": 0.9978,
    "pH": 3.5,
    "sulphates": 0.56,
    "alcohol": 9.4
}

def test_predict_endpoint():
    response = requests.post(
        f"{URL}/predict",
        headers={
            "accept": "application/json",
            "Content-Type": "application/json",
        },
        json=test_data
    )

    assert response.status_code == 200, f"Ошибка {response.status_code}"
    result = response.json()["result"]
    assert result == 0, f"Ожидался результат 0, модель выдала - {result}"
