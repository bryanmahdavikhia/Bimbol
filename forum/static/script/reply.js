function replyFunction() {
    $(".want-reply").on("click", function(){
        console.log("reply dipencet");
        var id = $(this).attr("data-replyId");
        console.log(id);
        var tmp = "#reply-form-" + id.toString();
        console.log(tmp);
        $(".reply-block-form").removeClass("enable");
        $(tmp).addClass("reply-block-form enable");
    });
}


function cancelFunction() {
    $(".cancel-button").on("click", function(){
        console.log("cancel dipencet");
        var id = $(this).attr("data-replyId");
        console.log(id);
        var tmp = "#reply-form-" + id.toString();
        console.log(tmp);
        $(tmp).removeClass("enable");
    });
}

$(document).ready(function(){
    replyFunction();
    cancelFunction();

    console.log("masokkkkkk");
    const title = $('#post-title');
    const desc = $('#post-desc');
    const author = $('#post-author');

    $.ajax({
        type: 'GET',
        url: 'json',
        success: function(data) {
            console.log("berhasil");
            const post = data[0].fields;

            console.log(data);
            title.append(post.title);
            desc.append(post.desc);
            author.append(post.username);
        },
        error: function(data) {
            console.log(data);
        }
    });
});

