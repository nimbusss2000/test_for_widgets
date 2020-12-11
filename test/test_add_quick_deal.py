# -*- coding: utf-8 -*-

from model.deal import Deal


def test_add_quick_deal(app):
    app.deal.create(Deal(deal_name="testt2", contact_name="test_namet2", company_name="test_company21"))
    app.session.logout()

