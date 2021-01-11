# -*- coding: utf-8 -*-

def test_outgoing_missing(app):
    old_deals = app.deal.get_deal_list()
    app.deal.create_call_outgoing()
    new_deals = app.deal.get_deal_list()
    assert len(old_deals) + 1 == len(new_deals)




