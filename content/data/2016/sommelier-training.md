Date: 2016-03-10
Title: Sommelier Training
Category: data
Slug: sommelier-training
Summary: My unsophisticated palate doesn't understand professional wine connoisseuring. Luckily, with the help of TensorFlow, I'll suggest a path to transform any wine newb into a 3-Star Michelin Oenologist.  
 
What's the best way to refine my wine intelligence? Since nothing immediately comes to mind, I'll take the fallback 
algorithmic approach and brute-force a solution: sampling lots and lots of wine! So, let's determine the amount 
of wine I need to drink to achieve the same culinary genius as Robin Williams in Neverland!

After googling around for a few minutes, I was able to find a wine training set composed of a dozen wine features 
(acidity, pH, alcohol, etc) and a ranked quality. I then proceeded to classify this wine quality (at different splits: good/bad, good/okay/bad, etc) 
with a fancy-pants <a href=https://github.com/chrisvmiller/analytics/blob/master/sommelier_training/WineClassifier.ipynb>neural network</a>. 
The converged prediction iteration count, after normalizing by the amount of wine it takes to blindfoldedly distinguish 
between red and white, is shown in the chart below: 
 
![Photo]({attach}/assets/data/2016/sommelier-training.png){.image_center_style}

Now, I only need to convince my wife that purchasing 7 Balthazars of pink bubbly wine is intended for research 
and my life will be fantastic.
