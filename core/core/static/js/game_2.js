var drag_str = "";
var drop_str = "";

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    console.log("drag ____before", ev.target.id)
    ev.dataTransfer.setData("text", ev.target.id);

}
    

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    // console.log("firstElementChild ----____----", ev.target.firstElementChild.src);
    console.log("game_2222222222222222222222222222");

    console.log("id <<<<<< ",data);
    var incoming_letter_list = data.split(".")[0].split('/')
    console.log(incoming_letter_list)
    var incoming_letter = incoming_letter_list[incoming_letter_list.length-1]
    console.log(incoming_letter)
    // var present_letter = ev.target.firstElementChild.src
    var present_letter_list = ev.target.firstElementChild.src.split(".")[0].split("/");
    console.log(present_letter_list)
    var present_letter = present_letter_list[present_letter_list.length-1]

    console.log(present_letter)

    if (present_letter == incoming_letter){
        console.log("Yes yo win ");

        var id_ = "/static/alphabets/"+ present_letter +".png"
        console.log(" ----- id ", id_)
        document.getElementById(id_).style.background = "DodgerBlue";
    }
    else{
        var id_ = "/static/alphabets/"+ present_letter +".png"
        console.log(" ----- id ", id_)
        document.getElementById(id_).style.background = "#ff6347";
    }


    ev.target.appendChild(document.getElementById(data));

    // setTimeout(function(){window.top.location.reload()} , 1000);

}


// collect all the divs
var divs = document.getElementsByTagName('div');
var divs_choice = document.getElementById('choice');
// get window width and height
var winWidth = divs_choice.offsetWidth;
var winHeight = divs_choice.offsetHeight;

console.log(winHeight,  ": ", winWidth)

// i stands for "index". you could also call this banana or haircut. it's a variable
for ( var i=0; i < divs.length; i++ ) {
 	
    // shortcut! the current div in the list
    var thisDiv = divs[i];
    
    // get random numbers for each element
    randomTop = getRandomNumber(500, winHeight);
    randomLeft = getRandomNumber(0, winWidth);
    
    // update top and left position
    thisDiv.style.top = randomTop +"px";
    thisDiv.style.left = randomLeft +"px";
    
}

// function that returns a random number between a min and max
function getRandomNumber(min, max) {
    
  return Math.random() * (max - min) + min;
    
}