def Render(path):
    return (
        f"<br><br>"
        f"<div class=\"w3-container\">"
        f"<div class=\"w3-content\">"
        f"<div class=\"w3-card w3-padding\">"
        f"<h1>HTTP Error</h1>"
        f"<p>404 - Page not found<p>"
        f"<p>This url: <b>{path}</b> cannot be found on this server.</p>"
        f"</div>"
        f"</div>"
        f"</div>"
    )