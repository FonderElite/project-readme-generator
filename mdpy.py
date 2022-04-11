import time,os,platform
class Mdpy(object):
    def __init__(self) -> None:
        pass
    @staticmethod
    def banner(x) -> str:
        print(x,end="")
        print('''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✦ Github:https://github.com/FonderElite | Droid    ✦
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        ''')
        time.sleep(1.5)
        clear =  os.system("clear") if platform.system == "Windows" else os.system("cls")
        time.sleep(1)
        print(x)

    def simple_generate(self):
        proj_name = input("Project Name: ")
        demo_img = input("Demo Image src location: ")
        title_info = input("Info about " + proj_name + ": ")
        install_info = input("Info on how to install " + proj_name + ": ")
        usage_info = input("Instructions for usage: ")
        print("\n")
        file_content = f'''
# {proj_name}

{title_info}

# Project Demo

<img src="{demo_img}" align="center" width="650px">

## Installation

<p>{install_info}</p>

## Usage
<p>{usage_info}</p>

## Contributing 
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

'''
        with open("README.md","w+") as f:
            f.write(file_content)

        


if __name__ == '__main__':
    class_mdpy = Mdpy()
    banner = class_mdpy.banner('''
╔╦╗┌─┐┬─┐┬┌─┌┬┐┌─┐┬ ┬┌┐┌  ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
║║║├─┤├┬┘├┴┐ │││ │││││││  ║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
╩ ╩┴ ┴┴└─┴ ┴─┴┘└─┘└┴┘┘└┘  ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─
    ''')

    if os.path.isfile("README.md") == False:
        class_mdpy.simple_generate()
    elif os.path.isfile("README.md") == True:
        class_mdpy.simple_generate()
        print("README.md already exists...")
        time.sleep(1)
        print("Overwriting current README.md with new contents.")


