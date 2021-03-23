import {docReady} from './modules/docready.js'
import {getCookie} from './modules/cookies.js'

docReady(function () {
    let personSelectedID = null
    if (document.getElementById('user') != null) {
        document.getElementById('user').addEventListener('change', function () {
            personSelectedID = this.value
        })
    }

    if (document.getElementById('submit-user') != null) {
        document.getElementById('submit-user').addEventListener('click', function () {
            submitUser(personSelectedID)
        })
    }

    function submitUser(personSelectedID) {
        location.replace('http://127.0.0.1:8000/cyberparlements/')
        fetch(location.href, {
            method: 'POST',
            body: JSON.stringify({
                person_selected_id: personSelectedID
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