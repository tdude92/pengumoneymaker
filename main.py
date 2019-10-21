import sys
import subprocess
import platform
import time

scripts = ["appsetup", "goldminer"]

if __name__ == "__main__":
    try:
        script = sys.argv[1].strip("- ")
        with open("browser_pos.txt", "r") as rf:
            if rf.read() == "" and not script in ("appsetup", "scripts"):
                raise RuntimeError("Run 'python main.py -appsetup' before running main.py")

        if script == "scripts":
            print(',\n'.join(scripts))
        elif script in scripts:
            print("Quit by going to the console and typing Ctrl+C!\nRunning...\n")
            time.sleep(1)
            
            if platform.system() == "Windows":
                subprocess.run(["python", "scripts/" + script + ".py"])
            elif platform.system() == "Linux":
                subprocess.run(["python3", "scripts/" + script + ".py"])
            else:
                raise ValueError(platform.system() + " is not supported by pengumoneymaker.")
        else:
            raise ValueError("'" + script +"' is not a valid script.\nFor a list of scripts, type 'python main.py -scripts'.")
    except IndexError:
        print("To run this program, type 'python main.py <script-name>'.")
        print("For a list of scripts, type 'python main.py -scripts'.")
    except ValueError as error:
        print(error)
    except RuntimeError as error:
        print(error)