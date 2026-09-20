import boto3
from collections import defaultdict

tagging = boto3.client(
    "resourcegroupstaggingapi",
    region_name="af-south-1"
)

REQUIRED_TAGS = [
    "CostCentre",
    "Team",
    "Environment"
]


def audit_tag_compliance():

    non_compliant = {}

    paginator = tagging.get_paginator(
        "get_resources"
    )

    for page in paginator.paginate():

        for resource in page[
            "ResourceTagMappingList"
        ]:

            arn = resource[
                "ResourceARN"
            ]

            existing_tags = {
                t["Key"]
                for t in resource.get(
                    "Tags",
                    []
                )
            }

            missing = [
                tag
                for tag in REQUIRED_TAGS
                if tag not in existing_tags
            ]

            if missing:
                non_compliant[
                    arn
                ] = missing

    return non_compliant


violations = audit_tag_compliance()

print(
    f"Violations: "
    f"{len(violations)}"
)