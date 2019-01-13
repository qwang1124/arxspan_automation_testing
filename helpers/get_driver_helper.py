import os
import os.path
from pathlib import Path


class GetDriverHelper:
    @staticmethod
    def get_chrome_driver():
        path = Path(Path(os.getcwd()).parent)
        path = Path(path).parent
        if os.name == 'nt':
            return str(path.joinpath('drivers/chromedriver.exe'))
        return str(path.joinpath('drivers/chromedriver'))
