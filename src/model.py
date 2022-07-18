
from datetime import datetime
import os
import json

class MODEL:

    def __init__(self, par_dir):
        self.par_dir = par_dir

    def build(self):
        None

    def run(self):
        while True:
            self.curr_time = datetime.utcnow()
            if self.curr_time.second%5 == 0:
                self._save_val()

    def _save_val(self):
        curr_time = self.curr_time.strftime("%Y-%m-%d %H:%M:%S")
        self.dict_time = {"curr_time": curr_time}
        path = os.path.join(self.par_dir, "data", "file.json")
        with open(path, "w") as file:
            json.dump(self.dict_time, file)