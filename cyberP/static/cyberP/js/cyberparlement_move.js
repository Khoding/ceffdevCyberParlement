import {getCookie} from './modules/cookies.js'

let submit = document.getElementById("cp-move-submit")
if(submit != null) {
    submit.addEventListener('click', function () {
        submitCyberparlementSelected(cyberparlementID)
    })
}

function submitCyberparlementSelected(cyberparlementSelectedID) {
    location.replace('http://127.0.0.1:8000/cyberparlements/')
    fetch(location.href, {
        method: 'POST',
        body: JSON.stringify({
            cyberparlement_selected_id: cyberparlementSelectedID
        }),
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json'
        }
    }).then(function (response) {
        if (response.ok) {
            return response.json()
        }
    })
}