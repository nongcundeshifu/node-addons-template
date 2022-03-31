//
// Created by nongcundeshifu on 2022/3/28.
//

#include "gtest/gtest.h"
#include "example.h"
#include <iostream>

TEST(testExample, test1) {
    EXPECT_EQ(2*3, 6);
    std::cout<<"test success"<<std::endl;
}

TEST(testExample, add) {
    EXPECT_EQ(add(2, 3), 5);
}
