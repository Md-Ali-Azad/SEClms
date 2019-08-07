
$(function(){

    $('#brnsearch').keyup(function() {
    
        $.ajax({
            type: "GET",
            url: "/brnsearch/",
            data: { 
                'search_textbrn' : $('#brnsearch').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccessbrn,
            dataType: 'html'
        });
        
    });

});

function searchSuccessbrn(data, textStatus, jqXHR)
{
    $('#brnsearch-results').html(data);
}