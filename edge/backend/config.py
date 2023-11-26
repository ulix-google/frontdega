import os
from dotenv import load_dotenv

from bodegabar import bodegabar


class Config:
    """Setup configuration used by the server.

    Initializes and provides handles to the distinct clients and objects
    needed by the backend server.

    Attributes:
        None
    """

    def __init__(self):
        # Load a .env file which should hold variables for the pull up service 
        # in the following format:
        #   SPREADSHEET_ID="example_spreadsheet_id"
        #   SHEET_TAB_NAME="example_sheet_tab_name"
        load_dotenv()
        SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
        SHEET_TAB_NAME = os.getenv("SHEET_TAB_NAME")
        FIRST_DATE_CELL = os.getenv("FIRST_DATE_CELL")
        FIRST_TOTAL_PULL_UP_CELL = os.getenv("FIRST_TOTAL_PULL_UP_CELL")
        self.bodega = bodegabar.Bodegabar(
            sheet_tab_name=SHEET_TAB_NAME,
            spreadsheet_id=SPREADSHEET_ID,
            first_date_cell=FIRST_DATE_CELL,
            fist_total_pull_up_cell=FIRST_TOTAL_PULL_UP_CELL,
        )
    