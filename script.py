import codecademylib
import pandas as pd
inventory = pd.read_csv("inventory.csv")
print(inventory.head(10))
staten_island = inventory.iloc[:9]
product_request = staten_island.product_description
seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]
print(seed_request)
inventory["In stock"] = inventory.quantity.apply(lambda x: True if x > 0 else False)
print(inventory)

inventory["total_value"] = inventory.price * inventory.quantity
print(inventory)
inventory["full_description"] = inventory.apply(lambda row: \
                "{} - {}".format(row.product_type, row.product_description), axis = 1)
print(inventory)