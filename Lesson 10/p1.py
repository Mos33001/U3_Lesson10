import time
print("-" * 80)
print("Life Decison Bot:")

password = input("Are you hungry? ")
time.sleep(1)
if password.lower() == "yes":
	time.sleep(1)
	print("Then go get food.")
	time.sleep(1)
	print("Unless you aint got no money. Then tough luck.")
else:
	print("Not hungry?")
	time.sleep(1)
	print("You should still get food.")
	time.sleep(1)
	print("Foods great.")