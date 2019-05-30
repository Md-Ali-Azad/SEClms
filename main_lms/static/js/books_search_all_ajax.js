
$(function(){

    $('#ballsearch').keyup(function() {
    
        $.ajax({
            type: "GET",
            url: "/ballsearch/",
            data: { 
                'search_textball' : $('#ballsearch').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccessball,
            dataType: 'html'
        });
        
    });

});

function searchSuccessball(data, textStatus, jqXHR)
{
    $('#ballsearch-results').html(data);
}