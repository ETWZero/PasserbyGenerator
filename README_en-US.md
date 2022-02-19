# SaltyFishyMan's Passerby Skin Generator

This Blender file has no special purpose, it's just a Minecraft skin generator with some built-in skin part nodes that the user can easily drag and drop to link them together and finally generate a Minecraft skin.

In addition, this skin generator can theoretically support the generation of dynamic skin sequences and can support high-resolution skins (128x, 256x, etc. ) - provided that the textures with corresponding characteristics (such as dynamic textures and high-resolution textures) are available.

## How to use

### How to edit skins

#### Basic usage

Switch to the "Skin_Generator" workspace. To add its corresponding skin part to the character's body, drag the skin part node onto the long yellow curve above it with left click. If you need to remove an unsuitable skin part, hold down Alt key and left click to move the node out of the yellow curve.

There are two types of skin part nodes, one that allows you to change the clothing color and others that does not. The customization of clothing color can be done by modifying the Custom_Color. The skin parts that cannot change the clothing color can only be dragged to the main node and cannot change the color.

The compositor area can automatically update the skin texture compositing result in real time. The preview area on the left side cannot be updated in real time, so you need to perform perspective operations in the preview area (such as holding down the middle button to rotate the perspective, using the scroll wheel to zoom the perspective, etc.) to update the skin compositing results.

#### Advanced usage

##### Contrast/brightness ratio of colors in shadows

In this generator node, you can customize the contrast/brightness ratio of the colors in the shadows. Select a skin part, press "Tab" to expand the node tree, you will find a node tree named "Color_shader", select the node and press "Tab After selecting the node and pressing "Tab" to expand it, you will find a gray box named "Edit Scale of Value and Saturation". Simply adjust the numbers in this node to change the contrast/brightness ratio. If you need to make separate adjustments to individual skin parts, just click on the number in front of the shield to separate that node out.

##### Adding color textures to skins

Every skin that allows custom colors can have color textures added to it. This skin generator comes with a color gradient texture. In case the skin part is already connected to the main composite, you can connect this node to the "Custom_Color" node of the skin part to preview the effect of the color texture.

If you need more than one color texture, select the texture node and the color gradient node, press "Shift+D" and left-click somewhere else to copy the node. If you right-click on the painting, a copy will be made in the original location instead of undoing the copy.

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

### How to export/import nodes

#### Export

1. Create a new file and click "File"->"Append" in the top bar. 
2. In the pop-up file manager, find the file you need to export the node, find the "NodeTree" folder in the file, and double-click it to enter. 
3. Find the nodes you need to export, hold Ctrl or Shift to multi-select, select the nodes you need to export, and press the "Append" button to export these nodes to a new file. 
4. Save the .blend file.

#### Import

Basically the same as above. After importing, if you need to add nodes, you can Shift+A (Add Node) -> Group at the composite node to find the imported nodes and place them in the composite node.

### Caution

1. The main purpose of the mask is to prevent the outer layer of skin from blocking the inner skin, so the mask drawing step can be considered as follows: copy the corresponding mask of the inner layer to the position of the outer layer. This is the principle of automatic mask generation for nodes.

## Principle of the skin generator

The skin generator is inspired by a well-known dress-up game: Gacha Life, and a more famous social networking module: Essential.

First of all, let's introduce why you need to add a mask to the skin part. Minecraft skins are divided into two layers, the inner layer and the outer layer. And the textures of the inner layer and the outer layer are placed in the same image file. This leads to a very awkward situation: if you simply overlay the textures, you may have the outer layer's already existing textures obscuring the inner layer textures. So it is necessary to eliminate the outer layer of the texture, and the mask is created. The purpose of masking is to wipe out the existing texture and place a new one.

This problem is solved, but there is another problem - the problem of custom colors. What can be done to replace the color of the texture? The method used here is the grayscale and add color method. By changing the skin to grayscale and multiplying it with color afterwards, you can get a skin part with a decent effect. The darker the color, the higher the contrast, and then multiply it with the previous grayscale to get a better skin part.

## What to do next

1. Continue expanding the skin component. 
1. Add color textures. (Initially done)
2. Find a way to enhance the shading effect of the grayscale + color skin part. (Initially done)
2. Change the HSVA of chroma keying from pure black to transparent color.(Initially done)

## Copyright & Sharing Notice

The composite node of this skin generator was created by ETW_Zero (eric_zane@hotmail.com). The skin textures for this skin generator were created by ETW_Zero. The player model for this skin generator was created by ETW_Zero.

This skin generator and node set, and its generated textures, image files, and model files are distributed by CC BY-NC-SA 4.0 protocol; only do not distribute the above files to any platform of NetEase Minecraft (网易我的世界)(including but not limited to NetEase Minecraft forum(网易我的世界论坛), NetEase Da Shen（网易大神）, NetEase Minecraft Skin Component Market（网易我的世界皮肤组件市场）, etc.); only do not distribute the above files to [MCBBS(我的世界中文论坛)](www.mcbbs.net). With that in mind, please share and create under the premise of respecting this agreement.

All Right Reserved by ETW_Zero.