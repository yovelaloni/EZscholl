#############################################################################
# Generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#  Dec 27, 2020 06:43:11 PM +0200  platform: Windows NT
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
        -menu "$top.m49" -background #ffd5ea \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+381+108
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "משחקים"
    vTcl:DefineAlias "$top" "Games" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    ttk::label $top.tLa45 \
        -background #ffd5ea -foreground $vTcl(actual_gui_fg) \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -relief flat -anchor w -justify left -text {משחקים לימודיים} 
    vTcl:DefineAlias "$top.tLa45" "TLabel1" vTcl:WidgetProc "Games" 1
    menu $top.m49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff8080 \
        -font {-family {Segoe UI} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    button $top.but56 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff8080 -cursor hand2 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {משחק זיכרון} 
    vTcl:DefineAlias "$top.but56" "Memory" vTcl:WidgetProc "Games" 1
    button $top.but57 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff8080 -cursor hand2 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {משחק חשבון} 
    vTcl:DefineAlias "$top.but57" "Math" vTcl:WidgetProc "Games" 1
    button $top.but58 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff8080 -cursor hand2 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {משחק לימוד אנגלית} 
    vTcl:DefineAlias "$top.but58" "English" vTcl:WidgetProc "Games" 1
    button $top.but59 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff8080 -cursor hand2 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {משחק גיאוגרפיה} 
    vTcl:DefineAlias "$top.but59" "Geography" vTcl:WidgetProc "Games" 1
    button $top.but60 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff8080 -cursor hand2 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {משחקי אומנות} 
    vTcl:DefineAlias "$top.but60" "Art" vTcl:WidgetProc "Games" 1
    button $top.but61 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff8080 -cursor hand2 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {חזרה לתפריט הראשי} 
    vTcl:DefineAlias "$top.but61" "BackToMenu" vTcl:WidgetProc "Games" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tLa45 \
        -in $top -x 0 -relx 0.383 -y 0 -rely 0.067 -width 0 -relwidth 0.192 \
        -height 0 -relheight 0.087 -anchor nw -bordermode ignore 
    place $top.but56 \
        -in $top -x 0 -relx 0.383 -y 0 -rely 0.2 -width 107 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but57 \
        -in $top -x 0 -relx 0.383 -y 0 -rely 0.333 -width 107 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but58 \
        -in $top -x 0 -relx 0.383 -y 0 -rely 0.467 -width 107 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but59 \
        -in $top -x 0 -relx 0.383 -y 0 -rely 0.6 -width 107 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but60 \
        -in $top -x 0 -relx 0.383 -y 0 -rely 0.733 -width 107 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but61 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.889 -width 137 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
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

