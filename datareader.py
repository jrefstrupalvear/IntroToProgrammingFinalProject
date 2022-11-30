import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("AAPL.csv.xlsx")


data.plot()
plt.show()
import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('AAPL.csv')

print(df) 