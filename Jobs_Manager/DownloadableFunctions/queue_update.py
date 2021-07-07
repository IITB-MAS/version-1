# PASSIVE

import pandas as pd
from pandas.core.common import SettingWithCopyWarning
import warnings
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

###################################################################################


def introduction():
    function_type = 'Queue update'
    dependant_functions = []
    active_passive = 'passive'
    performative_types = ['request_queue_update']
    return {'function_type': function_type, 'Dependant Function': dependant_functions, "active_passive": active_passive,
            "performative_types": performative_types}


###################################################################################

def execute(performative_type,job_data):
    try:
        job_details = eval(job_data)
    except:
        job_details = job_data

    import csv
    rest_all = []
    Ji = job_details[0]
    with open('DataBase\SingleMechineSequencing\job_data_Li_Ei.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for line in csv_reader:
            if eval(line[0]) != Ji:
                rest_all.append(line)

    print(rest_all)
    with open('DataBase\SingleMechineSequencing\job_data_Li_Ei.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Ji', 'Pi', 'Di', 'Di', 'Ei', 'allotment'])
        for line in rest_all:
            csv_writer.writerow(line)

        new_line = job_details
        csv_writer.writerow(new_line)

    output_performative_type = 'inform'
    output_result = 'done'
    comments = 'None'
    output_dict = {'performative_type': output_performative_type, 'result': output_result, 'comments': comments}
    return output_dict


###################################################################################

