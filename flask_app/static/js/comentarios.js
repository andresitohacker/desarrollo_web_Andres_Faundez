const validarComentario = () => {
    let error = [];
    const nombre = document.getElementById("com-nombre");
    const texto = document.getElementById("comentario");

    const valNombre = (name) => name && name.trim().length>=3 && name.trim().length<=80;
    const valTexto = (text) => text && text.trim().length>=5 && text.trim().length<=300;

    if (!valNombre(nombre.value)){
        error.push("Nombre no valido")
    };
    if (!valTexto(texto.value)){
        error.push("Comentario no valido")
    };

    if (error.length) {
        
    }
    if (error.length > 0) {
        alert(error.join("\n"));
        return false;
    }
    return true;
};
 
const form = document.getElementById("form-comentarios");

if (form){
    form.addEventListener("submit", (e) =>{
        const ok = validarComentario();
        if (ok==false){
            e.preventDefault();
        }
    });
}