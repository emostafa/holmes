# Holmes

Holmes is a small inspection tool to give you stats and insights about the programming files
you have written.

# Running the inspection tool

from the command line, go to the project directory, cd to "src" directory, then:
```
python app.py
```

# Results

The inspection tool loops through the directories in your home folder, counts
different type of programming languages files.

You should expect that looks like this:

    Inspecting your folders, please be patient...
    ('C', 6595)
    ('TypeScript', 5327)
    ('Java', 33)
    ('HTML', 8164)
    ('ELM', 0)
    ('Python', 4527)
    ('Kotlin', 0)
    ('Javascript', 467324)
    ('C++', 65)
    ('C#', 4)
    ('Shell', 452)
    ('CSS', 2584)
    ('Go', 1290)
    ('PHP', 11033)
    ('Ruby', 21090)
    ('Rust', 79)


# TODO

- Show graph of dates for each language, showing how many files was created on that specific date
- Show how many lines were written in every language
- Exclude hidden directories
