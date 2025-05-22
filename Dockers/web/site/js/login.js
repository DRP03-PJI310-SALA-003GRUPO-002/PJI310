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
async function logarge() {
    const usuario = document.getElementById("cpfge").value;
    const senha = document.getElementById("senhage").value;

    if (!usuario || !senha) {
        alert("Por favor, preencha todos os campos.");
        return;
    }

    try {
        // Primeiro: login
        const loginResponse = await fetch("http://localhost:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ usuario: usuario, senha: senha })
        });

        const loginData = await loginResponse.json();

        if (!loginResponse.ok) {
            alert(loginData.erro || "Erro ao fazer login.");
            return;
        }

        const token = loginData.token;
        localStorage.setItem("token", token);

        // Segundo: obter dados do usuário com o token
        const userResponse = await fetch("http://localhost:5000/get_user", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ token: token })
        });

        const userData = await userResponse.json();

        if (!userResponse.ok) {
            alert("Erro ao buscar informações do usuário.");
            return;
        }

        // Verificar cargo
        if (userData.cargo === "gerente_ti") {
            alert("Login realizado com sucesso!");
            window.location.href = "gerencia.html";
        } else {
            alert("Acesso negado. Este login não pertence a um gerente.");
        }

    } catch (error) {
        console.error("Erro de rede:", error);
        alert("Erro de rede. Tente novamente.");
    }
}






// function logarge() {
//     var cpfge = document.getElementById("cpfge").value;
//     var senhage = document.getElementById("senhage").value;

//     if (cpfge === "XXX.XXX.XXX-XX" && senhage === "123456") {
//         window.location.href = "login.html"
//         alert("Login realizado com sucesso!");
//         location.href = "home.html";
//     } 
//     else {
//         alert("Usuário ou senha inválidos.");
//     }
// }