
$(function(){

    $('#isearch').keyup(function() {
    
        $.ajax({
            type: "GET",
            url: "/isearch/",
            data: { 
                'search_texti' : $('#isearch').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccessi,
            dataType: 'html'
        });
        
    });

});

function searchSuccessi(data, textStatus, jqXHR)
{
    $('#isearch-results').html(data);
}