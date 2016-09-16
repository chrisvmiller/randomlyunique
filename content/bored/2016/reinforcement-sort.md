Date: 2016-09-15 
Title: Reinforcement Sort 
Category: bored
Slug: reinforcement-sort 
Summary: Are concise and highly effective sorting algorithms better than a bloated imprecise sort done through reinforcement learning? Of course they are - duh

<p align="center">
You know Quicksort and Merge sort and Timsort and Shell sort <br>
Heapsort and Bubble sort and Insertion sort and Selection sort <br>
But do you recall the most god-awful sort of all? 
</p>

A Reinforcement Sort (a sort done through reinforcement(ish) learning) is the Nickelback of sorting 
algorithms - a perfect superposition of horrible and awesome. This rockstar was developed using an 
epsilon greedy <a href=https://en.wikipedia.org/wiki/Q-learning>Q-learning</a> approach
with the aim of generating the best python sorting script. This mainly involved combining code 
fragments together and giving rewards based on how well these scripts sort a list. The exact setup is 
summarized as follows:

1) <a href=https://github.com/chrisvmiller/analytics/blob/master/reinforcement_sort/action.py#L50>State</a>: A binary array chad-kroegered from a md5 hash of the python code string <br>
2) <a href=https://github.com/chrisvmiller/analytics/blob/master/reinforcement_sort/action.py#L8>Actions</a>: 
I figured sorting will require some looping, swapping and probably a conditional or two, so I made these actions on a state<br>
3) <a href=https://github.com/chrisvmiller/analytics/blob/master/reinforcement_sort/reward.py>Reward</a>: 
The state receives a score of -1 if the python code doesn't run, -10 is the code is over 300 characters or +1000 if the list is correctly sorted. <br>

After <a href=https://github.com/chrisvmiller/analytics/blob/master/reinforcement_sort/learn_sort.py>training</a> up a neural net, 
I received this optimal sort: 
 
    :::python
    for i, _ in enumerate(unsorted_list):
	    for j, _ in enumerate(unsorted_list):
		    if(unsorted_list[i] < unsorted_list[j]):
		        unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i];

Now you may be telling yourself that this looks exactly like a Bubble Sort, but I assure you it's not. 
A Bubble Sort has a reasonable time complexity of O(n^2), but a Reinforcement Sort 
runs in O(oh god, why am I doing this).
