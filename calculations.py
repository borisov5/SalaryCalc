import os
import json

from global_constants import *


def parse_to_float(input_value):
    try:
        result = float(input_value)
        return result
    except:
        print("Exception, cannot parse this string to float")
    return False


def employee_calculations(bms, pe, y, it, ampi, hi, pit):
    bms = parse_to_float(bms)
    if bms == False:
        print("Incorrect input, cannot parse bms to float")
        return False

    pe = parse_to_float(pe)
    if pe == False:
        print("Incorrect input, cannot parse pe to float")
        return False

    y = parse_to_float(y)
    if y == False:
        print("Incorrect input, cannot parse y to float")
        return False

    ssi = bms + ((bms * pe * y) / 100)

    tb = ssi - ((ssi * (it + ampi + hi)) / 100)

    income_tax = ssi * (it / 100)

    additional_mandatory_pension_insurance = ssi * (ampi / 100)

    health_insurance = ssi * (hi / 100)

    natbr = tb - (tb * (pit / 100))

    data_obj = {
        'BMS': format(bms, '.2f'),
        'SSI': format(ssi, '.2f'),
        'PE': pe,
        'Y': int(y),
        'IT': format(income_tax, '.2f'),
        'AMPI': format(additional_mandatory_pension_insurance, '.2f'),
        'HI': format(health_insurance, '.2f'),
        'TB': format(tb, '.2f'),
        'NATBR': format(natbr, '.2f'),
    }

    with open(os.path.join(DB_FOLDER_NAME, DATA_FILE), 'w') as json_file:
        json_file.write(json.dumps(data_obj))
    return True


def employer_calculations(bms, pe, y, eit, eampi, awod, ehi):
    bms = parse_to_float(bms)
    if bms == False:
        print("Incorrect input, cannot parse bms to float")
        return False

    pe = parse_to_float(pe)
    if pe == False:
        print("Incorrect input, cannot parse pe to float")
        return False

    y = parse_to_float(y)
    if y == False:
        print("Incorrect input, cannot parse y to float")
        return False

    ssi = bms + ((bms * pe * y) / 100)

    employer_income_tax = ssi * (eit / 100)

    employer_additional_mandatory_pension_insurance = ssi * (eampi / 100)

    accident_at_work_and_occupational_disease = ssi * (awod / 100)

    employer_health_insurance = ssi * (ehi / 100)

    total_costs_to_the_employer = employer_income_tax +\
                                  employer_additional_mandatory_pension_insurance + \
                                  accident_at_work_and_occupational_disease + \
                                  employer_health_insurance

    data_obj = {
        'EIT': format(employer_income_tax, '.2f'),
        'EAMPI': format(employer_additional_mandatory_pension_insurance, '.2f'),
        'AWOD': format(accident_at_work_and_occupational_disease, '.2f'),
        'EHI': format(employer_health_insurance, '.2f'),
        'TCTTE': format(total_costs_to_the_employer, '.2f'),
    }

    with open(os.path.join(DB_FOLDER_NAME, EMPLOYER_DATA_FILE), 'w') as json_file:
        json_file.write(json.dumps(data_obj))

    return True
