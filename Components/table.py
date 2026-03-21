def RenderTable(table_list, heading):
    ## RenderTable(['Heading 1', 'Heading 2', 'Heading 3'], ['Val 1', 'Val 2', 'Val 3'])
    table_render = "<table class=\"w3-table-all\">"
    heading_render = "<thead><tr>"
    for e in heading:
        heading_render += f"<td>{e}</td>"
    
            
    heading_render += "</tr></thead>"
    tt_item_render = "<tbody>"
    for item in table_list:
        item_render = "<tr>"
        for e in item:
            item_render += f"<td>{e}</td>"
        item_render += "</tr>"
        tt_item_render += item_render

    table_render += heading_render
    table_render += tt_item_render
    table_render += "</table>"
    return table_render
            
