# ADR-001: ROS 2 Distribution Selection

**Status**: Accepted
**Date**: 2025-12-06
**Deciders**: Architecture Team
**Technical Story**: Module 2 - ROS 2 Fundamentals

---

## Context and Problem Statement

We need to select a ROS 2 distribution for the Physical AI & Humanoid Robotics book. The choice affects reader experience, long-term support, compatibility with simulation tools, and example code longevity.

**Key Considerations**:
- Long-term support (LTS) for book lifecycle
- Compatibility with Ubuntu 22.04 LTS
- Gazebo Fortress integration
- Python 3.10+ support
- Community adoption and resources
- Annual update cycle commitment

---

## Decision Drivers

1. **Book Longevity**: Examples should remain valid for 2-3 years minimum
2. **Reader Success**: Most readers use Ubuntu LTS releases
3. **Ecosystem Maturity**: Stable packages and extensive documentation
4. **Learning Curve**: Well-documented, beginner-friendly resources
5. **Simulation Compatibility**: Seamless Gazebo and Isaac Sim integration

---

## Considered Options

### Option 1: ROS 2 Humble Hawksbill (LTS)
- **Release**: May 2022
- **Support**: Until May 2027 (5 years)
- **Target Platform**: Ubuntu 22.04 LTS (Jammy Jellyfish)
- **Python**: 3.10
- **Gazebo**: Fortress (default), Garden (compatible)
- **DDS**: FastDDS, CycloneDDS

### Option 2: ROS 2 Iron Irwini
- **Release**: May 2023
- **Support**: Until November 2024 (1.5 years) - **Already EOL**
- **Target Platform**: Ubuntu 22.04 LTS
- **Python**: 3.10
- **Gazebo**: Fortress, Garden

### Option 3: ROS 2 Jazzy Jalisco (Future LTS)
- **Release**: May 2024
- **Support**: Until May 2029 (5 years)
- **Target Platform**: Ubuntu 24.04 LTS (Noble Numbat)
- **Python**: 3.12
- **Gazebo**: Harmonic (default)

---

## Decision Outcome

**Chosen Option**: **ROS 2 Humble Hawksbill (LTS)**

**Rationale**:

1. **Long-Term Support**: Supported until May 2027, covering the book's expected 2-year primary usage period plus updates
2. **Platform Stability**: Ubuntu 22.04 LTS widely adopted and stable
3. **Ecosystem Maturity**: 2+ years of community packages, tutorials, and troubleshooting resources
4. **Gazebo Fortress**: Default simulator with extensive ROS 2 Humble documentation
5. **Learning Resources**: Largest collection of tutorials and community support for Humble
6. **Compatibility**: Works seamlessly with Isaac Sim 2023.1+ and current Jetson SDKs

**Migration Path**:
- Annual updates will document Humble → Jazzy migration when Jazzy ecosystem matures (2025-2026)
- Appendix will include compatibility notes for Iron (for users already on it)

---

## Consequences

### Positive

- ✅ **Extended Support**: 2+ years remaining LTS coverage at book release
- ✅ **Mature Ecosystem**: Well-tested packages and extensive documentation
- ✅ **Reader Success**: Most learners already familiar with Ubuntu 22.04
- ✅ **Stable Examples**: Code examples remain valid through 2027
- ✅ **Gazebo Integration**: Fortress is battle-tested with Humble

### Negative

- ⚠️ **Not Cutting-Edge**: Jazzy has newer features (not critical for learning)
- ⚠️ **Python 3.10**: Not latest Python (3.12 in Jazzy), but still supported
- ⚠️ **Eventual Migration**: Readers may need to upgrade to Jazzy in 2026-2027

### Neutral

- ℹ️ **Iron Skipped**: Iron's short support cycle makes it unsuitable for book content
- ℹ️ **Jazzy Future**: Can be covered in annual updates when ecosystem matures

---

## Validation

**Tested Combinations**:
- ✅ Ubuntu 22.04 + ROS 2 Humble + Gazebo Fortress
- ✅ ROS 2 Humble + Isaac Sim 2023.1
- ✅ ROS 2 Humble + Jetson Orin (JetPack 5.1+)
- ✅ Python 3.10 + rclpy (Humble)

**Community Validation**:
- ROS 2 Humble is recommended distribution in official tutorials (as of 2025)
- Largest number of third-party packages support Humble
- Most robotics courses and bootcamps use Humble

---

## Alternatives Rejected

### Why Not Iron?
- **EOL Risk**: Iron reached end-of-life in November 2024
- **No LTS**: Short support cycle incompatible with book longevity
- **Limited Benefit**: Minimal feature differences from Humble for learning

### Why Not Jazzy?
- **Ecosystem Immaturity**: Released May 2024, fewer tested packages
- **Platform Change**: Ubuntu 24.04 adoption still growing
- **Overkill for Learning**: Advanced features not needed for foundational book
- **Migration Complexity**: Readers on 22.04 would need full OS upgrade

---

## Related Decisions

- [ADR-002: Gazebo Version Selection](./ADR-002-gazebo-version.md) - Directly depends on Humble compatibility
- [ADR-004: Humanoid Platform Selection](./ADR-004-humanoid-platform.md) - ROS 2 Humble support required

---

## References

- [ROS 2 Humble Documentation](https://docs.ros.org/en/humble/)
- [ROS 2 Releases](https://docs.ros.org/en/rolling/Releases.html)
- [Ubuntu 22.04 LTS Release Notes](https://releases.ubuntu.com/22.04/)
- [Gazebo Fortress with ROS 2](https://gazebosim.org/docs/fortress/ros2_integration)

---

## Notes

- This decision aligns with Constitution Principle III (Technical Accuracy) by using stable, well-documented platform
- Annual update cycle (Constitution governance) will revisit this decision in 2026 for Jazzy migration
- All code examples will be tested on Ubuntu 22.04 + ROS 2 Humble before publication
