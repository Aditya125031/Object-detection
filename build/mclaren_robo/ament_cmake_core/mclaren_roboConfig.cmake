# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_mclaren_robo_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED mclaren_robo_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(mclaren_robo_FOUND FALSE)
  elseif(NOT mclaren_robo_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(mclaren_robo_FOUND FALSE)
  endif()
  return()
endif()
set(_mclaren_robo_CONFIG_INCLUDED TRUE)

# output package information
if(NOT mclaren_robo_FIND_QUIETLY)
  message(STATUS "Found mclaren_robo: 0.0.0 (${mclaren_robo_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'mclaren_robo' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${mclaren_robo_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(mclaren_robo_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${mclaren_robo_DIR}/${_extra}")
endforeach()
