import multtestlib
import functions


def main():
    for i in range(0, 20):
        with multtestlib.Pool(1) as pool:
            pool.starmap(multtestlib.test_func,
                         [(functions.slow_function, 1, '', 1),
                          (functions.slow_function, 2, '', 2),
                          (functions.slow_function, 3, '', 3),
                          (functions.slow_function, 4, '', 4),
                          (functions.slow_function, 5, '', 5),
                          (functions.slow_function, 6, '', 6),
                          (functions.slow_function, 7, '', 7),
                          (functions.slow_function, 8, '', 8),
                          (functions.slow_function, 9, '', 9),
                          (functions.slow_function, 10, '', 10),
                          (functions.slow_function, 11, '', 11),
                          (functions.slow_function, 12, '', 12),
                          (functions.slow_function, 13, '', 13),
                          (functions.slow_function, 14, '', 14),
                          (functions.slow_function, 15, '', 15),
                          (functions.slow_function, 16, '', 16),
                          (functions.slow_function, 17, '', 17),
                          (functions.slow_function, 18, '', 18),
                          (functions.slow_function, 19, '', 19),
                          (functions.slow_function, 20, '', 20),
                          (functions.slow_function, 21, '', 21),
                          (functions.slow_function, 22, '', 22),
                          (functions.slow_function, 23, '', 23),
                          (functions.slow_function, 24, '', 24),
                          (functions.slow_function, 25, '', 25),
                          (functions.slow_function, 26, '', 26),
                          (functions.slow_function, 27, '', 27),
                          (functions.slow_function, 28, '', 28),
                          (functions.slow_function, 29, '', 29),
                          (functions.slow_function, 30, '', 30),
                          (functions.slow_function, 31, '', 31),
                          (functions.slow_function, 32, '', 32),
                          (functions.slow_function, 33, '', 33),
                          (functions.slow_function, 34, '', 33),
                          (functions.slow_function, 35, '', 35),
                          (functions.slow_function, 36, '', 36),
                          (functions.slow_function, 37, '', 37),
                          (functions.slow_function, 38, '', 38),
                          (functions.slow_function, 39, '', 39),
                          (functions.slow_function, 40, '', 40),
                          (functions.slow_function, 41, '', 41),
                          (functions.slow_function, 42, '', 42),
                          (functions.slow_function, 43, '', 43),
                          (functions.slow_function, 44, '', 44),
                          (functions.slow_function, 45, '', 45),
                          (functions.slow_function, 46, '', 46),
                          (functions.slow_function, 47, '', 47),
                          (functions.slow_function, 48, '', 48),
                          (functions.slow_function, 49, '', 49),
                          (functions.slow_function, 50, '', 40),
                          (functions.slow_function, 51, '', 51),
                          (functions.slow_function, 52, '', 52),
                          (functions.slow_function, 53, '', 53),
                          (functions.slow_function, 54, '', 54),
                          (functions.slow_function, 55, '', 55),
                          (functions.slow_function, 56, '', 56),
                          (functions.slow_function, 57, '', 57),
                          (functions.slow_function, 58, '', 58),
                          (functions.slow_function, 59, '', 59),
                          (functions.slow_function, 60, '', 50),
                          (functions.slow_function, 61, '', 61),
                          (functions.slow_function, 62, '', 62),
                          (functions.slow_function, 63, '', 63),
                          (functions.slow_function, 64, '', 64),
                          (functions.slow_function, 65, '', 65),
                          (functions.slow_function, 66, '', 66),
                          (functions.slow_function, 67, '', 67),
                          (functions.slow_function, 68, '', 68),
                          (functions.slow_function, 69, '', 69),
                          (functions.slow_function, 70, '', 70),
                          (functions.slow_function, 71, '', 71),
                          (functions.slow_function, 72, '', 72),
                          (functions.slow_function, 73, '', 73),
                          (functions.slow_function, 74, '', 74),
                          (functions.slow_function, 75, '', 75),
                          (functions.slow_function, 76, '', 76),
                          (functions.slow_function, 77, '', 77),
                          (functions.slow_function, 78, '', 78),
                          (functions.slow_function, 79, '', 79),
                          (functions.slow_function, 80, '', 80),
                          (functions.slow_function, 81, '', 81),
                          (functions.slow_function, 82, '', 82),
                          (functions.slow_function, 83, '', 83),
                          (functions.slow_function, 84, '', 84),
                          (functions.slow_function, 85, '', 85),
                          (functions.slow_function, 86, '', 86),
                          (functions.slow_function, 87, '', 87),
                          (functions.slow_function, 88, '', 88),
                          (functions.slow_function, 89, '', 89),
                          (functions.slow_function, 90, '', 90),
                          (functions.slow_function, 91, '', 91),
                          (functions.slow_function, 92, '', 92),
                          (functions.slow_function, 93, '', 93),
                          (functions.slow_function, 94, '', 94),
                          (functions.slow_function, 95, '', 95),
                          (functions.slow_function, 96, '', 96),
                          (functions.slow_function, 97, '', 97),
                          (functions.slow_function, 98, '', 98),
                          (functions.slow_function, 99, '', 99),
                          (functions.slow_function, 100, '', 100),
                          ])


if __name__ == "__main__":
    multtestlib.init()
    multtestlib.freeze_support()
    main()
    multtestlib.end()
