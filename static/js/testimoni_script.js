$(".link-delete").on("click", function(e){
    e.preventDefault();
    var $this = $(this);
    if(confirm("Apa kamu yakin ingin menghapus testimoni ini?")){
        $.ajax({
            url: $this.attr("href"),
            type: "GET",
            dataType: "json",
            success: function(resp){
                if(resp.message == "success"){
                    $(mycard).fadeOut("slow", function(){
                        $(mycard).remove();
                    });
                }else{
                    alert(resp.message);
                }
            }
        });
    }
    return false;
});