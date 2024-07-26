# Wallpaper Changer

This project is a simple Python script that automatically changes your desktop wallpaper at regular intervals. The script selects a random wallpaper from a specified directory and sets it as the desktop background.

## Features

- Automatically changes the wallpaper at regular intervals (every 5 seconds by default).
- Supports `.jpg` and `.png` image formats.
- Uses the Windows API to set the desktop wallpaper.

## Requirements

- Python 3.x
- Libraries: `os`, `ctypes`, `random`, `schedule`, `time`, `Pillow` (PIL)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Bax-dev/wallpaper_project.git
    cd wallpaper-changer
    ```

2. **Install the required Python libraries:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Update the `wallpapers_dir` variable:**

    Edit the `wallpaper.py` file and set the `wallpapers_dir` variable to the path of your wallpapers directory.

    ```python
    wallpapers_dir = r"C:\Users\your-username\Documents\Wallpapers"
    ```

## Usage

1. **Run the script:**

    ```sh
    python wallpaper.py
    ```

    This will start the script and change the wallpaper every 5 seconds.

2. **Create an executable (optional):**

    To create a standalone executable that can run without needing Python installed, use PyInstaller:

    ```sh
    pip install pyinstaller
    pyinstaller --onefile wallpaper.py
    ```

    The executable will be located in the `dist` directory.

## Customization

- **Change the interval:**

    The script uses the `schedule` library to change the wallpaper every 5 seconds. You can customize this interval by modifying the `schedule.every(5).seconds.do(change_wallpaper)` line in the `wallpaper.py` file.

    ```python
    # Change wallpaper every minute
    schedule.every(1).minutes.do(change_wallpaper)
    ```

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Pillow](https://python-pillow.org/) for image processing.
- [Schedule](https://schedule.readthedocs.io/) for job scheduling.
