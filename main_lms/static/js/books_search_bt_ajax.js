
$(function(){

    $('#btsearch').keyup(function() {
    
        $.ajax({
            type: "GET",
            url: "/ballsearch/",
            data: { 
                'search_textbt' : $('#btsearch').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccessbt,
            dataType: 'html'
        });
        
    });

});

function searchSuccessbt(data, textStatus, jqXHR)
{
    $('#btsearch-results').html(data);
}