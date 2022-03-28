import bindings from "bindings"
import {AddonsTypesName} from "../addons.types";

const ADDONS_NAME = 'camera_node_addons'

export function loadAddons(): AddonsTypesName {
    return bindings(ADDONS_NAME);
}
