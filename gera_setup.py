import cx_Freeze
executables = [
    cx_Freeze.Executable(script = "main.py", icon = "space.ico")
]
cx_Freeze.setup(
    name = "Space Marker",
    options = {
        "build_exe":{
            "packages":["pygame", "json", ""],
            "include_files":["bg.jpg", "star_list", "space.png", "Space_Machine_Power.mp3"]
        }
    }, executables = executables
)