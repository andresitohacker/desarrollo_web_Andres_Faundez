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
        const points = data.map(({date, count}) => {
            const [year, month, day] = date
                .split("-")
                .map((part) => parseInt(part, 10));
            return [
                Date.UTC(year, month - 1, day), count
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


const  A_porMes = () => {
    Highcharts.chart('container3',{
        chart: {
            type: 'column'
        },
        title: {
            text: 'perros vs gatos por mes'
        },
        xAxis: {
            
        } 
    })
}