"""
********
组件的事件
********


- 事件.按钮_被点击 = wx.EVT_BUTTON
- 事件.复选框_被点击 = wx.EVT_CHECKBOX
- 事件.选择_被点击 = wx.EVT_CHOICE
- 事件.列表框_被点击 = wx.EVT_LISTBOX
- 事件.列表框_被双击 = wx.EVT_LISTBOX_DCLICK
- 事件.菜单_被点击 = wx.EVT_MENU
- 事件.菜单范围_被点击 = wx.EVT_MENU_RANGE
- 事件.滑块_被点击 = wx.EVT_SLIDER
- 事件.无线电箱_被点击 = wx.EVT_RADIOBOX
- 事件.单选按钮_被点击 = wx.EVT_RADIOBUTTON

- 事件.鼠标左键按下 = wx.EVT_LEFT_DOWN
- 事件.鼠标左键松开 = wx.EVT_LEFT_UP
- 事件.鼠标左键双击 = wx.EVT_LEFT_DCLICK
- 事件.鼠标右键按下 = wx.EVT_RIGHT_DOWN
- 事件.鼠标右键松开 = wx.EVT_RIGHT_UP
- 事件.鼠标右键双击 = wx.EVT_RIGHT_DCLICK
- 事件.鼠标中键按下 = wx.EVT_MIDDLE_DOWN
- 事件.鼠标中键松开 = wx.EVT_MIDDLE_UP
- 事件.鼠标中键双击 = wx.EVT_MIDDLE_DCLICK
- 事件.鼠标中键滚动 = wx.EVT_MOUSEWHEEL
- 事件.鼠标移动 = wx.EVT_MOTION
- 事件.鼠标进入 = wx.EVT_ENTER_WINDOW
- 事件.鼠标离开 = wx.EVT_LEAVE_WINDOW
- 事件.点击某键 = wx.EVT_CHAR_HOOK
- 事件.按下某键 = wx.EVT_KEY_DOWN
- 事件.松开某键 = wx.EVT_KEY_UP
- 事件.获得焦点 = wx.EVT_SET_FOCUS
- 事件.失去焦点 = wx.EVT_KILL_FOCUS
- 事件.按钮被单击 = wx.EVT_BUTTON
- 事件.创建完毕 = wx.EVT_WINDOW_CREATE
- 事件.尺寸被改变 = wx.EVT_SIZE
- 事件.位置被移动 = wx.EVT_MOVE
- 事件.将被关闭 = wx.EVT_CLOSE
- 事件.内容被改变 = wx.EVT_TEXT
- 事件.按下Enter键 = wx.EVT_TEXT_ENTER
- 事件.达到限制长度 = wx.EVT_TEXT_MAXLEN
- 事件.状态被改变 = wx.EVT_RADIOBUTTON
- 事件.狀态被改变 = wx.EVT_CHECKBOX
- 事件.选中列表项 = wx.EVT_COMBOBOX
- 事件.文本发生变化 = wx.EVT_TEXT
- 事件.弹出列表项 = wx.EVT_COMBOBOX_DROPDOWN
- 事件.收起列表项 = wx.EVT_COMBOBOX_CLOSEUP
- 事件.被拖动 = wx.EVT_SLIDER
- 事件.向小拖动 = wx.EVT_SCROLL_PAGEUP
- 事件.向大拖动 = wx.EVT_SCROLL_PAGEDOWN
- 事件.正在拖动 = wx.EVT_SCROLL_THUMBTRACK
- 事件.停止拖动 = wx.EVT_SCROLL_THUMBRELEASE
- 事件.数值被调整 = wx.EVT_SPINCTRL
- 事件.周期事件 = wx.EVT_TIMER
- 事件.表项被单击 = wx.EVT_CHECKLISTBOX
- 事件.表项被双击 = wx.EVT_LISTBOX_DCLICK
- 事件.链接被单击 = wx.adv.EVT_HYPERLINK
- 事件.双击某一天 = wx.adv.EVT_CALENDAR
- 事件.日期已更改 = wx.adv.EVT_CALENDAR_SEL_CHANGED
- 事件.年月已更改 = wx.adv.EVT_CALENDAR_PAGE_CHANGED
- 事件.内容被更改 = wx.adv.EVT_DATE_CHANGED
- 事件.内容被修改 = wx.adv.EVT_TIME_CHANGED
- 事件.左键开始拖动 = wx.EVT_LIST_BEGIN_DRAG
- 事件.右键开始拖动 = wx.EVT_LIST_BEGIN_RDRAG
- 事件.开始编辑标签 = wx.EVT_LIST_BEGIN_LABEL_EDIT
- 事件.编辑标签结束 = wx.EVT_LIST_END_LABEL_EDIT
- 事件.表项被删除 = wx.EVT_LIST_DELETE_ITEM
- 事件.表项全部被删 = wx.EVT_LIST_DELETE_ALL_ITEMS
- 事件.选中表项 = wx.EVT_LIST_ITEM_SELECTED
- 事件.取消选中表项 = wx.EVT_LIST_ITEM_DESELECTED
- 事件.表项已激活 = wx.EVT_LIST_ITEM_ACTIVATED
- 事件.中键单击表项 = wx.EVT_LIST_ITEM_MIDDLE_CLICK
- 事件.右键单击表项 = wx.EVT_LIST_ITEM_RIGHT_CLICK
- 事件.表项按下某键 = wx.EVT_LIST_KEY_DOWN
- 事件.插入新表项 = wx.EVT_LIST_INSERT_ITEM
- 事件.左键单击某列 = wx.EVT_LIST_COL_CLICK
- 事件.右键单击某列 = wx.EVT_LIST_COL_RIGHT_CLICK
- 事件.开始调整列宽 = wx.EVT_LIST_COL_BEGIN_DRAG
- 事件.分隔线在拖动 = wx.EVT_LIST_COL_DRAGGING
- 事件.列宽被修改 = wx.EVT_LIST_COL_END_DRAG
- 事件.表项被选中 = wx.EVT_LIST_ITEM_CHECKED
- 事件.表项未选中 = wx.EVT_LIST_ITEM_UNCHECKED
- 事件.滚动事件 = wx.EVT_SCROLL
- 事件.滚到最小位置 = wx.EVT_SCROLL_TOP
- 事件.滚到最大位置 = wx.EVT_SCROLL_BOTTOM
- 事件.向小滚动 = wx.EVT_SCROLL_PAGEUP
- 事件.向大滚动 = wx.EVT_SCROLL_PAGEDOWN
- 事件.停止滚动 = wx.EVT_SCROLL_CHANGED
- 事件.选项被单击 = wx.EVT_RADIOBOX
- 事件.颜色被更改 = wx.EVT_COLOURPICKER_CHANGED
- 事件.点击某颜色 = wx.EVT_COLOURPICKER_CURRENT_CHANGED
- 事件.取消更改颜色 = wx.EVT_COLOURPICKER_DIALOG_CANCELLED
- 事件.点击链接 = wx.EVT_TEXT_URL
- 事件.响应左键事件 = hyperlink.EVT_HYPERLINK_LEFT
- 事件.响应中键事件 = hyperlink.EVT_HYPERLINK_MIDDLE
- 事件.响应右键事件 = hyperlink.EVT_HYPERLINK_RIGHT
- 事件.数字被调整 = floatspin.EVT_FLOATSPIN

"""
import wx.lib.agw.floatspin as floatspin
import wx.lib.agw.hyperlink as hyperlink

import wx
import wx.adv
from wx import *


class 事件:
    按钮被点击 = wx.EVT_BUTTON
    复选框被点击 = wx.EVT_CHECKBOX
    选择被点击 = wx.EVT_CHOICE
    列表框被点击 = wx.EVT_LISTBOX
    列表框被双击 = wx.EVT_LISTBOX_DCLICK
    菜单被点击 = wx.EVT_MENU
    菜单范围被点击 = wx.EVT_MENU_RANGE
    滑块被点击 = wx.EVT_SLIDER
    单选框被点击 = wx.EVT_RADIOBOX
    单选框按钮被点击 = wx.EVT_RADIOBUTTON

    鼠标左键按下 = wx.EVT_LEFT_DOWN
    鼠标左键松开 = wx.EVT_LEFT_UP
    鼠标左键双击 = wx.EVT_LEFT_DCLICK
    鼠标右键按下 = wx.EVT_RIGHT_DOWN
    鼠标右键松开 = wx.EVT_RIGHT_UP
    鼠标右键双击 = wx.EVT_RIGHT_DCLICK
    鼠标中键按下 = wx.EVT_MIDDLE_DOWN
    鼠标中键松开 = wx.EVT_MIDDLE_UP
    鼠标中键双击 = wx.EVT_MIDDLE_DCLICK
    鼠标中键滚动 = wx.EVT_MOUSEWHEEL
    鼠标移动 = wx.EVT_MOTION
    鼠标进入 = wx.EVT_ENTER_WINDOW
    鼠标离开 = wx.EVT_LEAVE_WINDOW
    点击某键 = wx.EVT_CHAR_HOOK
    按下某键 = wx.EVT_KEY_DOWN
    松开某键 = wx.EVT_KEY_UP
    获得焦点 = wx.EVT_SET_FOCUS
    失去焦点 = wx.EVT_KILL_FOCUS
    按钮被单击 = wx.EVT_BUTTON
    创建完毕 = wx.EVT_WINDOW_CREATE
    尺寸被改变 = wx.EVT_SIZE
    位置被移动 = wx.EVT_MOVE
    将被关闭 = wx.EVT_CLOSE
    内容被改变 = wx.EVT_TEXT
    按下Enter键 = wx.EVT_TEXT_ENTER
    达到限制长度 = wx.EVT_TEXT_MAXLEN
    状态被改变 = wx.EVT_RADIOBUTTON
    狀态被改变 = wx.EVT_CHECKBOX
    选中列表项 = wx.EVT_COMBOBOX
    文本发生变化 = wx.EVT_TEXT
    弹出列表项 = wx.EVT_COMBOBOX_DROPDOWN
    收起列表项 = wx.EVT_COMBOBOX_CLOSEUP
    被拖动 = wx.EVT_SLIDER
    向小拖动 = wx.EVT_SCROLL_PAGEUP
    向大拖动 = wx.EVT_SCROLL_PAGEDOWN
    正在拖动 = wx.EVT_SCROLL_THUMBTRACK
    停止拖动 = wx.EVT_SCROLL_THUMBRELEASE
    数值被调整 = wx.EVT_SPINCTRL
    周期事件 = wx.EVT_TIMER
    表项被单击 = wx.EVT_CHECKLISTBOX
    表项被双击 = wx.EVT_LISTBOX_DCLICK
    链接被单击 = wx.adv.EVT_HYPERLINK
    双击某一天 = wx.adv.EVT_CALENDAR
    日期已更改 = wx.adv.EVT_CALENDAR_SEL_CHANGED
    年月已更改 = wx.adv.EVT_CALENDAR_PAGE_CHANGED
    内容被更改 = wx.adv.EVT_DATE_CHANGED
    内容被修改 = wx.adv.EVT_TIME_CHANGED
    左键开始拖动 = wx.EVT_LIST_BEGIN_DRAG
    右键开始拖动 = wx.EVT_LIST_BEGIN_RDRAG
    开始编辑标签 = wx.EVT_LIST_BEGIN_LABEL_EDIT
    编辑标签结束 = wx.EVT_LIST_END_LABEL_EDIT
    表项被删除 = wx.EVT_LIST_DELETE_ITEM
    表项全部被删 = wx.EVT_LIST_DELETE_ALL_ITEMS
    选中表项 = wx.EVT_LIST_ITEM_SELECTED
    取消选中表项 = wx.EVT_LIST_ITEM_DESELECTED
    表项已激活 = wx.EVT_LIST_ITEM_ACTIVATED
    中键单击表项 = wx.EVT_LIST_ITEM_MIDDLE_CLICK
    右键单击表项 = wx.EVT_LIST_ITEM_RIGHT_CLICK
    表项按下某键 = wx.EVT_LIST_KEY_DOWN
    插入新表项 = wx.EVT_LIST_INSERT_ITEM
    左键单击某列 = wx.EVT_LIST_COL_CLICK
    右键单击某列 = wx.EVT_LIST_COL_RIGHT_CLICK
    开始调整列宽 = wx.EVT_LIST_COL_BEGIN_DRAG
    分隔线在拖动 = wx.EVT_LIST_COL_DRAGGING
    列宽被修改 = wx.EVT_LIST_COL_END_DRAG
    表项被选中 = wx.EVT_LIST_ITEM_CHECKED
    表项未选中 = wx.EVT_LIST_ITEM_UNCHECKED
    滚动事件 = wx.EVT_SCROLL
    滚到最小位置 = wx.EVT_SCROLL_TOP
    滚到最大位置 = wx.EVT_SCROLL_BOTTOM
    向小滚动 = wx.EVT_SCROLL_PAGEUP
    向大滚动 = wx.EVT_SCROLL_PAGEDOWN
    停止滚动 = wx.EVT_SCROLL_CHANGED
    选项被单击 = wx.EVT_RADIOBOX
    颜色被更改 = wx.EVT_COLOURPICKER_CHANGED
    点击某颜色 = wx.EVT_COLOURPICKER_CURRENT_CHANGED
    取消更改颜色 = wx.EVT_COLOURPICKER_DIALOG_CANCELLED
    点击链接 = wx.EVT_TEXT_URL
    响应左键事件 = hyperlink.EVT_HYPERLINK_LEFT
    响应中键事件 = hyperlink.EVT_HYPERLINK_MIDDLE
    响应右键事件 = hyperlink.EVT_HYPERLINK_RIGHT
    数字被调整 = floatspin.EVT_FLOATSPIN


# 鼠标指针
# https://wxpython.org/Phoenix/docs/html/wx.StockCursor.enumeration.html
class 鼠标指针:
    无 = wx.CURSOR_NONE
    最大 = wx.CURSOR_MAX
    箭头 = wx.CURSOR_ARROW
    指向右侧的箭头 = wx.CURSOR_RIGHT_ARROW
    靶心 = wx.CURSOR_BULLSEYE
    矩形字符 = wx.CURSOR_CHAR
    十字 = wx.CURSOR_CROSS
    手型 = wx.CURSOR_HAND
    文本编辑型 = wx.CURSOR_IBEAM #工字梁垂直线
    表示鼠标左键按下 = wx.CURSOR_LEFT_BUTTON
    放大镜 = wx.CURSOR_MAGNIFIER
    表示按下中间按钮的鼠标 = wx.CURSOR_MIDDLE_BUTTON
    不可输入的符号 = wx.CURSOR_NO_ENTRY
    画笔 = wx.CURSOR_PAINT_BRUSH
    铅笔 = wx.CURSOR_PENCIL
    指向左的 = wx.CURSOR_POINT_LEFT
    指向右的 = wx.CURSOR_POINT_RIGHT
    箭头和问号 = wx.CURSOR_QUESTION_ARROW
    表示按下右键的鼠标 = wx.CURSOR_RIGHT_BUTTON
    调整大小的指向NE_SW = wx.CURSOR_SIZENESW
    调整大小的指向N_S = wx.CURSOR_SIZENS
    调整大小的指向NW_SE = wx.CURSOR_SIZENWSE
    调整大小的指向W_E = wx.CURSOR_SIZEWE
    一般大小的游标 = wx.CURSOR_SIZING
    Spraycan游标 = wx.CURSOR_SPRAYCAN
    沙漏 = wx.CURSOR_WAIT
    监视沙漏 = wx.CURSOR_WATCH
    透明 = wx.CURSOR_BLANK
    标准X11_wxGTK = wx.CURSOR_DEFAULT
    MacOS_Theme_Plus箭头 = wx.CURSOR_COPY_ARROW
    箭头和沙漏 = wx.CURSOR_ARROWWAIT


# 边框
# https://wxpython.org/Phoenix/docs/html/wx.Window.html
class 边框:
    窗口边框 = wx.BORDER_DEFAULT  # 窗口类将决定要显示的边框类型（如果有）。

    细边框 = wx.BORDER_SIMPLE  # 在窗口周围显示细边框。wx.SIMPLE_BORDER是此样式的旧名称。

    下陷边框 = wx.BORDER_SUNKEN  # 显示下陷的边框。wx.SUNKEN_BORDER是此样式的旧名称。

    凸起边框 = wx.BORDER_RAISED  # 显示凸起的边框。wx.RAISED_BORDER是此样式的旧名称。

    静态控件边框 = wx.BORDER_STATIC  # 显示适合静态控件的边框。wx.STATIC_BORDER是此样式的旧名称。仅Windows。

    系统边框 = wx.BORDER_THEME  # 在当前平台上显示适合控件的本机边框。在Windows上，这将是一个主题边框；在大多数其他平台上，将使用凹陷的边框。有关Windows主题边框的更多信息，请参见Windows主题边框。

    无边框 = wx.BORDER_NONE  # 不显示任何边框，覆盖窗口的默认边框样式。wx.NO_BORDER是此样式的旧名称。


# 边框_ = wx.BORDER_DOUBLE #此样式已过时，不应使用。

class 窗口样式:
    透明 = wx.TRANSPARENT_WINDOW  # 窗口是透明的，即它将不接收绘画事件。仅Windows。

    tab导航 = wx.TAB_TRAVERSAL  # wxWidgets使用此样式的窗口支持TAB其子级之间的导航，例如 wx.Dialog 和 wx.Panel。几乎不应在应用程序代码中使用它。

    支持导航键 = wx.WANTS_CHARS  # 使用它来指示窗口希望获取所有键的所有char / key事件-甚至对于通常用于对话框导航的键，例如TAB或ENTER，如果没有这种样式就不会生成这些键。如果您需要使用此样式来获取箭头等，但仍希望进行正常的键盘导航，则应调用“导航”以响应Tab和Shift-Tab的键事件。

    #  = wx.NO_FULL_REPAINT_ON_RESIZE #在Windows上，此样式用于在更改大小后完全禁用重新绘制窗口。由于现在是默认行为，因此样式现在已过时，不再起作用。

    垂直滚动条 = wx.VSCROLL  # 使用此样式可以启用垂直滚动条。请注意，此样式不能与不支持滚动条的本机控件一起使用，也不能与大多数端口中的顶级窗口一起使用。

    水平滚动条 = wx.HSCROLL  # 使用此样式启用水平滚动条。与wx.VSCROLL适用于此样式的限制相同。

    自动显示滚动条 = wx.ALWAYS_SHOW_SB  # 如果窗口具有滚动条，请在不需要滚动条时将其禁用，而不是隐藏它们（例如，当窗口的大小足够大而无需滚动条进行导航时）。目前，此样式已针对wxMSW，wxGTK和wxUniversal实现，并且在其他平台上不起作用。

    清除绘制闪烁 = wx.CLIP_CHILDREN  # 使用此样式可以消除由于重新绘制背景而在其上绘制子级而引起的闪烁。仅Windows。

    强制重绘窗口 = wx.FULL_REPAINT_ON_RESIZE  # 注意使用此样式可以在重新调整窗口大小时强制完全重绘窗口，而不是仅重绘受调整大小影响的窗口部分。请注意，默认情况下是2.5.1发行版之前的行为，并且如果您遇到以前使用过的代码重绘问题，则可能需要尝试此操作。目前，此样式仅适用于GTK + 2和Windows，并且始终在其他平台上进行完整的重新绘制。


class 按钮样式:
    文字左对齐 = wx.BU_LEFT  # 左对齐标签。仅Windows和GTK +。
    文字在顶部 = wx.BU_TOP  # 将标签对准按钮的顶部。仅Windows和GTK +。
    文字右对齐 = wx.BU_RIGHT  # 右对齐位图标签。仅Windows和GTK +。
    文字在底部 = wx.BU_BOTTOM  # 将标签对准按钮的底部。仅Windows和GTK +。
    精准贴合 = wx.BU_EXACTFIT  # 默认情况下，即使所有按钮的内容足够小以适合较小的尺寸，它们也至少由标准按钮尺寸制成。这样做是为了保持一致性，因为大多数平台在本机对话框中使用大小相同的按钮，但可以通过指定此标志来覆盖它们。如果指定了该按钮，则其大小将刚好足以容纳其内容。请注意，在MSW下，即使按钮具有非空标签，即使采用这种样式，该按钮仍将至少具有标准高度。
    不显示标签 = wx.BU_NOTEXT  # 即使按钮具有一个或其id是带有关联标签的标准库存ID之一，也无法在按钮中显示文本标签#如果不使用此样式，则仅应显示位图但使用标准ID的按钮也会显示标签。
    无边框 = wx.BORDER_NONE  # 创建一个无边框的按钮。目前已在MSW，GTK2和OSX / Cocoa中实现


# 文字方向
class 文本样式:
    左对齐 = wx.ALIGN_LEFT  # 将文本向左对齐。
    右对齐 = wx.ALIGN_RIGHT  # 将文本向右对齐。
    居中 = wx.ALIGN_CENTRE_HORIZONTAL  # 将文本居中（水平）。


class 标签样式:
    自动调整大小 = wx.ST_NO_AUTORESIZE  # ：默认情况下，控件将调整其大小以使其完全适合SetLabel 被调用时文本的大小。如果提供了此样式标志，则控件将不会更改其大小（此样式对于也具有ALIGN_RIGHT 或 ALIGN_CENTRE_HORIZONTAL 样式的控件特别有用， 因为否则在调用以后它们将不再有意义 SetLabel）。
    省略号在开头 = wx.ST_ELLIPSIZE_START  # ：如果labeltext宽度超过控件宽度，则用省略号替换标签的开头；用途wx.Control.Ellipsize。
    省略号在中间 = wx.ST_ELLIPSIZE_MIDDLE  # ：如果标签文本的宽度超过控件的宽度，则用省略号替换标签的中间；用途wx.Control.Ellipsize。
    省略号在末尾 = wx.ST_ELLIPSIZE_END  # ：如果标签文本的宽度超过控件的宽度，请用省略号替换标签的末尾；用途wx.Control.Ellipsize。
