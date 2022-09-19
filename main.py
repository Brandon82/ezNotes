import dearpygui.dearpygui as dpg
import os 
from dearpygui.demo import show_demo
from themes import *
from helpers import *
import ctypes
import subprocess

ctypes.windll.shcore.SetProcessDpiAwareness(2)

W_WIDTH = 700
W_HEIGHT = 400
SIDEBAR_SIZE = 150
APP_NAME = 'ez.Notes'

CUR_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
NOTE_PATH = os.path.dirname(os.path.realpath(__file__))

#file_path = os.getcwd()
note_list = ['Notes', 'Settings', 'Themes']

dpg.create_context()

def auto_center_cb(s, d):
    win_width = dpg.get_item_width(mainw)
    win_height = dpg.get_item_height(mainw)
    dpg.set_item_width(item=spcr1, width=(win_width - SIDEBAR_SIZE - dpg.get_item_width(clear_btn)*1.5))

def sidebar_cb(s, d):
    #s=sender=tag
    if s in note_list:
        if s==note_list[0]:
            apply_tab_button_active(sbb1, sidebar_buttn)
            apply_tab_button_inactive(sbb2)
            apply_tab_button_inactive(sbb3)
            if(dpg.does_item_exist(tab2) or dpg.does_item_exist(tab3)):
                dpg.hide_item(tab2)
                dpg.hide_item(tab3)
                dpg.show_item(tab1)
        elif s==note_list[1]:
            apply_tab_button_active(sbb2, sidebar_buttn)
            apply_tab_button_inactive(sbb1)
            apply_tab_button_inactive(sbb3)
            if(dpg.does_item_exist(tab1) or dpg.does_item_exist(tab3)):
                dpg.hide_item(tab1)
                dpg.hide_item(tab3)
                dpg.show_item(tab2)
        elif s==note_list[2]:
            apply_tab_button_active(sbb3, sidebar_buttn)
            apply_tab_button_inactive(sbb1)
            apply_tab_button_inactive(sbb2)
            if(dpg.does_item_exist(tab1) or dpg.does_item_exist(tab2)):
                dpg.hide_item(tab1)
                dpg.hide_item(tab2)
                dpg.show_item(tab3)

def open_note_cb(s, d):
    subprocess.Popen(f'explorer /select,{NOTE_PATH}')

with dpg.font_registry():
    title_font = dpg.add_font('C:\Windows\Fonts\Kayak Sans Bold.otf', 20)
    default_font = dpg.add_font(CUR_FILE_PATH + '\Fonts\OpenSans-SemiBold.ttf', 20)
    open_sans_bold_title = dpg.add_font(CUR_FILE_PATH + '\Fonts\OpenSans-Bold.ttf', 20)

with dpg.window(width = W_WIDTH, height = W_HEIGHT, no_title_bar=True, no_resize=True, no_move=True) as mainw:
    dpg.bind_font(default_font)

    with dpg.group(horizontal=True) as main_group:
        with dpg.child_window(label='side_bar', show=True, width=SIDEBAR_SIZE) as side_bar:
            dpg.add_text(APP_NAME)
            dpg.add_dummy(height=100)

            sbb1 = dpg.add_button(label='Notes', width=SIDEBAR_SIZE-1, tag='Notes', height=30, callback=sidebar_cb)
            apply_tab_button_active(sbb1, sidebar_buttn)
            sbb2 = dpg.add_button(label='Settings', width=SIDEBAR_SIZE-1, tag='Settings', height=30, callback=sidebar_cb)
            apply_tab_button_inactive(sbb2)
            sbb3 = dpg.add_button(label='Themes', width=SIDEBAR_SIZE-1, tag='Themes', height=30, callback=sidebar_cb)
            apply_tab_button_inactive(sbb3)

        # --- Main Tab ---
        with dpg.child_window(label='tab1', show=True) as tab1:

            with dpg.group(horizontal=True) as t1_header:
                dpg.add_text("Note 1:")
                spcr1 = dpg.add_spacer(width=400)
                clear_btn = dpg.add_button(label='Clear note', tag='clearbtn', width=130, height=28)

            line1 = LayoutHelper()
            line1.add_widget(dpg.add_input_text(tag='note_input', default_value='Enter Note', multiline=True, height=200), 95)
            line1.add_widget(dpg.add_spacer(), 5.0)
            line1.submit()
            
            save_btn = dpg.add_button(label='Save note', tag='savebtn', width=180, height=30)
            opennote_btn = dpg.add_button(label='Open File Path', tag='openfilebtn', width=180, height=30, callback=open_note_cb)

            with dpg.group(horizontal=True) as cur_path_grp:
                dpg.add_text('Note Path: ')
                cur_path_text = dpg.add_text(NOTE_PATH, color=(150, 150, 150))

        # --- Settings Tab ---
        with dpg.child_window(label='tab2', show=False) as tab2:
            dpg.add_text("Settings [NYI]:")
            #dpg.add_text("UI Font: ")
            dpg.add_combo(label='UI Font', tag='uifont_combo', items=('a', 'b', 'c'), width=240)

            #dpg.add_text("Note Font: ")
            dpg.add_combo(label='Note Font', tag='notefont_combo', items=('a', 'b', 'c'), width=240)
            dpg.add_checkbox(label='Auto-save notes')

            open_gh_btn = dpg.add_button(label='Open Github', tag='openghbtn', width=180, height=30)


            with dpg.group(horizontal=True) as cur_path_grp:
                dpg.add_text('App Path: ')
                cur_path_text = dpg.add_text(CUR_FILE_PATH, color=(150, 150, 150))

            with dpg.group(horizontal=True) as cur_path_grp:
                dpg.add_text('Note Path: ')
                cur_path_text = dpg.add_text(NOTE_PATH, color=(150, 150, 150))
            

        with dpg.child_window(label='tab3', show=False) as tab3:
            dpg.add_text("Themes:")
            dpg.add_color_edit(label='Main Background', no_picker=True)
            dpg.add_color_edit(label='Sidebar Background', no_picker=True)
            dpg.add_color_edit(label='Text', no_picker=True)
            dpg.add_color_edit(label='Accent Color', no_picker=True)
            reset_theme_btn = dpg.add_button(label='Reset Theme', tag='resetthemebtn', width=180, height=30)





with dpg.theme() as zero_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 0)
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 0)
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 1)
            dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize, 0)

            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, 0)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 0)  
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 0, 0)
            dpg.add_theme_style(dpg.mvStyleVar_ChildBorderSize, 1)
            dpg.add_theme_color(dpg.mvThemeCol_Border, child_bg_col)

with dpg.theme() as sb_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, sidebar_col) 
        dpg.add_theme_color(dpg.mvThemeCol_Button, sidebar_col)   


#show_demo()
dpg.show_style_editor()

apply_main_theme()
dpg.bind_item_theme(mainw, zero_theme)
dpg.bind_item_theme(side_bar, sb_theme)

apply_main_theme(tab1, True)
apply_main_theme(tab2, True)
apply_main_theme(tab3, True)

dpg.create_viewport(title = 'Simple ', width = W_WIDTH+16, height = W_HEIGHT+38)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(mainw, True)

dpg.set_viewport_resize_callback(auto_center_cb)

dpg.start_dearpygui()
dpg.destroy_context()