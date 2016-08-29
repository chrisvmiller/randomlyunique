Date: 2015-11-23
Title: Mate Locate 
Category: bored
Slug: mate-locate 
Summary: A lost spouse in a crowded mall without a phone is a stressful situation. It may be tempting to search the entire mall, but is it better to stay put? 
 
 
As I write this, I'm taking a break from searching for my recently wandered off and phoneless wife. I wish to find her as 
quickly as possible, but I'm currently experiencing some inner turmoil. Should I continue on this wife-hunt or is it 
more time-efficient to remain stationary and wait until she walks by? Do two confined random-walks meet quicker
than a single random-walk finding a stationary point? Wait a second, I can write a script 
(<a href="https://github.com/chrisvmiller/analytics/blob/master/mate_locate/locate.py">click here!</a>) that simulates 
finding my lost and (presumingly) scared wife!  

In order to keep things simple, I'll assume this mall is a bounded square grid where my wife and I are initially assigned 
to a random location. Then, during each iteration, a non-stationary person walks a single square in any 
horizontal, vertical or diagonal direction. Whenever my wife and I are in the same square, I will record the total number of squares 
traveled and reset the simulation. This process repeats for two scenarios: 1) We're both randomly moving 
around 2) One person remains stationary, until representative total-distance averages are reached.     

The diagram below shows a typical example for each scenario:

![Photo]({attach}/assets/bored/2015/mate-locate.png){.image_center_style}

After running this simulation for a few different sized grids, I confirmed that two people randomly walking around is 
approximately 1.6x faster! Now, I would typically follow this result, but my wife already found me like 45 minutes ago and 
she's been patiently waiting for me to finish this blog post.
 