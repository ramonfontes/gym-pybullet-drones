from gym.envs.registration import register

register(
    id='ctrl-aviary-v0',
    entry_point='gym_pybullet_drones.envs:CtrlAviary',
)

register(
    id='dyn-ctrl-aviary-v0',
    entry_point='gym_pybullet_drones.envs:DynCtrlAviary',
)

register(
    id='vision-ctrl-aviary-v0',
    entry_point='gym_pybullet_drones.envs:VisionCtrlAviary',
)




register(
    id='takeoff-aviary-v0',
    entry_point='gym_pybullet_drones.envs.single_agent_rl:TakeoffAviary',
)

register(
    id='hover-aviary-v0',
    entry_point='gym_pybullet_drones.envs.single_agent_rl:HoverAviary',
)

register(
    id='flythrugate-aviary-v0',
    entry_point='gym_pybullet_drones.envs.single_agent_rl:FlyThruGateAviary',
)




register(
    id='flock-aviary-v0',
    entry_point='gym_pybullet_drones.envs.multi_agent_rl:FlockAviary',
)

register(
    id='leaderfollower-aviary-v0',
    entry_point='gym_pybullet_drones.envs.multi_agent_rl:LeaderFollowerAviary',
)

register(
    id='norm-dyn-ctrl-aviary-v0',
    entry_point='gym_pybullet_drones.envs.multi_agent_rl:NormDynCtrlAviary',
)

register(
    id='meetup-aviary-v0',
    entry_point='gym_pybullet_drones.envs.multi_agent_rl:MeetupAviary',
)