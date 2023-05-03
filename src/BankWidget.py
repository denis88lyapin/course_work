
class BankWidget:
    def __int__(self, date, description, from_, to, operationAmount):
        self.date = date
        self.description = description
        self.from_ = from_
        self.to = to
        self.operationAmount = operationAmount

    def __repr__(self):
        return f"" \
               f"{self.__class__.__name__}\n" \
               f"date = {self.date}\n" \
               f"description = {self.description}\n" \
               f"from_ = {self.from_}\n" \
               f"to = {self.to}\n" \
               f"operationAmount = {self.operationAmount}"
    def get_transaction(self):
        return f"{self.date} {self.description} 
