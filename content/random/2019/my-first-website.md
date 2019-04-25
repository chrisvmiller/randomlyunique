Date: 2019-07-05
Title: My First Website
Category: random
Slug: my-first-website
Summary: My first website

When I was a wee lad, <button class="btn btn-default btn-sm toggle-start-hidden">Show Desired Image</button>

<div>
<img src="/assets/random/2019/decay_correct.png" width="300" class="image_center_style">
</div>

<script>
    function checky(score){
        if(ii==3){
            document.forms[0].answer.value++;			
		} else{				
            document.forms[0].answer.value--;
		}	
    }
    
    KImg = new Array(7)
    KImg[1] = new Image();
    KImg[1].src="/assets/random/2019/decay_1.png";
    KImg[2] = new Image();
    KImg[2].src="/assets/random/2019/decay_2.png";
    KImg[3] = new Image();
    KImg[3].src="/assets/random/2019/decay_correct.png";
    KImg[4] = new Image();
    KImg[4].src="/assets/random/2019/decay_3.png";
    KImg[5] = new Image();
    KImg[5].src="/assets/random/2019/decay_4.png";
    KImg[6] = new Image();
    KImg[6].src="/assets/random/2019/decay_5.png";
	
	var ii=1;        
    var tempSpeed=null;
    var timerID=null;
    var timer=60;
	
	function clockSpeed(newSpeed){
        clearTimeout(timerID);	
        tempSpeed=newSpeed;
        upDate(tempSpeed);
	}

	function upDate(){
        if (ii<6){
            ii++;
        }else{
			ii=Math.ceil(Math.random() * 6);
		}
			
		document.t.src=KImg[ii].src;
		timerID=setTimeout("upDate()", tempSpeed);
	}
					
    //There is only one, Christopher Vincent Miller...true
		
		
	function begin(){		
		timer=30
		document.forms[0].answer.value=0
	}
		
		
	function Go(){
	    if(timer >= 0){
	        document.time.Go.value = timer;
            timer -= 1;
            setTimeout("Go()",1000);
        }
        else{    	
		    finish();
        }  
    }
		
	function reset(){	
			timer=setTimeout			
	}			
					
	function finish(score){					
        if (document.forms[0].answer.value<=-5){
			alert("You're very sad score was " + document.forms[0].answer.value + ". Not too good, bro. What happened?") 
        }
        if(0>=document.forms[0].answer.value && document.forms[0].answer.value>=-4){	
            alert ("You're score was " + document.forms[0].answer.value + ". Ummm, better luck next time...")
        }
        if(4>=document.forms[0].answer.value && document.forms[0].answer.value>=1){	
            alert ("You're final score was " + document.forms[0].answer.value + ". You did pretty good, nice job.")
        }
        if(17>=document.forms[0].answer.value && document.forms[0].answer.value>=5){	
            alert ("You're super-duper great score was " + document.forms[0].answer.value + ". Very nice, you're the ultimate physicist.  Tru bro!!!")
        }				
		if(document.forms[0].answer.value>=18){
			alert ("In real life, you wouldn't see that many decays. You lose, cheater! ")
		}	
    }
</SCRIPT>



<FORM name=speed>
<H1>
<CENTER><FONT color=black>Choose your Destiny...</CENTER></H1>
<CENTER>
    <INPUT onclick=clockSpeed(1750); type=radio name=tic> Level 1 
    <INPUT onclick=clockSpeed(1000); type=radio name=tic> Level 2 
    <INPUT onclick=clockSpeed(800); type=radio name=tic> Level 3 
    <INPUT onclick=clockSpeed(600); type=radio name=tic> Level 4 
    <INPUT onclick=clockSpeed(1); type=radio name=tic> Level 5 
</CENTER><BR><BR>

<CENTER>
<IMG height=250 src="/assets/random/2019/decay_correct.png" width=350 align=center border=0 name=t> 
</CENTER>

<CENTER>
    <FORM name="miller">
    <BR>
    <FONT color=black>Score: </FONT>
    <INPUT size=2 value=0 name=answer><BR><BR>
    </FORM>
</CENTER>

<CENTER>
<FORM name=time>
<FONT color=black>Time: </FONT>
<INPUT size=2 name=Go></FORM>
</CENTER>

<CENTER>
<INPUT onclick="clearTimeout(timerID); upDate();begin();Go()" type=button value=" Start "> 
<INPUT onclick=checky(this.value) type=button value=" NOW!!! " name=score> 
<INPUT onclick=reset() type=button value=" Done ">
</CENTER>

