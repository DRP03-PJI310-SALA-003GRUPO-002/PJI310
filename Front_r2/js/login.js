const btn1Button = document.querySelector("#btn1");
const btn2Button = document.querySelector("#btn2");
const bodyElement = document.querySelector("body");
function setBodyClass(className) {
    bodyElement.className = ''; // Remove todas as classes existentes
    bodyElement.classList.add(className); // Adiciona a nova classe
}
    btn1Button.addEventListener("click", () => {
    container.classList.toggle("show-second");
});

btn1Button.addEventListener("click", () => {
    setBodyClass("btn1");
});

btn2Button.addEventListener("click", () => {
    setBodyClass("btn2");
});

function logar() {
    var cpf = document.getElementById("cpf").value;
    var senha = document.getElementById("senha").value;

    if (cpf === "XXX.XXX.XXX-XX" && senha === "123456") {
        window.location.href = "login.html"
        alert("Login realizado com sucesso!");
        location.href = "index.html";
    } 
    else {
        alert("Usuário ou senha inválidos.");
    }
}
function logarge() {
    var cpfge = document.getElementById("cpfge").value;
    var senhage = document.getElementById("senhage").value;

    if (cpfge === "XXX.XXX.XXX-XX" && senhage === "123456") {
        window.location.href = "login.html"
        alert("Login realizado com sucesso!");
        location.href = "home.html";
    } 
    else {
        alert("Usuário ou senha inválidos.");
    }
}