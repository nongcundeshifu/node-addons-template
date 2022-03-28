# node-addons-template

一个开发node c++插件的项目模板。

> 注意，该项目在clion下创建。

## 目录说明

- addons：c++插件源码
- include：存放一些头文件的目录
- src：封装addons插件的ts代码
  - addons-test：对c++插件代码进行测试
  - utils：模块内部使用的工具类，不对外导出
  - addons.types.ts：c++插件函数的类型定义

## 一些配置

- addons中会启用c++异常，你可以通过try来捕获c++中node-addons-api中抛出的异常