var drag_str = "";
var drop_str = "";

function allowDrop1(ev) {
    ev.preventDefault();
  
}

function drag1(ev) {
  
    console.log("drag ____before gam1", ev.target.id)
    ev.dataTransfer.setData("text", ev.target.id);

}
    

function drop1(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    // console.log("firstElementChild ----____----", ev.target.firstElementChild.src);


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

        var id_ = "/static/alphabets/"+ incoming_letter +".png"
        console.log(" ----- id same ", id_)
        document.getElementById(id_).style.background = "DodgerBlue";
       

        
     
    }
    else{
        var id_ = "/static/alphabets/"+ present_letter +".png"
        console.log(" ----- id dufferent", id_)
        document.getElementById(id_).style.background = "#ff6347";
    }


    ev.target.appendChild(document.getElementById(data));

    // setTimeout(function(){window.top.location.reload()} , 1000);

    
}