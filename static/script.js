let isVisible = false; // track state

function toggleMessage() {
    const output = document.getElementById("output");
    
    if (isVisible) {
        output.innerText = "";          // hide text
    } else {
        output.innerText = "You clicked the button!";  // show text
    }

    isVisible = !isVisible; // flip the state
}
