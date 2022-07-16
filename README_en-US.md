# SaltyFishyMan's Passerby Skin Generator

This Blender file has no special purpose, it's just a Minecraft skin generator with some built-in skin part nodes that the user can easily drag and drop to link them together and finally generate a Minecraft skin.

In addition, this skin generator can theoretically support the generation of dynamic skin sequences and can support high-resolution skins (128x, 256x, etc. ) - provided that the textures with corresponding characteristics (such as dynamic textures and high-resolution textures) are available.

## How to use

### Prepare for use

Download Blender 3.2 to open this file.

Before you can use the generator, you need to install the addon that comes with the generator. Switch to the "Plugins" tab in "Edit" -> "Preferences", click the "Install "button in the pop-up file explorer, look for the file directory where the generator is located, and double-click the add-on (named "PasserbyGeneratorAddon.py"), then check the "Render. Refresh Skin Preview" plug-in is checked, then the plug-in can be installed successfully.

### How to edit skins

#### Description of the generator interface

Switch to the "Skin_Generator" workspace, the window is divided into three parts: left, middle and right.

Left side: The upper part of the window is for the model (or skin) preview, and the lower part is for the image editor. In the image editor window, press the "T" key to bring up the sidebar, and in the "Settings" tab there will be the "Salty Man's Passerby Skin Generator" option, in which you can Update the skin preview, or change the model of the skin, and also see the category of the current model (Steve or Alex).

Middle: The upper section is the asset manager, which contains all the skin parts, routine parts, and color gradient parts for this generator. The lower section area is the compositor node, used to place skin nodes for skin generation.

Right side: Properties area, used to set up the project.

#### Basic usage

Switch to the "Skin_Generator" workspace. To add its corresponding skin part to the character's body, drag the skin part node onto the long yellow curve above it with left click. If you need to remove an unsuitable skin part, hold down Alt key and left click to move the node out of the yellow curve.

There are two types of skin part nodes, one that allows you to change the clothing color and others that does not. The customization of clothing color can be done by modifying the Custom_Color. The skin parts that cannot change the clothing color can only be dragged to the main node and cannot change the color.

The compositor area can automatically update the skin texture compositing result in real time. The preview area on the left side cannot be updated in real time, so you need to perform perspective operations in the preview area (such as holding down the middle button to rotate the perspective, using the scroll wheel to zoom the perspective, etc.) to update the skin compositing results.

The generator supports both Steve and Alex models, with the Steve and Alex icons corresponding as identifiers in the thumbnails. If mixed it will lead to a possible mapping mismatch in the final skin.

#### Advanced usage

##### Contrast/brightness ratio of colors in shadows

In this generator node, you can customize the contrast/brightness ratio of the colors in the shadows. Select a skin part, press "Tab" to expand the node tree, you will find a node tree named "Color_shader", select the node and press "Tab After selecting the node and pressing "Tab" to expand it, you will find a gray box named "Edit Scale of Value and Saturation". Simply adjust the numbers in this node to change the contrast/brightness ratio. If you need to make separate adjustments to individual skin parts, just click on the number in front of the shield to separate that node out.

##### Adding color textures to skins

Every skin that allows custom colors can have color textures added to it. This skin generator comes with a color gradient texture. In case the skin part is already connected to the main composite, you can connect this node to the "Custom_Color" node of the skin part to preview the effect of the color texture.

If you need more than one color texture, select the texture node and the color gradient node, press "Shift+D" and left-click somewhere else to copy the node. If you right-click on the painting, a copy will be made in the original location instead of undoing the copy.

##### Adding color patterns to skins

Every skin that allows custom colors can have a color pattern added to it, and the user can also connect the color output of the color texture to the color input of the color pattern. The usage is similar to color textures, but the colors of color textures are gradient and the interpolation value can be set by yourself (RGB or HSV); the number of colors of color patterns is extremely limited and only the specified colors can be set.

### How to do skin export

1. Press F12, or click "Render" -> "Render Image" in the top bar
2. In the rendering window, click "Image" -> "Save" in the top bar, and find a suitable location in the file manager that pops up and save it.

## Customization method

If you have the ability to create skin parts, feel free to contribute!

### Example node function explanation

Currently this generator provides examples of 4 basic types of skin widgets: 

Directly placed skin widgets, skin widgets with grayscale, skin widgets with two shades of gray, and color grayscale control skin widgets.

Directly placed skin widgets is easy to understand, as long as you have a suitable skin widget, just replace the first skin file of the routine node with your own skin widget.

Skin widgets with grayscale, it is possible to make that widget color change by adjusting the custom color. If the skin part is all grayscale, just convert it to grayscale (note that it is not de-colored, mainstream image processing software can basically do color to grayscale function), delete the second texture (note that it is not deleting the texture node, but should click the "X" sign in the node); the skin part should be in The skin part should be grayscale in the texture part; it just needs an extra step to make a mask of the grayscale area and add it to the second image file node: the mask color is arbitrary, so you can just take the grayscale file as a mask file.

Skin widgets with two shades of gray can change both colors of the skin part, depending on the grayscale area assigned. This allows for the derivation of multi-gray skin parts.

The color grayscale control widget can change the color of light and dark areas, while the grayscale map controls the color of the entire texture.

### Masking methods

There are three ways to add a mask: draw your own mask, use the node-generated mask, and don't use the mask.

Draw your own mask. As the name implies, you need to draw your own masked area. The color of the mask is optional, just make sure that the area outside the mask is transparent. Add the mask to the "Put mask here" input texture, and then connect the corresponding node to the Alpha overlay node to set the mask.

Use the node-generated mask, connect the node contained in the "Automask" node group to the Alpha node to automatically generate a mask that does not block the inner layer based on the skin.

Don't use the mask, unlink the nodes in the Alpha overlay (Ctrl+Right click).

### How to create a new node as an example of  the node

1. Click on the desired node, press Shift+D to copy it, and finally click on the appropriate location to finish copying.
2. At this time, there will be a number "2" after the name of the node (or before the blue and white shield symbol), click that number to create a new node.
3. After the creation is complete, rename the node. For cases where the arm thickness is different, we recommend naming it with specificity (e.g. Steve/Alex, Thick/Slim, thick/thin, etc.).
4. After that, select the newly created node and press Alt+P to separate the skin part node from the box.
5. Finally, just customize the node according to the customization method above.

### How to generate asset thumbnails

1. You can try to render asset thumbnails yourself, but I have also prepared a thumbnail template. Please read on if you need it. 
2. Open the template file "Skin_Template_Render.blend". 
3. Modify the image texture of the "Skin" material and change it to the skin texture you need to generate thumbnails. If you are not satisfied with the base skin texture, you can also modify the image texture of the "Base_Skin" material and customize a base texture. 
4. Modify the model type. This template contains two models, you need to modify the category of both models separately to display them properly. There is a huge white gear next to the model, select it, and in the sidebar's entry tab, the last "Properties" entry has "Steve & Alex", modify the value to change the model. 0 means Steve, 1 means Alex. 
5. In the "Scene" tab in the lower right corner, change the active camera, where Head is the head, Upper_Head is the upper body, Upper is the upper body except the head, Pants_Shoes is the lower body, and FullBody is the whole body.
6. In the compositor to change the classification of asset thumbnails identify the picture, currently divided into two categories of four: can modify the skin color (rainbow ribbon), the model applies to Steve model or Alex model, or universal (Steve icon, Alex icon, a mix of both icons). The compositing group is marked with a logo, and images are added by connecting them to the appropriate location.
7. Just render with the current render settings.

### How to export/import assets

#### Export

1. Create a new file, click "File" -> "Append" in the top bar. 
2. In the pop-up file manager, find the file you need to export nodes to, find the "NodeTree" folder in the file, double-click it to enter. 
3. **Check the "Pseudo-User" option on the right**, then find the nodes that need to be exported, hold Ctrl or Shift to multi-select, select the nodes that need to be exported, and press the "Append" button to export these nodes to the file. 
Assign these nodes, see "How to Assign Nodes" below. 
5. Save the .blend file.

#### Import

If the skin nodes have been assetized, place the .blend file in "C:\\\<username>\Documents\Blender\Assets" to complete the import - don't forget to add it to Blender's "Settings"->"Files & Paths" to set your own asset library path! Next, open the Asset Manager and select the asset library as "User Library" to display all skinned part nodes.

### How to assetize nodes

1. Right click on the node name in the node group and select "Mark as asset" to assetize the node. 
2. Create a new node or find the asset manager area, select the node you just marked as an asset, and press "n" to expand the sidebar, you can change the thumbnail, description of the asset, and author information.

### Caution

1. The main purpose of the mask is to prevent the outer skin from blocking the inner skin, so the masking step can be considered as follows: copy the corresponding mask of the inner layer to the position of the outer layer. This is the principle of automatic mask generation for nodes.

## Principle of the skin generator

The skin generator is inspired by a well-known dress-up game: Gacha Life, and a more famous social networking module: Essential.

First of all, let's introduce why you need to add a mask to the skin part. Minecraft skins are divided into two layers, the inner layer and the outer layer. And the textures of the inner layer and the outer layer are placed in the same image file. This leads to a very awkward situation: if you simply overlay the textures, you may have the outer layer's already existing textures obscuring the inner layer textures. So it is necessary to eliminate the outer layer of the texture, and the mask is created. The purpose of masking is to wipe out the existing texture and place a new one.

This problem is solved, but there is another problem - the problem of custom colors. What can be done to replace the color of the texture? The method used here is the grayscale and add color method. By changing the skin to grayscale and multiplying it with color afterwards, you can get a skin part with a decent effect. The darker the color, the higher the contrast, and then multiply it with the previous grayscale to get a better skin part.

## What to do next

1. Continue expanding the skin component. 
2. Add color textures. (Initially done)
3. Find a way to enhance the shading effect of the grayscale + color skin part. (Initially done)
4. Change the HSVA of chroma keying from pure black to transparent color.(Initially done)

## Copyright & Sharing Notice

The composite node of this skin generator was created by ETW_Zero (eric_zane@hotmail.com). If not otherwise specified, The skin textures for this skin generator were created by ETW_Zero. The player model for this skin generator was created by ETW_Zero.

This skin generator and node set, and its generated textures, image files, and model files are distributed by CC BY-NC-SA 4.0 protocol; only do not distribute the above files to any platform of NetEase Minecraft (网易我的世界)(including but not limited to NetEase Minecraft forum(网易我的世界论坛), NetEase Da Shen（网易大神）, NetEase Minecraft Skin Component Market（网易我的世界皮肤组件市场）, etc.); only do not distribute the above files to [MCBBS(我的世界中文论坛)](www.mcbbs.net). With that in mind, please share and create under the premise of respecting this agreement.

All Right Reserved by ETW_Zero.