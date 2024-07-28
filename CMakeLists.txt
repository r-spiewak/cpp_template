cmake_minimum_required(VERSION 3.15)
project(cpp_template CXX)


message("Building with CMake version: ${CMAKE_VERSION}")

add_library(cpp_template src/cpp_template.cpp)
target_include_directories(cpp_template PUBLIC include)



set_target_properties(cpp_template PROPERTIES PUBLIC_HEADER "include/cpp_template.h")
install(TARGETS cpp_template)
