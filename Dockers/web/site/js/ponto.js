document.addEventListener("DOMContentLoaded", () => {
    const usuarioInput = document.getElementById("usuario");
    const cpfInput = document.getElementById("cpf");
    const enviarBtn = document.getElementById("enviar");

    const token = localStorage.getItem("token");

    if (!token) {
        alert("Token não encontrado. Por favor, faça login novamente.");
        window.location.href = "login.html";
        return;
    }

    // Chamar /get_user para preencher campos
    fetch("http://localhost:5000/get_user", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ token: token })
    })
    .then(response => response.json())
    .then(data => {
        if (data.usuario && data.cpf) {
            usuarioInput.value = data.usuario;
            cpfInput.value = data.cpf;
            usuarioInput.setAttribute("readonly", true);
            cpfInput.setAttribute("readonly", true);
        } else {
            alert("Erro ao obter dados do usuário.");
        }
    })
    .catch(error => {
        console.error("Erro ao obter dados do usuário:", error);
        alert("Erro de rede ao buscar dados do usuário.");
    });

    // Inserir ponto com timestamp
    enviarBtn.addEventListener("click", (e) => {
        e.preventDefault(); // Impede o submit do form

        const timestamp = new Date().toISOString();

        fetch("http://localhost:5000/inserir_ponto", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                token: token,
                timestamp: timestamp
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(`Ponto registrado com sucesso para ${data.message.usuario} às ${data.message.timestamp}`);
            } else {
                alert(data.erro || "Erro ao registrar ponto.");
            }
        })
        .catch(error => {
            console.error("Erro ao registrar ponto:", error);
            alert("Erro de rede ao tentar registrar ponto.");
        });
    });
});
