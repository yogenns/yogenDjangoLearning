import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','yogenDjango.settings')
import django
django.setup()

import random
from yogenapp.models import AccessRecord,Topic,WebPage
from faker import Faker

fakegen = Faker()
topics = ['Search','Sales','News','Entertainment','Economy']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        topic = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.name()

        webpage = WebPage.objects.get_or_create(topic=topic,url=fake_url,name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpage,date=fake_date)[0]


if __name__ == "__main__":
    print("Populate")
    populate(20)
    print("Done")