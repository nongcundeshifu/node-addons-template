cmake_minimum_required(VERSION 3.21)
project(node-addons-template)

set(CMAKE_CXX_STANDARD 14)

# 添加一些头文件
include_directories(include C:\\Users\\nongcundeshifu\\AppData\\Local\\node-gyp\\Cache\\12.22.6\\include\\node node_modules\\node-addon-api)

# 用于添加源码文件，但是添加这个的原因是为了让ide能够进行代码提示，通常无需对这些源码进行构建，真正的编译是通过node-gyp的binding.gyp配置来编译的。
# 注意，不能把包含带napi的源码文件添加进来，因为此时是无法通过编译的。
add_executable(addons addons/main.cpp)

# ------添加google test

# 下载并配置google test依赖
include(FetchContent)
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/e2239ee6043f73722e7aa812a459f54a28552929.zip
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)
# 下载并配置google test依赖

# 构建googletest代码，使用了google test，则不需要main文件了
enable_testing()

add_executable(addons_test addons/__test__/testExample.cpp)
target_link_libraries(
        addons_test
        gtest_main
)

include(GoogleTest)
gtest_discover_tests(addons_test)
# ------添加google test