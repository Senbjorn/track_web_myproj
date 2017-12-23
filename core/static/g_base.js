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

    //modal
    $(document).on('click', '.editLink', function (event) {
        $('#editModalLabel').html($(this).data('data-formLabel'));
        $('#editModal').modal('show');
        $.get(this.href, function (data) {
            $('#edit-body').html(data);
        });
        event.preventDefault();
    });

    $(document).on('submit', '[data-formType="editModal"]', function (event) {
        $.post(this.action, $(this).serialize(), function (data) {
            if (data == "OK") document.location.reload();
            else $('#edit-body').html(data);
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