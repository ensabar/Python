import json


def read_json_plot_properties(file, plot_type):
    with open(file, 'r') as myfile:
        data=myfile.read()

    title = data[plot_type]['title']
    x_label = data[plot_type]['x_label']
    y_label = data[plot_type]['y_label']
    data.close()
    return title, x_label, y_label
