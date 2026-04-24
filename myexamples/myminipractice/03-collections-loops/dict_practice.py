countries = {"somalia":"Mogadishu","france":"Paris","kenya":"Nairobi"}
print(countries)
print("keys",list(countries.keys()))
print("values",list(countries.values()))

print(countries.get("angola","unknown"))

print("Before edit",countries['france'])

countries['france'] = 'unknown'

print("After edit",countries['france'])