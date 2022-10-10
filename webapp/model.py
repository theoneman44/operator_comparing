from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tarif(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mobile_operator_name = db.Column(db.String, nullable=True)
    tarif_name = db.Column(db.String, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    phone_internet_quantity = db.Column(db.Integer, nullable=True)
    unlim_phone_internet = db.Column(db.Boolean, nullable=True)
    phone_minutes_quantity = db.Column(db.Integer, nullable=True)
    unlim_phone_minutes = db.Column(db.Boolean, nullable=True)
    phone_sms_quantity = db.Column(db.Integer, nullable=True)
    social_offer_price = db.Column(db.Integer, nullable=True)
    messenger_price = db.Column(db.Integer, nullable=True)
    music_offer_price = db.Column(db.Integer, nullable=True)
    video_offer_price = db.Column(db.Integer, nullable=True)
    stream_offer_price = db.Column(db.Integer, nullable=True)
    ext_information = db.Column(db.Text, nullable=True)

    # метод представления базы данных при выводе
    def __repr__(self):
        return f"Tarif {self.mobile_operator_name}, {self.tarif_name}, {self.price}"
