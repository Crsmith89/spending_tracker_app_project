import pdb

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

merchant_1 = Merchant("Tesco Superstore", "Inverurie")
merchant_repository.save(merchant_1)
print(merchant_1)

merchant_2 = Merchant("Amazon", "Online purchase")
merchant_repository.save(merchant_2)
print(merchant_2)

merchant_3 = Merchant("Marine Bar", "Buckie")
merchant_repository.save(merchant_3)
print(merchant_3)

tag_1 = Tag("Groceries", "Weekly grocery shop")
tag_repository.save(tag_1)

tag_2 = Tag("Online Purchase", "Monitor")
tag_repository.save(tag_2)

tag_3 = Tag("Food & Drink", "Social event")
tag_repository.save(tag_3)

# transaction_1 = Transaction(merchant_1, 50.55, "2021-03-12")
# transaction_repository.save(transaction_1)

# transaction_2 = Transaction(merchant_2, 199.99, "2021-05-16")
# transaction_repository.save(transaction_2)

# transaction_3 = Transaction(merchant_3, 90.56, "2021-06-18")
# transaction_repository.save(transaction_3)

# pdb.set_trace() 