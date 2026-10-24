import yaml
from psychopy import visual
from psychopy.hardware import keyboard

# Załadowanie ustawień z pliku .yaml: funkcja load_config
def load_config(file_name="config.yaml"):
    with open(file_name, encoding="utf-8") as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

_config_defaults = load_config()


#okienko z testem
win = visual.Window(
    size=_config_defaults["screen_size"],
    fullscr=_config_defaults["fullscr"],
    color=_config_defaults["screen_color"],
    units=_config_defaults["unit"],
    checkTiming=_config_defaults["checkTiming"]
)


#klawiatura
kb = keyboard.Keyboard()

#bodźce: bc: niebieskie koło, gc: zielone koło, bs: niebieski kwadrat, gs: zielony kwadrat
stim_bc = visual.Circle(win, radius=_config_defaults["circle_radius_1"], fillColor=_config_defaults["circle_color_1"], lineColor=None)
stim_gc = visual.Circle(win, radius=_config_defaults["circle_radius_2"], fillColor=_config_defaults["circle_color_2"], lineColor=None)

stim_bs = visual.Rect(win, width=_config_defaults["square_size_1"], height=_config_defaults["square_size_1"], fillColor=_config_defaults["square_color_1"], lineColor=None)
stim_gs = visual.Rect(win, width=_config_defaults["square_size_2"], height=_config_defaults["square_size_2"], fillColor=_config_defaults["square_color_2"], lineColor=None)


#na potrzeby innych funkcji składamy bodźce w listę
stim_list = [stim_bc, stim_gc, stim_bs, stim_gs]

#na potrzeby innych funkcji tworzymy słownik
stim_names = {
    stim_bc: "blue_circle",
    stim_gc: "green_circle",
    stim_bs: "blue_square",
    stim_gs: "green_square",
}


#Punkt fiksacji (biały krzyżyk)
fixation = visual.TextStim(win, text='+', color=_config_defaults["fixation_point_color"], height = _config_defaults["fixation_point_height"])


#  Wskazówki
cue_bg = visual.Rect(win, width=_config_defaults["cue_bg_width"], height=_config_defaults["cue_bg_height"], fillColor=_config_defaults["cue_bg_fillColor"], lineColor=_config_defaults["cue_bg_lineColor"], lineWidth=_config_defaults["cue_bg_lineWidth"])
cue_text_color = visual.TextStim(win, text='KOLOR', color=_config_defaults["cue_text_color_text_color"], height=_config_defaults["cue_text_color_height"], bold=_config_defaults["cue_text_color_isBold"])
cue_text_shape = visual.TextStim(win, text='KSZTAŁT', color=_config_defaults["cue_text_shape_text_color"], height=_config_defaults["cue_text_shape_height"], bold=_config_defaults["cue_text_shape_isBold"])


#  Feedback:
feedback_correct = visual.TextStim(win, text='✓', color=_config_defaults["feedback_correct_color"], height=_config_defaults["feedback_correct_height"])
feedback_incorrect = visual.TextStim(win, text='✗', color=_config_defaults["feedback_incorrect_color"], height=_config_defaults["feedback_incorrect_height"])
feedback_timeout = visual.TextStim(win, text='ZA WOLNO', color=_config_defaults["feedback_timeout_color"], height=_config_defaults["feedback_timeout_height"])


# Poprawne odpowiedzi
answers_color = {stim_bc: _config_defaults["key_2"], stim_gc: _config_defaults["key_1"], stim_bs: _config_defaults["key_2"], stim_gs: _config_defaults["key_1"]}
answers_shape = {stim_bc: _config_defaults["key_1"], stim_gc: _config_defaults["key_1"], stim_bs: _config_defaults["key_2"], stim_gs: _config_defaults["key_2"]}

intro_instructions = ["instructions/instrukcja_glowna1.txt",
                      "instructions/instrukcja_glowna2.txt",
                      "instructions/instrukcja_glowna3.txt",
                      "instructions/instrukcja_glowna4.txt"]