import socket
import json

# Where to save parsed output
output_path = "game/vmc_data.json"  # Adjust this if needed

# Your UDP port to listen on
PORT = 11125

# Optional: Remap blendshape keys to your model's Live2D parameters
BLENDSHAPE_TO_L2D = {
    "EyeBlinkLeft": "ParamEyeLOpen",
    "EyeBlinkRight": "ParamEyeROpen",
    "JawOpen": "ParamMouthOpenY",
    "MouthSmileLeft": "ParamMouthForm",
    "MouthSmileRight": "ParamMouthForm",
    "MouthFrownLeft": "ParamMouthForm",
    "MouthFrownRight": "ParamMouthForm",
    # Add more mappings as needed
}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))
print(f"Listening for tracking data on UDP port {PORT}...")

while True:
    try:
        data, addr = sock.recvfrom(8192)
        payload = json.loads(data.decode('utf-8'))

        # Extract blendshapes
        blend_dict = {}
        for item in payload.get("BlendShapes", []):
            src = item["k"]
            val = item["v"]

            if src in BLENDSHAPE_TO_L2D:
                target = BLENDSHAPE_TO_L2D[src]
                blend_dict[target] = val

        # Optionally include head rotation, eye direction, etc.
        blend_dict["_timestamp"] = payload.get("Timestamp")
        blend_dict["_face_found"] = payload.get("FaceFound")

        with open(output_path, "w") as f:
            json.dump(blend_dict, f)
    except Exception as e:
        print("Error parsing packet:", e)
