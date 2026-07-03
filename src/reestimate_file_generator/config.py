from dataclasses import dataclass


@dataclass(frozen=True)
class FileConfig:
    filename: str
    sheet_name: str
    loan_col_idx: int = 0
    cancellation_amount_col: str | None = None


PORTFOLIO_FILENAME = "Loan_Portfolio Characteristics (5).xlsx"
CANCELLATION_AMOUNT_COL = "Cancellation Amount"
HISTORICAL_FILENAME = "Historical Loan Performance (Time series Dataset) (3) (1).xlsx"
HISTORICAL_SHEET = "Sheet1"
HISTORICAL_OBLIGATION_COL_IDX = 2

FILE_CONFIGS: list[FileConfig] = [
    FileConfig(
        "Loan_Portfolio Characteristics (5).xlsx",
        "Sheet1",
        cancellation_amount_col=CANCELLATION_AMOUNT_COL,
    ),
    FileConfig(
        "Historical Loan Performance (Time series Dataset) (3) (1).xlsx",
        "Sheet1",
    ),
    FileConfig("Forecasted P&I Schedules (Timeseries Dataset) (3).xlsx", "Sheet1"),
    FileConfig("Intragovernmental Transfer (IGT) Data (3).xlsx", "in"),
    FileConfig("Recovery Ratings (3).xlsx", "Sheet1"),
    FileConfig("Risk Ratings (3).xlsx", "Sheet1"),
    FileConfig("cashflow 32 loans (2).xlsx", "Sheet1"),
]
