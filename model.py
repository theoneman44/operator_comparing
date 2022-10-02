from sqlalchemy import Column, Integer, String

from db import Base, engine


class Tarif(Base):
    __tablename__ = 'tarifs'

    id = Column(Integer, primary_key=True)
    mobile_operator_name = Column(String)
    tarif_name = Column(String)
    package_offer = Column(String)
    tarif_change = Column(String)
    price = Column(String)
    phone_internet = Column(String)
    phone_minutes = Column(String)
    phone_sms = Column(String)
    social_offer = Column(String)
    music_offer = Column(String)
    video_offer = Column(String)
    stream_offer = Column(String)
    ext_information = Column(String)

    def __repr__(self):
        return f"Tarif {self.id}, {self.mobile_operator_name}, {self.tarif_name}"


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
