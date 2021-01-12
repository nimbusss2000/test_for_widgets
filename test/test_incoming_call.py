# -*- coding: utf-8 -*-

def test_incoming_missing(app):  # для входящего с неизвестного номера
    old_deals = app.deal.get_deal_list()
    app.deal.wait_incoming_call()
    new_deals = app.deal.get_deal_list()
    assert len(old_deals) + 1 == len(new_deals)