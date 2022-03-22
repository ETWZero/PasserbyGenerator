# 咸鱼人的路人甲皮肤生成器

这个 Blender 文件没什么特别的用途，就是一个Minecraft皮肤生成器，里面内置了一些皮肤部件节点，用户可以轻易地拖拽这些节点，将其连结在一起，最后生成一个Minecraft皮肤。

除此之外，本皮肤生成器在理论上还可以支持生成动态皮肤序列，可以支持高分辨率皮肤（128x，256x等分辨率）——前提是拥有对应特性的纹理（比如动态纹理和高分辨率的纹理）。

## 使用方法

### 使用前的准备

下载Blender 3.1以打开本文件。

在您使用该生成器之前，需要将安装生成器附带的插件。在“编辑”->“偏好设置”中切换到“插件”选项卡，点击右上角的“安装”按钮，在弹出的文件资源管理器中寻找生成器所在的文件目录，并双击该插件（名称为“PasserbyGeneratorAddon.py”），之后将“Render： Refresh Skin Preview”插件勾选，此时插件即可安装成功。

### 如何编辑皮肤

#### 生成器区域说明

切换到“Skin_Generator”（皮肤生成）工作区，此时的窗口分为左中右三部分：

左侧：上部分区域为模型效果预览效果，下部分为图像编辑器。在图像编辑器窗口中按下“T”键弹出侧边栏，在“设置”选项卡中会有“咸鱼人的路人甲皮肤生成器”选项，在该区域中您可以更新皮肤预览，或者更改皮肤的模型，同时还可以查看当前模型的类别（Steve或Alex）。

中间：上部分为资产管理器，在该资产管理器中包含了该生成器的所有皮肤部件、例程部件，以及颜色渐变部件。下部分区域为合成器节点，用来放置皮肤节点以进行皮肤生成。

右侧：属性区，用来对工程进行设定。

#### 基础用法

在资产管理器中寻找自己需要的部件，将部件拖动到下侧节点区域中，此时部件会变成一个节点，将节点再次拖动到黄色的线条上，即可为皮肤添加部件。如果要删除皮肤部件，可以右键节点选择“删除并重连”，或者选中节点按下快捷键“Ctrl+X”键进行删除。如果要切换皮肤部件的位置，可以按住“Alt”键，拖动需要拖动的节点，此时节点即可从连线上脱离，然后就可以放置在需要的位置上了。

皮肤部件节点分为两类，一类可以更改服装颜色（缩略图中拥有“彩虹”图标），一类无法改变服装颜色（缩略图中无“彩虹图标”）。服装颜色的自定义可以通过修改Custom_Color颜色来完成。而无法改变服装颜色的皮肤部件仅能拖动到主要节点上，无法改变颜色。

合成器区域可实时更新皮肤纹理合成结果。左侧预览区无法实时更新，需要安装插件后，在图像编辑器的侧边栏里进行操作，在“设置”选项卡中的“咸鱼人的路人甲皮肤生成器”选项中按下“更新皮肤预览”按钮才能够进行更新。

生成器支持Steve和Alex模型，在缩略图中以Steve和Alex图标对应作为标识。如果混用的话会导致最后皮肤可能存在映射错位的情况。

#### 进阶用法

##### 阴影处颜色的对比度/亮度比例

在本生成器节点中，可以自定义阴影处颜色的对比度于亮度的比例。选中一个皮肤部件，按“Tab”键展开节点树，会发现一个名为“Color_shader”的节点树，选中该节点后按“Tab”键展开，会发现一个名为“Edit Scale of Value and Saturation”的灰色框。只需要调节该节点里的数字，即可改变对比度/亮度比例。如果需要对单独的皮肤部件进行单独的调整，仅需要点击盾牌前面的数字，即可将该节点独立出来。

##### 为皮肤添加色彩纹理

每个允许自定义颜色的皮肤都可以添加色彩纹理。本皮肤生成器自带了一个颜色渐变的纹理，在皮肤部件已经连接到主合成的情况下，你可以将该节点连接至皮肤部件的“Custom_Color”节点，来预览该色彩纹理的效果。

如果需要多个色彩纹理，选中纹理节点和颜色渐变节点，按下“Shift+D”并在其他地方左键单击一下，即可将该节点复制出来。如果右键单击的画，会在原来的位置复制出一份，而不是取消复制。

### 如何进行皮肤导出

1. 按下F12，或者顶栏中点击“渲染”->“渲染图像”
2. 在弹出的渲染窗口中，在顶栏中点击“图像”->“保存”，在弹出的文件管理器中找到一个合适的位置，保存即可。

## 自定义方法

如果你有能力创作皮肤部件的话，欢迎贡献出自己的力量！

### 例程节点功能解释

目前本生成器提供了4类基础的皮肤部件的例子，分别为：

直接放置的皮肤部件、带有灰度的皮肤部件、带有两种灰度的皮肤部件、颜色灰度控制皮肤部件。

直接放置的皮肤部件很好理解，只要你拥有一件合适的皮肤部件就可以了，将该例程节点的第一个皮肤文件换成自己的皮肤部件即可。

带有灰度的皮肤部件，它可以通过调节自定义颜色来让该部件进行颜色变化。如果该皮肤部件全部都是灰度区域，只要将其转换为灰度（注意，不是去色处理，主流图像处理软件基本都可以做到颜色到灰度功能），删掉第二张纹理即可（注意，不是删除纹理节点，是应该点击该节点里的“X”号）；该皮肤部件应该在可变色的纹理部分进行灰度处理；只是需要额外的步骤，还需要将进行灰度处理的区域制成蒙版，将该蒙版加入到第二个图像文件节点即可：蒙版颜色随意，因此可以直接拿灰度文件当成蒙版文件即可。

带有两种灰度的皮肤部件则可以更改皮肤部件的两种颜色，更改的区域取决于分配的灰度区域。由此可以派生出多灰度皮肤部件。

颜色灰度控制部件可以更改亮处和暗处的颜色，同时由灰度图来控制整个纹理的颜色。

### 蒙版方式

蒙版添加给出了三种方式：自主绘制蒙版、使用节点生成的蒙版、不使用蒙版。

自主绘制蒙版，顾名思义，需要自己绘制蒙版的区域。蒙版的颜色随意，只需要确保蒙版之外的区域为透明即可。将蒙版添加至“Put mask here”的输入纹理处，然后将对应的节点连接到Alpha上叠节点，即可设置蒙版。

使用节点生成的蒙版，将“Automask”节点组包含的节点连接至Alpha节点处，即可根据皮肤自动生成不阻挡内层的蒙版。

不使用蒙版，将Alpha上叠处的节点取消连结即可（快捷键为“Ctrl+右键”）。

### 如何以例程节点为例，创建新的节点

1. 点击需要的节点，按下Shift+D进行复制，最后在合适的位置点击一下，即可复制完成。
2. 此时该节点名称后（或蓝白色盾牌标志前）会有一个数字“2”，点击那个数字，即可创建一个新的节点。
3. 创建完成后，将该节点重命名。对于手臂粗细不一样的情况，推荐在命名时进行特异性标注（比如Steve/Alex，Thick/Slim，粗/细等）。
4. 之后选中新建的节点，按下Alt+P键，将该皮肤部件节点与框分离。
5. 最后根据上面的自定义方法，对该节点进行自定义即可。

### 如何生成资产缩略图

1. 您可以自己尝试渲染资产缩略图，但本人同样也准备了一个缩略图模板。如果需要的话请继续阅读。
2. 打开模板文件“Skin_Template_Render.blend”。
3. 修改“Skin”材质的图片纹理，将其改为需要生成缩略图的皮肤纹理。如果对基底的皮肤纹理不满意，也可以修改“Base_Skin”材质的图片纹理，自定义一个基底的纹理。
4. 修改模型类型。这个模板里包含两个模型，需要分别将两个模型都修改类别才能正常显示。模型旁边有一个巨大的白色齿轮，选中它，在侧边栏的条目选项卡中，最后的“属性”条目中有“Steve&Alex”，修改其后的数值即可更改模型。0代表Steve，1代表Alex。
5. 在右下角的“场景”选项卡中，更改激活的相机，其中Head是头部，Upper_Head是上半身，Upper则是除了头部的上半身，Pants_Shoes是下半身，FullBody是全身。
6. 在合成器中更改资产缩略图的分类标识图片，目前分为两类四种：能否修改皮肤颜色（彩虹色带），模型适用于Steve模型还是Alex模型，或者通用（Steve图标、Alex图标、两者混用的图标）。合成组上有标识，将图片连接到相应的位置即可添加。
7. 以当前渲染设置进行渲染即可。

### 如何导出/导入资产

#### 导出

1. 新建一个文件，在顶栏单击“文件”->“追加”。
2. 在弹出的文件管理器中，找到需要导出节点的文件，在文件中找到“NodeTree”文件夹，双击进入。
3. **在右侧的选项勾选“伪用户”**，之后找到需要导出的节点，按住Ctrl或Shift进行多选，选中需要导出的节点，按下“追加”按钮即可将这些节点导出到该文件中。
4. 将这些节点资产化，详见下文“如何将节点资产化”。
5. 保存该.blend文件。

#### 导入

如果皮肤节点已经资产化，将该.blend文件放在“C:\\<用户名>\Documents\Blender\Assets”中即可导入完成——别忘了在Blender的“设置”->“文件&路径”中设置自己的资产库路径！接下来打开资产管理器，将资产库选择为“用户库”，即可显示所有皮肤部件节点。

### 如何将节点资产化

1. 右键节点组里的节点名称，选择“标记为资产”，即可完成节点的资产化。
2. 新建或找到资产管理器区域，选择刚才标记为资产的节点，按下“n”键展开侧边栏，即可更改资产的缩略图、资产的描述，以及作者信息。

### 注意事项

1. 蒙版的主要作用是为了防止外层皮肤遮挡住内层皮肤，因此蒙版的绘制步骤可以考虑这样进行：将内层对应的蒙版复制到外层的位置上。这就是节点自动生成蒙版的原理。

## 皮肤生成器的原理

该皮肤生成器的灵感来源于一款知名的换装游戏：Gacha Life，以及一个比较著名的社交联机模组：Essential。

首先介绍一下，为什么要为皮肤部件添加蒙版。Minecraft皮肤分为两层，内层与外层。而内层与外层的纹理是放在同一个图像文件里的。这就导致会发生一种十分尴尬的情况：如果只是单纯的覆盖纹理，那么就可能会让外层已存在的纹理遮挡住内层纹理。于是就需要将外层遮挡的这部分纹理消除，蒙版应运而生。蒙版的作用就是将已存在的纹理抹掉，然后放置上新的纹理。

这个问题解决了，但是另一个问题，即自定义颜色的问题就出现了。如何做才能更换纹理的颜色呢？这里采用的方法是灰度和添加颜色的方法。将皮肤改成灰度，之后用颜色将其相乘，就可以获得效果还算可以的皮肤部件了。在此基础上，由灰度来决定此处颜色的对比度大小，颜色越深对比度相应地越高，再与前文的灰度相乘即可获得效果不错的皮肤部件了。

## 接下来将要进行的工作

1. 继续扩充皮肤部件。
1. 添加颜色纹理。（已初步完成）
2. 灰度图+颜色的皮肤部件寻找阴影效果增强的方法。（已初步完成）
2. 将色度抠像的HSVA由纯黑色更改为透明色。（已经完成）

## 版权&分享声明

本皮肤生成器的合成节点由ETW_Zero（eric_zane@outlook.com）创作。本皮肤生成器的皮肤纹理由ETW_Zero创作。本皮肤生成器的玩家模型由ETW_Zero创作。

本皮肤生成器与节点组，及其生成的纹理、图像文件、模型文件均由 CC BY-NC-SA 4.0 协议进行分发，唯需勿将上述文件发布至网易我的世界任何平台（包括但不限于网易我的世界论坛、网易大神、网易我的世界皮肤组件市场等平台）；唯需勿将上述文件发布至[我的世界中文论坛](www.mcbbs.net)。在此前提下，请在尊重该协议的前提下进行分享与创作。

本文件的最终保留解释权归ETW_Zero所有。

