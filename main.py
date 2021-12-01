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
        copyfile("Day01Part1_Input.txt", f"Day{i:02d}Part1_Input.txt")
        copyfile("Day01Part2_Input.txt", f"Day{i:02d}Part2_Input.txt")


def main():
    startTime = time.time()
    Day01.Part1("Day01Part1_Input.txt")
    Day01.Part2("Day01Part2_Input.txt")
    Day02.Part1("Day02Part1_Input.txt")
    Day02.Part2("Day02Part2_Input.txt")
    Day03.Part1("Day03Part1_Input.txt")
    Day03.Part2("Day03Part2_Input.txt")
    Day04.Part1("Day04Part1_Input.txt")
    Day04.Part2("Day04Part2_Input.txt")
    Day05.Part1("Day05Part1_Input.txt")
    Day05.Part2("Day05Part2_Input.txt")
    Day06.Part1("Day06Part1_Input.txt")
    Day06.Part2("Day06Part2_Input.txt")
    Day07.Part1("Day07Part1_Input.txt")
    Day07.Part2("Day07Part2_Input.txt")
    Day08.Part1("Day08Part1_Input.txt")
    Day08.Part2("Day08Part2_Input.txt")
    Day09.Part1("Day09Part1_Input.txt")
    Day09.Part2("Day09Part2_Input.txt")
    Day10.Part1("Day10Part1_Input.txt")
    Day10.Part2("Day10Part2_Input.txt")
    Day11.Part1("Day11Part1_Input.txt")
    Day11.Part2("Day11Part2_Input.txt")
    Day12.Part1("Day12Part1_Input.txt")
    Day12.Part2("Day12Part2_Input.txt")
    Day13.Part1("Day13Part1_Input.txt")
    Day13.Part2("Day13Part2_Input.txt")
    Day14.Part1("Day14Part1_Input.txt")
    Day14.Part2("Day14Part2_Input.txt")
    Day15.Part1("Day15Part1_Input.txt")
    Day15.Part2("Day15Part2_Input.txt")
    Day16.Part1("Day16Part1_Input.txt")
    Day16.Part2("Day16Part2_Input.txt")
    Day17.Part1("Day17Part1_Input.txt")
    Day17.Part2("Day17Part2_Input.txt")
    Day18.Part1("Day18Part1_Input.txt")
    Day18.Part2("Day18Part2_Input.txt")
    Day19.Part1("Day19Part1_Input.txt")
    Day19.Part2("Day19Part2_Input.txt")
    Day20.Part1("Day20Part1_Input.txt")
    Day20.Part2("Day20Part2_Input.txt")
    Day21.Part1("Day21Part1_Input.txt")
    Day21.Part2("Day21Part2_Input.txt")
    Day22.Part1("Day22Part1_Input.txt")
    Day22.Part2("Day22Part2_Input.txt")
    Day23.Part1("Day23Part1_Input.txt")
    Day23.Part2("Day23Part2_Input.txt")
    Day24.Part1("Day24Part1_Input.txt")
    Day24.Part2("Day24Part2_Input.txt")
    Day25.Part1("Day25Part1_Input.txt")
    Day25.Part2("Day25Part2_Input.txt")
    print(f"Execution Time: {time.time() - startTime}")


if __name__ == "__main__":
    # execute only if run as a script
    main()
