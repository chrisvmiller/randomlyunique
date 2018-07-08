Date: 2016-07-03
Title: A Token of Tolkien
Category: data
Slug: a-token-of-tolkien
Summary:  If you're searching for a horrible book report generator, then look no further! In this post, I will create one sentence synopses for The Hobbit and The Lord of the Rings.


The Hobbit and The Lord of the Rings are undeniably great books, with rich complex characters and a deep thoughtful story. 
So, this seems like an ideal case to apply an autosummary algorithm!

The method I programmed <button class="btn btn-default btn-sm toggle-start-hidden">Show Code</button> is pretty straightforward,
where I find the most representative sentence within a given blob of text. This is accomplished by tokenizing each sentence, converting to a 
tf-idf matrix, multiplying this matrix by it's transpose to get a similarity between sentences, mapping to a graph where each node is a sentence
and each edge is its similarity, then PageRanking to determine the 'best' sentence. 

    :::python
    from nltk import sent_tokenize
    from nltk.corpus import stopwords
    from operator import itemgetter
    from networkx import from_numpy_matrix, pagerank
    from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
    
    MIN_SENT_LENGTH = 3
    FILE_PATH = 'PATH_TO_LORD_OF_THE_RINGS_TEXT'
    
    STOPWORDS = stopwords.words("english")
    
    
    def load_document():
        '''
        Opens up the Lord of the Rings file and cleans up the text
        '''
        document = open(FILE_PATH).read()
        encoded_document = document.decode('unicode_escape').encode('ascii', 'ignore')
        return encoded_document.lower()
    
    
    def setup_sentences(document):
        '''
        Tokenizes the document into sentences, then filters for short sentences
        '''
        sentences = sent_tokenize(document)
        sentences = filter(lambda sent: len(sent.split()) > MIN_SENT_LENGTH, sentences)
    
        return sentences
    
    def rank_sentences(sentences):
        '''
        Ranks sentences using a page rank algorithm
        '''
        word_counts = CountVectorizer(
            min_df=1E-3,
            stop_words=STOPWORDS,
            analyzer='word',
        ).fit_transform(set(sentences))
    
        tfidf = TfidfTransformer().fit_transform(word_counts)
        pairwise_similarity = tfidf * tfidf.T
        graph = from_numpy_matrix(pairwise_similarity.toarray())
    
        ranked_sentences = pagerank(graph)
        ranked_sorted = sorted(ranked_sentences.items(), key=itemgetter(1), reverse=True)
        top_sentences = [sentences[index] for index, score in ranked_sorted[:10]]
    
        return top_sentences
    
    
    def print_results(sentences):
        for index, sentence in enumerate(sentences, start=1):
            print "\n{0}: {1}".format(index, sentence.capitalize())
    
    
    if __name__ == "__main__":
        document = load_document()
        sentences = setup_sentences(document)
    
        best_sentences = rank_sentences(sentences)
        print_results(best_sentences)

The 'ok, these seems reasonable, I guess' results are shown below:

![Photo]({attach}/assets/data/2016/a-token-of-tolkien.png){.image_center_style}

<span style="color:green; font-weight: bold;">Special Bonus:</span> When I apply this autosummary to sentences that contain the word "Sam" throughout The Lord of the Rings trilogy, I get: 

![Photo]({attach}/assets/data/2016/a-token-of-tolkien_sam.png){.image_center_style}