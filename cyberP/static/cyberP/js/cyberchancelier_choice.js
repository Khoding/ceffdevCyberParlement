import {getCookie} from './modules/cookies.js'

docReady(function () {
    let person_selected_id = null

    document.getElementById('cyberchancelier').addEventListener('change', function () {
        person_selected_id = this.value
    })

    document.getElementById('submit-cyberchancelier').addEventListener('click', function () {
        submitCyberchancelier(person_selected_id)
    })

    function submitCyberchancelier(person_selected_id) {
        fetch(location.href, {
            method: 'POST',
            body: JSON.stringify({
                person_selected_id: person_selected_id
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
})

function docReady(fn) {
    if (document.readyState === "complete" || document.readyState === "interactive") {
        setTimeout(fn, 1)
    } else {
        document.addEventListener("DOMContentLoaded", fn)
    }
}