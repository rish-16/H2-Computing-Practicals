"""
Unit converter.
Write a program that helps the user to convert a given quantity from one unit of (distance, area or volume) measurement to another.
The problem:
• Request an quantity from the user.
• Have the user specify if the quantity is a length, area or volume.
• Have the user select the base unit of measurement from the following list:
    • mm
    • cm
    • m
    • km.
• Then have the user select the desired base unit of measurement that the given quantity should be converted to.
• Print out converted quantity (including the new unit of measurement).
"""

magnitude = float(input('Enter a quantity: '))
option = input('Select either length, area, or volume: ')
base = input('Select base unit of measurement (mm, cm, m, km): ')
convert_to = input('Select base unit of measurement to convert to (mm, cm, m, km): ')

def convert_mm_cm(mm_value):
    return mm_value / 10

def convert_mm_m(mm_value):
    return mm_value / 10 / 100

def convert_mm_km(mm_value):
    return mm_value / 10/ 100 /1000

def convert_cm_mm(cm_value):
    return cm_value * 10

def convert_cm_m(cm_value):
    return cm_value / 100

def convert_cm_km(cm_value):
    return cm_value / 100 / 1000

def convert_m_mm(m_value):
    return m_value * 100 * 10

def convert_m_cm(m_value):
    return m_value * 100

def convert_m_km(m_value):
    return m_value / 1000

def convert_km_m(km_value):
    return km_value * 1000

def convert_km_cm(km_value):
    return km_value * 1000 * 100

def convert_km_mm(km_value):
    return km_value * 1000 * 100 * 10

def calc_area(length):
    return length * length

def calc_volume(length):
    return length * length * length

def get_value(magnitude, option, base, convert_to):
    if option == 'length':
        if base == 'mm' and convert_to == 'cm':
            value = convert_mm_cm(magnitude)
        elif base == 'mm' and convert_to == 'm':
            value = convert_mm_m(magnitude)
        elif base == 'mm' and convert_to == 'km':
            value = convert_mm_m(magnitude)

        elif base == 'cm' and convert_to == 'mm':
            value = convert_cm_mm(magnitude)
        elif base == 'cm' and convert_to == 'm':
            value = convert_mm_m(magnitude)
        elif base == 'cm' and convert_to == 'km':
            value = convert_mm_km(magnitude)

        elif base == 'm' and convert_to == 'mm':
            value = convert_m_mm(magnitude)
        elif base == 'm' and convert_to == 'cm':
            value = convert_m_cm(magnitude)
        elif base == 'm' and convert_to == 'km':
            value = convert_m_km(magnitude)

        elif base == 'km' and convert_to == 'mm':
            value = convert_km_mm(magnitude)
        elif base == 'km' and convert_to == 'cm':
            value = convert_km_cm(magnitude)
        elif base == 'km' and convert_to == 'm':
            value = convert_km_m(magnitude)

        unit1 = base
        unit2 = convert_to

    elif option == 'area':
        if base == 'mm' and convert_to == 'cm':
            value = convert_mm_cm(magnitude)
        elif base == 'mm' and convert_to == 'm':
            value = convert_mm_m(magnitude)
        elif base == 'mm' and convert_to == 'km':
            value = convert_mm_m(magnitude)

        elif base == 'cm' and convert_to == 'mm':
            value = convert_cm_mm(magnitude)
        elif base == 'cm' and convert_to == 'm':
            value = convert_mm_m(magnitude)
        elif base == 'cm' and convert_to == 'km':
            value = convert_mm_km(magnitude)

        elif base == 'm' and convert_to == 'mm':
            value = convert_m_mm(magnitude)
        elif base == 'm' and convert_to == 'cm':
            value = convert_m_cm(magnitude)
        elif base == 'm' and convert_to == 'km':
            value = convert_m_km(magnitude)

        elif base == 'km' and convert_to == 'mm':
            value = convert_km_mm(magnitude)
        elif base == 'km' and convert_to == 'cm':
            value = convert_km_cm(magnitude)
        elif base == 'km' and convert_to == 'm':
            value = convert_km_m(magnitude)

        value = calc_area(value)
        unit1 = base + '^2'
        unit2 = convert_to + '^2'

    elif option == 'volume':
        if base == 'mm' and convert_to == 'cm':
            value = convert_mm_cm(magnitude)
        elif base == 'mm' and convert_to == 'm':
            value = convert_mm_m(magnitude)
        elif base == 'mm' and convert_to == 'km':
            value = convert_mm_m(magnitude)

        elif base == 'cm' and convert_to == 'mm':
            value = convert_cm_mm(magnitude)
        elif base == 'cm' and convert_to == 'm':
            value = convert_mm_m(magnitude)
        elif base == 'cm' and convert_to == 'km':
            value = convert_mm_km(magnitude)

        elif base == 'm' and convert_to == 'mm':
            value = convert_m_mm(magnitude)
        elif base == 'm' and convert_to == 'cm':
            value = convert_m_cm(magnitude)
        elif base == 'm' and convert_to == 'km':
            value = convert_m_km(magnitude)

        elif base == 'km' and convert_to == 'mm':
            value = convert_km_mm(magnitude)
        elif base == 'km' and convert_to == 'cm':
            value = convert_km_cm(magnitude)
        elif base == 'km' and convert_to == 'm':
            value = convert_km_m(magnitude)

        value = calc_volume(value)
        unit1 = base + '^3'
        unit2 = convert_to + '^3'

    print ('{} {} = {} {}'.format(magnitude, unit1, value, unit2))

get_value(magnitude, option, base, convert_to)
