# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_udemy_ros2_pkg_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED udemy_ros2_pkg_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(udemy_ros2_pkg_FOUND FALSE)
  elseif(NOT udemy_ros2_pkg_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(udemy_ros2_pkg_FOUND FALSE)
  endif()
  return()
endif()
set(_udemy_ros2_pkg_CONFIG_INCLUDED TRUE)

# output package information
if(NOT udemy_ros2_pkg_FIND_QUIETLY)
  message(STATUS "Found udemy_ros2_pkg: 0.0.0 (${udemy_ros2_pkg_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'udemy_ros2_pkg' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${udemy_ros2_pkg_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(udemy_ros2_pkg_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "rosidl_cmake-extras.cmake;ament_cmake_export_dependencies-extras.cmake;ament_cmake_export_include_directories-extras.cmake;ament_cmake_export_libraries-extras.cmake;ament_cmake_export_targets-extras.cmake;rosidl_cmake_export_typesupport_targets-extras.cmake;rosidl_cmake_export_typesupport_libraries-extras.cmake")
foreach(_extra ${_extras})
  include("${udemy_ros2_pkg_DIR}/${_extra}")
endforeach()
