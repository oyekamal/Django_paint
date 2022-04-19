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

    // console.log("originalTarget ----____----", ev.originalTarget);
    // console.log("target ----____----", ev.target);
    console.log("firstElementChild ----____----", ev.target);
    // console.log("nextElementSibling ----____----", ev.target.nextElementSibling);
    console.log("id <<<<<< ",data);
    console.log("id ---- " + document.getElementById(data));
    ev.target.appendChild(document.getElementById(data));
}