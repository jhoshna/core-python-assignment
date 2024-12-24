def calculate_fare(dist):
    base = 50
    per_km = 10
    return base + (dist * per_km)


distances = [5, 10, 3]
total = 0

for i, dist in enumerate(distances, start=1):
    price = calculate_fare(dist)
    print(f"Trip {i}: ${price}")
    total += price

print(f"Total Fare:{total}")
