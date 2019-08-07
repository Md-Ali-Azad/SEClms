$(function(){

    $('#rtsearch').keyup(function() {
    
        $.ajax({
            type: "GET",
            url: "/rtbooks/",
            data: { 
                'search_textrt' : $('#rtsearch').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccessrt,
            dataType: 'html'
        });
        
    });

});

function searchSuccessrt(data, textStatus, jqXHR)
{
    $('#rtsearch-results').html(data);
}


