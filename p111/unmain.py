import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random as rng
import pandas as pd

df = pd.read_csv ("medium_data.csv")
data = df ["reading_time"].tolist()
fig = ff.create_distplot ([data] , ["Math score"], show_hist = False)
#fig.show()

mean = st.mean(data)
std_deviation = st.stdev(data)
print("mean of popultion : ",mean)
print("Standard deviation of popultion : ",std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range (0,counter):
        ri = rng.randint(0,len(data)-1)
        value = data[ri]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

mean_list = []
for i in range (0,1000):
    s = random_set_of_mean(100)
    mean_list.append(s)
mean = st.mean(mean_list)
std_deviation = st.stdev(mean_list)
print("\n")
print("mean of sample distribution : ",mean)
print("Standard deviation of sample distribution : ",std_deviation)



first_std_start, first_std_end = mean-std_deviation, mean+std_deviation
second_std_start, second_std_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_start, third_std_end = mean-(3*std_deviation), mean+(3*std_deviation)

fig = ff.create_distplot ([mean_list] , ["Student mark"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_start,third_std_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))

#fig.show()


# finding the mean of the first data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.
df = pd.read_csv ("sample_1.csv")
data = df ["reading_time"].tolist()
mean_sample_1 = st.mean(data)
fig = ff.create_distplot ([mean_list] , ["reading_time"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_sample_1, mean_sample_1], y=[0, 0.17], mode="lines", name="mean_sample_1 "))
fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
#fig.show()

# finding the mean of the SECOND data (STUDENTS WHO HAD EXTRA CLASSES ) and plotting it on the plot.
df = pd.read_csv ("sample_2.csv")
data = df ["reading_time"].tolist()
mean_sample_2 = st.mean(data)
fig = ff.create_distplot ([mean_list] , ["reading_time"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_sample_2, mean_sample_2], y=[0, 0.17], mode="lines", name="mean_sample_2 "))
fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))

#fig.show()

# finding the mean of the THIRD data (STUDENTS WHO GOT FUNSHEET) and plotting it on the plot.
df = pd.read_csv ("sample_3.csv")
data = df ["reading_time"].tolist()
mean_sample_3 = st.mean(data)
fig = ff.create_distplot ([mean_list] , ["reading_time"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_sample_3, mean_sample_3], y=[0, 0.17], mode="lines", name="mean_sample_3 "))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
#fig.show()

#finding the z score using the formula
#zScore = (New Sample Mean - Sampling Distribution Mean) / standard deviation

zScore1 = (mean_sample_1 - mean) / std_deviation
print(zScore1)
zScore2 = (mean_sample_2 - mean) / std_deviation
print(zScore2)
zScore3 = (mean_sample_3 - mean) / std_deviation
print(zScore3)

#all of them are not effective