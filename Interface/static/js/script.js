let showDownload = window.localStorage.getItem('show');



//document.getElementById("loading").style.display = "none";

// get the eshow value to flag if downoad button will show up
let show = document.getElementById('show-value').innerHTML
//showDownload !='1'  &&  
if(show == "False"){
    console.log("sa unang false")
    alert("Invalid File Input")

    window.localStorage.removeItem("show");
    document.getElementById("download").style.display = "none";

//showDownload !='1'
}else if(show == "Empty"){
    alert("Empty File Input")
    window.localStorage.removeItem("show");
    document.getElementById("download").style.display = "none";
}else if(show == "True"){
    document.getElementById("download").style.display = "block";
}else{
    document.getElementById("download").style.display = "none";
}




function removeDisable(){

    window.localStorage.setItem("show", "1");

}

