Date: 2016-07-03
Title: A Token of Tolkien
Category: data
Slug: a-token-of-tolkien
Summary:  If you're searching for a horrible book report generator, then look no further! In this post, I will create one sentence synopses for The Hobbit and The Lord of the Rings.


The Hobbit and The Lord of the Rings are undeniably great books, with rich complex characters and a deep thoughtful story. 
So, this seems like an ideal case to apply an autosummary algorithm meant for tasks like factual news articles!

The <a href=https://github.com/chrisvmiller/analytics/blob/master/autosummarizer/summarize.py>method</a> I programmed is pretty straightforward,
where I find the most representative sentence within a given blob of text. This is accomplished by tokenizing each sentence, converting to a 
tf-idf matrix, multiplying this matrix by it's transpose to get a similarity between sentences, mapping to a graph where each node is a sentence
and each edge is its similarity, then PageRanking to determine the 'best' sentence. 

The 'ok, these seems reasonable, I guess' results are shown below:

![Photo]({attach}/assets/data/2016/a-token-of-tolkien_part1.png){.image_center_style}

<span style="color:green; font-weight: bold;">Special Bonus:</span> When I apply this autosummary to sentences that contain the word "Sam" throughout The Lord of the Rings trilogy, I get: 

![Photo]({attach}/assets/data/2016/a-token-of-tolkien_part2.png){.image_center_style}