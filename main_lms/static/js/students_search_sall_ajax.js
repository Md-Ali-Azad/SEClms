
$(function(){

    $('#sallsearch').keyup(function() {
    
        $.ajax({
            type: "GET",
            url: "/sallsearch/",
            data: { 
                'search_textsall' : $('#sallsearch').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccesssall,
            dataType: 'html'
        });
        
    });

});

function searchSuccesssall(data, textStatus, jqXHR)
{
    $('#sallsearch-results').html(data);
}