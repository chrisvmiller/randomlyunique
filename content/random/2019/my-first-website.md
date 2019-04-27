Date: 2019-07-05
Title: My First Website
Category: random
Slug: my-first-website
Summary: My first website

When I was a wee lad, 


this includes all those bad errors too  

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
        if(17>=final_score && final_score>=5){	
            message = "You're super-duper great score was " + final_score + ". Very nice, you're the ultimate physicist."
        }				
		if(final_score>=18){
			message = "In real life, you wouldn't see that many decays. You lose, cheater!"
		}	
		return message
    }
 
    KImg = new Array(7)
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
        if (document.getElementById("decay_image").src == KImg[2].src){
            document.getElementById("score").value++;
        } else {
            document.getElementById("score").value--;
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
       
        document.getElementById("decay_image").src = KImg[2].src;
    }        
        
    function imageCycler(){
        randomInt = Math.floor(Math.random() * 6);
        document.getElementById("decay_image").src = KImg[randomInt].src;
        
        document.getElementById("score").innerHTML =  document.getElementById("score").value;
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
        stopCounters()
        document.getElementById("countdown").value = 30;
        countDownTimer = setInterval(countDownClock, 1000);
        document.getElementById("score").value = 0;
        document.getElementById("finalMessage").innerHTML = "";
    }

</script>

<form name=speed>
    <center>    
    <h1>Choose your Destiny...</h1>
        <input type="radio" value="900" name=tic checked="checked"> Level 1
        <input type="radio" value="300" name=tic> Level 2 
        <input type="radio" value="1" name=tic> Level 3
    </center>
</form>

<center >
    <img id="decay_image" height=250 src="/assets/random/2019/decay_correct.png" width=350 border=0> 
</center>

<center>
Timer: <button id="countdown">30</button>
Score: <button id="score">0</button>

<button onClick="setup_counter();setup_images();">Start!</button>
<button onClick="check_score()"> NOW !!! </button>
<button onClick="stopCounters()">Stop!</button>

<p id="finalMessage" > </p>
</center>