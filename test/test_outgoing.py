# -*- coding: utf-8 -*-

def test_outgoing_missing(app):
    old_deals = app.deal.count()
    app.deal.create_call_outgoing()
    new_deals = app.deal.count()
    assert new_deals == old_deals + 1




