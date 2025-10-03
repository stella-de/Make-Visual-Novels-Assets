init python:
# vmc_listener.py
    from pythonosc import dispatcher, osc_server
    import threading
    import json

    shared_file = "game/vmc_data.json"

    def handle_param(address, *args):
        param_name = address.split('/')[-1]
        value = args[0]

        try:
            with open(shared_file, "r") as f:
                data = json.load(f)
        except:
            data = {}

        data[param_name] = value

        with open(shared_file, "w") as f:
            json.dump(data, f)

    def start_server():
        disp = dispatcher.Dispatcher()
        disp.map("/VMC/Ext/Blend/Val/*", handle_param)

        server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 39539), disp)
        print("Listening for VMC on UDP 39539...")
        server.serve_forever()

    threading.Thread(target=start_server).start()
