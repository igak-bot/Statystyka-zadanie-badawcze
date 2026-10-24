from psychopy.event import clearEvents

import setup as stp
import stimuli as stm
import checking as chk
import tofile as tf
from psychopy import visual, core, event
import os

def single_run(n, trial_type, results, is_practice = False):
    stims, focus_times = stm.make_stim_list(n, mixed_trial=False)
    for i in range(n):
        stim = stims[i]
        focus_time = focus_times[i]
        answered = False
        correct_answer = False
        if is_practice:
            chk.check_correct(stim=stim, trial_type=trial_type, focus_time=focus_time, is_mixed=False)
            chk.give_feedback()
        else:
            trial_results = chk.check_correct(stim=stim, trial_type=trial_type, focus_time=focus_time, is_mixed=False)
            tf.save_data(result_list=results, block_name=f"Single_{trial_type}", stim=stim, trial_type=trial_type,
                      is_switch=False, trial_results=trial_results)

def mixed_run(n, results, is_practice = False):
    stims, focus_times, switch_queue, trial_types = stm.make_stim_list(n, mixed_trial=True)
    for i in range(n):
        stim = stims[i]
        focus_time = focus_times[i]
        trial_type = trial_types[i]
        answered = False
        correct_answer = False
        is_sw = switch_queue[i]
        if is_practice:
            chk.check_correct(stim=stim, trial_type=trial_type, focus_time=focus_time, is_mixed=True)
            chk.give_feedback()
        else:
            trial_results = chk.check_correct(stim=stim, trial_type=trial_type, focus_time=focus_time, is_mixed=True)
            tf.save_data(result_list=results, block_name="Mixed_Block", stim=stim, trial_type=trial_type, is_switch=is_sw,
                      trial_results=trial_results)


def show_instruction(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = f"Instrukcja z pliku '{file_name}'\n\nNaciśnij dowolny klawisz, aby kontynuować."

    height = 24

    instr_stim = visual.TextStim(stp.win, text=text_content, color='white', height=height,
        wrapWidth=800, alignText='center')
    instr_stim.draw()

    stp.win.flip()

# Wyświetlenie instrukcji

def wait_response():
    stp.kb.clearEvents()
    event.waitKeys(keyList=['space'])  # Oczekiwanie na reakcję użytkownika
    stp.win.flip()
    core.wait(0.5)