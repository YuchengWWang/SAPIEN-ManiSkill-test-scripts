import sapien
import numpy as np
from mani_skill.agents.base_agent import BaseAgent, Keyframe
from mani_skill.agents.controllers import *
from mani_skill.agents.registration import register_agent

@register_agent()
class Cheetah(BaseAgent):
    uid = "cheetah"
    urdf_path = f"assets/cheetah/mini_cheetah.urdf"
    fix_root_link = True
    load_multiple_collisions = True
    balance_passive_force = False
    keyframes = dict(
        standing=Keyframe(
            pose=sapien.Pose(p=[0, 0, 0.31]),
            qpos=np.array(
                [0., 0., 0., 0., -0.8, -0.8, -0.8, -0.8, 1.6, 1.6, 1.6, 1.6,]
            ),
        )
    )

    abad_joint_names = [
        "abad_fr",
        "abad_fl",
        "abad_hr",
        "abad_hl",
    ]
    hip_joint_names = [
        "hip_fr",
        "hip_fl",
        "hip_hr",
        "hip_hl",
    ]
    knee_joint_names = [
        "knee_fr",
        "knee_fl",
        "knee_hr",
        "knee_hl",
    ]
    
    abad_stiffness = 1e3
    abad_damping = 1e2
    abad_force_limit = 100
    hip_stiffness = 1e3
    hip_damping = 1e2
    hip_force_limit = 100
    knee_stiffness = 1e3
    knee_damping = 1e2
    knee_force_limit = 100

    @property
    def _controller_configs(self):
        abad_pd_joint_pos = PDJointPosControllerConfig(
            self.abad_joint_names,
            lower=None,
            upper=None,
            stiffness=self.abad_stiffness,
            damping=self.abad_damping,
            force_limit=self.abad_force_limit,
            normalize_action=False,
        )
        abad_pd_joint_delta_pos = PDJointPosControllerConfig(
            self.abad_joint_names,
            lower=-0.1,
            upper=0.1,
            stiffness=self.abad_stiffness,
            damping=self.abad_damping,
            force_limit=self.abad_force_limit,
            use_delta=True,
        )
        hip_pd_joint_pos = PDJointPosControllerConfig(
            self.hip_joint_names,
            lower=None,
            upper=None,
            stiffness=self.hip_stiffness,
            damping=self.hip_damping,
            force_limit=self.hip_force_limit,
            normalize_action=False,
        )
        hip_pd_joint_delta_pos = PDJointPosControllerConfig(
            self.hip_joint_names,
            lower=-0.1,
            upper=0.1,
            stiffness=self.hip_stiffness,
            damping=self.hip_damping,
            force_limit=self.hip_force_limit,
            use_delta=True,
        )
        knee_pd_joint_pos = PDJointPosControllerConfig(
            self.knee_joint_names,
            lower=None,
            upper=None,
            stiffness=self.knee_stiffness,
            damping=self.knee_damping,
            force_limit=self.knee_force_limit,
            normalize_action=False,
        )
        knee_pd_joint_delta_pos = PDJointPosControllerConfig(
            self.knee_joint_names,
            lower=-0.1,
            upper=0.1,
            stiffness=self.knee_stiffness,
            damping=self.knee_damping,
            force_limit=self.knee_force_limit,
            use_delta=True,
        )

        controller_configs = dict(
            pd_joint_delta_pos=dict(
                abad=abad_pd_joint_delta_pos, hip=hip_pd_joint_delta_pos, knee=knee_pd_joint_delta_pos
            ),
            pd_joint_pos=dict(
                abad=abad_pd_joint_pos, hip=hip_pd_joint_pos, knee=knee_pd_joint_pos
            ),
        )

        # Make a deepcopy in case users modify any config
        return deepcopy_dict(controller_configs)
    
    