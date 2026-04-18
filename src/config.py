"""Project-wide paths and constants. Import from notebooks, never hardcode paths."""

from pathlib import Path

# --- Paths ----------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_EXTERNAL = PROJECT_ROOT / "data" / "external"
DATA_INTERIM = PROJECT_ROOT / "data" / "interim"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
REFERENCES = PROJECT_ROOT / "references"
FIGURES = PROJECT_ROOT / "reports" / "figures"

# --- Raw file locations (single source of truth) -------------------------
LICENSES_RAW = DATA_RAW / "Delaware_Business_Licenses.csv"
SBA_7A_RAW = DATA_RAW / "foia-7a-fy2020-present-as-of-251231.csv"
SBA_504_RAW = DATA_RAW / "foia-504-fy2010-present-asof-251231.csv"
BUDGET_RAW = DATA_RAW / "Annual_Appropriated_Expense_and_Positions_Budgets.csv"
SBF_RAW = DATA_RAW / "Small_Business_Focus.csv"

# CENSUS_RAW = DATA_EXTERNAL / "census" / "de_acs_2023.csv"
# TRACTS_SHP = DATA_EXTERNAL / "boundaries" / "delaware_tracts.shp"

# --- Analysis parameters --------------------------------------------------
TARGET_STATE = "DE"
TARGET_STATE_FIPS = "10"  # Delaware FIPS code, for census joins
COUNTIES = ["New Castle", "Kent", "Sussex"]

# Active SSBCI participating lenders (for H1 capital-desert analysis)
SSBCI_LENDERS = [
    "Del-One Federal Credit Union",
    "True Access Capital",
    "Community Bank Delaware",
]
