import boto3
import time
from datetime import datetime

dms = boto3.client(
    "database-migration-service",
    region_name="af-south-1"
)


def get_task_progress(task_arn):

    response = dms.describe_replication_tasks(
        Filters=[
            {
                "Name": "replication-task-arn",
                "Values": [task_arn]
            }
        ]
    )

    if not response["ReplicationTasks"]:
        return None

    task = response["ReplicationTasks"][0]

    stats = task.get(
        "ReplicationTaskStats",
        {}
    )

    return {
        "task_id":
            task["ReplicationTaskIdentifier"],
        "status":
            task["Status"],
        "tables_loaded":
            stats.get(
                "TablesLoaded",
                0
            ),
        "tables_loading":
            stats.get(
                "TablesLoading",
                0
            ),
        "tables_errored":
            stats.get(
                "TablesErrored",
                0
            ),
        "full_load_pct":
            stats.get(
                "FullLoadProgressPercent",
                0
            )
    }


def monitor_task(
        task_arn,
        poll_interval=30
):

    terminal = {
        "stopped",
        "failed",
        "deleting"
    }

    while True:

        progress = get_task_progress(
            task_arn
        )

        if not progress:
            break

        print(
            f"{progress['status']} "
            f"{progress['full_load_pct']}%"
        )

        if (
            progress["status"]
            in terminal
        ):
            break

        time.sleep(
            poll_interval
        )
