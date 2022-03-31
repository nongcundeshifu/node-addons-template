import bindings from "bindings"
import {AddonsTypesName} from "../addonsModel";

const ADDONS_NAME = 'addonsName'

export function loadAddons(): AddonsTypesName {
    return bindings(ADDONS_NAME);
}
