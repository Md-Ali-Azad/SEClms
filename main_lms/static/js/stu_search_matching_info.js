$(function() {

    $('#sid').keyup(function() {

        $.ajax({
            type: "GET",
            url: "/ssearch_m_info/",
            data: {
                'search_textsm': $('#sid').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess11,
            dataType: 'html'
        });

    });

});

function searchSuccess11(data, textStatus, jqXHR) {
    $('#matching_info_s').html(data);
}


$(function() {

    $('#sname').keyup(function() {

        $.ajax({
            type: "GET",
            url: "/ssearch_m_info/",
            data: {
                'search_textsm': $('#sname').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess22,
            dataType: 'html'
        });

    });

});

function searchSuccess22(data, textStatus, jqXHR) {
    $('#matching_info_s').html(data);
}