import boto3

fis = boto3.client(
    "fis",
    region_name="af-south-1"
)


def summarise_fis_experiments():

    experiments = (
        fis.list_experiments()
           .get(
               "experiments",
               []
            )
    )

    for exp in experiments:

        detail = (
            fis.get_experiment(
                id=exp["id"]
            )["experiment"]
        )

        print(
            exp["id"],
            detail["state"]["status"]
        )