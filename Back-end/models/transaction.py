class TransactionModel:
    def __init__(self, db):
        self.collection = db.collection('transactions')

    def create_transaction(self, transaction_data):
        result = self.collection.add(transaction_data)
        return result.id

    def get_transaction(self, transaction_id):
        transaction = self.collection.document(transaction_id).get()
        return transaction.to_dict()

    def get_all_transactions(self):
        transactions = self.collection.stream()
        return [trans.to_dict() for trans in transactions]

class TokenizationVault:
    def __init__(self, db):
        self.collection = db.collection('token_vault')

    def store_token(self, token, encrypted_data):
        self.collection.document(token).set({'data': encrypted_data})

    def retrieve_token(self, token):
        record = self.collection.document(token).get()
        return record.to_dict() if record.exists else None
