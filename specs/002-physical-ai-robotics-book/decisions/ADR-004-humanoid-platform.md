# ADR-004: Humanoid Robot Platform Selection

**Status**: Accepted
**Date**: 2025-12-06
**Deciders**: Architecture Team
**Technical Story**: Module 3-4 - Simulation Platform Choice

---

## Context and Problem Statement

We need to select a humanoid robot platform for simulation examples throughout the book. The platform will be used for URDF modeling, Gazebo/Isaac Sim scenes, perception demonstrations, and the VLA capstone project.

**Key Considerations**:
- Simulation availability (not requiring physical hardware per ADR-003)
- URDF/SDF model quality and documentation
- Realistic humanoid kinematics (bipedal, manipulation)
- Community support and learning resources
- Complexity appropriate for educational content
- License compatibility (models, documentation)

---

## Decision Drivers

1. **Simulation-Only**: Must work entirely in virtual environments (per ADR-003)
2. **Educational Value**: Balance realism with learning curve
3. **Availability**: Open-source models, well-documented
4. **Complexity**: Not too simple (toy), not too complex (overwhelming)
5. **Relevance**: Representative of real humanoid robotics

---

## Considered Options

### Option 1: Generic Humanoid (Custom-Built)
- **Approach**: Create simplified custom humanoid from scratch
- **DOF**: 12-15 joints (simplified)
- **Models**: Custom URDF, optimized for teaching
- **Availability**: Built specifically for book
- **Complexity**: Controlled, educational-focused
- **Realism**: Simplified physics, reduced complexity

### Option 2: Simulation-Only Humanoid (No Physical Counterpart)
- **Examples**: Simulated human models, game characters
- **Approach**: Use existing simulation-optimized models
- **DOF**: Varies (15-30 joints)
- **Models**: Available in Isaac Sim, Gazebo libraries
- **Availability**: Pre-built, tested in simulators
- **Complexity**: Moderate
- **Realism**: Good sim physics, no physical deployment path

### Option 3: Real Humanoid Platform (Simulation Models)
- **Examples**: UnitreeH1, Figure 01, Tesla Optimus, Boston Dynamics Atlas
- **Approach**: Use simulation models of actual commercial/research robots
- **DOF**: 20-30+ joints
- **Models**: Official or community URDF/SDF files
- **Availability**: Mixed (some open-source, some proprietary)
- **Complexity**: High realism, complex kinematics
- **Realism**: Matches physical robot characteristics

---

## Decision Outcome

**Chosen Option**: **Simulation-Only Humanoid (Option 2) - Specifically using Isaac Sim's built-in humanoid asset**

**Specific Choice**: NVIDIA Isaac Sim's "Carter" Humanoid or "Human" Character Asset

**Rationale**:

1. **Zero Setup**: Pre-configured in Isaac Sim, no model sourcing needed
2. **Optimized**: Tuned for Isaac Sim physics and rendering
3. **Documented**: NVIDIA provides usage examples and tutorials
4. **Consistent**: All readers use identical model (reproducibility)
5. **Appropriate Complexity**: ~20 DOF, realistic but not overwhelming
6. **Sensor-Ready**: Pre-configured camera, depth, IMU attachment points
7. **VLA-Friendly**: Suitable for manipulation and navigation tasks

**Fallback for Gazebo** (Module 2):
- Use simplified humanoid from `gazebo_models` repository
- Focus on basic bipedal kinematics, not full humanoid complexity
- Module 2 emphasis on ROS 2 concepts, not realistic humanoid control

---

## Consequences

### Positive

- ✅ **Immediate Availability**: No model hunting, licensing, or conversion
- ✅ **Consistency**: All readers have identical starting point
- ✅ **Performance**: Optimized for Isaac Sim rendering and physics
- ✅ **Support**: NVIDIA documentation and community resources
- ✅ **Scalability**: Easy to duplicate/modify for multi-agent scenarios
- ✅ **Sensor Integration**: Pre-rigged for cameras, depth sensors, IMUs
- ✅ **USD Native**: Proper scene graph structure for synthetic data generation

### Negative

- ⚠️ **Gazebo Limited**: Less detailed model available for Module 2
- ⚠️ **No Physical**: Can't deploy to real humanoid robot
- ⚠️ **NVIDIA Lock-In**: Tied to Isaac Sim ecosystem
- ⚠️ **Simplified Control**: Not full humanoid locomotion complexity

### Mitigation

- 📖 **Module 2 Simplification**: Use basic bipedal model in Gazebo, note it's introductory
- 📊 **Realism Discussion**: Appendix covers real humanoid platforms (H1, Atlas, etc.)
- 🔗 **Optional Reading**: Link to Unitree H1, Figure 01 for interested readers
- 🎓 **Learning Focus**: Emphasize AI/perception over mechanical engineering

---

## Technical Specifications

**Isaac Sim Humanoid Asset**:
- **DOF**: ~20 articulated joints
- **Sensors**: RGB camera (head), depth camera, IMU, joint encoders
- **Manipulation**: 7-DOF arms (realistic human-like)
- **Locomotion**: Bipedal legs with realistic kinematics
- **Mass/Inertia**: Realistic physics properties
- **Height**: ~1.7m (human-scale)

**Gazebo Fallback (Module 2)**:
- Use `gazebo_models/humanoid_description` or custom simplified version
- Focus: Basic URDF structure, joint control, sensor plugins
- Complexity: Reduced (12-15 DOF) for ROS 2 learning

**Capabilities for Book**:
- Navigation in indoor environments
- Object manipulation (pick, place, handover)
- Visual perception (object detection, depth estimation)
- Voice-commanded actions (VLA pipeline)
- Multi-agent collaboration scenarios

---

## Use Cases in Book

**Module 2 (ROS 2 Fundamentals)**:
- URDF modeling basics with simplified humanoid
- Joint control via ROS 2 topics
- Launch files for multi-jointed systems
- Gazebo sensor plugins (camera, lidar placeholder)

**Module 3 (Isaac Sim)**:
- Full humanoid model in photorealistic environment
- Synthetic RGB-D data generation
- VSLAM demonstration with humanoid-mounted cameras
- Perception model training on simulated data

**Module 4 (VLA Pipeline)**:
- Voice commands → humanoid actions
- "Pick up the red cube" → vision + manipulation
- "Navigate to the kitchen" → path planning + locomotion
- End-to-end capstone: voice-controlled assistant robot

---

## Alternatives Rejected

### Why Not Custom-Built (Option 1)?
- **Time Investment**: Significant effort to create quality URDF
- **Validation**: Hard to ensure physics accuracy without testing
- **Limited Realism**: Simplified model reduces learning value
- **Maintenance**: Ongoing updates needed if issues found

### Why Not Real Platform (Option 3)?
- **Availability Issues**: URDF models for H1, Atlas, Optimus vary in quality
- **Licensing**: Proprietary models may have usage restrictions
- **Complexity Mismatch**: Full 30+ DOF overwhelming for beginners
- **No Physical Path**: Per ADR-003, simulation-only approach chosen
- **Support Burden**: Troubleshooting diverse platforms difficult

**Note on Real Platforms**:
- Appendix will mention Unitree H1, Figure 01, Tesla Optimus, Boston Dynamics Atlas
- Readers interested in real humanoids can research independently
- Focus: AI and software (book scope), not mechanical/hardware engineering

---

## Related Decisions

- [ADR-003: Isaac Sim Deployment](./ADR-003-isaac-sim-deployment.md) - Simulation-only approach enables this choice
- [ADR-002: Gazebo Version](./ADR-002-gazebo-version.md) - Fortress used for Module 2 basic humanoid

---

## References

- [NVIDIA Isaac Sim Assets](https://docs.omniverse.nvidia.com/isaacsim/latest/features/environment_setup/assets/usd_assets_overview.html)
- [Gazebo Model Repository](https://github.com/osrf/gazebo_models)
- [Unitree H1 Humanoid](https://www.unitree.com/h1) (reference)
- [USD Character Animation](https://openusd.org/release/index.html)

---

## Notes

- Supports Constitution Principle IV (Reproducibility) via standardized asset
- Aligns with simulation-only approach (ADR-003)
- Readers can substitute their own humanoid models if desired (advanced)
- Annual updates will track new Isaac Sim humanoid assets
