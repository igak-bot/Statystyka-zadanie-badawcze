import setup as stp
import random

# Losowanie bodźców: funkcja make_stim_list
def make_stim_list(n, mixed_trial=False):
    # m to wielokrotność liczby 4 (dla równego podziału)
    m = n - (n % 4)

    while True:
        # ustawiamy bazowe limity dla każdego bodźca
        quota = {s: m // 4 for s in stp.stim_list}

        # jeśli n nie dzieli się idealnie przez 4, dodajemy losowe unikalne bodźce jako dopełnienie
        if n % 4 != 0:
            extra_opts = random.sample(stp.stim_list, n % 4)
            for s in extra_opts:
                quota[s] += 1

        stim_queue = []
        failed = False

        for _ in range(n):
            # filtrujemy bodźce, które mają jeszcze wolną kwotę (częstość > 0)
            available = [s for s, q in quota.items() if q > 0]

            # zapobiegamy powtórzeniom pod rząd (usuwamy ostatnio dodany bodziec z dostępnych opcji)
            if stim_queue:
                available = [s for s in available if s != stim_queue[-1]]

            # jeśli wpadliśmy w ślepy zaułek (brak alternatywnych opcji), przerywamy i losujemy od nowa
            if not available:
                failed = True
                break

            chosen = random.choice(available)
            stim_queue.append(chosen)
            quota[chosen] -= 1

        # jeśli udało się wygenerować całą listę bez błędu, wychodzimy z pętli while
        if not failed:
            break

    # losujemy n czasów wyświetlania się punktów fiksacji
    focus_times = [random.randint(400, 700) for _ in range(n)]

    # sekcja dla prób mieszanych
    if mixed_trial:
        l = (n - 1) - (n - 1) % 2
        switch_opts = [True, False]
        switch_queue = []
        switch_quota = {}
        trial_type_queue = []

        for i in switch_opts:
            switch_quota[i] = l / 2

        switch_queue.append(random.choice(switch_opts))
        switch_quota[switch_queue[0]] = switch_quota[switch_queue[0]] - 1

        for i in range(l - 1):
            if switch_quota[switch_queue[i]] == 0:
                if switch_queue[i] in switch_opts:
                    switch_opts.remove(switch_queue[i])
            switch_queue.append(random.choice(switch_opts))
            switch_quota[switch_queue[i + 1]] = switch_quota[switch_queue[i + 1]] - 1

        if l != n - 1:
            switch_opts = [True, False]
            switch_queue.append(random.choice(switch_opts))

        trial_type_queue.append(random.choice(["color", "shape"]))

        for switch in switch_queue:
            if switch:
                if trial_type_queue[-1] == "color":
                    trial_type_queue.append("shape")
                else:
                    trial_type_queue.append("color")
            else:
                if trial_type_queue[-1] == "color":
                    trial_type_queue.append("color")
                else:
                    trial_type_queue.append("shape")

        switch_queue.insert(0, None)

        return stim_queue, focus_times, switch_queue, trial_type_queue

    else:
        return stim_queue, focus_times


# Podsumowując, funkcja zwraca:
    # listę bodźców stim_queue
    # listę czasów wyświetlania punktów fiksacji focus_times
    # w próbach mieszanych:
        # listę pomocniczą switch_queue
        # listę typów prób trial_type_queue