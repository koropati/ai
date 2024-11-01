import pandas as pd
import numpy as np

class ExcelReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.alternatives = None
        self.criteria_names = None
        self.criteria_type = None
        self.weights = None
        self.criteria_values = None
        self.alternative_labels = None

    def read_excel(self):
        # Baca data dari sheet pertama (kriteria dan nilai)
        df = pd.read_excel(self.filepath, sheet_name=0, header=None)

        # Baris pertama (0) adalah nama-nama kriteria
        self.criteria_names = df.iloc[0, 1:].values

        # Baris kedua (1) adalah jenis kriteria (benefit atau cost)
        self.criteria_type = df.iloc[1, 1:].values

        # Baris ketiga (2) adalah bobot tiap kriteria
        self.weights = df.iloc[2, 1:].values.astype(float)

        # Kolom pertama adalah kode alternatif
        self.alternatives = df.iloc[3:, 0].values

        # Sisanya adalah nilai kriteria
        self.criteria_values = df.iloc[3:, 1:].values.astype(float)

        # Baca data dari sheet kedua (label alternatif)
        df_labels = pd.read_excel(self.filepath, sheet_name=1, header=None)
        
        # Buat dictionary untuk mapping kode alternatif ke label/nama alternatif
        self.alternative_labels = dict(zip(df_labels[0], df_labels[1]))

        return {
            "alternatives": self.alternatives,
            "criteria_names": self.criteria_names,
            "criteria_type": self.criteria_type,
            "weights": self.weights,
            "criteria_values": self.criteria_values,
            "alternative_labels": self.alternative_labels
        }
