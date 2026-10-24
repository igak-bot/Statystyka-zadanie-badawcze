import setup as stp
from psychopy import core

def check_correct(stim, trial_type, focus_time, is_mixed, reaction_time=1500, cue_time=600):
    global answered, correct_answer, rt, response_key

    stp.kb.clearEvents()

    stp.fixation.draw()
    stp.win.flip()
    core.wait(focus_time / 1000.0)

    if is_mixed:
        stp.cue_bg.draw()
        if trial_type == "color":
            stp.cue_text_color.draw()
        else:
            stp.cue_text_shape.draw()
        stp.win.flip()
        core.wait(cue_time / 1000.0)

    stim.draw()
    stp.win.flip()

    stp.kb.clock.reset()

    keys = stp.kb.waitKeys(maxWait=reaction_time / 1000.0, keyList=['d', 'k'], waitRelease=False)

    if keys:
        answered = True
        response_key = keys[0].name
        rt = keys[0].rt * 1000.0

        if trial_type == "color":
            correct_key = stp.answers_color[stim]
        else:
            correct_key = stp.answers_shape[stim]

        if response_key == correct_key:
            correct_answer = True
        else:
            correct_answer = False
    else:
        answered = False
        correct_answer = False
        response_key = None
        rt = None
    return {
        "answered": answered,
        "correct_answer": correct_answer,
        "rt": rt,
        "response_key": response_key
    }


# Czekamy na odpowiedź przez zadany czas (reaction_time)

# Funkcja zwraca zmienne:
# answered - czy odpowiedź została udzielona (True/False)
# correct_answer - czy udzielona odpowiedź jest poprawna (True/False)


def give_feedback():
    global answered, correct_answer
    if not answered:
        stp.feedback_timeout.draw()
    elif correct_answer:
        stp.feedback_correct.draw()
    else:
        stp.feedback_incorrect.draw()

    stp.win.flip()
    core.wait(0.5)
    stp.win.flip()
    core.wait(0.5)

    # Funkcja wyświetla odpowiedni feedback:
    # answered = False: ZA WOLNO
    # answered = True i correct_answer = False: ŹLE
    # answered = True i correct_answer = True: DOBRZE