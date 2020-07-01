import os
import click

from glob import glob
from subprocess import call
from app import db
from app.models import(
    Permissions,
    Blog,
    User,
    Role,
    Category
)


import config
from config import Config
from flask import current_app
from flask.cli import with_appcontext
from werkzeug.exceptions import MethodNotAllowed, NotFound


HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)

def register_app(app):
    @app.cli.command('seed-db')
    @click.command()
    def seed():
        print('Starting db seed')
        db.create_all()

        seed_users()
        seed_categories()
        seed_blog()
        

        db.session.commit()
        print('DB seed complete')


def seed_users():
    print('adding roles and admin')
    Role.insert_roles()

    admin = User(
        username='guyaadvocates',
        password=Config.ADMIN_PASSWORD,
        role=Role.query.filter_by(permissions=Permissions.ADMINISTER).first()
    )

    db.session.add(admin)


def seed_categories():
    print('adding categories')
    Role.insert_roles()

    tele = Category(
        name='Telecommunications, Media and Technology Law.'
    )
    comm = Category(
        name='Commercial and Corporate Law.'
    )
    emp = Category(
        name='Employment Law.'
    )
    disp = Category(
        name='Dispute Resolution.'
    )
    cat = Category(
        name='Property Law.'
    )
    priv = Category(
        name='Private Clients.'
    )

    db.session.add(tele)
    db.session.add(comm)
    db.session.add(emp)
    db.session.add(disp)
    db.session.add(cat)
    db.session.add(priv)

def seed_blog():
    print('Adding insights')
    if config.Development:
        baseurl = 'http://localhost:5000/static/'
    else:
        baseurl = '/static/'

    telecom = Blog(
            title = "Telecommunication and Technology Advancements",
            description = "Informed by the unprecedented changes in the sectors of technology, media and telecommunications, Innovation is key, and so tech and telecoms suppliers, and creators and distributors of media, need to protect their investments and maximize their commercial opportunities.Guya Advocates offers advice that is industry specific, and commercially strategic. Whilst we consistently provide advice that is of the highest quality, we take pride in our ability to make even the most complex of matters appear simple and practical.More specifically we advise on",

            image_url = "/static/assets/markus-spiske-iar-afB0QQw-unsplash.jpg",
            category_id = 1
        )
    
    db.session.add(telecom)

    commer = Blog(
            title = "Commercial Enteprises in Regards to law",
            description = " Guya Advocates commercial lawyers provide expert and specialist legal and commercial support for businesses from incorporation to winding up. Without sound corporate law advice, no organization can function at its best. Our passion is driving through business deals to a speedy and successful conclusion. We believe and remain focused on adding value and completing transactions.We deliver results in a full range of corporate and commercial legal areas, including:  ",
            image_url = "/static/assets/abstract-1238932_1920.jpg",
            category_id = 2
        )

    db.session.add(commer)


    emplo = Blog(
            title = "Employment and its Associated practices",
            description = "Employment law is an area of law which touches on every business whether small or large.At Guya Advocates, we help you navigate the wide range of laws and regulations governing all businesses and assist you both before and when disputes arise, as they often do.We provide legal services across sectors in relation to the following",
            image_url = "/static/assets/office-2009693.jpg",
            category_id = 3
        )

    db.session.add(emplo)


    
    dispu = Blog(
            title = "Dispute resolution is not the ens solution",
            description = "Our lawyers recognize that every dispute and every business is different and each will need its own tailored solution to suit your needs. Our advice is practical and commercial but focuses on our clients’ objectives.We recognize that disputes are not all about the courtroom, particularly where our clients are keen to preserve a commercial relationship. We therefore encourage our clients, where appropriate, to explore other quick, practical and cost-effective avenues to resolve their disputes, including mediation or other forms of Alternative Dispute Resolution (ADR), and we shall guide you carefully through that process.Out litigation team handles litigation arising from a wide range of matters including but not limited to",
            image_url = "/static/assets/silhouette-3303823.png",
            category_id = 4
        )

    db.session.add(dispu)


    
    prope = Blog(
            title = "We value property ",
            description = " Our Team Specializes in all areas of property law including commercial and residential conveyancing. Whether you’re purchasing, selling or leasing commercial property, as an owner, occupier, lender, borrower, investor or developer, our real estate team can provide expert advice and help.We work closely with our clients to develop relationships based on trust so that we can fully understand their requirements. Whether we are representing your personal or your business interests, we get to know you thoroughly so that we can offer strategic advice on how to achieve your objectives.",
            image_url = "/static/assets/architecture-1522920.jpg",
            category_id = 5
        )
    

    db.session.add(prope)

    priva = Blog(
            title = "When it Comes to Private Clients",
            description = "Our private client practice area provides legal direction to individuals and families.We provide all round legal services by incorporating other practice areas when handling personal legal issues.Our Private Practice areas encompasses",
            image_url = "/static/assets/hands-699486_1920.jpg",
            category_id = 6
        )

    
    
    db.session.add(priva)