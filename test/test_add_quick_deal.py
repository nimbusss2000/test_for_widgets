# -*- coding: utf-8 -*-

from model.deal import Deal


def test_add_quick_deal(app):
    old_deals = app.deal.get_deal_list()
    app.deal.create(Deal(deal_name="Python_test", contact_name="contact_name", company_name="company_name"))
    new_deals = app.deal.get_deal_list()
    assert len(old_deals) + 1 == len(new_deals)



