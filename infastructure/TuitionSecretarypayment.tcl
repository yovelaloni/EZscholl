#############################################################################
# Generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#  Dec 30, 2020 03:53:48 PM +0200  platform: Windows NT
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



    menu .pop64 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 1 
    vTcl:DefineAlias ".pop64" "Popupmenu1" vTcl:WidgetProc "" 1

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
        -menu "$top.m45" -background #ffcf9f \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+468+138
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1540 845
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "תשלום שכר לימוד"
    vTcl:DefineAlias "$top" "Tuition" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    button $top.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffb871 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {תפריט ראשי} 
    vTcl:DefineAlias "$top.but46" "mainmenu" vTcl:WidgetProc "Tuition" 1
    button $top.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffb871 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text תשלום 
    vTcl:DefineAlias "$top.but47" "submitpayment" vTcl:WidgetProc "Tuition" 1
    entry $top.ent48 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 104 
    vTcl:DefineAlias "$top.ent48" "anount_entry" vTcl:WidgetProc "Tuition" 1
    entry $top.ent49 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 194 
    vTcl:DefineAlias "$top.ent49" "card_entry" vTcl:WidgetProc "Tuition" 1
    entry $top.ent53 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 114 
    vTcl:DefineAlias "$top.ent53" "id_entry" vTcl:WidgetProc "Tuition" 1
    message $top.mes54 \
        -background #ffcf9f \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Message -width 370 
    vTcl:DefineAlias "$top.mes54" "userDetails" vTcl:WidgetProc "Tuition" 1
    message $top.mes55 \
        -background #ffcf9f \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {סכום לתשלום} -width 140 
    vTcl:DefineAlias "$top.mes55" "amount" vTcl:WidgetProc "Tuition" 1
    message $top.mes56 \
        -background #ffcf9f \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {מספר כרטיס} -width 130 
    vTcl:DefineAlias "$top.mes56" "card" vTcl:WidgetProc "Tuition" 1
    message $top.mes57 \
        -background #ffcf9f \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {תעודת זהות של בעל כרטיס} -width 150 
    vTcl:DefineAlias "$top.mes57" "id" vTcl:WidgetProc "Tuition" 1
    message $top.mes58 \
        -background #ffcf9f \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text שנה -width 140 
    vTcl:DefineAlias "$top.mes58" "year" vTcl:WidgetProc "Tuition" 1
    message $top.mes69 \
        -background #ffcf9f \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text חודש -width 60 
    vTcl:DefineAlias "$top.mes69" "month" vTcl:WidgetProc "Tuition" 1
    entry $top.ent72 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 10 
    vTcl:DefineAlias "$top.ent72" "year_entry" vTcl:WidgetProc "Tuition" 1
    entry $top.ent73 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 74 
    vTcl:DefineAlias "$top.ent73" "month_entry" vTcl:WidgetProc "Tuition" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but46 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.844 -width 147 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 0 -relx 0.35 -y 0 -rely 0.844 -width 137 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent48 \
        -in $top -x 0 -relx 0.45 -y 0 -rely 0.222 -width 104 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent49 \
        -in $top -x 0 -relx 0.3 -y 0 -rely 0.311 -width 194 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent53 \
        -in $top -x 0 -relx 0.433 -y 0 -rely 0.4 -width 114 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.mes54 \
        -in $top -x 0 -relx 0.233 -y 0 -rely 0.022 -width 0 -relwidth 0.617 \
        -height 0 -relheight 0.118 -anchor nw -bordermode ignore 
    place $top.mes55 \
        -in $top -x 0 -relx 0.633 -y 0 -rely 0.222 -width 0 -relwidth 0.233 \
        -height 0 -relheight 0.051 -anchor nw -bordermode ignore 
    place $top.mes56 \
        -in $top -x 0 -relx 0.65 -y 0 -rely 0.311 -width 0 -relwidth 0.217 \
        -height 0 -relheight 0.051 -anchor nw -bordermode ignore 
    place $top.mes57 \
        -in $top -x 0 -relx 0.683 -y 0 -rely 0.4 -width 0 -relwidth 0.25 \
        -height 0 -relheight 0.051 -anchor nw -bordermode ignore 
    place $top.mes58 \
        -in $top -x 0 -relx 0.617 -y 0 -rely 0.489 -width 0 -relwidth 0.233 \
        -height 0 -relheight 0.051 -anchor nw -bordermode ignore 
    place $top.mes69 \
        -in $top -x 0 -relx 0.683 -y 0 -rely 0.578 -width 0 -relwidth 0.1 \
        -height 0 -relheight 0.051 -anchor nw -bordermode ignore 
    place $top.ent72 \
        -in $top -x 0 -relx 0.483 -y 0 -rely 0.489 -width 84 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent73 \
        -in $top -x 0 -relx 0.5 -y 0 -rely 0.578 -width 74 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
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

