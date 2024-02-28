import json


def fill_values(report, values):
    for i in report:
        for j in values['values']:
            if i.get('id') == j.get('id'):
                i['value'] = j.get('value')
        if 'values' in i.keys():
            fill_values(i['values'], values)


with open("tests.json", "r") as report_file:
    report_data = json.load(report_file)
with open("values.json", "r") as values_file:
    values_data = json.load(values_file)

fill_values(report_data['tests'], values_data)

with open("report.json", "w") as report_file:
    json.dump(report_data, report_file, indent=1)
