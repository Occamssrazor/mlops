> python api/api.py

> curl -X 'POST' \
'http://0.0.0.0:8080/predict' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
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
'

> pytest api/test.py 