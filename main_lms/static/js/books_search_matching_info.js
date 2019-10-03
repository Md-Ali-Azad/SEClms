$(function() {

    $('#bid').keyup(function() {

        $.ajax({
            type: "GET",
            url: "/bsearch_m_info/",
            data: {
                'search_textbm': $('#bid').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess1,
            dataType: 'html'
        });

    });

});

function searchSuccess1(data, textStatus, jqXHR) {
    $('#matching_info').html(data);
}


$(function() {

    $('#bname').keyup(function() {

        $.ajax({
            type: "GET",
            url: "/bsearch_m_info/",
            data: {
                'search_textbm': $('#bname').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess2,
            dataType: 'html'
        });

    });

});

function searchSuccess2(data, textStatus, jqXHR) {
    $('#matching_info').html(data);
}