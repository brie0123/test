import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# dataframe 생성
data = pd.DataFrame({
    'name':['alice','peter','sam'],
    'age':[22,31,25],
    'weight':[75.5,80,55.1]
})

st.dataframe(data, use_container_width=True)

fig,ax = plt.subplots()
ax.bar(data['name'], data['age'])
st.pyplot(fig)

# seaborn
barplot = sns.barplot(x='name',y='age',data=data,ax=ax,palette='Set2')
fig = barplot.get_figure()

st.pyplot(fig)

labels = ['G1','G2','G3','G4','G5']
men_means = [20,15,30,35,27]
women_means = [25,32,30,20,25]
men_std = [2,3,4,1,2]
women_std = [3,5,2,3,3]
width = 0.35

fig,ax = plt.subplots()

ax.bar(labels, men_means, width,yerr=men_std, label='Men')
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means, label='Women')
ax.set_ylabel('Score')
ax.set_title('Scores by group and gender')
ax.legend()

st.pyplot(fig)


# barcode

code = np.array([
    1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,
    0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,
    1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1])

pixel_per_bar = 4   # 바코드의 폭
dpi = 100           # 인치당 해상도

fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2),dpi=dpi)
ax = fig.add_axes([0,0,1,1])
ax.set_axis_off()

ax.imshow(code.reshape(1,-1), cma2p='binary',aspect='auto',interpolation='nearest')

st.pyplot(fig)
