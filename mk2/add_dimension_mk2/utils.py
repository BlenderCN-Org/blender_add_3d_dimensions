import bpy


# Add a TextCurve
def addText(string='', loc=((0, 0, 0)), textsize=1, align='CENTER', offset_y=0, font=''):

    tcu = bpy.data.curves.new(string + 'Data', 'FONT')
    text = bpy.data.objects.new(string + 'Text', tcu)
    text.location = loc

    if font == '':
        fnt = bpy.data.fonts[0]
    else:
        fnt = bpy.data.fonts.load(font)

    tcu.body = string
    tcu.align = align
    tcu.size = textsize
    tcu.offset_y = offset_y
    tcu.font = fnt
    bpy.context.scene.objects.link(text)

    return text


def addUnits(stext, units):
    scale = bpy.context.scene.unit_settings.scale_length
    unit_system = bpy.context.scene.unit_settings.system
    separate_units = bpy.context.scene.unit_settings.use_separate
    if unit_system == 'METRIC':
        if units == 'None': scale_steps = 1
        if units == '\u00b5m': scale_steps = 1000000
        if units == 'mm': scale_steps = 1000
        if units == 'cm': scale_steps = 100
        if units == 'm': scale_steps = 1
        if units == 'km': scale_steps = 1/1000
        if units == 'thou': scale_steps = 36000 * 1.0936133
        if units == '"': scale_steps = 36 * 1.0936133
        if units == '\'': scale_steps = 3 * 1.0936133
        if units == 'yd': scale_steps = 1 * 1.0936133
        if units == 'mi': scale_steps = 1/1760 * 1.0936133
        dval = stext * scale_steps * scale
    elif unit_system == 'IMPERIAL':
        if units == 'None': scale_steps = 3 * 1.0936133
        if units == '\u00b5m': scale_steps = 1000000
        if units == 'mm': scale_steps = 1000
        if units == 'cm': scale_steps = 100
        if units == 'm': scale_steps = 1
        if units == 'km': scale_steps = 1/1000
        if units == 'thou': scale_steps = 36000 * 1.0936133
        if units == '"': scale_steps = 36 * 1.0936133
        if units == '\'': scale_steps = 3 * 1.0936133
        if units == 'yd': scale_steps = 1 * 1.0936133
        if units == 'mi': scale_steps = 1/1760 * 1.0936133
        dval = stext * scale_steps * scale
    else:
        dval = stext
    return dval