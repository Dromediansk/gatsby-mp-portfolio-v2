import subprocess as cmd


def commitAndPush(message):
    cmd.run(f"git commit -m '{message}'", check=True, shell=True)
    cmd.run("git push --set-upstream origin scripts",
            check=True, shell=True)


cmd.run("git add -A", check=True, shell=True)

defaultResponse = input(
    "Do you want to use the default message for this commit? ('update the repository') ([y]/n)\n")
message = "update the repository"

if defaultResponse.startswith('y'):
    commitAndPush(defaultResponse)

elif defaultResponse.startswith('n'):
    message = input("What message you want?\n")
    commitAndPush(message)
else:
    correctionAnswer = input("Please provide a correct answer ([y]/n):")
    if correctionAnswer.startswith('n') or correctionAnswer.startswith('n'):
        commitAndPush(correctionAnswer)
