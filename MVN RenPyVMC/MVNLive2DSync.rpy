init python:
    import json

    def update_from_vmc(live2d):
        try:
            with open("vmc_data.json", "r") as f:
                data = json.load(f)

            if not data.get("_face_found"):
                return 0.1  # pause if no face

            # Example: drive Live2D parameters
            if "ParamEyeLOpen" in data:
                live2d.blend_parameter("ParamEyeLOpen", "Overwrite", data["ParamEyeLOpen"])
               

            if "ParamMouthOpenY" in data:
                live2d.set_parameter("ParamMouthOpenY", data["ParamMouthOpenY"])

            # Repeat for all relevant ones
        except Exception as e:
            renpy.log("VMC error: " + str(e))

        return 0.016  # ~60fps