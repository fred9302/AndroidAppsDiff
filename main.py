import numpy as np
import pandas as pd

def read_csv(path: str):
    return pd.read_csv(path)

def main():
    paths = {
        "oneplus_8t": "/home/frederik/Dropbox/Frederik/Backups/OnePlus 8T/AppListBackup/app-list-backup-2025-11-21-21-59-25.csv",
        "oneplus_15": "/home/frederik/Dropbox/Frederik/Backups/OnePlus 15/AppListBackup/app-list-backup-2025-11-21-21-44-05.csv"
    }
    dfs = {
        "oneplus_8t": read_csv(paths["oneplus_8t"]),
        "oneplus_15": read_csv(paths["oneplus_15"])
    }
    installed_apps = {
        "oneplus_8t": pd.Series(dfs["oneplus_8t"].),
        "oneplus_15": 
    }

if __name__ == "__main__":
    main()