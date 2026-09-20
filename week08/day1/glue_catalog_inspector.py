import boto3

glue = boto3.client(
    'glue',
    region_name='af-south-1'
)

# List all databases

print("DATABASES")
print("-" * 40)

db_response = glue.get_databases()

for db in db_response['DatabaseList']:
    print(f"Database: {db['Name']}")

# List all tables in fintrust_curated

print("\nTABLES")
print("-" * 40)

tbl_response = glue.get_tables(
    DatabaseName='fintrust_curated'
)

for tbl in tbl_response['TableList']:
    print(
        f"Table: {tbl['Name']} | "
        f"Location: "
        f"{tbl['StorageDescriptor']['Location']}"
    )

# Get schema for transactions table

tbl_detail = glue.get_table(
    DatabaseName='fintrust_curated',
    Name='transactions'
)

columns = (
    tbl_detail['Table']
    ['StorageDescriptor']
    ['Columns']
)

print("\nTRANSACTIONS TABLE SCHEMA")
print("-" * 40)

for col in columns:
    print(
        f"{col['Name']:25s} "
        f"{col['Type']}"
    )

# Show partition keys

partition_keys = (
    tbl_detail['Table']
    ['PartitionKeys']
)

print("\nPARTITION KEYS")
print("-" * 40)

for pk in partition_keys:
    print(
        f"{pk['Name']:25s} "
        f"{pk['Type']}"
    )