const API_URL = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
const contenedorDolares = document.getElementById(
    "dolars-container-javascrips"
);
const textoUltimaFecha = document.getElementById("ult-fecha-dolar");

function imprimirValores(dolar) {
    const nombreDolar = document.createElement("span");
    const precioVenta = document.createElement("p");
    const tituloVenta = document.createElement('b');
    const precioCompra = document.createElement("p");
    const tituloCompra = document.createElement('b');
    const variacion = document.createElement("p");
    const tituloVariacion = document.createElement("b");
    const contenedorDolar = document.createElement("div");

    tituloVenta.innerHTML = 'Venta: ';
    tituloCompra.innerHTML = 'Compra: ';
    tituloVariacion.innerHTML = 'Variación: ';
    tituloVariacion.className += 'text-white';
    precioVenta.appendChild(tituloVenta);
    precioCompra.appendChild(tituloCompra);
    variacion.appendChild(tituloVariacion);

    nombreDolar.innerHTML = dolar.nombre;
    precioVenta.innerHTML += `$${dolar.venta}`;
    dolar.compra !== 'No Cotiza' ? precioCompra.innerHTML += `$${dolar.compra}` : precioCompra.innerHTML += `No cotiza`;
    dolar.variacion ? variacion.innerHTML += `${dolar.variacion}%` : variacion.innerHTML += `-`;

    nombreDolar.className += 'pt-2 pb-2';
    contenedorDolar.className += "carta pt-2 pb-3";
    if (dolar.variacion !== undefined) {
        if (dolar.variacion.includes('-')){
            variacion.className += 'text-danger'
            variacion.innerHTML += ' ▼'
        } else {
            variacion.className += 'text-success';
            variacion.innerHTML += ' ▲'
        }
    }
    if (
        dolar.nombre !== "Dolar Soja" &&
        dolar.nombre !== "Argentina" &&
        dolar.nombre !== "Bitcoin"
    ) {
        contenedorDolar.appendChild(nombreDolar);
        contenedorDolar.appendChild(precioVenta);
        contenedorDolar.appendChild(precioCompra);
        contenedorDolar.appendChild(variacion);

        contenedorDolares.appendChild(contenedorDolar);
    } else if (dolar.nombre === "Argentina") {
        textoUltimaFecha.innerHTML = `Ultima actualización: ${dolar.fecha}`;
    }
}

function llamarApiDolares() {
    fetch(API_URL)
        .then((res) => res.json()) //SE PONE COMO PRIMER THEN
        .then((res) => {
            //RES = ARRAY DE OBJETOS
            for (dolar of res) {
                imprimirValores(dolar.casa);
            }
        });
}

llamarApiDolares();
