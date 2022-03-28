import bindings from "bindings"
import {AddonsTypesName} from "../addons.types";

const ADDONS_NAME = 'addonsName'

export function loadAddons(): AddonsTypesName {
    return bindings(ADDONS_NAME);
}
