
import os
import json
from dash import Dash, html, dcc, Input, Output, dash_table
from datetime import datetime
import json

class DASHBOARD():

    def __init__(self, par_dir):
        self.path_curr_time = os.path.join(par_dir, "data", "file.json")
        self.app = Dash('Sample')
        self.port = 8050
        self.dict_curr_time = {}
    
    def build(self):
        self._set_callback()
        self._set_layout()
        
    def _set_callback(self):
        self.app.callback(Output('curr-time','children'),
                            Input('interval', 'n_intervals')
                            )(self._get_curr_time)

    def _set_layout(self):
        self.app.layout = html.Div(children=[
                                    html.H1(children='MAREX'),
                                    html.H3(children='Current_Time'),
                                    html.Br(),
                                    html.Div(id="curr-time"),
                                    dcc.Interval(id = 'interval', interval = 2*1000, n_intervals = 0)
                                    ])

    def _get_curr_time(self, n):
        with open(self.path_curr_time, "r") as file:
            curr_time = json.load(file)
        pair_table = [{'Val_1': 'curr_time', "Val_2": curr_time['curr_time']}]
        return dash_table.DataTable(pair_table, id = 'curr-time-table')

    def run(self):
        self.app.run_server(port = self.port, host='0.0.0.0')