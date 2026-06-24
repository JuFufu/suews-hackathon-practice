"""Smoke test: confirm SUEWS (via supy) runs end to end.

Run with: python analysis/smoke_test.py
Uses supy's bundled sample dataset (not the hackathon city dataset,
which is released at kickoff on 24 June).
"""
import warnings

warnings.filterwarnings("ignore")
import supy as sp


def main():
    df_state, df_forcing = sp.load_SampleData()
    df_output, df_state_final = sp.run_supy(df_forcing.iloc[:288], df_state)
    print("SUEWS sample run OK")
    print(f"supy version: {sp.__version__}")
    print(df_output.SUEWS[["QN", "QH", "QE", "Tsurf"]].tail())


if __name__ == "__main__":
    main()
