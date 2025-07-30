# Pandas tool for code execution
import pandas as pd
import matplotlib.pyplot as plt
import io
import traceback
import re
class PandasTool:
    def __init__(self, df):
        self.df = df

    def run_code(self, code):
        local_vars = {'df': self.df, 'pd': pd, 'plt': plt}
        try:
             # Remove markdown formatting like ```python ... ```
            if code.startswith("```"):
                code = re.sub(r"```(?:python)?", "", code)
                code = code.replace("```", "").strip()
            exec(code, {}, local_vars)
            if 'result' in local_vars:
                return str(local_vars['result'])
            return "Executed successfully"
        except Exception as e:
            return f"Error:\n{traceback.format_exc()}"
