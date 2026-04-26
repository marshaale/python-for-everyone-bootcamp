phonebook = {
    "john":"123456",
    "doe":"2345768",
    "sara":"0916372",
    "ali":"91038101"
}

print("contact of sara:",phonebook.get("sara","unknown"))

print("contact of jane",phonebook.get("jane","unknown"))

for name in phonebook:
    print(name,phonebook.get(name,"unknown"))