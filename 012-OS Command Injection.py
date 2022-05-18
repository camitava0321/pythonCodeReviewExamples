# -*- coding: utf-8 -*-
#author : Amitava Chakraborty

import random
import numpy as np
import matplotlib.pyplot as plt
@app.route("/dns")
def page():

    hostname = request.values.get(hostname)
    cmd = 'nslookup ' + hostname

    return subprocess.check_output(cmd, shell=True)