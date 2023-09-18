#### Inventory management system

To run the project follow instructions:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn main:app --reload
```

To run tests and check coverage:
```
pytests
coverage run -m pytest
coverage report -m  
```

API Documentation:
```
http://127.0.0.1:8000/docs
```