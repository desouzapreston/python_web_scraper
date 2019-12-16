/* Get all elements with class="close" */
var closebtns = document.getElementsByClassName("close");
var i;
/* Loop through the elements, and hide the parent, when clicked on */
for (i = 0; i < closebtns.length; i++) {
    closebtns[i].addEventListener("click", function() {
        this.parentElement.style.display = 'none';
    });
}

/* Get all elements with class="generate" */
var generatebtns = document.getElementsByClassName("generate");
var j;
/* Loop, show new filters, when clicked on */
for (i = 0; i < generatebtns; i++) {
    generatebtns[i].addEventListener("click", function() {
        //TODO: use jQuery Append to generate new filter tag
    })
}