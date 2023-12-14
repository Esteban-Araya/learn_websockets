lasText = document.getElementById("last_text")
input = document.getElementById("name")
const pk = JSON.parse(document.getElementById("pk").textContent);

console.log("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

// Se crea la conexión por websocket
url = 'ws://'
            + window.location.host
        // + '192.168.211.46:8000'
        + '/ws/chat/' 
        + pk + '/'
console.log(window.location)
const chatSocket = new WebSocket(url);
console.log(chatSocket.protocol)
// Cada que se recibe un mensaje se lee y se imprime en pantalla
chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        
        lasText.innerText = data.message
    }
// Envia el texto 
function sendMessage() {
    
    chatSocket.send(JSON.stringify({
        'message': input.value

    }));
}