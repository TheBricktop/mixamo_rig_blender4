import bpy

def restore_armature_layers(layers_select):
    # Check if the active object is an armature
    if bpy.context.active_object.type != 'ARMATURE':
        return

    armature = bpy.context.active_object.data

    # Check Blender version
    if bpy.app.version < (4, 0, 0):
        # For Blender v3 and earlier, restore layers visibility
        for i in range(len(armature.layers)):
            armature.layers[i] = layers_select[i]
    else:
        # For Blender v4, restore collections visibility
        for i, collection in enumerate(armature.collections):
            if i < len(layers_select):
                collection.is_visible = layers_select[i]
        

def enable_all_armature_layers():
    # Check if the active object is an armature
    if bpy.context.active_object.type != 'ARMATURE':
        return []

    armature = bpy.context.active_object.data
    layers_select = []

    # Check Blender version
    if bpy.app.version < (4, 0, 0):
        # For Blender v3 and earlier, use layers
        for i in range(len(armature.layers)):
            layers_select.append(armature.layers[i])
            armature.layers[i] = True
    else:
        # For Blender v4, use collections
        for collection in armature.collections:
            layers_select.append(collection.is_visible)
            collection.is_visible = True

    return layers_select
