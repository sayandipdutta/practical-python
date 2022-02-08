# bounce.py
#
# Exercise 1.5
height = 100  # meters
dampening_factor = 3/5

for i in range(10):
    height *= dampening_factor  # type: ignore
    print(f"Height after {i + 1} bounces: {height}")

# Alternate method
height = 100
print("Final height", height * (dampening_factor ** 10))
