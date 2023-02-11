#!/usr/bin/env python
# coding: utf-8

# In[1]:


a={"name":"vishwak","age":"22","loc":"chennai"}
print(type(a))
print(isinstance(a,dict))


# In[2]:


print(a.get("name"))


# In[3]:


a["add"]="test"
print(a)


# In[4]:


a={'name': 'vishwak', 'age': '22', 'loc': 'chennai', 'add': 'test'}
del a["add"]
print(a)


# In[5]:


print(len(a))
print(sorted(a))


# In[6]:


a={'name': 'vishwak', 'age': '22', 'loc': 'chennai', 'name': 'test'}
print(a["name"])


# In[7]:


print(a.keys())
print(a.values())
print(a.items())


# In[8]:


##operators
##airthmetic
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)##will give qoutient 
print(a%b)##will give reminder.


# In[9]:


##relational op
a=5
b=2
print(a==b)
print(a!=b)
print(a>b)
print(a<=b)
print(a<b)
print(a>=b)


# In[10]:


##logical operator
print(True and True)
print(True and False)
print(True or False)
print(False or True)
print(False or False)
print(not True)
print(not False)


# In[ ]:




