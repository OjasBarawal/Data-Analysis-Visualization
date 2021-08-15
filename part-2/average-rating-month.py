import justpy as jp
import pandas


data = pandas.read_csv('reviews.csv', parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average = data.groupby('Month').mean()


chart_definition = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Course Rating by Month'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Months'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: true
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: 'Month {point.x} of {point.y} Stars'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Ratings',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""


def app():
    web_page = jp.QuasarPage()
    heading_1 = jp.QDiv(
        a=web_page,
        text='Analysis of Course Reviews',
        classes='text-h2 text-center text-weight-medium q-pa-md'
    )
    paragraph_1 = jp.QDiv(
        a=web_page,
        text='These Graphs represents Course Review Analysis.',
        classes='text-h5 text-center text-weight-regular q-pa-md'
    )
    high_charts = jp.HighCharts(a=web_page, options=chart_definition)

    high_charts.options.xAxis.categories = list(month_average.index)
    high_charts.options.series[0].data = list(month_average['Rating'])

    return web_page


jp.justpy(app)
