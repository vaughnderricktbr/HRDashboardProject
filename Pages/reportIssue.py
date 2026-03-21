def RenderPage():
    return (
        f"<br><br>"
        f"<div class=\"w3-container\">"
        f"<div class=\"w3-content\">"
        f"<div class=\"w3-card\">"

        # HEADER
        f"<div class=\"w3-red w3-padding\">"
        f"<h2>Report Issue"
        f"</div>"

        # CONTENT

        f"<form class=\"w3-padding\">"

        f'<label><b>First Name:</b></label>'
        f'<input class="w3-input w3-border" type="text">'

        f'<label><b>Email Address:</b></label>'
        f'<input class="w3-input w3-border" type="text">'

        f'<label><b>What issue are you having?:</b></label>'
        f'<textarea class="w3-input w3-border" type="text" height="500"></textarea>'

        f"<p>Note, this form doesn't work.<p>"
        f'<button class="w3-btn w3-red">Report Issue</button>'
        f"</form>"

        ## END CONTENT
        f"</div>"
        f"</div>"
        f"</div>"
    ) 