cmake_minimum_required(VERSION 3.21)
project(camera_node_addons)

set(CMAKE_CXX_STANDARD 14)

# 添加一些头文件
include_directories(C:\\Users\\nongcundeshifu\\AppData\\Local\\node-gyp\\Cache\\12.22.6\\include\\node include node_modules\\node-addon-api)

# 用于测试代码的执行文件，并且让ide支持代码提示，但是不会真正运行它。真正编译lib库，是通过node-gpy工具来进行编译的。
add_executable(camera_node_addons addons/main.cpp)
