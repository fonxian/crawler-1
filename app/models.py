# -*- coding: UTF-8 -*-

from . import db

class Build(db.Model):
    __tablename__ = 't_build_main'
    company_id = db.Column(db.String,primary_key=True)
    credit_code = db.Column(db.String)
    company_name = db.Column(db.String)
    company_person = db.Column(db.String)
    area = db.Column(db.String)
    reg_type = db.Column(db.String)
    address = db.Column(db.String)
    create_time = db.Column(db.DATETIME)
    update_time = db.Column(db.DATETIME)

    def __repr__(self):
        return '<t_build_main %r> ' % self.company_name


class BuildRegister(db.Model):
    __tablename__ = 't_build_register'
    company_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, primary_key=True)
    id_card = db.Column(db.String, primary_key=True)
    reg_type = db.Column(db.String)
    reg_code = db.Column(db.String)
    reg_profession = db.Column(db.String)
    create_time = db.Column(db.DATETIME)
    update_time = db.Column(db.DATETIME)

    def __repr__(self):
        return '<t_build_register %r> ' % self.name

class BuildBusinessRight(db.Model):
    __tablename__ = 't_build_business_right'
    company_id = db.Column(db.String, primary_key=True)
    right_type = db.Column(db.String)
    right_code = db.Column(db.String)
    right_name = db.Column(db.String)
    sign_time = db.Column(db.DATETIME)
    effetive_time = db.Column(db.DATETIME)
    sign_org = db.Column(db.String)
    create_time = db.Column(db.DATETIME)
    update_time = db.Column(db.DATETIME)

    def __repr__(self):
        return '<t_build_business_right %r> ' % self.right_name



class BuildProject(db.Model):
    __tablename__ = 't_build_project'
    company_id = db.Column(db.String, primary_key=True)
    project_id = db.Column(db.String,primary_key=True)
    project_name = db.Column(db.String,primary_key=True)
    area = db.Column(db.String)
    type = db.Column(db.String)
    unit_name = db.Column(db.String)
    create_time = db.Column(db.DATETIME)
    update_time = db.Column(db.DATETIME)

    def __repr__(self):
        return '<t_build_project %r> ' % self.project_name

class BadBehavior(db.Model):
    __tablename__ = 't_bad_behavior'
    company_id = db.Column(db.String, primary_key=True)
    bad_id = db.Column(db.String, primary_key=True)
    bad_entity = db.Column(db.String, primary_key=True)
    content = db.Column(db.String)
    dept = db.Column(db.String)
    effective_time = db.Column(db.DATETIME)
    create_time = db.Column(db.DATETIME)
    update_time = db.Column(db.DATETIME)

    def __repr__(self):
        return '<t_bad_behavior %r> ' % self.bad_entity

class GoodBehavior(db.Model):
    pass

class Black(db.Model):
    __tablename__ = 't_black'
    company_id = db.Column(db.String, primary_key=True)
    black_entity = db.Column(db.String, primary_key=True)
    content = db.Column(db.String)
    dept = db.Column(db.String)
    black_time = db.Column(db.DATETIME)
    remove_time = db.Column(db.DATETIME)
    create_time = db.Column(db.DATETIME)
    update_time = db.Column(db.DATETIME)

    def __repr__(self):
        return '<t_black %r> ' % self.black_entity
