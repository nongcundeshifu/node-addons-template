#include <iostream>
#include "napi.h"
#include "hello.h"

// 声明一个函数，此函数封装了hello库的getHelloStr方法
Napi::String helloFn(const Napi::CallbackInfo& info) {
    Napi::Env env = info.Env();
    // 获取参数
    Napi::String name = info[0].As<Napi::String>();
    return Napi::String::New(env, getHelloStr(name.ToString()));
}

// node c++模块的入口函数
Napi::Object Init(Napi::Env env, Napi::Object exports) {
    // 将helloFn函数，作为exports对象的hello属性，暴露给node层，此时用户require()这个构建出来的.node文件后，就得到一个含有hello方法的对象。
    // 这和你在node中的module.exports = { hello: function () { xxx } } 是一样的。
    exports.Set("hello", Napi::Function::New(env, helloFn));
    return exports;
}

// "node_addons_template" 是模块名称
NODE_API_MODULE(node_addons_template, Init);
