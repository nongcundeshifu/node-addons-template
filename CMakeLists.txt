cmake_minimum_required(VERSION 3.21)
project(node-addons-template)

set(CMAKE_CXX_STANDARD 14)

# 添加一些头文件
include_directories(include C:\\Users\\xxxxx\\AppData\\Local\\node-gyp\\Cache\\12.22.6\\include\\node node_modules\\node-addon-api)
# 需要链接的lib库文件所在的目录
link_directories(lib)

# 用于测试代码的执行文件，并且让ide支持代码提示，但是不会真正运行它。真正编译lib库，是通过node-gpy工具来进行编译的。
add_executable(addons addons/addons.cpp)

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

add_executable(addons_test addons/__test__/testExample.cpp addons/__test__/example.cpp addons/__test__/example.h)
target_link_libraries(
        addons_test
        gtest_main
)

include(GoogleTest)
gtest_discover_tests(addons_test)
# ------添加google test