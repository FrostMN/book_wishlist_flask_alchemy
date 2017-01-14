###Basic Flask and SQLAlchemy app. Book reading wishlist. 

Setup

Set up virtual environment, Mac

```
virtualenv -p python3 venv
source venv/bin/activate
```

Set up virtual environment, PC

```
virtualenv venv
venv/bin/activate
```

Install requirements

```
pip install -r requirements.txt
```

Set up database - start Python console

```
python
```

And type the following into the console

```
from app import db
from models import *
db.create_all()
```

Configure Flask environment variables, Mac

```
export $FLASK_APP=app.py
export $FLASK_DEBUG=1
```

Configure Flask environment variables, PC

```
set FLASK_APP=app.py
set FLASK_DEBUG=1
```

Run app

```
flask run
```

App should be at 127.0.0.1:5000
