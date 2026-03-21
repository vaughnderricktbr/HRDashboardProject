import time

# COPYRIGHT SYMBOL: \u00A9

def Render(append_element):
    return(
        f"<div class=\"w3-container\">"
        f"<div class=\"w3-content\">"
        f"<h1>Welcome to HR Dashboard</h1>"
        f"{append_element}"

        f"<p>\u00A9{time.gmtime(time.time()).tm_year} - Sample Dashboard</p>"
        f"</div>"
        f"</div>"
    )