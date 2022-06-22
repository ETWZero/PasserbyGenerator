# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

'''
目前需要完善的工作：
（已完成）优化纹理更新，如果存在Preview就不必设置，而是Alt+P更新
（已完成）更新可见性形态键
'''
import bpy

bl_info = {
    "name" : "Passerby generator addon",
    "author" : "Eric Zane",
    "description" : "Passerby generator addon.",
    "blender" : (2, 93, 0),
    "version" : (0, 1, 2),
    "location" : "Image Editor -> Sidebar -> Settings",
    "warning" : "",
    "category" : "Render"
}

class RefreshSkinPreview(bpy.types.Operator):
    bl_idname = "object.renderskin"
    bl_label = "更新皮肤预览"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.render.filepath = "//texture//Preview"
        bpy.ops.render.render(write_still=True)

        try:
            SkinImage = bpy.data.images["Preview.png"]
        except KeyError as e:
            bpy.ops.image.open(filepath="//texture//Preview.png", files=[{"name":"Preview.png", "name":"Preview.png"}], relative_path=True, show_multiview=False)
            bpy.data.materials["Skin_Without_Eye"].node_tree.nodes["Image Texture"].image = bpy.data.images["Preview.png"]
        finally:
            SkinImage.reload()

        return {"FINISHED"}

class ChangeRigType(bpy.types.Operator):
    bl_idname = "object.changerigtype"
    bl_label = "更改模型类型"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.data.objects["Armature"].pose.bones["Setting"]["Steve&Alex"] == 0:
            bpy.data.objects["Armature"].pose.bones["Setting"]["Steve&Alex"] = 1
        else:
            bpy.data.objects["Armature"].pose.bones["Setting"]["Steve&Alex"] = 0
        for items in bpy.data.objects:
            items.hide_render = items.hide_render

        # bpy.context.object.update_tag()
        #bpy.ops.scene.
        return {"FINISHED"}

class RefreshSkinPreviewUi(bpy.types.Panel):
    bl_category = "Settings"
    bl_label = "咸鱼人的路人甲皮肤生成器"
    #bl_idname = "EASYFX_PT_Blur"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        obj = context.object

        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.renderskin")

        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.changerigtype")

        row = layout.row()
        if bpy.data.objects["Armature"].pose.bones["Setting"]["Steve&Alex"] == 0:
            row.label(text="当前模型：Steve")
        else:
            row.label(text="当前模型：Alex")
        #return super().draw(context)


def register():
    bpy.utils.register_class(RefreshSkinPreview)
    bpy.utils.register_class(ChangeRigType)
    bpy.utils.register_class(RefreshSkinPreviewUi)

def unregister():
    bpy.utils.unregister_class(RefreshSkinPreview)
    bpy.utils.unregister_class(ChangeRigType)
    bpy.utils.unregister_class(RefreshSkinPreviewUi)

if __name__ == "__main__":
    register()