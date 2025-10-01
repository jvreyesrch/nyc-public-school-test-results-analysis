# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...
# Add as many cells as you like...

#best math schools in descending order (scores above 80%)
math_schools = schools[schools['average_math'] >= 800*0.8]
math_schools_srt = math_schools.sort_values('average_math', ascending = False)
best_math_schools = math_schools_srt[['school_name','average_math']]
#print(best_math_schools)

#top 10 performing schools
schools['total_SAT'] = schools[['average_math','average_reading','average_writing']].sum(axis=1)
schools_srt = schools.sort_values('total_SAT', ascending = False)
top_10_schools = schools_srt[['school_name','total_SAT']][:10]
print(top_10_schools)

#single borough with the largest combined SAT score
borough_agg = schools.groupby('borough').agg(
    num_schools=('total_SAT','count'),
    average_SAT = ('total_SAT','mean'),
    std_SAT = ('total_SAT','std')
)
##print(borough_agg)
top_borough = borough_agg['std_SAT'].idxmax()
largest_std_dev = borough_agg.loc[[top_borough]].round(2)
print(largest_std_dev)