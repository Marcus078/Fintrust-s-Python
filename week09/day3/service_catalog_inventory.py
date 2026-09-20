ervice_catalog_inventory.pyimport boto3

sc = boto3.client(
    "servicecatalog",
    region_name="af-south-1"
)

shared = sc.list_accepted_portfolio_shares()[
    "PortfolioDetails"
]

owned = sc.list_portfolios()[
    "PortfolioDetails"
]

all_portfolios = {
    p["Id"]: p
    for p in shared + owned
}

for pid, portfolio in all_portfolios.items():

    print(
        f"\nPortfolio:"
        f" {portfolio['DisplayName']}"
    )

    products = sc.search_products_as_admin(
        PortfolioId=pid
    )["ProductViewDetails"]

    for p in products:

        summary = p[
            "ProductViewSummary"
        ]

        print(
            f"Product: "
            f"{summary['Name']}"
        )