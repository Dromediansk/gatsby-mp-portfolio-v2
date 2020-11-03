import subprocess as cmd


def commitAndPush(message):
    cmd.run(f"git commit -m '{message}'", check=True, shell=True)
    cmd.run("git push --set-upstream origin scripts",
            check=True, shell=True)


cmd.run("git add -A", check=True, shell=True)

defaultCommit = "update the repository"

defaultResponse = input(
    f"Do you want to use the default message for this commit? ('${defaultCommit}') ([y]/n)\n")

if defaultResponse.startswith('y'):
    commitAndPush(defaultCommit)

elif defaultResponse.startswith('n'):
    commit = input("What commit message do you want?\n")
    commitAndPush(commit)
else:
    correctionAnswer = input("Please provide a correct answer ([y]/n):")
    if correctionAnswer.startswith('n') or correctionAnswer.startswith('n'):
        commitAndPush(correctionAnswer)
