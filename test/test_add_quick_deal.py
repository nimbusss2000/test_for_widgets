# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.deal import Deal


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Deal(deal_name=random_string('Сделка_', 5), contact_name=random_string('Контакт_', 6),
                 company_name=random_string('Компания_', 6)) for i in range(2)]


@pytest.mark.parametrize('deal', testdata, ids=[repr(x) for x in testdata])
def test_add_quick_deal(app, deal):
    old_deals = app.deal.get_deal_list()
    app.deal.create(deal)
    assert len(old_deals) + 1 == app.deal.count()
    new_deals = app.deal.get_deal_list()
    old_deals.append(deal)
    assert sorted(old_deals, key=Deal.id_or_max) == sorted(new_deals, key=Deal.id_or_max)




