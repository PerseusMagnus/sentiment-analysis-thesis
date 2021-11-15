let showDownload = window.localStorage.getItem('show');

//document.getElementById("loading").style.display = "none";

// get the eshow value to flag if downoad button will show up
let show = document.getElementById('show-value').innerHTML


if(showDownload !='1' || show == "False"){
    document.getElementById("download").style.display = "none";
    alert("Invalid File Input")
    Swal.fire(
        'Good job!',
        'You clicked the button!',
        'success'
      )
}else{
    document.getElementById("download").style.display = "block";
}



if ("{{ show }}" == "False") {
    alert("hahah");
    console.log("Hello")
}
else{
    console.log("Hi")
}

function removeDisable(){

 //   window.localStorage.setItem("show", "1");

 //  document.getElementById("download").disabled = false;

 //   document.getElementById("loading").style.display = "block";

 //   document.getElementById("download").style.display = "block";


}

