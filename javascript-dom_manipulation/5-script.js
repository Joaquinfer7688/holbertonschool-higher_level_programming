var updateHeaderButton = document.getElementById("update_header");
updateHeaderButton.addEventListener("click", function() {
    var header = document.querySelector("header");

    header.textContent = "New Header!!!";
});
