Date: 2017-03-17
Title: Glib Graphology
Category: data
Slug: glib-graphology
Summary: In this entry, I continue my pursuit of inappropriately using algorithms by comparing my signature with famous celebrity autographs!   

Graphology, the act of evaluating personality characteristics from handwriting, isn't 
too objective, but - hey - I'll still take a crack at it!  Using a set of 
300 famous signatures, I'll attempt to compose my personality from various celebrities! 

The algorithm in a nutshell involved calculating image keypoints via a Scale-Invariant 
Feature Transform (SIFT), followed by a simple pixel-wise Manhattan distance comparison 
between my keypoints (it's actually a small normalized neighbourhood around these keypoint) and each celeb. 
The chart below is my purposed celebrity mixture: 

![Photo]({attach}/assets/data/2017/glib-graphology.png){.image_center_style}