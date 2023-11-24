import cx_Freeze
executables = [
    cx_Freeze.Executable(script = "main.py", icon = "space.ico")
]
cx_Freeze.setup(
    name = "Space Marker",
    options = {
        "build_exe":{
            "packages":["pygame", "tkinter", "ast", "math"],
            "include_files":["bg.jpg", "SalvarPontos.txt", "space.png", "Space_Machine_Power.mp3"]
        }
    }, executables = executables
)