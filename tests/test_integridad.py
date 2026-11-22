import unittest
from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
class IntegridadDatos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df=pd.read_csv(ROOT/'data'/'precios_historicos_normalizados.csv',parse_dates=['Fecha'])
    def test_columnas(self):
        self.assertEqual(list(self.df.columns),['Fecha','Cierre','Apertura','Maximo','Minimo','Volumen'])
    def test_fechas_y_nulos(self):
        self.assertTrue(self.df.Fecha.is_monotonic_increasing)
        self.assertFalse(self.df.Fecha.duplicated().any())
        self.assertFalse(self.df.isna().any().any())
    def test_ohlc(self):
        d=self.df
        self.assertTrue((d.Maximo>=d[['Apertura','Cierre','Minimo']].max(axis=1)).all())
        self.assertTrue((d.Minimo<=d[['Apertura','Cierre','Maximo']].min(axis=1)).all())
        self.assertTrue((d.Volumen>=0).all())
    def test_tamano(self):
        self.assertEqual(len(self.df),2518)
if __name__=='__main__':unittest.main()
