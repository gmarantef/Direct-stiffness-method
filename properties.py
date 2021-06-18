from typing import List

from creator.bo.vectors import PositionVector, EffortVector, DeformationVector, WebVector, WebMaterialVector, WebSectionVector

# Sistema de unidades
FORCE_UNIT = "N"
LENGTH_UNIT = "m"
SPIN_UNIT = "rd"
PRESSURE_UNIT = "N/m^2"
AREA_UNIT = "m^2"
INERTIA_UNIT = "m^4"

# Tipología estructural articulada o no articulada
STRUCTURE_TYPE = "articulada"

# Defino la estructura (Entradas manuales)
# La posición de nudos debe ir en orden con la numeración de los nudos
# Las listas de esfuerzos y deformaciones deben ir en orden con la numeración de los nudos
# El momento positivo es el que sale del plano
# Las direcciones de barras relacionan los nudos de inicio y fin que se ordenan igual que las posiciones de nudos
# Los materiales y perfiles se organizan en arrays en el mismo orden que hasta ahora
#
# Nudos estado inicial de carga
joints_positions: List[PositionVector] = [PositionVector(0.0, 0.0), PositionVector(2.0, 3.46),
                                          PositionVector(4.0, 6.92), PositionVector(4.0, 0.0),
                                          PositionVector(6.0, 3.46), PositionVector(8.0, 0.0)]
effort_vectors: List[EffortVector] = [EffortVector(0.0, None, 0.0), EffortVector(0.0, 0.0, 0.0),
                                      EffortVector(0.0, 0.0, 0.0), EffortVector(0.0, -10000.0, 0.0),
                                      EffortVector(0.0, 0.0, 0.0), EffortVector(None, None, 0.0)]
deformation_vectors: List[DeformationVector] = [DeformationVector(None, 0.0, 0.0),
                                                DeformationVector(None, None, 0.0),
                                                DeformationVector(None, None, 0.0),
                                                DeformationVector(None, None, 0.0),
                                                DeformationVector(None, None, 0.0),
                                                DeformationVector(0.0, 0.0, 0.0)]
# Barras
web_locations: List[WebVector] = [WebVector(1, 2), WebVector(2, 3), WebVector(3, 4), WebVector(1, 4),
                                  WebVector(2, 4), WebVector(2, 5), WebVector(3, 5), WebVector(4, 5),
                                  WebVector(4, 6), WebVector(5, 6)]
web_materials: List[WebMaterialVector] = [WebMaterialVector("ASTM A572", "Grade 50"),
                                          WebMaterialVector("ASTM A572", "Grade 50"),
                                          WebMaterialVector("ASTM A572", "Grade 50"),
                                          WebMaterialVector("ASTM A572", "Grade 50"),
                                          WebMaterialVector("ASTM A572", "Grade 50"),
                                          WebMaterialVector("ASTM A572", "Grade 50"),
                                          WebMaterialVector("ASTM A572", "Grade 50"),
                                          WebMaterialVector("ASTM A572", "Grade 50"),
                                          WebMaterialVector("ASTM A572", "Grade 50"),
                                          WebMaterialVector("ASTM A572", "Grade 50")]
web_sections: List[WebSectionVector] = [WebSectionVector("IPN 220"), WebSectionVector("IPN 220"),
                                        WebSectionVector("IPN 220"), WebSectionVector("IPN 220"),
                                        WebSectionVector("IPN 220"), WebSectionVector("IPN 220"),
                                        WebSectionVector("IPN 220"), WebSectionVector("IPN 220"),
                                        WebSectionVector("IPN 220"), WebSectionVector("IPN 220")]

# Parámetros para la iteración y obtención del Dataset
NUMBER_STATE_EFFORTS = 100    # Número de estados de carga
EFFORT_MAX: int = 500    # Máximo esfuerzo que pueda aparecer en + o -
