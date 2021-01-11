
class Deal:

    def __init__(self, deal_name=None, contact_name=None, company_name=None, id=None):
        self.deal_name = deal_name
        self.contact_name = contact_name
        self.company_name = company_name
        self.id = id

    def __repr__(self):
        return f'{self.id, self.deal_name}'

    def __eq__(self, other):
        return self.id == other.id and self.deal_name == other.deal_name