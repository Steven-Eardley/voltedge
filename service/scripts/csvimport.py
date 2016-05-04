from octopus.modules.sheets import commasep, sheets

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

SPEC = [
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
        "coerce": ["date"],
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
