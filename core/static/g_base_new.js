$(document).ready(function () {

    //sidebar
    $(".submenu .list-group-item").each(function () {
        $(this).hover(function () {
            (this).classList.add("active");
        },
        function () {
            (this).classList.remove("active");
        })
    });

    $(document).on('click', '[data-item-type="a"]', function (event) {
        document.location.href=($(this).data('href'));
    });


    //modal
    $(document).on('click', '.main-modal-link', function (event) {
        $('#mainModalLabel').html($(this).data('main-modal-label'));
        $('#mainModal').modal('show');
        $.get($(this).data('main-modal-get-link'), function (data) {
            $('#mainModalBody').html(data);
        });
        event.preventDefault();
    });

    $(document).on('submit', '[data-form-type="mainModalForm"]', function (event) {
        $.post(this.action, $(this).serialize(), function (data) {
            if (data == "OK") document.location.reload();
            else $('#mainModalBody').html(data);
        })
        event.preventDefault();
    });
    //likes
    $(document).on('submit', '[data-action-type="LIKE"]', function (event) {
        $.post(this.action, $(this).serialize(), function (data) {
            document.location.reload();
        });
        event.preventDefault();
    });


});