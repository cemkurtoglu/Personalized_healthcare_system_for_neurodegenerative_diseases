
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let submitFunc = $('#health_record_form').on('submit', function (e) {
    e.preventDefault();
    setTimeout((function () {
        const csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        $.ajax({
            type: "POST",
            url: 'api/post_form/',
            enctype: 'multipart/form-data',
            data: {
                'csrfmiddlewaretoken': csrfmiddlewaretoken,
                'rid': $("#rid").val() || '',
                'first_name': $("#first_name").val().trim() || '',
                'last_name': $("#last_name").val().trim() || '',
                'birth_date': $("#birth_date").val().trim() || '',
                'gender': $("#gender").val().trim() || '',
                'marital_status': $("#marital_status").val().trim() || '',
                'exam_date': $("#exam_date").val().trim() || '',
                'cdrsb': $("#cdrsb").val() || '',
                'adas11': $("#adas11").val().trim() || '',
                'adas13': $("#adas13").val().trim() || '',
                'mmse': $("#mmse").val().trim() || '',
                'ravlt_immediate': $("#ravlt_immediate").val().trim() || '',
                'ravlt_learning': $("#ravlt_learning").val().trim() || '',
                'ravlt_forgetting': $("#ravlt_forgetting").val().trim() || '',
                'faq': $("#faq").val().trim() || '',
                'ventricles': $("#ventricles").val().trim() || '',
                'hippocampus': $("#hippocampus").val().trim() || '',
                'whole_brain': $("#whole_brain").val().trim() || '',
                'entorhinal': $("#entorhinal").val().trim() || '',
                'fusiform': $("#fusiform").val().trim() || '',
                'mid_temp': $("#mid_temp").val().trim() || '',
                'icv': $("#icv").val().trim() || '',
                'diagnosis': $("#diagnosis").val().trim() || '',

            },

            success: function (response) {
                console.log(response)

                if (response['message'] === 'success') {
                    console.log("success log /n")
                    let customId = parseInt(response['id'])
                    console.log(response)
                    console.log(customId)
                    window.location.href = 'result/' + response.id
                    $.getScript("static/js/generatePrediction.js")


                } else {
                    const small = document.getElementById('message-content');
                    small.innerText = "Something went wrong";

                }


            },
            error: function (error) {
                console.log(error);
                const small = document.getElementById('message-content');
                small.innerText = error;

            }
        });

    }), 800);


})