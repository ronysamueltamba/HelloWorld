customer = {
    "name" : "Rony Samuel Tamba",
    "age" : 21,
    "is_verified" : True
}

customer ["birthday"] = "29 oktober"
print(customer.get("birthday", "29 10 1999"))