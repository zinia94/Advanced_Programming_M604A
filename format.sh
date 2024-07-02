source env/bin/activate
python3 -m black .
python3 -m black src
python3 -m black test
python3 -m black app.py