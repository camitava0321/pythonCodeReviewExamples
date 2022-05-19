# -*- coding: utf-8 -*-
# author : Amitava Chakraborty

import pickle


@app.route("/import_object", methods=['POST'])
def import_object():
    data = request.files.get('user_file').read()
    user_object = pickle.loads(data)
    store_in_database(user_object)
    return 'OK'
