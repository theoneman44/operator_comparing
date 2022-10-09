from sqlalchemy import Column, Integer, String, Boolean
from db import Base, engine


class Tarif(Base):
    __tablename__ = 'tarifs'

    id = Column(Integer, primary_key=True)
    mobile_operator_name = Column(String)
    tarif_name = Column(String)
    price = Column(Integer)
    phone_internet_quantity = Column(Integer)
    unlim_phone_internet = Column(Boolean)
    phone_minutes_quantity = Column(Integer)
    unlim_phone_minutes = Column(Boolean)
    phone_sms_quantity = Column(Integer)
    social_offer_price = Column(Integer)
    messenger_price = Column(Integer)
    music_offer_price = Column(Integer)
    video_offer_price = Column(Integer)
    stream_offer_price = Column(Integer)
    ext_information = Column(String)

    def __repr__(self):
        return f"Tarif {self.id}, {self.mobile_operator_name}, {self.tarif_name}"


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
