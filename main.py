import setup as stp
import tofile as tf
import experiment as exp
import time
from psychopy import core



def trial(single_training_n = stp._config_defaults["single_training_n"],
          # ilość bodźców wyświetlanych podczas treningu kolor i treningu kształt
          # (z load_config)
          single_trial_n = stp._config_defaults["single_trial_n"],
          # ilość bodźców wyświetlanych podczas próby kolor i próby kształt
          # (z load_config)
          mixed_training_n = stp._config_defaults["mixed_training_n"],
          # ilość bodźców wyświetlanych podczas treningu mieszanego
          # (z load_config)
          mixed_trial_n = stp._config_defaults["mixed_trial_n"]):
          # ilość bodźców wyświetlanych podczas próby mieszanej
          # (z load_config)

    # Utworzenie listy na wyniki prób

    results = []

    # INSTRUKCJA
    for i in stp.intro_instructions:
        exp.show_instruction(i)
        exp.wait_response()

    # TRENING KOLOR

    # Wyświetlenie informacji o rozpoczęciu treningu KOLOR

    exp.show_instruction("instructions/trening_kolor.txt")
    exp.wait_response()

    exp.single_run(single_training_n, "color", results = results, is_practice=True)


# ///////////////////////////////////////////////////

    #PRÓBA KOLOR

    # Wyświetlenie informacji o rozpoczęciu badania KOLOR
    exp.show_instruction("instructions/test_kolor.txt")
    exp.wait_response()

    exp.single_run(single_trial_n, "color", results = results)


# ///////////////////////////////////////////////////
    # TRENING KSZTAŁT

    # Wyświetlenie informacji o rozpoczęciu treningu KSZTAŁT
    exp.show_instruction("instructions/trening_ksztalt.txt")
    exp.wait_response()

    exp.single_run(single_training_n, "shape", results = results, is_practice=True)


# ///////////////////////////////////////////////////

    #PRÓBA KSZTAŁT

    # Wyświetlenie informacji o rozpoczęciu badania KSZTAŁT
    exp.show_instruction("instructions/test_ksztalt.txt")
    exp.wait_response()

    exp.single_run(single_trial_n, "shape", results = results)

    # Wyświetlenie informacji o zakończeniu badania KSZTAŁT

# ///////////////////////////////////////////////////
    # TRENING MIESZANE

    # Wyświetlenie informacji o rozpoczęciu treningu MIESZANE
    exp.show_instruction("instructions/trening_mieszane.txt")
    exp.wait_response()

    exp.mixed_run(mixed_training_n, results, is_practice=True)



# ///////////////////////////////////////////////////

    #PRÓBA MIESZANE

    # Wyświetlenie informacji o rozpoczęciu badania MIESZANE
    exp.show_instruction("instructions/test_mieszane.txt")
    exp.wait_response()

    exp.mixed_run(mixed_trial_n, results = results)

    # Wyświetlenie informacji o zakończeniu badania
    exp.show_instruction("instructions/text_end.txt")
# ///////////////////////////////////////////////////

    current_time = time.strftime("%Y%m%d-%H%M%S")
    unique_filename = f"results_{current_time}.csv"

    tf.save_tofile(results, unique_filename, "results")

if __name__ == "__main__":
    trial()
    stp.win.close()
    core.quit()