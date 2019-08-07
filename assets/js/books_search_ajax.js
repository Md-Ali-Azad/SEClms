$(function(){

    $('#bsearch').keyup(function() {
    
        $.ajax({
            type: "GET",
            url: "/bsearch/",
            data: { 
                'search_text' : $('#bsearch').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
        
    });

});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}


