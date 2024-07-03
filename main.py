import os, time


def main():
    t0 = time.time_ns()
    print(os.listdir())
    print("Temps d'exécution : {} ns".format(time.time_ns() - t0))
    return


if __name__ == "__main__":
    main()
