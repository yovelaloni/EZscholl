#############################################################################
# Generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#  Dec 24, 2020 08:19:06 PM +0200  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}



    menu .pop51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 1 
    vTcl:DefineAlias ".pop51" "Popupmenu1" vTcl:WidgetProc "" 1

proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m46" -background #ccfdd5 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 1
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "קישורים"
    vTcl:DefineAlias "$top" "zoomlinkes" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    button $top.but45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #93ff93 -cursor hand2 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {קישור לשיעור מתמטיקה} 
    vTcl:DefineAlias "$top.but45" "zoom_math" vTcl:WidgetProc "zoomlinkes" 1
    menu $top.m46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    button $top.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #93ff93 -cursor hand2 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {קישור לשיעור היסטוריה} 
    vTcl:DefineAlias "$top.but47" "zoom_history" vTcl:WidgetProc "zoomlinkes" 1
    button $top.but48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #93ff93 -cursor hand2 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {קישור לשיעור תנך} 
    vTcl:DefineAlias "$top.but48" "zoom_bible" vTcl:WidgetProc "zoomlinkes" 1
    button $top.but49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #93ff93 -cursor hand2 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {קישור לשיעור עברית} 
    vTcl:DefineAlias "$top.but49" "zoom_hebrew" vTcl:WidgetProc "zoomlinkes" 1
    button $top.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #93ff93 -cursor hand2 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {קישור מעודכן מהמורה} 
    vTcl:DefineAlias "$top.but46" "zoom_updated_link_math" vTcl:WidgetProc "zoomlinkes" 1
    button $top.but69 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #93ff93 -cursor hand2 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {קישור מעודכן מהמורה} 
    vTcl:DefineAlias "$top.but69" "updated_history" vTcl:WidgetProc "zoomlinkes" 1
    button $top.but70 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #93ff93 -cursor hand2 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {קישור מעודכן מהמורה} 
    vTcl:DefineAlias "$top.but70" "Button1" vTcl:WidgetProc "zoomlinkes" 1
    button $top.but71 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #93ff93 -cursor hand2 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {קישור מעודכן מהמורה} 
    vTcl:DefineAlias "$top.but71" "Button2" vTcl:WidgetProc "zoomlinkes" 1
    message $top.mes72 \
        -background #ccfdd5 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {אם התבקשת להיכנס לקישור מעודכן 
                   נא לחץ כאן   } \
        -width 210 
    vTcl:DefineAlias "$top.mes72" "Message1" vTcl:WidgetProc "zoomlinkes" 1
    button $top.but73 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #93ff93 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {תפריט ראשי} 
    vTcl:DefineAlias "$top.but73" "mainmenu" vTcl:WidgetProc "zoomlinkes" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but45 \
        -in $top -x 0 -relx 0.533 -y 0 -rely 0.178 -width 136 -relwidth 0 \
        -height 63 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 0 -relx 0.533 -y 0 -rely 0.356 -width 136 -relwidth 0 \
        -height 63 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 0 -relx 0.533 -y 0 -rely 0.533 -width 136 -relwidth 0 \
        -height 63 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 0 -relx 0.533 -y 0 -rely 0.711 -width 136 -relwidth 0 \
        -height 63 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 0 -relx 0.2 -y 0 -rely 0.178 -width 176 -relwidth 0 \
        -height 53 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but69 \
        -in $top -x 0 -relx 0.2 -y 0 -rely 0.356 -width 177 -relwidth 0 \
        -height 54 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but70 \
        -in $top -x 0 -relx 0.2 -y 0 -rely 0.533 -width 177 -relwidth 0 \
        -height 54 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but71 \
        -in $top -x 0 -relx 0.2 -y 0 -rely 0.711 -width 177 -relwidth 0 \
        -height 54 -relheight 0 -anchor nw -bordermode ignore 
    place $top.mes72 \
        -in $top -x 0 -relx 0.183 -y 0 -rely 0.022 -width 0 -relwidth 0.35 \
        -height 0 -relheight 0.14 -anchor nw -bordermode ignore 
    place $top.but73 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.889 -width 137 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

