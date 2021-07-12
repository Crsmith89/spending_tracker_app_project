import pdb

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository



merchant_1 = Merchant("Tesco Superstore", "Inverurie" )
merchant_repository.save(merchant_1)
print(merchant_1)

merchant_2 = Merchant("Amazon", "Online purchase")
merchant_repository.save(merchant_2)
print(merchant_2)

merchant_3 = Merchant("Rangers shop", "Ibrox - Glasgow")
merchant_repository.save(merchant_3)
print(merchant_3)

# tag_1 = Tag("Groceries", "Weekly grocery shop")

# pdb.set_trace() 