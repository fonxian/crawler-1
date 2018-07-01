# -*- coding: UTF-8 -*-

from . import db

class Build(db.Model):
    __tablename__ = 't_build_main'
    company_id = db.Column(db.String,primary_key=True)
    credit_code = db.Column(db.String)
    company_name = db.Column(db.String)
    company_person = db.Column(db.String)
    area = db.Column(db.String)
    business_code = db.Column(db.String)
    address = db.Column(db.String)
    create_time = db.Column(db.DATETIME)
    update_time = db.Column(db.DATETIME)

    def __repr__(self):
        return '<t_build_main %r> ' % self.company_name