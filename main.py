## Don't forget to install the dependency!
from pypresence import Presence # pip install pypresence
import time

client_id = "832598829810581534"    # Replace with the client ID of your application

RPC = Presence(client_id)           # Create the presence object with our client ID
RPC.connect()                       # Init the RPC connection

while True:
    details = "example details"     # 1st line in status
    state   = "example state"       # 2nd line in status

    large_image = "example_large"       # Large image key
    large_text  = "large image text"    # Large image tooltip text

    small_image = "example_small"       # Small image key
    small_text  = "small image text"    # Small image tooltip text

    buttons = [
        {
            "label": "button 1",            # label shown on the button
            "url":   "https://example.com"  # where to send a user that clicks the button
        }, 
        {
            "label": "button 2",            # The max number of buttons you can have is two,
            "url":   "https://example.com"  # and their labels cannot be empty.
        }
    ]

    RPC.update (                    # Update presence
        state = state,
        details = details,
        large_image = large_image,
        large_text = large_text,
        small_image = small_image,
        small_text = small_text,
        buttons = buttons
    )

    time.sleep(15)                  # Presence can only be updated every 15 seconds