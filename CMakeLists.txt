cmake_minimum_required(VERSION 3.15)
project(cpp_template CXX)


message("Building with CMake version: ${CMAKE_VERSION}")

# Add project headers
include_directories(include)

# Add project
add_library(cpp_template src/cpp_template.cpp include/cpp_template.h)
#target_include_directories(cpp_template PUBLIC include)
#target_link_libraries(cpp_template)
#target_link_libraries(cpp_template <any other libraries that need to be linked to cp_template>)


set_target_properties(cpp_template PROPERTIES PUBLIC_HEADER "include/cpp_template.h")
install(TARGETS cpp_template)

message("CMAKE_BINARY_DIR: ${CMAKE_BINARY_DIR}")
include(${CMAKE_BINARY_DIR}/cmake_install.cmake)
#include(${CMAKE_BINARY_DIR}/generators/conan_toolchain.cmake)
message("CMAKE_PREFIX_PATH: ${CMAKE_PREFIX_PATH}")
#include(${CMAKE_PREFIX_PATH})


# Find and add all tests

find_package(Catch2 REQUIRED)

file(GLOB_RECURSE test_files RELATIVE ${CMAKE_SOURCE_DIR} "tests/*.cpp")
add_executable(all_tests ${test_files})
target_link_libraries(all_tests cpp_template Catch2::Catch2WithMain)

include(Catch)
catch_discover_tests(all_tests)

# This would work if the tests directory had its own CmakeLists.txt file.
#add_subdirectory(tests)
