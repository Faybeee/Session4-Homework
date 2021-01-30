#10. Create a data visualisation diagram to show destination and highest scores?
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("Holidays.csv")
data2 = data.sort_values("Score")
data2.plot.bar(x = "Destination", y = ["Score"])
plt.show()
