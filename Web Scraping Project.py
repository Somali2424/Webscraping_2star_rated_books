#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Goal: GET TITLE OF EVERY BOOK WITH 2 STAR RATING


# In[3]:


import requests
import bs4


# In[4]:


'http://books.toscrape.com/catalogue/page-2.html'


# In[5]:


'http://books.toscrape.com/catalogue/page-3.html'


# In[6]:


base_url='http://books.toscrape.com/catalogue/page-{}.html'



# In[9]:


#page_num='12'
#base_url.format(page_num)


# In[10]:


res=requests.get(base_url.format(1))


# In[11]:


soup=bs4.BeautifulSoup(res.text,'lxml')


# In[36]:


products=soup.select('.product_pod')


# In[37]:


products


# In[19]:


example=products[0]


# In[21]:


example


# In[ ]:





# In[22]:


str(example)


# In[24]:


'star-rating Three' in str(example)


# In[25]:


example


# In[28]:


[]==example.select(".star-rating.Two")


# In[34]:


example.select('a')[1]['title']


# In[35]:


#we can check if something is 2 stars(string call in, example.select(rating))
#example.select('a')[1]['title'] to grab book title


# In[39]:


two_star_titles=[]

for n in range (1,51):
    
    scrape_url=base_url.format(n)
    res=requests.get(scrape_url)
    
    soup=bs4.BeautifulSoup(res.text,'lxml')
    books=soup.select(".product_pod")
    for book in books:
        if len(book.select('.star-rating.Two'))!=0:
            book_title=book.select('a')[1]['title']
            two_star_titles.append(book_title)


# In[40]:


two_star_titles


# In[ ]:




