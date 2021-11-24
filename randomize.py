import numpy as np
from typing import *

CHRZANY = {
    "Magda": "667442997",
    "Ela": "+48 609 384 665",
    "Staszek": "661 439 154",
    "Tomek": "607 160 108",
    "Paweł": "792 982 499",
}

MSG_FMT = '''Witaj, {giver}!
Twój numer bierze udział w świątecznej loterii CHRZANUJ ŚWIĘTA!
Nasz system wylosował dla Ciebie Chrzana o imieniu: {receiver}.
Mamy nadzieję, że masz cudowny pomysł na prezent dla {receiver}!

Jeśli chcesz poznać zasady poufności, wyślij SMS o treści REGULAMIN w odpowiedzi na ten numer ;)
'''

REGULAMIN = '''Losowanie zostało sporządzone i przeprowadzone przez niezależną Komisję Gier i Zakładów w składzie:
- Radosław Cymer
Losowanie zostało przeprowadzone RAZ w sposób zautomatyzowany, bez udziału osób trzecich a audyt kodu przed losowaniem odbył się pod przewodnictwem:
- Magdalena Chrzan
Tylko Komisja jest świadoma pełnego stanu losowania (z użyciem komputerowej magii) i jest zobowiązana do zachowania poufności pod karą chłosty.
Kod jest dostępny w publicznym repozytorium dostępnym po wysłaniu SMS o treści LOL.
Wszelkie wątpliwości można rozwiać udając się na Smolną 38, Warszawa, biuro czynne w piątki i soboty od godziny 23.
JAZDAAA.
'''

# jazd(a-z)jazd
def completely_random_and_unbiased_permutation_with_no_fixed_points_trust_me(n: int):
    perm = np.random.permutation(n)

    for i, k in enumerate(perm):
        if i == k:
            break
    else:
        return perm

    return completely_random_and_unbiased_permutation_with_no_fixed_points_trust_me(n)


def map_givers_and_receivers(keys: list[str], perm: list[int]):
    assert len(keys) == len(perm)
    return {k: keys[p] for k, p in zip(keys, perm)}


def format_messages(gib_rec_map: Dict[str, str]):
    for k,v in gib_rec_map.items():
        print("-"*40)
        print(CHRZANY[k])
        print(MSG_FMT.format(giver=k, receiver=v))
        print("-"*40)
        print()


def main():
    perm = completely_random_and_unbiased_permutation_with_no_fixed_points_trust_me(
        len(CHRZANY)
    )

    maź = map_givers_and_receivers(list(CHRZANY.keys()), perm)

    print(maź)

    format_messages(maź)


if __name__ == "__main__":
    main()
