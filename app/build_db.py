# -*- coding: UTF-8 -*-

from app.models import *
import datetime



def insert_build_main(company_id,credit_code,company_name,company_person,area,reg_type, address):
    build = Build().query.filter_by(company_id=company_id).first()
    if build is None:

        t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        build = Build(
            company_id = company_id,
            credit_code = credit_code,
            company_name = company_name,
            company_person = company_person,
            area = area,
            reg_type = reg_type,
            address = address,
            create_time = t,
            update_time = t
        )

        db.session.add(build)
        db.session.commit()

    else:
        print('记录已存在')


def insert_build_register():
    pass


def insert_build_right():
    pass


