
#include <iostream>
#include "gtest/gtest.h"
#include "hello.h"

TEST(baseTest, hello) { // NOLINT(cert-err58-cpp)
    auto helloStr = getHelloStr("Li");
    EXPECT_EQ(helloStr, "hello Li");
    std::cout<<"test pass"<<endl;
}
