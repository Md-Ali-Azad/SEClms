
$(function(){

    $('#brbdsearch').keyup(function() {
    
        $.ajax({
            type: "GET",
            url: "/brbdsearch/",
            data: { 
                'search_textbrbd' : $('#brbdsearch').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccessbrbd,
            dataType: 'html'
        });
        
    });

});

function searchSuccessbrbd(data, textStatus, jqXHR)
{
    $('#brbdsearch-results').html(data);
}