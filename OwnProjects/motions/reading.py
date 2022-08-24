import json


def read_json_plot_properties(file, motion, plot_type):
    with open(file, 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    title = obj[motion][plot_type]['title']
    x_label = obj[motion][plot_type]['x_label']
    y_label = obj[motion][plot_type]['y_label']
    
    return title, x_label, y_label
