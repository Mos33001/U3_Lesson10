import time
print("-" * 80)
print("Welcome to CLUB425, the most lit club in downtown ACTvF. Before you can enter, I need you to answer some questions...")
print(" ")
x = int(input("What is your age?: "))
time.sleep(1)
if x >= 21:
	print(" ")
	print("You may enter")
else:
	print(" ")
	print("You aren't allowed in. Please leave")


