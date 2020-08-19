#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyttsx3


# In[1]:


import pyttsx3


# In[2]:


speaker = pyttsx3.init()


# In[4]:


pip install pyPDF2


# In[4]:


import PyPDF2


# In[13]:


book = open ('file.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)


# In[14]:


for num in range(1, pages):
    page = pdfReader.getPage(1)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()


# In[15]:


stop


# In[ ]:




