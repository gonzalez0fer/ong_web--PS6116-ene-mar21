from __future__ import absolute_import, unicode_literals
import urllib
from bs4 import BeautifulSoup
import urllib.request
from celery import shared_task
from datetime import datetime

from apps.main.dollar_rates.models import DollarRate
from apps.main.equipments.models import Equipment
from apps.main.notifications.models import Notifications
from apps.main.users.models import CustomUser

@shared_task
def web_scrapping_BCV():
    url = "http://www.bcv.org.ve/"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    content_dollar = soup.find("div", {"id":"dolar"})
    price = content_dollar.div.strong.text.strip()
    value = float(price.replace('.','').replace(',','.'))
    DollarRate.objects.create(value=value)
    return True

@shared_task
def maintenance_daily_checks():
    equipments = Equipment.objects.all()
    for i in equipments:
        if i.maintenance_date == datetime.today().date():
            total_users = CustomUser.objects.all().order_by('id')
            
            for j in total_users:
                Notifications.objects.create(refectory_id=i.refectory_id,
                        read=False,
                        notification_type='Mantenimiento',
                        notification_message='Mantenimiento pendiente del %s' %(i.name),
                        user_notification_id=j.id,
                        equipment_id=i.id
                )
    return True
