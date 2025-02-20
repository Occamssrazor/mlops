# Структура проекта

mlops/          
|- .dvc/           - настройка удаленного хранилища        
|- api/            - сервис и тест предикта       
|- data/           - данные        
|- mlartifacts/    - артефакты млфлоу         
|- mlflow/         - эксперименты и тесты с моделью    
|- mlruns/         - хранилище млфлоу       
|- myenv/          - виртуальное окружение     
.dockerignore      
.gitignore     
.gitlab-ci.yml    
data.dvc 
Dockerfile           
lint.toml       
Model_Experiments_Results.md    
README.md    
requirements.txt    

# Инструкция
> sudo docker build -t mydocker .   

> sudo docker run -d -p 8080:8080 mydocker    

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

#### Модель должна выдать 0. Она выдает 0, когда предсказанное качество ниже 6.5