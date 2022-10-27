from webapp import db1, db2, create_app

db1.create_all(app=create_app())
db2.create_all(app=create_app())
