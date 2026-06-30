from dataclasses import dataclass


@dataclass(frozen=True)
class FileConfig:
    filename: str
    sheet_name: str
    loan_col_idx: int = 0


PORTFOLIO_FILENAME = "Loan_Portfolio Characteristics (5).xlsx"

FILE_CONFIGS: list[FileConfig] = [
    FileConfig("Loan_Portfolio Characteristics (5).xlsx", "Sheet1"),
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
