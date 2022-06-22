
import { loadAddons } from "../utils";

const addons = loadAddons()

describe('基础测试', function () {
    it('API导出测试', function () {
        expect(Reflect.has(addons, 'hello')).toBeTruthy();
    });
    it('测试hello方法', function () {
        const helloStr = addons.hello('Li');
        expect(helloStr).toBe('hello Li');
    });
});
