
import {loadAddons} from "../utils";

const addons = loadAddons();

describe('helloWorldTest', function () {
    it('hello world', function () {
        const helloStr = addons.helloWorld();
        expect(helloStr).toBe("hello world");
    });
});
