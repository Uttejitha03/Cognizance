import pandas as pd
series = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
newseries = series.str.title()
print("resulting series : ")
print(newseries)