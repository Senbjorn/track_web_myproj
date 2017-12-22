$(document).ready(function () {



    //navbar

    //sidebar
    $(".submenu .list-group-item").each(function () {
        $(this).hover(function () {
            (this).classList.add("active");
        },
        function () {
            (this).classList.remove("active");
        })
    });
})