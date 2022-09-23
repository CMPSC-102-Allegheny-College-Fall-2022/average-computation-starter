# Computing Averages

## Assigned: Friday, September 23, 2022

## Due: Friday, September 30, 2022

## Project Goals

This programming project invites you to combine what you learned about the basics of Python programming to implement a useful program that computes the average of all of the numbers in a file that is provided as input to a program. The program will input the numerical values in a file, iterate through them, and return the average (i.e., arithmetic mean) of all the values. Along with adding documentation to the provided source code, you will create your own Python functions that use both iteration constructs and conditional logic to implement a correct program that passes the test suite and all checks. 

## Project Access

You can access this assignment by clicking the link provided to you in Discord or in the course schedule. Once you click this link it will create a GitHub repository that you can clone to your computer by using the `git clone` command to download the project from GitHub to your computer. Now you are ready to add source code and documentation to the project!

## Expected Output

This project invites you to implement a program called `average` that performs arithmetic. The program accepts through its command-line a file that contains integer values encoded as text. If you run the program with the command `poetry run average --dir input --file numbers.txt` it produces this output:

```
😃 Computing the average of numbers in a file called input/numbers.txt!

😉 Phew, that was hard work!

✨ The average of the input values is -0.95
```

Although this example shows the `average` program performing its computation with the `numbers.txt` file in the `input` directory, it should work in a general-purpose fashion for any text file that contains integer numbers aligned in a single row like:

```
-19
-24
-81
12
16
```

To learn more about how to run this program, you can type the command `poetry run average --help` to see the following output showing how to use `average`:

```shell
Usage: average [OPTIONS]

  Process a file by computing the average of all the numbers.

Options:
  --dir PATH
  --file PATH
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it
                        or customize the installation.

  --help                Show this message and exit.
```

Please note that the provided source code does not contain all of the functionality to produce this output. As explained in the next section, you should add all of the missing features to ensure that `average` produces the expected output. Once the program is working correctly, it should produce all of the expected output described in this section.

```
Don't forget that if you want to run the `average` program you must use your
terminal window to first go into the GitHub repository containing this
project and then go into the `average` directory that contains the project's
source code. Finally, remember that before running the program you must run
`poetry install` to add the dependencies.
```

## Adding Functionality

If you study the file `average/average/main.py` you will see that it has many `TODO` markers that designate the parts of the program that you need to implement before `average` will produce correct output. If you run the provided test suite with the command `poetry run task test` you will see that it produces output like the following:

```
    def test_average_computation_five_numbers():
        """Confirm that it is possible to average together five non-zero numbers."""
        number_list = """-72
            29
            61
            -42
            44"""
        average_value = main.compute_average(number_list)
>       assert average_value == ((-72 + 29 + 61 + -42 + 44) / 5)
E       assert 0 == (((((-72 + 29) + 61) + -42) + 44) / 5)
```

Note that this test case fails because of the fact that, by default, the `compute_average` function returns `0` instead of the correct arithmetic mean of the numbers specified in the `number_list` variable. You will need to add source code to the `compute_average` function so that it correctly calculates the average of the input values!

In summary, you should implement the following functions for the `average` program:

- `def compute_average(contents: str) -> float:`
- `def average(dir: Path = typer.Option(None), file: Path = typer.Option(None)) -> None:`

It is worth noting that the `compute_average` function accepts as input a `str` that is a one-number-per-line encoding of the file that contains the integer numbers. This means that `compute_average` will need to iterate through each line in the file and convert the text-based encoding of the number to an `int`. The `compute_average` function should also handle the circumstance in which the user-provided file (i.e., `numbers.txt`) does not have any numbers inside of it! If there were no numbers in the file, then the function can return `-1` to indicate that it did not compute an average. As you are finishing your implementation of the `compute_average` function, you should also ensure that, if all of the numbers inside of the file are `0`, then it returns an average of `0`.

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that it includes the following section that specifies different executable tasks:

```toml
[tool.taskipy.tasks]
black = { cmd = "black average tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 average tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy average", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle average tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint average tests", help = "Run the pylint checks for source code documentation" }
test = { cmd = "pytest -x -s", help = "Run the pytest test suite" }
test-silent = { cmd = "pytest -x --show-capture=no", help = "Run the pytest test suite without showing output" }
all = "task black && task flake8 && task pydocstyle && task pylint && task mypy && task test"
lint = "task black && task flake8 && task pydocstyle && task pylint"
```

This section makes it easy to run commands like `poetry run task lint` to automatically run all of the linters designed to check the Python source code in your program and its test suite. You can also use the command `poetry run task black` to confirm that your source code adheres to the industry-standard format defined by the `black` tool. If it does not adhere to the standard then you can run the command `poetry run black average tests` and it will automatically reformat the source code.

Along with running tasks like `poetry run task lint`, you can also check your submission using GatorGrade with the command `gatorgrade --config config/gatorgrade.yml`. If `gradle grade` shows that all checks pass, you will know that you made progress towards correctly implementing and writing about `average`.

If your program has all of the anticipated functionality, you can run the command `poetry run task test` and see that the test suite produces output like this:

```shell
collected 5 items

tests/test_average.py .....
```

You will know that the `compute_average` function correctly returns `0` when all of the inputs are `0` if the following test case passes:

``` python 
def test_average_computation_five_numbers_all_zero():
    """Confirm that it is possible to average together five zero numbers."""
    number_list = """0
        0
        0
        0
        0"""
    average_value = main.compute_average(number_list)
    assert average_value == 0
````

Lines `3` through `7` of this test case define the `number_list` variable as one
that contains a list of `0` values separated by newlines. The purpose of
`number_list` is to represent the string that would arrive from the input file
if a person ran the `average` program on the command-line. Line `8` of this test
case calls the `compute_average` function with the `number_list` as the input
and stores the output in a variable called `average_value`. Finally, line `9`
confirms that `compute_average` calculates the average of the input as `0`.

You will know that the `compute_average` function correctly returns `-1` when
there is no input to the function if the follow test case passes:

``` python 
def test_average_computation_no_provided_numbers():
    """Confirm that it is possible to average together no numbers."""
    number_list = ""
    average_value = main.compute_average(number_list)
    assert average_value == -1
```

On line `3` in the above source code, this test defines `number_list` as an empty string, denoted by `""`. Finally, on line `4` it calls the `compute_average` function with `number_list` as its input and on line `5` it confirms that the computed `average_value` is `-1`, as required by the specification of the function under test.

Once all of the test cases pass, you can run the all of the automated checks by typing `poetry run task all` in your terminal and confirming that there are no errors in the output. If all of the checks pass, then you can run the program with the command `poetry run average --dir input --file numbers.txt` and then confirm that it produces the expected output, including the average of `-0.95`.

## Project Reflection

Once you have finished all of the previous technical tasks, you can use a text editor to answer all of the questions in the `writing/reflection.md` file. For instance, you should provide the output of the Python program in a fenced code block, explain the meaning of the Python source code segments that you implemented and tested, compare and contrast different implementations of the Python function called `compute_average`, and answer all of the other questions about your experiences in completing this project. One specific goal for this reflection is to ensure that you understand how to accept as input the textual representation of a list of numbers, convert that to a list of numerical values, and then perform an average computation on those values.

## Submission

As you are working on your lab, you are to commit and push regularly. The commands are the following.

```bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 50%]:**: For the lab01 repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes. This is only checking some baseline writing and commit requirements as well as correct running of the program. An additional reduction will given if the commit log shows a cluster of commits at the end clearly used just to pass this requirement. An addition reduction will also be given if there is no commit during lab work times. All other requirements are evaluated manually.

- **Mastery of Technical Writing [up to 25%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 25%]**: Students will receive a portion of their assignment grade when their program implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this assignment. As a part of this grade, the instructor will assess aspects of the programming including, but not limited to, the completeness and the correctness of the program and the use of effective source code comments.

## Seeking Assistance

Students who have questions about this project outside of the lab time are invited to ask them in the course's Discord channel or during instructor's or TL's office hours.
