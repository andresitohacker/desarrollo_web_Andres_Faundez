//Aca van las validaciones y el funcionamiento del boton 

const validarNota= (nota) =>{
    if (!nota || isNaN(nota)){
        return false;
    }

    if (!Number.isInteger(nota)){
        return false;
    }
    if (nota < 1 || nota > 7){
        return false;
    }
    return true;
}

document.addEventListener("DOMContentLoaded", () => {
    const botones = document.querySelectorAll(".evaluar");
    botones.forEach((boton) => {
        boton.addEventListener("click", async () => {
            const avisoId = boton.getAttribute("data-id");
            const input = prompt("Ingrese una nota del 1 al 7:");
            if (input === null){
                return;
            }
            const nota = Number(input);
            if (!validarNota(nota)) {
                alert("Nota inválida. Por favor ingrese un número entero entre 1 y 7.");
                return;
            }
            const form = new FormData();
            form.append("aviso_id", avisoId);
            form.append("nota", nota);

            fetch("/api/evaluar", {
                method: "POST",
                body: form
            })
            .then((response) => response.text())
            .then((nuevoProm) => {
                const fila = boton.closest("tr"); //Asi agarramos la fila completa a la que agarramos el boton
                const casilla = fila.querySelectorAll("td"); //Ahora tomamos la casilla para saber cual modificar 
                const posNota = casilla[5];

                if (nuevoProm !== "-"){
                    posNota.textContent = nuevoProm;


                }
            })
            .catch(() => {
                alert("Error al evaluar");
            });
        });
    });
});