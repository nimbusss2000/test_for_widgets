
from model.deal import Deal

def test_del_first_deal(app):
    if app.deal.count() == 0:
        app.deal.create(Deal(deal_name='before_del', contact_name='before_del', company_name='before_del'))
    app.deal.delete_first_deal()


