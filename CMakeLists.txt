cmake_minimum_required(VERSION 3.16)
project(references LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(wxWidgets REQUIRED COMPONENTS core base)

add_executable(references
        cpp/gui/MainFrame.cpp
        cpp/gui/App.h
        cpp/gui/App.cpp
)

target_link_libraries(references
        PRIVATE
        wxWidgets::wxWidgets
)

target_include_directories(references
        PRIVATE
        cpp/gui
)