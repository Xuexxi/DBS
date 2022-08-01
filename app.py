#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request,render_template
import joblib
app = Flask (__name__)


# In[2]:


#@app.route ("/",methods = ["GET","POST"])


# In[3]:


#methods = ["GET","POST"]


# In[4]:


@app.route ("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        return(render_template ("index.html",result1="OK",result2="OK"))
    else:
        return(render_template ("index.html",result1="WAITING",result2="WAITING"))
               
if __name__=="main":
    app.run()


# In[5]:


#@app.route('/', methods=['GET', 'POST'])


# In[ ]:


app.run()


# In[ ]:




