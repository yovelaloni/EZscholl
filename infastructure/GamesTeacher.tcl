#############################################################################
# Generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#  Dec 31, 2020 11:23:38 AM +0200  platform: Windows NT
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
        -menu "$top.m45" -background #ff8080 
    wm focusmodel $top passive
    wm geometry $top 600x450+383+106
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
    wm title $top "דף משחקים מורה"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff8080 -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    label $top.lab46 \
        -background #ff8080 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -text משחקים 
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
        -pady 0 -text הוסף 
    vTcl:DefineAlias "$top.but51" "InsertButton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #e8cae7 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {חזרה לתפריט הראשי} 
    vTcl:DefineAlias "$top.but52" "BackToMenu" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent53 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 364 
    vTcl:DefineAlias "$top.ent53" "EntryGame" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab54 \
        -background #ff8080 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -text {:הכנס קישור למשחק נוסף} 
    vTcl:DefineAlias "$top.lab54" "Label2" vTcl:WidgetProc "Toplevel1" 1
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
        -in $top -x 0 -relx 0.567 -y 0 -rely 0.844 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but52 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.889 -width 127 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent53 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.756 -width 364 -relwidth 0 \
        -height 30 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 0 -relx 0.65 -y 0 -rely 0.778 -width 0 -relwidth 0.257 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
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

