window.onload = () => {
    document.getElementById('consultarBtn').addEventListener('click', consultarPontos);
};

async function consultarPontos() {
    const month = document.getElementById('month').value;
    const year = document.getElementById('year').value;
    const token = localStorage.getItem("token");
    const tabela = document.querySelector("#resultado tbody");

    // Limpa resultados anteriores
    tabela.innerHTML = "";

    if (!month || !year) {
        alert("Preencha todos os campos!");
        return;
    }

    if (!token) {
        alert("Token de autenticação não encontrado. Por favor, faça login novamente.");
        return;
    }

    try {
        const response = await fetch("http://localhost:5000/get_pontos_by_month", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ month, year, token })
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.erro || "Erro na consulta.");
            return;
        }

        if (data.length === 0) {
            tabela.innerHTML = "<tr><td colspan='5'>Nenhum resultado encontrado.</td></tr>";
        } else {
            data.forEach(ponto => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${ponto.id}</td>
                    <td>${ponto.cpf}</td>
                    <td>${ponto.usuario}</td>
                    <td>${ponto.validado ? "Sim" : "Não"}</td>
                    <td>${new Date(ponto.data_hora).toLocaleString("pt-BR")}</td>
                `;
                tabela.appendChild(row);
            });
        }

    } catch (error) {
        alert("Erro ao conectar com a API.");
        console.error(error);
    }
}
