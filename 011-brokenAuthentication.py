# -*- coding: utf-8 -*-
# author : Amitava Chakraborty

import random
import numpy as np
import matplotlib.pyplot as plt


@app.route('/admin/init', methods=['POST'])
def reinitialize():
    cursor.execute("DROP DATABASE analytics")
    return 'Database has been dropped
