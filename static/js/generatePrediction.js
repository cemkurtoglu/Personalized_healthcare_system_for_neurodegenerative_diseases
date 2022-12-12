$.ajax({
    type: "POST",
    url: 'api/generate_prediction/' + response.id,
    enctype: 'multipart/form-data',
    headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Accept": "application/json",
        'Content-Type': 'application/json'
    },
    data: JSON.stringify([{
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

    }]),


    success: function (response) {
        console.log(response)


    },
    error: function (error) {
        console.log(error);
        console.log(this.data)


    }
});