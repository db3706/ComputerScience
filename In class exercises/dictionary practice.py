post2 = dict(message="SS Cotopaxi", language="English")
print(post2)

post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"

print(post2)

print(post2['datetime'])

if 'location' in post2:
	print(post2['location'])
else:
	print("The post does not contain a location value")
    
loc = post2.get('user_id', None)
print(loc)

for key in post2.keys():
	value = post2[key]
	print(key, "=", value)
