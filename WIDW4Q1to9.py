import pandas as pd

data = pd.read_csv("Holidays.csv")
#print(data)
print("")
print("1. How many rows and columns are there in your file?")
print(data.shape)
print("")

print("2. Print row 3-8 ( using iloc/loc).")
print(data.iloc[4:9])
print("")

print("3. Find the mean number of all-inclusive hotels across all destinations.")
rounded = data["All inc hotel"].mean()
roundsimp = round(rounded, 3)
print(rounded)
print(roundsimp)
print("")

print("4. Find the lowest scoring destination.")
print(data[data.Score == data.Score.min()])
print("")

print("5. Find the highest scoring destination.")
print(data[data.Score == data.Score.max()])
print("")

print("6. Find all the destinations where there are more than 9 all-inclusive hotels.")
print(data[data["All inc hotel"] > 9])
print("")

print("7. Filter the data by destination and score above 8.")
print("NOTE: Wasn't sure if you just wanted alphabetical order of destination by score over 8 or just the Destinations so did both.")
data2 = data.sort_values("Destination")
print(data2.loc[data2["Score"] > 8])
print("")

print(data2.loc[data2["Score"] > 8, "Destination"])
print("")

print("8. Filter the data by destination & score below 2 (I need to know if these destinations should be removed or there is a problem).")
data2 = data.sort_values("Destination")
print(data2.loc[data2["Score"] < 2])

print("")

print(data2.loc[data2["Score"] < 2, "Destination"])
print("")

print("9. Is there a correlation between number of all-inclusive hotels and score?")
correlation = data["All inc hotel"].corr(data["Score"])
corrsimp = round(correlation, 3)

if correlation >= 0.75 or correlation <= -0.75:
    print("The correlation is significant at ", corrsimp, ".")

elif (correlation <0.75 and correlation >=0.5) or (correlation >-0.75 and correlation <-0.5):
    print("There is a weak correlation at", corrsimp, ".")

else:
    print("The correlation is", corrsimp, ", which is not significant.")
