cmake_minimum_required(VERSION 3.22)
project(node_addons_template)

set(CMAKE_CXX_STANDARD 14)

# 添加一些头文件，TODO：这里的xxxxxxxxxx路径需要自行补齐。
include_directories(include C:\\Users\\xxxxxxxxxx\\AppData\\Local\\node-gyp\\Cache\\12.22.7\\include\\node node_modules\\node-addon-api)

# 设置需要链接的lib库文件所在的目录
link_directories(lib)

add_library(node_addons_template addons/addons.cpp)

# 设置需要链接的lib库文件，因为设置了link_directories，所以这里的目录可以不用以 lib\\ 开头
target_link_libraries(node_addons_template hello.lib)

# ------添加google test

# 下载并配置google test依赖
include(FetchContent)
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/e2239ee6043f73722e7aa812a459f54a28552929.zip
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# 构建googletest代码，使用了google test，则不需要main文件了
enable_testing()

# 添加需要测试的测试文件。注意，这里不能包含node-addon-api相关代码的文件
add_executable(addons_test addons/test/bash.test.cpp)

# 把需要链接的hello库添加进来，gtest_main是不能去掉的
target_link_libraries(
        addons_test
        gtest_main
        hello.lib
)

include(GoogleTest)
gtest_discover_tests(addons_test)
