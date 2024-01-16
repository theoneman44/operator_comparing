from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tarif_3in1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mobile_operator_name = db.Column(db.String, nullable=True)
    tarif_name = db.Column(db.String, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    phone_internet_qty = db.Column(db.Integer, nullable=True)
    phone_minutes_qty = db.Column(db.Integer, nullable=True)
    phone_sms_qty = db.Column(db.Integer, nullable=True)
    social_offer_price = db.Column(db.Integer, nullable=True)
    messenger_price = db.Column(db.Integer, nullable=True)
    music_offer_price = db.Column(db.Integer, nullable=True)
    video_offer_price = db.Column(db.Integer, nullable=True)
    ext_information = db.Column(db.Text, nullable=True)
    family_num = db.Column(db.Integer, nullable=True)
    internet_speed = db.Column(db.Integer, nullable=True)
    traffic_qty = db.Column(db.Integer, nullable=True)
    channels_qty = db.Column(db.Integer, nullable=True)
    tv_name = db.Column(db.String, nullable=True)
    page_link = db.Column(db.String, nullable=True)

    # метод представления базы данных при выводе
    def __repr__(self) -> str:
        return f"Tarif {self.mobile_operator_name}, {self.tarif_name}, {self.price}"
