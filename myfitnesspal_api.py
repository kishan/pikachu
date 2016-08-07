import myfitnesspal

client = myfitnesspal.Client('kspatel2018')

day = client.get_date(2016, 8, 1)

print day
print day.meals
