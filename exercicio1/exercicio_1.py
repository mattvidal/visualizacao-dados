import matplotlib.pyplot as plt
import numpy as np
 
city=['Delhi','Beijing','Washington','Tokyo','Moscow']
Gender=['Male','Female']
pos = np.arange(len(city))
Happiness_Index_Male=[60,40,70,65,85]
Happiness_Index_Female=[30,60,70,55,75]
 
plt.bar(pos,Happiness_Index_Male,color='blue',edgecolor='black')
plt.bar(pos,Happiness_Index_Female,color='pink',edgecolor='black',bottom=Happiness_Index_Male)
plt.xticks(pos, city)
plt.xlabel('City', fontsize=16)
plt.ylabel('Happiness_Index', fontsize=16)
plt.title('Stacked Barchart - Happiness index across cities',fontsize=18)
plt.legend(Gender,loc=2)
plt.show()