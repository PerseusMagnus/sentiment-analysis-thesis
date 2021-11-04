let showDownload = window.localStorage.getItem('show');

document.getElementById("loading").style.display = "none";

if(showDownload !='1'){
    document.getElementById("download").style.display = "none";
}

function removeDisable(){

    window.localStorage.setItem("show", "1");


    document.getElementById("download").disabled = false;

    document.getElementById("loading").style.display = "block";

    document.getElementById("download").style.display = "block";


}

