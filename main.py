import Day01
import Day02
import Day03
import Day04
import Day05
import Day06
import Day07
import Day08
import Day09
import Day10
import Day11
import Day12
import Day13
import Day14
import Day15
import Day16
import Day17
import Day18
import Day19
import Day20
import Day21
import Day22
import Day23
import Day24
import Day25
import time
from shutil import copyfile


def init():
    for i in range(2, 26):
        copyfile("Day01.py", f"Day{i:02d}.py")
        copyfile("Day01_Input.txt", f"Day{i:02d}_Input.txt")


def main():
    startTime = time.time()
    print(f"Start Time: {time.asctime(time.localtime(startTime))}")
    Day01.Part1("Day01_Input.txt")
    Day01.Part2("Day01_Input.txt")
    Day02.Part1("Day02_Input.txt")
    Day02.Part2("Day02_Input.txt")
    Day03.Part1("Day03_Input.txt")
    Day03.Part2("Day03_Input.txt")
    Day04.Part1("Day04_Input.txt")
    Day04.Part2("Day04_Input.txt")
    Day05.Part1("Day05_Input.txt")
    Day05.Part2("Day05_Input.txt")
    Day06.Part1("Day06_Input.txt")
    Day06.Part2("Day06_Input.txt")
    Day07.Part1("Day07_Input.txt")
    Day07.Part2("Day07_Input.txt")
    Day08.Part1("Day08_Input.txt")
    Day08.Part2("Day08_Input.txt")
    Day09.Part1("Day09_Input.txt")
    Day09.Part2("Day09_Input.txt")
    Day10.Part1("Day10_Input.txt")
    Day10.Part2("Day10_Input.txt")
    Day11.Part1("Day11_Input.txt")
    Day11.Part2("Day11_Input.txt")
    Day12.Part1("Day12_Input.txt")
    Day12.Part2("Day12_Input.txt")
    Day13.Part1("Day13_Input.txt")
    Day13.Part2("Day13_Input.txt")
    Day14.Part1("Day14_Input.txt")
    Day14.Part2("Day14_Input.txt")
    Day15.Part1("Day15_Input.txt")
    Day15.Part2("Day15_Input.txt")
    Day16.Part1("Day16_Input.txt")
    Day16.Part2("Day16_Input.txt")
    Day17.Part1("Day17_Input.txt")
    Day17.Part2("Day17_Input.txt")
    Day18.Part1("Day18_Input.txt")
    Day18.Part2("Day18_Input.txt")
    Day19.Part1("Day19_Input.txt")
    Day19.Part2("Day19_Input.txt")
    Day20.Part1("Day20_Input.txt")
    Day20.Part2("Day20_Input.txt")
    Day21.Part1("Day21_Input.txt")
    Day21.Part2("Day21_Input.txt")
    Day22.Part1("Day22_Input.txt")
    Day22.Part2("Day22_Input.txt")
    Day23.Part1("Day23_Input.txt")
    Day23.Part2("Day23_Input.txt")
    Day24.Part1("Day24_Input.txt")
    Day24.Part2("Day24_Input.txt")
    Day25.Part1("Day25_Input.txt")
    Day25.Part2("Day25_Input.txt")
    print(f"Execution Time: {time.time() - startTime:.3f}")


if __name__ == "__main__":
    # execute only if run as a script
    main()
