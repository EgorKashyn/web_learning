const username = document.getElementById('username')
const password = document.getElementById('password')
const button = document.getElementById('button')


button.addEventListener("click", submitData)


async function submitData() {
    var url = 'http://localhost:8000/api?'

    let response = await fetch(url + "username=" + username.value + "&password=" + password.value)
    console.log(response)
    if (response.ok) {
        const button_div = document.getElementsByClassName("button")[0]
        var text = document.createElement("div1")
        text.textContent = "Registration completed"
        text.style = "color: green"

        button_div.insertAdjacentElement("beforeend", text)
        console.log(username.value)
    } else{
        const button_div = document.getElementsByClassName("button")[0]
        var text = document.createElement("div1")
        text.textContent = "Registration failed"
        text.style = "color: red"

        button_div.insertAdjacentElement("beforeend", text)
    }
    
}
