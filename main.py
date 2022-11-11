"""
inspect page
Network, Fetch/XHR, copy as cURL/bash
convert to python: https://curlconverter.com/
"""
from classes import NpcSingleton
from functions import put_text_to_image

npc = NpcSingleton()
npc.roll_npc()
npc.advance_by_xp()
#npc.present()
put_text_to_image(npc)
