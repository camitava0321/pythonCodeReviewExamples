# -*- coding: utf-8 -*-
#author : Amitava Chakraborty

import random
import numpy as np
import matplotlib.pyplot as plt
@login.route("/login", methods=['POST'])
def login():
     username = request.form.get("username")
     password = request.form.get("password")

     if validate_credentials(username, password):
         session['anti_crf_token'] = get_random_token()
         # ...