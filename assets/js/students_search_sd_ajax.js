
$(function(){

    $('#sdsearch').keyup(function() {
    
        $.ajax({
            type: "GET",
            url: "/sdsearch/",
            data: { 
                'search_textsd' : $('#sdsearch').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccesssd,
            dataType: 'html'
        });
        
    });

});

function searchSuccesssd(data, textStatus, jqXHR)
{
    $('#sdsearch-results').html(data);
}