import math

DEVICE_SPECS = {
    "Snowball-Storage": 80,
    "Snowball-Compute": 28,
    "Snowmobile": 100000
}

SNOWMOBILE_THRESHOLD = 10000


def plan_snow_transfer(
        data_size_tb,
        purpose="archive"
):

    if (
        data_size_tb >=
        SNOWMOBILE_THRESHOLD
    ):
        count = math.ceil(
            data_size_tb /
            DEVICE_SPECS["Snowmobile"]
        )

        return {
            "device":
                "Snowmobile",
            "count":
                count
        }

    device = (
        "Snowball-Storage"
        if purpose == "archive"
        else "Snowball-Compute"
    )

    usable = DEVICE_SPECS[
        device
    ]

    count = math.ceil(
        data_size_tb /
        usable
    )

    return {
        "device": device,
        "count": count,
        "capacity":
            count * usable
    }


plan = plan_snow_transfer(
    3000,
    "archive"
)

print(plan)