
# coding: utf-8

# In[6]:

v = [1,2,3]
w = [1,2,3]
def vector_add(v, w):
    return[v_i - w_i for v_i, w_i in zip(v,w)]
vector_add(v, w)


# In[7]:

s = [2,3,5]
v = [1,2,3]
def vector_mult(s, v):
    return[s_i * v_i for s_i, v_i in zip(s, v)]
vector_mult(s, v)


# In[23]:

vectors = [1,2,3,4,5,6]
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
        return result

    


# In[32]:

c = 2
v = [1,2,3,4,5]
def scalr_multiply(c, v):
    return[c * v_i for v_i in v]
scalr_multiply(c, v)

    


# In[42]:

vectors = [2,5,8,9]
def vector_mean(vectors):
    n = len(vectors)
    return scalr_multiply(1/n, vector_sum(vectors))


# In[46]:

v = [1,2,3,4]
w = [2,3,4,5]
def dot(v,w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
dot(v,w)
def sum_of_squares(v):
    return dot(v,v)
sum_of_squares(v)
import math
def magnitude(v):
    return math.sqrt(sum_of_squares(v))
magnitude(v)
    


# In[ ]:



