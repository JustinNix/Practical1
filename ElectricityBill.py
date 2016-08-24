TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator - ")
cost = (float(input("Please Enter Which tariff applies to your cost: " + "\n" + "Tariff_(11)"+ "\n"+ "Tariff_(31)" + "\n" + "Tariff: ")))
usage = (float(input("Enter Daily use in kWh: ")))
billingDays = (float(input("Enter Number of billing days: ")))

if cost == 11:
    total = TARIFF_11*usage*billingDays
    print("Estimated Bill: $" + str(total))
else:
    total = TARIFF_31*usage*billingDays
    print("Estimated Bill: $" + str(total))
