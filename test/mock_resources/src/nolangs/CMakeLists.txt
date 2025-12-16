cmake_minimum_required(VERSION 3.0.2...3.10)

project(nolangs)
find_package(catkin REQUIRED)
catkin_package()

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/bin)

add_executable(nolangs_exec
  main.cpp)

install(TARGETS nolangs_exec
  RUNTIME DESTINATION bin)
