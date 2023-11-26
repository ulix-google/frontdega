import logging
import google.auth
from googleapiclient import discovery


class Bodegabar:
    """Bodegabar can be used to interact with the Bodegabar (data).

    Bodegabar has functionality for reading pull up data created by the
    bodegabar (currently stored in a Google Sheet).

    Attributes:
        sheet_tab_name: A string representing the name of the tab sheet in
          which pull up data is stored.
        spreadsheet_id: A string representing the spreadsheet ID which
          contains the sheet which stores pull up data.
        first_date_cell: A string representing the first (top to bottom) date 
          cell (e.g. "A3").
        fist_total_pull_up_cell: A string representing the first (top to bottom) 
          cell that holds the total pull up data (e.g. "E3").
    """

    def __init__(self, 
                 sheet_tab_name: str, 
                 spreadsheet_id: str, 
                 first_date_cell: str,
                 fist_total_pull_up_cell: str):
        """Initializes the instance with the provided Google Sheet metadata.

        Args:
          sheet_tab_name: The name of the tab sheet in which pull up data is
            stored.
          spreadsheet_id: The spreadsheet ID which contains the sheet which
            stores pull up data.
          first_date_cell: A string representing the first (top to bottom) date 
            cell (e.g. "A3").
          fist_total_pull_up_cell: A string representing the first (top to 
            bottom) cell that holds the total pull up data (e.g. "E3").
        """
        credentials, _ = google.auth.default()
        service_resource = discovery.build("sheets", "v4", credentials=credentials)
        self.sheet_service = service_resource.spreadsheets()
        
        self._sheet_tab_name = sheet_tab_name
        self._spreadsheet_id = spreadsheet_id
        self._first_date_cell = first_date_cell
        self._fist_total_pull_up_cell = fist_total_pull_up_cell

    def read_total_pull_ups(self):
        ROW_LENGTH = 500
        dates = self._read_dates(ROW_LENGTH)
        total_pull_ups = self._read_total_pull_ups(ROW_LENGTH)
        out = []
        for i in range(len(dates)):
            total_count = int(total_pull_ups[i][0])
            if total_count == 0:
                continue
            element = {
                "date": dates[i][0],
                "count": int(total_pull_ups[i][0]),
            }
            out.append(element)
            
        logging.getLogger().info(f"response: {out}")
        return out
    
    def _read_total_pull_ups(self, row_length:int = 30):
        # The sheet service expects a range in the form of:
        # <Sheet Tab Name>!<Cell Range>.
        # Example 1: Exercise!A2
        # Example 2: Project!A2:B4
        end_range = str(int(self._fist_total_pull_up_cell[1]) + row_length)
        sheet_range = (
            self._sheet_tab_name + "!" 
            + self._fist_total_pull_up_cell + ":" 
            + self._fist_total_pull_up_cell[0] + end_range
        )
        result = (
            self.sheet_service.values()
            .get(spreadsheetId=self._spreadsheet_id, range=sheet_range)
            .execute()
        )
        values = result.get("values", [])
        if not values:
            logging.getLogger().error(f"Failed to read a value.")
            return 0
        return values
    
    def _read_dates(self, row_length:int = 30):
        # The sheet service expects a range in the form of:
        # <Sheet Tab Name>!<Cell Range>.
        # Example 1: Exercise!A2
        # Example 2: Project!A2:B4
        end_range = str(int(self._first_date_cell[1]) + row_length)
        sheet_range = (
            self._sheet_tab_name + "!" 
            + self._first_date_cell + ":" 
            + self._first_date_cell[0] + end_range
        )
        result = (
            self.sheet_service.values()
            .get(spreadsheetId=self._spreadsheet_id, range=sheet_range)
            .execute()
        )
        values = result.get("values", [])
        if not values:
            logging.getLogger().error(f"Failed to read a value.")
            return 0
        return values
