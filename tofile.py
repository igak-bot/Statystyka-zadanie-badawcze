import setup as stp
import os
import pandas as pd

global_trial_number = 0

def save_data(result_list, block_name, stim, trial_type, is_switch, trial_results):
    global global_trial_number
    global_trial_number += 1

    if is_switch is None:
        transition = "NA"
    elif is_switch:
        transition = "SWITCH"
    else:
        transition = "REPEAT"

    congruency = "congruent" if stp.answers_color[stim] == stp.answers_shape[stim] else "incongruent"

    individual_result = {
        "Trial_Number": global_trial_number,
        "Block_Name": block_name,
        "Transition": transition,
        "Cue_Type": trial_type,
        "Stimulus": stp.stim_names[stim],
        "Congruency": congruency,
        "Reaction_Time_ms": trial_results["rt"],
        "Correct": trial_results["correct_answer"],
        "Timeout": not trial_results["answered"],
        "Response_Key": trial_results["response_key"]
    }

    result_list.append(individual_result)



# do zarejestrowania:
    # numer kolejny próby w skali całego eksperymentu (od 1 do 200)
    # nazwa i typ aktualnej części badania
    # typ próby w kolejnych trialach (REPEAT/SWITCH)
    # rodzaj zaprezentowanego sygnału wskazującego aktualną regułę
    # cechy prezentowanego bodźca docelowego
    # stopień zgodności mapowania odpowiedzi (kongruentna/niekongruentna)
    # czas reakcji osoby badanej liczony od momentu pojawienia się bodźca
    # poprawność udzielonej odpowiedzi (lub przekroczenie czasu/timeout)
    # rodzaj udzielonej reakcji ("D"/"K")

def save_tofile(result_list,
              file_name,
              path = 'results'):
    os.makedirs(path, exist_ok=True)
    df = pd.DataFrame(result_list)
    df.to_csv(os.path.join(path, file_name), index=False)

    # Zapisuje wynik do pliku