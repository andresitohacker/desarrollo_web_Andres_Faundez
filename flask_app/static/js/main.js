

const agregarFotos = () => {
    const fotos = document.getElementById("fotos");
    const botonAgregarFoto = document.getElementById("agregar-foto");
    
    botonAgregarFoto.addEventListener("click", () => {
        if (fotos.children.length < 5) {
            const nuevoInput = document.createElement("input");
            nuevoInput.type = "file";
            nuevoInput.name = "foto";
            nuevoInput.accept = "image/*";
            fotos.appendChild(nuevoInput);

            if (fotos.children.length === 5) {
                botonAgregarFoto.disabled = true;
            }
        }
    });
};


const contactoPor = () => {
  const container = document.getElementById("contactos");
  const botonAgregarContacto = document.getElementById("agregar-contacto");

  // Función para ocultar/mostrar info-contacto
  const Ocultar = (item) => {
    const select = item.querySelector(".contactar_por");
    const info = item.querySelector(".info-contacto");

    select.addEventListener("change", () => {
      info.style.display = select.value ? "block" : "none";
    });
    info.style.display = select.value ? "block" : "none";
  };
  container.querySelectorAll(".contacto-item").forEach(Ocultar);

  botonAgregarContacto.addEventListener("click", () => {
    const contactosActuales = container.querySelectorAll(".contacto-item").length;
    
    if (contactosActuales < 5) {
      const base = container.querySelector(".contacto-item");
      const nuevo = base.cloneNode(true);

      const sel = nuevo.querySelector(".contactar_por");
      const info = nuevo.querySelector(".info-contacto");
      const input = nuevo.querySelector('input[name="id-contacto[]"]');

      if (sel) sel.value = "";
      if (input) input.value = "";
      if (info) info.style.display = "none";

      container.appendChild(nuevo);
      Ocultar(nuevo);

   
      if (container.querySelectorAll(".contacto-item").length === 5) {
        botonAgregarContacto.disabled = true;
      }
    }
  });
};


const prellenadoFecha = () => { 
    const fechaInput = document.getElementById("FechaDisponibleEntrega");
    const fechaActual = new Date();
    fechaActual.setHours(fechaActual.getHours() -1); // Sumar 3 horas a la fecha actual, acá aparece como resta pero es porque el toISOString lo convierte a UTC y Chile es UTC-4
    fechaInput.value = fechaActual.toISOString().slice(0, 16);
};

const validarFormulario = () => {

    let error = [];
    const validarTexto = (texto, min, max) =>  texto && texto.length >= min && texto.length <= max;
    const validarMail = (mail) => {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(mail);
    }
    const validarTelefono = (telefono) => {
    const regex = /^\+\d{3}\.\d{8}$/;
    return regex.test(telefono)};

    let regionInput = document.getElementById('region');
    let comunaInput = document.getElementById('comuna');
    let sectorInput = document.getElementById('sector');
    let nombreInput = document.getElementById('nombre');
    let emailInput = document.getElementById('email');
    let telefonoInput = document.getElementById('telefono');
    
    let tipoInput = document.getElementById('tipo');
    let cantidadInput = document.getElementById('cantidad');
    let edadInput = document.getElementById('edad');
    let unidadEdadInput = document.getElementById('unidadMedidaEdad');
    let fechaInput = document.getElementById('FechaDisponibleEntrega');



    if (!regionInput.value) {
        error.push("Debe seleccionar una región.");
    }
    if (!comunaInput.value) {
        error.push("Debe seleccionar una comuna.");
    }
    if (sectorInput.value){
        if (!validarTexto(sectorInput.value, 0, 100)) {
            error.push("El sector debe tener entre 0 y 100 caracteres.");
        }
    }
    if (nombreInput.value) {
        if (!validarTexto(nombreInput.value, 3, 50)) {
            error.push("El nombre debe tener entre 3 y 50 caracteres.");
        }
    }else {
        error.push("El nombre es obligatorio.");
    }
    if (emailInput.value) {
        if (!validarMail(emailInput.value) || emailInput.value.length > 100) {
            error.push("El correo electrónico no es válido.");
        }
    } else {
        error.push("El correo electrónico es obligatorio.");
    }
    if (telefonoInput.value) {
        if (!validarTelefono(telefonoInput.value)) {
            error.push("El teléfono no es válido. Debe seguir el formato +CCC.NNNNNNNN.");
        }
    }

    const contactos = document.querySelectorAll('.contacto-item');
    let numContactos = 0;

    contactos.forEach((contacto) => {
        const metodo = contacto.querySelector('.contactar_por');
        const idContacto = contacto.querySelector('.id-contacto');

        if (metodo.value) {
            numContactos += 1;
            if (!idContacto.value || !validarTexto(idContacto.value, 4, 50)) {
                error.push("El ID de contacto o URL debe tener entre 4 y 50 caracteres.");
            }
        }
    });

    if( numContactos >5 ) {
        error.push("No puede agregar más de 5 métodos de contacto.");
    }

    if (!tipoInput.value) {
        error.push("Debe seleccionar una opción.");
    }
    if (cantidadInput.value) {
        if (cantidadInput.value < 1) {
            error.push("La cantidad debe ser un número positivo.");
        }
    }else {
        error.push("La cantidad es obligatoria.");
    }
    if (edadInput.value) {
        if (edadInput.value < 1) {
            error.push("La edad debe ser un número positivo.");
        }
    }else {
        error.push("La edad es obligatoria.");
    }
    if (!unidadEdadInput.value) {
        error.push("Debe seleccionar una unidad de medida para la edad.");
    }
    
    if (fechaInput.value) {
        const fechaSeleccionada = new Date(fechaInput.value);
        const fechaActual = new Date();
        const fechaLimite = new Date(fechaActual.getTime() + 3 * 60 * 60 * 1000);
        if (fechaSeleccionada < fechaLimite) {
            error.push("La fecha debe ser al menos 3 horas en el futuro.");
        }
    } else {
        error.push("La fecha es obligatoria.");
    }
    
    //if (descripcionInput) Acá al ser opcional no consideré necesario una validación
    
    //Validación fotos
    const inputsFoto = document.querySelectorAll('input[name="foto"]');
    let cantidadFotos = 0;
    let unaFoto = false;

    inputsFoto.forEach((input) => {
        if (input.files.length > 0) {
            cantidadFotos += input.files.length;   //Esto pues cada input puede tener 0 o n fotos
            unaFoto = true;
        }
    });

    if (!unaFoto) {
        error.push("Debe subir al menos una foto.");
    }
    if (cantidadFotos > 5) {
        error.push("No puede subir más de 5 fotos.");
    }

    if (error.length > 0) {
        alert(error.join("\n"));
        return false;
    }
    return true;
};





contactoPor()
prellenadoFecha()
agregarFotos()

const confirmacion = document.getElementById("confirmacion");
const botonSi = document.getElementById("si");
const botonNo = document.getElementById("no");
const botonEnviar = document.getElementById("enviar");


botonEnviar.addEventListener("click", () => {
    confirmacion.style.display = "block";
});

botonNo.addEventListener("click", () => {
    confirmacion.style.display = "none";
});

botonSi.addEventListener("click", (e) => {
    const ok = validarFormulario(); 
    if (ok === false) {
      e.preventDefault();
      confirmacion.style.display = "none";           
    }
    else {
      confirmacion.style.display = "none";
    }
  });
