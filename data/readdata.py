import pandas as pd


def read_materials_dataset() -> pd.DataFrame:
    path_file: str = r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Materiales_Metalicos.xlsx"

    carbon_steel: pd.DataFrame = pd.read_excel(path_file, "Carbon Steel", engine="openpyxl")
    alloy_steel: pd.DataFrame = pd.read_excel(path_file, "Alloy Steel", engine="openpyxl")
    stainless_steel: pd.DataFrame = pd.read_excel(path_file, "Stainless Steel", engine="openpyxl")
    cast_iron: pd.DataFrame = pd.read_excel(path_file, "Cast Iron", engine="openpyxl")
    aluminum_alloys: pd.DataFrame = pd.read_excel(path_file, "Aluminum Alloys", engine="openpyxl")
    nickel_alloys: pd.DataFrame = pd.read_excel(path_file, "Nickel Alloys", engine="openpyxl")
    copper_alloys: pd.DataFrame = pd.read_excel(path_file, "Copper Alloys", engine="openpyxl")
    titanium_alloys: pd.DataFrame = pd.read_excel(path_file, "Titanium Alloys", engine="openpyxl")

    materials_dataset: pd.DataFrame = pd.concat([carbon_steel, alloy_steel, stainless_steel,
                                                 cast_iron, aluminum_alloys, nickel_alloys,
                                                 copper_alloys, titanium_alloys], ignore_index=True,
                                                sort=False)

    return materials_dataset


def read_sections_dataset() -> pd.DataFrame:
    path_file: str = r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Perfiles_Metalicos.xlsx"

    ipn: pd.DataFrame = pd.read_excel(path_file, "IPN", engine="openpyxl", header=[0, 1]).dropna(axis=1, how="all")
    ipe: pd.DataFrame = pd.read_excel(path_file, "IPE", engine="openpyxl", header=[0, 1]).dropna(axis=1, how="all")
    heb: pd.DataFrame = pd.read_excel(path_file, "HEB", engine="openpyxl", header=[0, 1]).dropna(axis=1, how="all")
    hea: pd.DataFrame = pd.read_excel(path_file, "HEA", engine="openpyxl", header=[0, 1]).dropna(axis=1, how="all")
    hem: pd.DataFrame = pd.read_excel(path_file, "HEM", engine="openpyxl", header=[0, 1]).dropna(axis=1, how="all")
    upn: pd.DataFrame = pd.read_excel(path_file, "UPN", engine="openpyxl", header=[0, 1]).dropna(axis=1, how="all")
    l: pd.DataFrame = pd.read_excel(path_file, "L", engine="openpyxl", header=[0, 1]).dropna(axis=1, how="all")
    ld: pd.DataFrame = pd.read_excel(path_file, "LD", engine="openpyxl", header=[0, 1]).dropna(axis=1, how="all")
    t: pd.DataFrame = pd.read_excel(path_file, "T", engine="openpyxl", header=[0, 1]).dropna(axis=1, how="all")

    sections_dataset: pd.DataFrame = pd.concat([ipn, ipe, heb, hea, hem, upn, l, ld, t], ignore_index=True, sort=False)

    return sections_dataset
