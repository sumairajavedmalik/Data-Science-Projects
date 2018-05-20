
# coding: utf-8

# In[1]:

import numpy as np


# In[3]:

a = np.arange(0,3)
a



# In[4]:

b = np.linspace(1,10,3)
b


# In[6]:

b = b.reshape((3,3))


# In[8]:

np.vstack((a,b))


# In[9]:

np.hstack((a,b))


# In[11]:

np.column_stack((a,b))


# In[12]:

np.row_stack((a,b))


# In[16]:

a = np.arange(0,9)
a


# In[17]:

b = a*2
b


# In[20]:

a = a.reshape((3,3))
a


# In[21]:

b = b.reshape(3,3)
b


# In[22]:

c = np.hstack((a,b))
c


# In[25]:

np.hsplit(c,2)


# In[26]:

c[1]


# In[27]:

c[0].size


# In[28]:

c[0].ndim


# In[29]:

c[0].T


# In[30]:

np.array(c)


# In[31]:

c = np.array([2+3j, 4+7j])


# In[33]:

c.imag


# In[34]:

c.real


# In[35]:

c.dtype


# In[38]:

x = np.eye(5)
x


# In[39]:

np.savetxt("test.txt",x)


# In[40]:

np.loadtxt("test.txt")


# In[43]:

np.loadtxt("Telecom_data.csv",delimiter = ",")


# In[ ]:



