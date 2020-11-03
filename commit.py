import subprocess as cmd

cp = cmd.run("git add .", check=True, shell=True)

response = input(
    "Do you want to use the default message for this commit?([y]/n)\n")
message = "update the repository"

if response.startswith('n'):
    message = input("What message you want?\n")

cp = cmd.run(f"git commit -m '{message}'", check=True, shell=True)
cp = cmd.run("git push --set-upstream origin scripts", check=True, shell=True)
