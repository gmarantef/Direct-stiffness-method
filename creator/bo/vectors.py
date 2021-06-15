from dataclasses import dataclass


@dataclass
class PositionVector:
    x: float
    y: float


@dataclass
class EffortVector:
    fx: float
    fy: float
    mz: float


@dataclass
class DeformationVector:
    dx: float
    dy: float
    phi: float


@dataclass
class WebVector:
    joint_start: int
    joint_end: int


@dataclass
class WebMaterialVector:
    material_name: str
    material_condition: str


@dataclass
class WebSectionVector:
    section_name: str
