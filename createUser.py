#Create App Context & DB
from app import create_app, db
import config

app = create_app()
app.app_context().push()
db.create_all()
print("DB created!")

#Create Admin User
from app.models import User
import hashlib

raw_password = 'admintaha'
admin = User(username='admin', password=raw_password, role='admin')
db.session.add(admin)
db.session.commit()
admin.password = admin.hash_password_with_salt(raw_password)
db.session.commit()
print("Admin user created!")
print(f"Users: {User.query.all()}")
