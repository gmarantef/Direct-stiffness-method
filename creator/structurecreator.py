from typing import List

from creator.bo.vectors import PositionVector, EffortVector, DeformationVector, WebVector
from creator.bo.materials import Material
from creator.bo.sections import Section
from creator.bo.joints import Joint
from creator.bo.webs import Web
from assistant import websnames


class StructureCreator:

    def __init__(self, joints_positions: List[PositionVector], effort_vectors: List[EffortVector],
                 deformation_vectors: List[DeformationVector], web_locations: List[WebVector],
                 materials: List[Material], sections: List[Section]) -> None:

        self.joint_number = len(joints_positions)
        self.joints_positions = joints_positions
        self.effort_vectors = effort_vectors
        self.deformation_vectors = deformation_vectors
        self.web_number = len(web_locations)
        self.web_locations = web_locations
        self.materials = materials
        self.sections = sections

        self.joints = self.create_joints()
        self.webs = self.create_webs()

    def create_joints(self) -> List[Joint]:

        joints: List[Joint] = []

        for i in range(self.joint_number):
            joints.append(Joint(i+1, self.joints_positions[i].x, self.joints_positions[i].y,
                                self.effort_vectors[i].fx, self.effort_vectors[i].fy, self.effort_vectors[i].mz,
                                self.deformation_vectors[i].dx, self.deformation_vectors[i].dy,
                                self.deformation_vectors[i].phi))

        return joints

    def create_webs(self) -> List[Web]:

        webs: List[Web] = []

        alphabet_ext: List[str] = websnames.webs_names(self.web_number)

        for i in range(self.web_number):
            for joint in self.joints:
                if joint.number == self.web_locations[i].joint_start:
                    joint_start: Joint = joint
                elif joint.number == self.web_locations[i].joint_end:
                    joint_end: Joint = joint
            webs.append(Web(alphabet_ext[i], joint_start, joint_end, self.materials[i], self.sections[i]))

        return webs
