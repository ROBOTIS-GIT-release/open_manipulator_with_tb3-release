Name:           ros-kinetic-open-manipulator-with-tb3-waffle-moveit
Version:        1.0.0
Release:        1%{?dist}
Summary:        ROS open_manipulator_with_tb3_waffle_moveit package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/open_manipulator_with_tb3_waffle_moveit
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-joint-state-publisher
Requires:       ros-kinetic-moveit-kinematics
Requires:       ros-kinetic-moveit-planners-ompl
Requires:       ros-kinetic-moveit-ros-move-group
Requires:       ros-kinetic-moveit-ros-visualization
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-urdf
Requires:       ros-kinetic-xacro
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-joint-state-publisher
BuildRequires:  ros-kinetic-moveit-kinematics
BuildRequires:  ros-kinetic-moveit-planners-ompl
BuildRequires:  ros-kinetic-moveit-ros-move-group
BuildRequires:  ros-kinetic-moveit-ros-visualization
BuildRequires:  ros-kinetic-robot-state-publisher
BuildRequires:  ros-kinetic-urdf
BuildRequires:  ros-kinetic-xacro

%description
An automatically generated packages including all the configurations and launch
files for OpenManipulator with TurtleBot3 Waffle by using MoveIt! Motion
Planning Framework.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Jun 01 2018 Pyo <pyo@robotis.com> - 1.0.0-1
- Autogenerated by Bloom

* Fri Jun 01 2018 Pyo <pyo@robotis.com> - 1.0.0-0
- Autogenerated by Bloom

