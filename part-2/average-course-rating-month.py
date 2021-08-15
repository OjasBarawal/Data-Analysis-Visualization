import justpy as jp
import pandas


data = pandas.read_csv('reviews.csv', parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_course_average = data.groupby(['Month', 'Course Name']).mean().unstack()


chart_definition = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Course Rating by Month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor: '#FFFFFF'
    },
    xAxis: {
        title: {
            text: 'Months'
        },
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' Stars'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    legend: {
        enabled: true
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
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

    high_charts.options.xAxis.categories = list(month_course_average.index)

    high_charts_data = [
        {
            'name': name_var,
            'data': [data_var for data_var in month_course_average[name_var]]
        }
        for name_var in month_course_average.columns
    ]

    high_charts.options.series = high_charts_data

    return web_page


jp.justpy(app)
