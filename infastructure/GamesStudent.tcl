#############################################################################
# Generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
<<<<<<< HEAD
#  Dec 27, 2020 06:43:11 PM +0200  platform: Windows NT
=======
#  Dec 31, 2020 11:27:28 AM +0200  platform: Windows NT
>>>>>>> vicky
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
<<<<<<< HEAD
        -menu "$top.m49" -background #ffd5ea \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+381+108
=======
        -menu "$top.m45" -background #ff8080 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+383+106
>>>>>>> vicky
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
<<<<<<< HEAD
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
=======
    wm title $top "דף משחקים מורה"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff8080 -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    label $top.lab46 \
        -activebackground #f9f9f9 -activeforeground black -background #ff8080 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text משחקים 
    vTcl:DefineAlias "$top.lab46" "Label1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #efc1f0 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text חשבון 
    vTcl:DefineAlias "$top.but47" "Math" vTcl:WidgetProc "Toplevel1" 1
    button $top.but48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #e9c9df -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text אנגלית 
    vTcl:DefineAlias "$top.but48" "English" vTcl:WidgetProc "Toplevel1" 1
    button $top.but49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #f5bcf4 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text זיכרון 
    vTcl:DefineAlias "$top.but49" "Memory" vTcl:WidgetProc "Toplevel1" 1
    button $top.but50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #e6ccdd -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text אומנות 
    vTcl:DefineAlias "$top.but50" "Art" vTcl:WidgetProc "Toplevel1" 1
    button $top.but51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #e4cddf -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {מחשק נוסף} 
    vTcl:DefineAlias "$top.but51" "AnotherGame" vTcl:WidgetProc "Toplevel1" 1
    button $top.but52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #e8cae7 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {חזרה לתפריט הראשי} 
    vTcl:DefineAlias "$top.but52" "BackToMenu" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab46 \
        -in $top -x 0 -relx 0.383 -y 0 -rely 0.044 -width 0 -relwidth 0.157 \
        -height 0 -relheight 0.091 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 0 -relx 0.4 -y 0 -rely 0.2 -width 77 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 0 -relx 0.4 -y 0 -rely 0.311 -width 77 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 0 -relx 0.4 -y 0 -rely 0.422 -width 77 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but50 \
        -in $top -x 0 -relx 0.4 -y 0 -rely 0.533 -width 77 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but51 \
        -in $top -x 0 -relx 0.4 -y 0 -rely 0.644 -width 77 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but52 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.889 -width 127 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
>>>>>>> vicky
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
