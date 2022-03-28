
#include <iostream>
#include "napi.h"

Napi::String helloWorld(Napi::CallbackInfo& info) {
    return Napi::String::New(info.Env(), "hello world");
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
    exports.Set("helloWorld", Napi::Function::New(env, helloWorld));
    return exports;
}


NODE_API_MODULE(addonsName, Init);
