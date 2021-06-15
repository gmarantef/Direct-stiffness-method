from typing import List

from creator.bo.materials import Material
from creator.bo.sections import Section
from creator.bo.joints import Joint
from creator.bo.webs import Web


def show_materials(materials: List[Material]):

    print("\nLista de materiales\n")
    for material in materials:
        print(material)


def show_sections(sections: List[Section]):

    print("\nLista de perfiles\n")
    for section in sections:
        print(section)


def show_joints(joints: List[Joint]):

    print("\nLista de nudos\n")
    for joint in joints:
        print(joint)


def show_webs(webs: List[Web]):

    print("\nLista de barras\n")
    for web in webs:
        print(web)

   
def bandwidth(webs: List[Web]):

    bandwidth_list: List[int] = []
    
    for web in webs:
        bandwidth_list.append(web.joint_end.number - web.joint_start.number)

    max_bandwidth: int = max(bandwidth_list)
    print(f"El ancho de banda de la estructura es = {max_bandwidth}")
