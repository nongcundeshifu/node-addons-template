import bindings from "bindings"
import { NodeAddonsTemplate } from "../types/NodeAddonsTemplate";

const ADDONS_NAME = 'node_addons_template'

/**
 * 加载封装的node addons sdk
 */
export function loadAddons(): NodeAddonsTemplate {
    return bindings(ADDONS_NAME);
}

