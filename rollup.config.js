import typescript from 'rollup-plugin-typescript2'
import pkg from './package.json'
import { resolve } from 'path'

export default {
    // 入口文件
    input: resolve(__dirname, './src/index.ts'),
    output: [
        {
            // 打包名称
            file: resolve(__dirname, `dist/index.js`),
            format: 'cjs',
            sourcemap: true,
            exports: 'named',
        },
        {
            file: resolve(__dirname, `dist/index-es.js`),
            format: 'es',
            sourcemap: true,
            exports: 'named',
        },
    ],
    external: [...Object.keys(pkg.dependencies || {}), ...Object.keys(pkg.peerDependencies || {})],
    plugins: [typescript()],
}
