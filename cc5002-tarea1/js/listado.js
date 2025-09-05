const listaAvisos = [
    {
        id: 1,
        fechaPub: "01/01/2023",
        fechaEnt: "15/01/2023",
        comuna: "Santiago",
        sector: "Centro",
        tipo: "Perro",
        cantidad: 2,
        edad: "3 meses",
        contacto: "Juan Pérez",
        fotos: ["img/cachorro1.jpg"]
    },
    {
        id: 2,
        fechaPub: "05/02/2023",
        fechaEnt: "20/02/2023",
        comuna: "Providencia",
        sector: "Parque Bustamante",
        tipo: "Gato",
        cantidad: 1,
        edad: "1 año",
        contacto: "Ana Gómez",
        fotos: ["img/gato1.jpg"]
    },
    {
        id: 3,
        fechaPub: "10/03/2023",
        fechaEnt: "25/03/2023",
        comuna: "Ñuñoa",
        sector: "Plaza Egaña",
        tipo: "Gato",
        cantidad: 3,
        edad: "6 meses",
        contacto: "Carlos Ruiz",
        fotos: ["img/gato2.jpg"]
    },
    {
        id: 4,
        fechaPub: "15/04/2023",
        fechaEnt: "30/04/2023",
        comuna: "La Florida",
        sector: "Jardín Alto",
        tipo: "Perro",
        cantidad: 1,
        edad: "2 años",
        contacto: "María López",
        fotos: ["img/perro1.jpg"]
    },
    {
        id: 5,
        fechaPub: "20/05/2023",
        fechaEnt: "05/06/2023",
        comuna: "Puente Alto",
        sector: "Las Vizcachas",
        tipo: "Perro",
        cantidad: 2,
        edad: "4 meses",
        contacto: "Pedro Fernández",
        fotos: ["img/perro2.jpg"]
    }
];

const avisos = (id) => {
    const detalle = document.getElementById("detalles");
    const avisoSeleccionado = listaAvisos.find(aviso => aviso.id === id);
    document.getElementById("listado").style.display = "none";
    detalle.style.display = "block";
    detalle.innerHTML = `
        <h2>Detalles del Aviso</h2>
        <ul>
            <li>ID: ${avisoSeleccionado.id}</li>
            <li>Fecha de Publicación: ${avisoSeleccionado.fechaPub}</li>
            <li>Fecha de Entrega: ${avisoSeleccionado.fechaEnt}</li>
            <li>Comuna: ${avisoSeleccionado.comuna}</li>
            <li>Sector: ${avisoSeleccionado.sector}</li>
            <li>Tipo: ${avisoSeleccionado.tipo}</li>
            <li>Cantidad: ${avisoSeleccionado.cantidad}</li>
            <li>Edad: ${avisoSeleccionado.edad}</li>
            <li>Contacto: ${avisoSeleccionado.contacto}</li>
            <li>Fotos: ${avisoSeleccionado.fotos.map(foto => `<img src="${foto}" alt="Foto del aviso" width="240" height="320" style="margin: 5px; cursor: pointer;" onclick="FotoGrande('${foto}')">`).join(' ')}</li>
        </ul>
        </ul>
        <div class="boton">
            <a href="#" onclick="volverAListado()" class="volver">Volver al listado</a>
        </div>
        
    `;
};

const FotoGrande = (src) => {
    const foto = window.open("", "Foto", "width=600,height=800");
    foto.document.write(`<img src="${src}" alt="Foto ampliada" style="width:100%">`);
    foto.document.write(`<br><button onclick="window.close()">Cerrar</button>`);
};

const volverAListado = () => {
    document.getElementById("detalles").style.display = "none";
    document.getElementById("listado").style.display = "block";
};

//Todo esto lo tenia en el main.js pero no se por que no funcionaba al referenciarlo desde ahi