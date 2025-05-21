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



async function logar() {
    const usuario = document.getElementById("cpf").value;
    const senha = document.getElementById("senha").value;

    if (!usuario || !senha) {
        alert("Por favor, preencha todos os campos.");
        return;
    }

    try {
        const response = await fetch("http://localhost:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ usuario: usuario, senha: senha })
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem("token", data.token); // ou sessionStorage
            alert("Login realizado com sucesso!");
            window.location.href = "ponto.html";
        } else {
            alert(data.erro || "Erro ao fazer login.");
        }
    } catch (error) {
        console.error("Erro de rede:", error);
        alert("Erro de rede. Tente novamente.");
    }
}


// function logar() {
//     var cpf = document.getElementById("cpf").value;
//     var senha = document.getElementById("senha").value;

//     if (cpf === "XXX.XXX.XXX-XX" && senha === "123456") {
//         window.location.href = "login.html"
//         alert("Login realizado com sucesso!");
//         location.href = "ponto.html";
//     } 
//     else {
//         alert("Usuário ou senha inválidos.");
//     }
// }
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