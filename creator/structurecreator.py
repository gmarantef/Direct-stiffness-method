from typing import List

from creator.bo.vectors import PositionVector, EffortVector, DeformationVector, WebVector
from creator.bo.materials import Material
from creator.bo.sections import Section
from creator.bo.joints import Joint
from creator.bo.webs import Web
from assistant.websnames import webs_names


class StructureCreator:

    def __init__(self, joints_positions: List[PositionVector] = None, effort_vectors: List[EffortVector] = None,
                 deformation_vectors: List[DeformationVector] = None, web_locations: List[WebVector] = None,
                 materials: List[Material] = None, sections: List[Section] = None, joints: List[Joint] = None) -> None:

        self.joint_number = len(joints_positions)
        self.joints_positions = joints_positions
        self.effort_vectors = effort_vectors
        self.deformation_vectors = deformation_vectors
        self.web_number = len(web_locations)
        self.web_locations = web_locations
        self.materials = materials
        self.sections = sections

        if joints is None:
            self.joints = self.create_joints()
        else:
            self.joints = joints
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

        alphabet_ext: List[str] = webs_names(self.web_number)

        for i in range(self.web_number):
            for joint in self.joints:
                if joint.number == self.web_locations[i].joint_start:
                    joint_start: Joint = joint
                elif joint.number == self.web_locations[i].joint_end:
                    joint_end: Joint = joint
            webs.append(Web(alphabet_ext[i], joint_start, joint_end, self.materials[i], self.sections[i]))

        return webs
