from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from webapp.db import Base, engine


class Links(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    mobile_operator_name = Column(String, nullable=False)
    tarif_name = Column(String, nullable=False)
    page_link = Column(Text, nullable=False)
    tarif = relationship("Tarif", back_populates="link",lazy="joined")

    # метод представления базы данных при выводе
    def __repr__(self):
        return f"Tarif {self.mobile_operator_name}, {self.tarif_name}, link: {self.page_link}"


class Tarif(Base):
    __tablename__ = 'tarifs'
    id = Column(Integer, primary_key=True)
    link_id = Column(Integer, ForeignKey(Links.id), index=True, nullable=False)
    mobile_operator_name = Column(String, nullable=False)
    tarif_name = Column(String, nullable=False)
    price = Column(Integer, nullable=True)
    phone_internet_quantity = Column(Integer, nullable=True)
    unlim_phone_internet = Column(Boolean, nullable=True)
    phone_minutes_quantity = Column(Integer, nullable=True)
    unlim_phone_minutes = Column(Boolean, nullable=True)
    phone_sms_quantity = Column(Integer, nullable=True)
    social_offer_price = Column(Integer, nullable=True)
    messenger_price = Column(Integer, nullable=True)
    music_offer_price = Column(Integer, nullable=True)
    video_offer_price = Column(Integer, nullable=True)
    stream_offer_price = Column(Integer, nullable=True)
    ext_information = Column(Text, nullable=True)
    link = relationship("Links", back_populates="tarif", lazy="joined")

    # метод представления базы данных при выводе
    def __repr__(self):
        return f"Tarif {self.mobile_operator_name}, {self.tarif_name}, {self.price}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
