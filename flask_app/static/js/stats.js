const A_porDia = (points) => {
    Highcharts.chart('container1', {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Avisos por día'
        },
        xAxis: {
            type: 'datetime'
        },
        yAxis: {
            title: {
                text: 'Número de avisos'
            },
        },
        legend: {
            align: "left",
            verticalAlign: "top",
            borderWidth: 0,
        },
        tooltip: {
            shared: true,
            crosshairs: true,
        },
        series: [{
            name: 'Avisos',
            data: points,
            linewidth: 1,
            marker: {
                enabled: true,
                radius: 4
            }
        }]

    });
};

fetch("http://127.0.0.1:5000/avisos_por_dia")
    .then((response)=> response.json())
    .then((data) => {
        const points = data.map(({fecha, total}) => {
            const [year, month, day] = fecha
                .split("-")
                .map((part) => parseInt(part, 10));
            return [
                Date.UTC(year, month - 1, day), total
            ];
        });
        A_porDia(points);
    })
    .catch(console.error);

const A_porTipo = (total_perros,total_gatos) => {
    Highcharts.chart('container2', {
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Avisos por tipo'
        },
        series: [{
            name: 'Avisos',
            data: [
                {name: 'Perro', y: total_perros},
                {name: 'Gato', y: total_gatos}]
        }]
    });
};

fetch("http://127.0.0.1:5000/avisos_por_tipo")
    .then((response)=> response.json())
    .then(({perro, gato})=> A_porTipo(perro, gato))
    .catch(console.error);


const  A_porMes = (meses, perroMes, gatoMes) => {
    Highcharts.chart('container3',{
        chart: {
            type: 'column'
        },
        title: {
            text: 'perros vs gatos por mes'
        },
        xAxis: {
            categories: meses,
            title: {
                text :"Meses"
            }
        },
        yAxis: {
            title:{
                text:"Cantidad"
            }
        },
        series:[
            {name: "Perros", data: perroMes},
            {name: "Gatos", data: gatoMes},
        ],
    });
};


fetch("http://127.0.0.1:5000/avisos_por_mes")
    .then((response)=> response.json())
    .then((datos)=>{
        const meses = datos.map(response => response.mes);
        const perroMes = datos.map(response => response.perro);
        const gatoMes = datos.map(response => response.gato);
        A_porMes(meses,perroMes,gatoMes)
    })
    .catch(console.error);
