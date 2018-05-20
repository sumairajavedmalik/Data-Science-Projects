
# coding: utf-8

# In[5]:

import numpy as np
a = np.arange(9).reshape(3,3)
a


# In[11]:

np.hsplit(a,3)


# In[12]:

np.vsplit(a,3)


# In[14]:

np.split(a,3 ,axis = 1)


# In[15]:

np.split(a, 3 , axis = 0)


# In[17]:

b = np.arange(27).reshape(3,3,3)
b


# In[19]:

np.dsplit(b,3)


# In[20]:

b.ndim


# In[21]:

b.size


# In[22]:

b.itemsize


# In[23]:

b.nbytes


# In[24]:

b.size *b.itemsize


# In[31]:

b.resize(3,3,3)
b


# In[32]:

b.T


# In[33]:

b.ndim


# In[ ]:




# In[ ]:



