# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Schwa-Launchpad/__init__.py
# Compiled at: 2018-05-02 11:52:41
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import *
from .Schwa-Launchpad import Schwa-Launchpad

def create_instance(c_instance):
    return Schwa-Launchpad(c_instance)


def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[
                         14, 32, 54], model_name=[
                         'Schwa-Launchpad', 'Schwa-Launchpad S', 'Schwa-Launchpad Mini']), 
       PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE, SCRIPT]),
                 outport(props=[NOTES_CC, REMOTE, SCRIPT])]}
