#############################################################################
# Generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#  Dec 30, 2020 08:46:51 PM +0200  platform: Windows NT
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
set vTcl(mode) Absolute
}




proc vTclWindow.top46 {base} {
    global vTcl
    if {$base == ""} {
        set base .top46
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m48" -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 1536x861+363+93
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1540 845
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    ttk::style configure TPanedwindow -background $vTcl(actual_gui_bg)
    ttk::style configure TPanedwindow.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TPanedwindow.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TPanedwindow.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::panedwindow $top.tPa54 \
        -orient horizontal 
    vTcl:DefineAlias "$top.tPa54" "TPanedwindow1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tPa54.p1 \
        -text {Pane 1} -width 75 -height 200 
    vTcl:DefineAlias "$top.tPa54.p1" "TPanedwindow1_p1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $top.tPa54.p1
    $top.tPa54 add $top.tPa54.p1 
    $top.tPa54 pane $top.tPa54.p1 -weight 0
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tPa54.p2 \
        -text {Pane 2} -width 125 -height 200 
    vTcl:DefineAlias "$top.tPa54.p2" "TPanedwindow1_p2" vTcl:WidgetProc "Toplevel1" 1
    set site_4_1 $top.tPa54.p2
    $top.tPa54 add $top.tPa54.p2 
    $top.tPa54 pane $top.tPa54.p2 -weight 0
    bind .top46.tPa54 <Map> {
        .top46.tPa54 sashpos 0 75
        bind .top46.tPa54 <Map> {}
    }
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tPa54 \
        -in $top -x 300 -y 260 -anchor nw -bordermode ignore 
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
Window show .top46 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

