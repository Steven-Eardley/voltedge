from octopus.modules.sheets import commasep, sheets
from octopus.modules.infosys import models

""""
{
    "col_name": "<name as it appears in the sheet>",
    "trim": "<whether to whitespace trim>",
    "normalised_name": "<normalised name of the column>",
    "default": "<default value if not set or set to the empty string>",
    "coerce": ["<name of coerce function>"],
    "ignore_values": ["<values that should be treated as empty string>"]
}
"""

SPEC = {
    "columns": [
        {
            "col_name": "reference",
            "coerce": ["unicode"],
        },
        {
            "col_name": "name",
            "coerce": ["unicode"],
        },
        {
            "col_name": "latitude",
            "coerce": ["float"],
        },
        {
            "col_name": "longitude",
            "coerce": ["float"],
        },
        {
            "col_name": "town",
            "coerce": ["unicode"],
        },
        {
            "col_name": "county",
            "coerce": ["unicode"],
        },
        {
            "col_name": "postcode",
            "coerce": ["unicode"],
        },
        {
            "col_name": "deviceOwnerName",
            "normalised_name": "device_owner_name",
            "coerce": ["unicode"],
        },
        {
            "col_name": "deviceOwnerWebsite",
            "normalised_name": "device_owner_website",
            "coerce": ["url"],
        },
        {
            "col_name": "deviceControllerName",
            "normalised_name": "device_controller_name",
            "coerce": ["unicode"],
        },
        {
            "col_name": "deviceControllerWebsite",
            "normalised_name": "device_controller_website",
            "coerce": ["url"],
        },
        {
            "col_name": "deviceNetworks",
            "normalised_name": "device_networks",
            "coerce": ["unicode"],
        },
        {
            "col_name": "chargeDeviceStatus",
            "normalised_name": "charge_device_status",
            "coerce": ["unicode"],
        },
        {
            "col_name": "dateCreated",
            "normalised_name": "date_created",
            "coerce": ["utcdatetime"],
            "ignore_values": ["0000-00-00 00:00:00"]
        },
        {
            "col_name": "paymentRequired",
            "normalised_name": "payment_required",
            "coerce": ["bool"],
        },
        {
            "col_name": "subscriptionRequired",
            "normalised_name": "subscription_required",
            "coerce": ["bool"],
        },
        {
            "col_name": "parkingFeesFlag",
            "normalised_name": "parking_fees",
            "coerce": ["bool"],
        },
        {
            "col_name": "onStreetFlag",
            "normalised_name": "on_street",
            "coerce": ["bool"],
        },
        {
            "col_name": "locationType",
            "normalised_name": "location_type",
            "coerce": ["unicode"],
        },
        {
            "col_name": "access24Hours",
            "normalised_name": "24_hr_access",
            "default": None,
            "coerce": ["bool"],
        },
        {
            "col_name": "connector1Type",
            "normalised_name": "connector_type",
            "coerce": ["unicode"],
        },
        {
            "col_name": "connector1RatedOutputKW",
            "normalised_name": "connector_kw",
            "coerce": ["float"],
        },
        {
            "col_name": "connector1OutputCurrent",
            "normalised_name": "connector_amp",
            "coerce": ["float"],
        },
        {
            "col_name": "connector1RatedVoltage",
            "normalised_name": "connector_volt",
            "coerce": ["float"],
        },
        {
            "col_name": "connector1ChargeMethod",
            "normalised_name": "connector_charge_method",
            "coerce": ["unicode"],
        },
        {
            "col_name": "connector1Description",
            "normalised_name": "connector_description",
            "coerce": ["unicode"],
        },
    ]
}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file', help='csv file to upload')
    args = parser.parse_args()

    if not args.file:
        parser.print_help()
        exit(1)
    else:
        # Column reader for the CSV spreadsheet
        reader = commasep.CsvReader(args.file)

        # Generate objects for the sheet rows
        mysheet = sheets.ObjectByRow(reader=reader, spec=SPEC)

        # Edit the struct that we have generated from above; fold lat and lon into an object
        struct = mysheet.dataobj_struct()
        location_substruct = {
            'fields': {
                'lat': {'coerce': 'float'},
                'lon': {'coerce': 'float'}
            }
        }

        struct['objects'] = ['location']
        struct['structs'] = {'location': location_substruct}
        del struct['fields']['latitude']
        del struct['fields']['longitude']

        # Make the object's data match the struct, and save to an ES compatible model
        objs = mysheet.dicts()

        for obj in objs:
            obj['location'] = {'lat': obj['latitude'], 'lon': obj['longitude']}
            del obj['latitude']
            del obj['longitude']
            ism = models.InfoSysModel(type='charger', record_struct=struct, record=obj)
            ism.save()

