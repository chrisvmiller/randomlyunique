Date: 2016-01-18
Title: Late Night Coding
Category: data
Slug: late-night-coding
Summary:  If I'm coding after-hours, I'm usually working on a relaxing personal project or angrily fighting some bug. Are these late night emotional extremes typical? Let's poll the public Github API and find out!
 
What are commit messages like after normal working hours?  Using every public Github commit message from November 2015, I'll 
dive into this question with a simple natural language processing script! 
 
After regexing only alphanumerics, removing stopwords, lemmatizing and binning unigrams
into daytime (9am to 9pm) and nighttime buckets, I found the more common daytime(/nighttime) words 
by subtracting nighttime(daytime) word frequencies from daytime(nighttime) 
word frequencies. The word clouds below highlight these most common commit words: 
  
![Photo]({attach}/assets/data/2016/late-night-coding.jpg){.image_center_style}
