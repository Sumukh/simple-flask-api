# Simple Flask API

A quick starting point for small API only flask applications. This is intended for quick flask APIs that may not be developed much more.

# Setup
```
# Optional but recommended:
python3 -m venv env; source env/bin/activate

pip install -r requirements.txt
./run-dev.sh
```

# Production
```
pip install gunicorn
./run-production.sh
```

## Limitations

* No tests
* No folder structure/blueprints for more complex APIs
* No DB integration to query / create records
* No schema / API versioning

