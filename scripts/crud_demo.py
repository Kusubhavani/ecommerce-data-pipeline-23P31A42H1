from config.database import SessionLocal
from models.user import User
from models.product import Product

session = SessionLocal()

# CREATE
new_user = User(name="David Miller", email="david@mail.com")
session.add(new_user)
session.commit()
print("User inserted")

# READ
users = session.query(User).all()
print("Users:")
for u in users:
    print(u.user_id, u.name, u.email)

# UPDATE
user = session.query(User).filter(User.name == "David Miller").first()
user.name = "David Updated"
session.commit()
print("User updated")

# DELETE
session.delete(user)
session.commit()
print("User deleted")

session.close()
