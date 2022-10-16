from flask import Flask, render_template, request

from webapp.db import db
from webapp.models import Tarif, Links


def queries(request_result):
    tarifs_list = Tarif.query.filter(Tarif.phone_internet_quantity == request_result['phone_internet_quantity'],
                                     Tarif.phone_minutes_quantity == request_result['phone_minutes_quantity'],
                                     Tarif.phone_sms_quantity == request_result['phone_sms_quantity']
                                     ).all()
    return tarifs_list
