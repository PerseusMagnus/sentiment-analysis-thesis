let showDownload = window.localStorage.getItem('show');



//document.getElementById("loading").style.display = "none";

// get the eshow value to flag if downoad button will show up
let show = document.getElementById('show-value').innerHTML
//showDownload !='1'  &&  
if(show == "False"){
    
    alert("Invalid File Input")

    window.localStorage.removeItem("show");
    document.getElementById("download").style.display = "none";
    document.getElementById("myBtn").style.display = "none";
    //document.getElementById("loading-bar").style.display = "none";


//showDownload !='1'
}else if(show == "Empty"){
    alert("Empty File Input")
    window.localStorage.removeItem("show");
    document.getElementById("download").style.display = "none";
    document.getElementById("myBtn").style.display = "none";
    //document.getElementById("loading-bar").style.display = "none";

}else if(show == "True"){
    document.getElementById("download").style.display = "block";
    document.getElementById("myBtn").style.display = "block";
    //document.getElementById("loading-bar").style.display = "none";

}else{
    document.getElementById("download").style.display = "none";
    document.getElementById("myBtn").style.display = "none";
    //document.getElementById("loading-bar").style.display = "none";
}


function showLoading(){
    //document.getElementById("loading-bar").style.display = "block";
}

function removeDisable(){

    window.localStorage.setItem("show", "1");

}

function clickLoading() {
    document.getElementById("container").css("opacity",0.5);
    //$("#loading-img").css({"display": "block"});
}