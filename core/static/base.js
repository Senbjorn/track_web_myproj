$(document).ready(function () {
    // $(document).on('click', '.editCommentLink', function (event) {
    //     $('#commentEditModal').modal('show');
    //     console.log(this.href);
    //     $.get(this.href, function (data) {
    //         $('#edit-comment-body').html(data);
    //     });
    //     event.preventDefault();
    // })
    //
    // $(document).on('submit', '[data-formType="commentEditForm"]', function (event) {
    //     $.post(this.action, $(this).serialize(), function (data) {
    //         if (data == "OK") document.location.reload();
    //         else $('#edit-comment-body').html(data);
    //     })
    //     event.preventDefault();
    // })

    function updateComments() {
        var comment_list = $('.pComments')
        console.log(comment_list[0])
    }

    $(document).on('click', '.editLink', function (event) {
        $('#editModalLabel').html($(this).data('data-formLabel'));
        $('#editModal').modal('show');
        $.get(this.href, function (data) {
            $('#edit-body').html(data);
        });
        event.preventDefault();
    })

    $(document).on('submit', '[data-formType="editForm"]', function (event) {
        $.post(this.action, $(this).serialize(), function (data) {
            if (data == "OK") document.location.reload();
            else $('#edit-body').html(data);
        })
        event.preventDefault();
    })

    window.setInterval(updateComments, 5000)

})
