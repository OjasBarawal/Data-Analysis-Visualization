import justpy as jp
import pandas


data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
pie_rating = data.groupby(['Course Name'])['Rating'].count()

chart_def = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Number of Ratings in the Courses'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    legend: {
        enabled: true
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Ratings',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""


def app():
    web_page = jp.QuasarPage()
    heading_1 = jp.QDiv(
        a=web_page,
        text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md"
    )
    paragraph_1 = jp.QDiv(
        a=web_page,
        text="These graphs represent course review analysis",
        classes="text-h5 text-center q-pa-md"
    )

    high_chart = jp.HighCharts(
        a=web_page,
        options=chart_def
    )

    high_chart_data = [
        {
            'name': name_var,
            'y': y_var
        }
        for name_var, y_var in zip(pie_rating.index, pie_rating)
    ]

    high_chart.options.series[0].data = high_chart_data

    return web_page


jp.justpy(app)