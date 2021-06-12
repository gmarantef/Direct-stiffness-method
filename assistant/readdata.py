# -*- coding: utf-8 -*-
"""
Created on Wed May 26 14:09:05 2021

@author: Guillermo
"""

from typing import List
import pandas as pd


# Función para la lectura del Dataset externo de materiales metálicos
def read_materials(pressure_unit: str) -> List[object]:
    from classes import materials as mt
    
    materials_list: List[object] = []
    
    # Carga del Dataset de materiales
    carbon_steel: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Materiales_Metalicos.xlsx",
            "Carbon Steel", engine="openpyxl")
    alloy_steel: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Materiales_Metalicos.xlsx",
            "Alloy Steel", engine="openpyxl")
    stainless_steel: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Materiales_Metalicos.xlsx",
            "Stainless Steel", engine="openpyxl")
    cast_iron: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Materiales_Metalicos.xlsx",
            "Cast Iron", engine="openpyxl")
    aluminum_alloys: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Materiales_Metalicos.xlsx",
            "Aluminum Alloys", engine="openpyxl")
    nickel_alloys: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Materiales_Metalicos.xlsx",
            "Nickel Alloys", engine="openpyxl")
    copper_alloys = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Materiales_Metalicos.xlsx",
            "Copper Alloys", engine="openpyxl")
    titanium_alloys: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Materiales_Metalicos.xlsx",
            "Titanium Alloys", engine="openpyxl")
    
    # Selecciono las variables deseadas de material, condición y E
    materials_data: pd.DataFrame = pd.concat([carbon_steel.iloc[:,[0,1,5]],
                                              alloy_steel.iloc[:,[0,1,5]],
                                              stainless_steel.iloc[:,[0,2,6]],
                                              cast_iron.iloc[:,[0,2,6]],
                                              aluminum_alloys.iloc[:,[0,1,5]],
                                              nickel_alloys.iloc[:,[0,1,5]],
                                              copper_alloys.iloc[:,[0,1,5]],
                                              titanium_alloys.iloc[:,[0,1,5]]],
                                              axis=0)
    
    # Cambio de unidades
    if pressure_unit == "kg/cm^2":
        materials_data.iloc[:,2] /= 14.22
    elif pressure_unit == "N/m^2" or pressure_unit == "Pa":
        materials_data.iloc[:,2] *= 6894.76
    elif pressure_unit == "kN/m^2" or pressure_unit == "kPa":
        materials_data.iloc[:,2] *= 6894.76e-3
    elif pressure_unit == "N/mm^2" or pressure_unit == "MPa":
        materials_data.iloc[:,2] *= 6894.76e-6
    elif pressure_unit == "kN/mm^2" or pressure_unit == "GPa":
        materials_data.iloc[:,2] *= 6894.76e-9
    elif pressure_unit == "atm":
        materials_data.iloc[:,2] /= 14.70
    elif pressure_unit == "bar":
        materials_data.iloc[:,2] /= 14.50
    elif pressure_unit == "psi":
        materials_data.iloc[:,2] /= 1.00
    elif pressure_unit == "kpsi":
        materials_data.iloc[:,2] /= 1000.00
    
    # Creo los objetos de la clase material
    for index, row in materials_data.iterrows():
        locals()["Material_"+str(index)] = mt.MaterialClass(row[0], row[1],
                                                            row[2],
                                                            materials_list,
                                                            pressure_unit)
        
    return materials_list


# Función para la lectura del Dataset externo de perfiles metálicos
def read_sections(area_unit: str, inertia_unit: str,
                  structure_type: str) -> List[object]:
    from classes import sections as sc
    
    sections_list: List[object] = []
    
    # Carga del Dataset de perfiles
    IPN: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Perfiles_Metalicos.xlsx",
            "IPN", engine="openpyxl", header=[0,1]).dropna(axis=1, how="all")
    IPE: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Perfiles_Metalicos.xlsx",
            "IPE", engine="openpyxl", header=[0,1]).dropna(axis=1, how="all")
    HEB: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Perfiles_Metalicos.xlsx",
            "HEB", engine="openpyxl", header=[0,1]).dropna(axis=1, how="all")
    HEA: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Perfiles_Metalicos.xlsx",
            "HEA", engine="openpyxl", header=[0,1]).dropna(axis=1, how="all")
    HEM: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Perfiles_Metalicos.xlsx",
            "HEM", engine="openpyxl", header=[0,1]).dropna(axis=1, how="all")
    UPN: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Perfiles_Metalicos.xlsx",
            "UPN", engine="openpyxl", header=[0,1]).dropna(axis=1, how="all")
    L: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Perfiles_Metalicos.xlsx",
            "L", engine="openpyxl", header=[0,1]).dropna(axis=1, how="all")
    LD: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Perfiles_Metalicos.xlsx",
            "LD", engine="openpyxl", header=[0,1]).dropna(axis=1, how="all")
    T: pd.DataFrame = pd.read_excel(
            r"C:\Users\Guillermo\Desktop\Python TFM\Datasets\DataSet_Perfiles_Metalicos.xlsx",
            "T", engine="openpyxl", header=[0,1]).dropna(axis=1, how="all")
    
    # Selecciono las variables deseadas de nombre, área e inercia en x
    sections_data: pd.DataFrame = pd.concat([IPN.iloc[:,[0,8,10]],
                                             IPE.iloc[:,[0,8,10]],
                                             HEB.iloc[:,[0,8,10]],
                                             HEA.iloc[:,[0,8,10]],
                                             HEM.iloc[:,[0,8,10]],
                                             UPN.iloc[:,[0,8,10]], 
                                             L.iloc[:,[0,10,11]],
                                             LD.iloc[:,[0,14,15]],
                                             T.iloc[:,[0,7,8]]], axis=0)
        
    # Cambio de unidades
    if area_unit == "km^2":
        sections_data.iloc[:,1] /= 1.00e10
    elif area_unit == "m^2":
        sections_data.iloc[:,1] /= 1.00e4
    elif area_unit == "dm^2":
        sections_data.iloc[:,1] /= 1.00e2
    elif area_unit == "cm^2":
        sections_data.iloc[:,1] *= 1.00
    elif area_unit == "mm^2":
        sections_data.iloc[:,1] *= 1.00e2
    
    if inertia_unit == "km^4":
        sections_data.iloc[:,2] /= 1.00e12
    elif inertia_unit == "m^4":
        sections_data.iloc[:,2] /= 1.00e8
    elif inertia_unit == "dm^4":
        sections_data.iloc[:,2] /= 1.00e4
    elif inertia_unit == "cm^4":
        sections_data.iloc[:,2] *= 1.00
    elif inertia_unit == "mm^4":
        sections_data.iloc[:,2] *= 1.00e4
    
    
    
    # Creo los objetos de la clase perfil
    for index, row in sections_data.iterrows():
        locals()["Perfil_"+str(index)] = sc.SectionClass(row[0], row[1],
                                                         row[2], sections_list,
                                                         area_unit, inertia_unit,
                                                         structure_type)
        
    return sections_list