import esphome.codegen as cg
from esphome.components import button, wake_on_lan
import esphome.config_validation as cv
from esphome.const import CONF_ID

CONF_WOL_TARGET = "target_mac_address"
CONF_WOL_DEFAULT_ID = "wol_button"

wake_on_lan_ns = cg.esphome_ns.namespace("wake_on_lan")

WakeOnLanButton = wake_on_lan_ns.class_("WakeOnLanButton", button.Button)

CONFIG_SCHEMA = cv.Schema({
  cv.Required(CONF_WOL_TARGET): cv.mac_address,
  cv.GenerateID(CONF_WOL_DEFAULT_ID): cv.use_id(WakeOnLanButton)
}).extend(button.BUTTON_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_macaddr(
        (int(x, 16) for x in config[CONF_WOL_TARGET].split(':'))
    ))
    yield cg.register_component(var)
    yield button.register_button(var, config)
    cg.add(var)