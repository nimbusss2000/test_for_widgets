
from model.deal import Deal

def test_del_first_deal(app):
    if app.deal.count() == 0:
        app.deal.create(Deal(deal_name='before_del', contact_name='before_del', company_name='before_del'))
    old_deals = app.deal.get_deal_list()
    app.deal.delete_first_deal()
    new_deals = app.deal.get_deal_list()
    assert len(old_deals) - 1 == len(new_deals)
    old_deals = old_deals[1:]
    assert old_deals == new_deals


