const A_porDia = () => {
    Highcharts.chart('avisosPorDia', {
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


