Date: 2016-01-18
Title: Late Night Coding
Slug: late-night-coding
Summary:  If I'm coding after-hours, I'm usually working on a relaxing personal project or angrily fighting some bug. Are these late night emotional extremes typical? Let's poll the public Github API and find out!
 
What are commit messages like after normal working hours?  Using every public Github commit message from November 2015, I'll 
dive into this question with a simple natural language processing script! 
 
With the help of Apache Spark, I regexed out alphanumerics, removed stopwords, lemmatized, then binned unigrams
into daytime (9am to 9pm) and nighttime buckets. After this separation, 
I found the most common daytime(/nighttime) words by subtracting nighttime(/daytime) word frequencies from daytime(/nighttime) 
word frequencies, which are highlighted in the word clouds below: 
  
<img src="/assets/2016/late-night-coding/late-night-coding.jpg" style='margin-top:10px;display:block;margin:auto;'>