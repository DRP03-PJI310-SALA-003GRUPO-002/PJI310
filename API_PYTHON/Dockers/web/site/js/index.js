const form = document.getElementById("form");
const campos = document.querySelectorAll(".input-box");

function nameValidate() {
    bodyElement.className = ''; // Remove todas as classes existentes
    bodyElement.classList.add(className); // Adiciona a nova classe
}



    function nameValidate(){
        if (campos[0].value.length<3) 
            {
            alert("Registro realizado com sucesso!");
            location.href = "home.html";
            } 
            else {
                alert("Erro.");
            }
    }
