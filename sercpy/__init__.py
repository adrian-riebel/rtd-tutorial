# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:51:50 2026

@author: adria
"""

import sys

from . import thermal
from .thermal import demand_profile

sys.modules[__name__ + ".demand_profile"] = demand_profile
