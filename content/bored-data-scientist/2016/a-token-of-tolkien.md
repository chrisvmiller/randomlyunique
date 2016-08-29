Date: 2016-07-03
Title: A Token of Tolkien
Category: bored
Slug: a-token-of-tolkien
Summary:  If you're searching for a horrible book report generator, then look no further! In this post, I will create one sentence synopses for The Hobbit and The Lord of the Rings.


The Hobbit and The Lord of the Rings are undeniably great books, with rich complex characters and a deep thoughtful story. 
So, this seems like an ideal case to apply an autosummary algorithm meant for tasks like factual news articles!

The <a href=https://github.com/chrisvmiller/analytics/blob/master/autosummarizer/summarize.py>method</a> I programmed is pretty straightforward,
where I find the most representative sentence within a given blob of text. This is accomplished by tokenizing each sentence, converting to a 
tf-idf matrix, multiplying this matrix by it's transpose to get a similarity between sentences, mapping to a graph where each node is a sentence
and each edge is its similarity, then PageRanking to determine the 'best' sentence. 

The 'ok, these seems reasonable, I guess' results are shown below:

<table class="table table-bordered">
    <thead>
      <tr class="text-center">
        <th class="text-center">Book</th>
        <th class="text-center">AutoSummary</th>
      </tr>
    </thead>
    <tbody>
        <tr>
          <td>The Hobbit</td>
          <td>Having made up his mind he crept along as cleverly as he could.</td>
        </tr>
    
        <tr>
          <td class="active">Fellowship of the Ring</td>
          <td class="active">If any of the Wise should with this Ring overthrow the Lord of Mordor, using his own arts, he would then set himself on Saurons throne, and yet another Dark Lord would appear.</td>
        </tr>
    
        <tr>
          <td>The Two Towers</td>
          <td>All Isengard must be emptied; and Saruman has armed the wild hillmen and herd-folk of Dunland beyond the rivers, and these also he loosed upon us.</td>
        </tr>
    
        <tr>
          <td class="active">The Return of the King</td>
          <td class="active">He (Frodo) felt that if once he went beyond the crown of the pass and took one step veritably down into the land of Mordor, that step would be irrevocable.</td>
        </tr>
    </tbody>
</table>

<span style="color:blue; font-weight: bold;">Special Bonus:</span> When I apply this autosummary to sentences that contain the word "Sam" throughout The Lord of the Rings trilogy, I get: 

<table class="table table-bordered">
    <thead>
      <tr class="text-center">
        <th class="text-center">Character</th>
        <th class="text-center">AutoSummary</th>
      </tr>
    </thead>
    <tbody>
        <tr>
          <td text-center">Sam</td>
          <td>And Sam had another growing anxiety.</td>
        </tr>
    </tbody>
</table>
  