Date: 2019-03-02
Title: My First Website
Category: random
Slug: my-first-website
Summary: As a wee lad in high school, my first foray into tech involved programming a science-themed javascript game.  

During my high school internship at Brookhaven National Lab, I dipped my toes into the world of
coding by creating a website for a high-energy physics experiment. The highlight of which was a
javascript game that simulated the experiment's goal of searching for a super-rare particle 
decay within a neverending stream of particles.

A direct port of this game - including every novice mistake - is found below. After pressing the 
start button, you are given thirty seconds to click "NOW" every time the desired particle decay (the 
starting image shown below) occurs. And, points will be lost if the wrong decay is triggered! 

<script>
							
	function finish(){		
        final_score = document.getElementById("score").value;				
				
        if (final_score<=-5){
			message ="You're very sad score was " + final_score + ". Not too good, bro. What happened?" 
        }
        if(0>=final_score && final_score>=-4){	
            message = "You're score was " + final_score + ". Ummm, better luck next time..."
        }
        if(4>=final_score && final_score>=1){	
            message = "You're final score was " + final_score + ". You did pretty good, nice job."
        }
        if(17>=final_score && final_score>=7){	
            message = "You're super-duper great score was " + final_score + ". Very nice, you're the ultimate physicist."
        }				
		if(final_score>=18){
			message = "In real life, you wouldn't see that many decays. You lose, cheater!"
		}	
		return message
    }
 
    KImg = new Array(6)
    KImg[0] = new Image();
    KImg[0].src="/assets/random/2019/decay_1.png";
    KImg[1] = new Image();
    KImg[1].src="/assets/random/2019/decay_2.png";
    KImg[2] = new Image();
    KImg[2].src="/assets/random/2019/decay_correct.png";
    KImg[3] = new Image();
    KImg[3].src="/assets/random/2019/decay_3.png";
    KImg[4] = new Image();
    KImg[4].src="/assets/random/2019/decay_4.png";
    KImg[5] = new Image();
    KImg[5].src="/assets/random/2019/decay_5.png";    

    function check_score(){
        if (document.images[0].hidden == false){
            document.getElementById("score").value++;
        } else {
            document.getElementById("score").value--;
        }
    }   
    
    function change_to_image(show_image_index){
        for (var i = 0, length = KImg.length; i < length; i++) {
            if (i == show_image_index) {
                document.images[i].hidden=false;       
            } else {
                document.images[i].hidden=true;  
            }
        }      
    }
    
    imageTimer = null;
    countDownTimer= null;
    function stopCounters(){
        if (imageTimer !== null) {
            clearInterval(imageTimer);
        }        
        if (countDownTimer !== null) {
            clearInterval(countDownTimer);
        }          
       
        change_to_image(0);
        document.getElementById("correct_decay_arrow_down").style.visibility = "visible";
    }        
        
    function imageCycler(){
        randomInt = Math.floor(Math.random() * 6);
        change_to_image(randomInt);      
        document.getElementById("score").innerHTML =  document.getElementById("score").value    
     }        
        
    function setup_images() {
	    var radios = document.getElementsByName('tic');
            for (var i = 0, length = radios.length; i < length; i++) {
                if (radios[i].checked) {
                    imageTimer = setInterval(imageCycler, radios[i].value);        
                }
            }
    }
    
    function countDownClock(){
        var currentTime = document.getElementById("countdown").value--;
        document.getElementById("countdown").innerHTML = currentTime;
        
        if(currentTime <=0){
            document.getElementById("finalMessage").innerHTML = finish();
            stopCounters();
        }
    }        
        
    function setup_counter() {
        stopCounters();
        document.getElementById("correct_decay_arrow_down").style.visibility = "hidden";
        document.getElementById("countdown").value = 30;
        document.getElementById("score").value = 0;
        countDownTimer = setInterval(countDownClock, 1000);
        imageCycler()
        document.getElementById("finalMessage").innerHTML = "";
    }

</script>
<form name=speed>
    <center>    
    <h2>Choose your Destiny...</h2>
    <p style="font-size: 12px">Keep in mind that the actual decay is a billion times rarer and happens a billion times faster than Level 3!</p>
        <input type="radio" value="1050" name=tic checked="checked"> Level 1 &nbsp
        <input type="radio" value="600" name=tic> Level 2 &nbsp 
        <input type="radio" value="25" name=tic> Level 3 &nbsp          
    </center>
</form>

<center>
    <span id=correct_decay_arrow_down> &#8595; Find this Decay &#8595; </span>  
    <img height=250 src="/assets/random/2019/decay_correct.png" width=350 border=0> 
    <img height=250 src="/assets/random/2019/decay_1.png" width=350 border=0 hidden> 
    <img height=250 src="/assets/random/2019/decay_2.png" width=350 border=0 hidden> 
    <img height=250 src="/assets/random/2019/decay_3.png" width=350 border=0 hidden> 
    <img height=250 src="/assets/random/2019/decay_4.png" width=350 border=0 hidden>
    <img height=250 src="/assets/random/2019/decay_5.png" width=350 border=0 hidden>
</center>

<center>
Timer: <button id="countdown" style="width: 40px; height: 40px; background-color: white; color: black;">30</button>
Score: <button id="score" style="width: 40px; height: 40px; background-color: white; color: black;">0</button>

<p id="finalMessage" > </p>

<button onClick="setup_counter();setup_images();" style="width: 75; height: 35px; background-color: black; color: white;">Start</button>
<button onClick="check_score()" style="width: 100px; height: 60px; background-color: #4CAF50; color: white;"> NOW !!! </button>
<button onClick="stopCounters()" style="width: 75px; height: 35px; background-color: black; color: white;">Stop</button>
</center>