lasText = document.getElementById("last_text")
input = document.getElementById("name")
chat = document.getElementById("chat")
const pk = JSON.parse(document.getElementById("pk").textContent);

messageSend = document.createElement("div")
messageSend.className = 'message message-send'

messageRecive = document.createElement("div")
messageRecive.className = 'message message-recived'

// Se crea la conexión por websocket
url = 'ws://' 
             + window.location.host
        //  + '10.0.10.75:8000'
        + '/ws/chat/' 
        + pk + '/'
const chatSocket = new WebSocket(url);
// Cada que se recibe un mensaje se lee y se imprime en pantalla
chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        lasText.innerText = data.message
        message = messageRecive.cloneNode(false)
        message.innerText = data.message
        chat.appendChild(message)
    }
// Envia el texto 

function sendMessage() {
    
    chatSocket.send(JSON.stringify({
        'message': input.value       
    }));
    message = messageSend.cloneNode(false)
    message.innerText = input.value
    chat.appendChild(message)
}
