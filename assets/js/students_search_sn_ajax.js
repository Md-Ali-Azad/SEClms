
$(function(){

    $('#snsearch').keyup(function() {
    
        $.ajax({
            type: "GET",
            url: "/snsearch/",
            data: { 
                'search_textsn' : $('#snsearch').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccesssn,
            dataType: 'html'
        });
        
    });

});

function searchSuccesssn(data, textStatus, jqXHR)
{
    $('#snsearch-results').html(data);
}