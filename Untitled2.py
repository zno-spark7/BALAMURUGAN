#!/usr/bin/env python
# coding: utf-8

# In[11]:


pip install matplotlib


# In[6]:


import matplotlib.pyplot as plt

labels = ['Apple', 'Banana', 'Cherry', 'Mango']
sizes = [30, 25, 20, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Fruit Distribution')
plt.show()


# In[12]:


import matplotlib.pyplot as plt

labels = ['Chrome', 'Firefox', 'Edge', 'Safari']
sizes = [65,20,10,5]

plt.pie(sizes,labels = labels, autopct = '%1.1f%%')
pie.title('Browser Usage Share')
plt.show()


# In[22]:


import matplotlib.pyplot as plt

students = ['A', 'B', 'C', 'D']
marks = [78,85,90,88]

plt.plot(students,marks, marker = '^')
plt.title('Students Marks')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()


# In[ ]:




