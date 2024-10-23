import os
import random
from tkinter import ttk, Toplevel, Tk, Button
from tkinter import font as tkFont  # Import font module from tkinter
from PIL import Image, ImageTk, ImageDraw, ImageFont
import pygame

def create_window(message):
    window = Toplevel()  # Use Toplevel() for child window
    window.title("Thông báo")
    
    # Create a new image for the text
    img = Image.new("RGB", (300, 100), color='#FFB6C1')
    
    # Load the custom font
    font_path = os.path.join(os.path.dirname(__file__), 'font', 'UVNVAN_B.ttf')  # Change the path to your font file
    try:
        font = ImageFont.truetype(font_path, 24)
    except OSError:
        print(f"Font not found at {font_path}, using default font.")
        font = ImageFont.load_default()

    # Draw text on the image with the custom font
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), message, font=font, fill=(255, 255, 255))
    
    # Convert the image to tkinter PhotoImage
    tk_image = ImageTk.PhotoImage(img)
    
    # Display image in label
    label = ttk.Label(window, image=tk_image)
    label.image = tk_image  # Keep a reference to avoid garbage collection
    label.pack(padx=20, pady=20)
    
    # Randomly position the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Random position ensuring the window is fully on the screen
    random_x = random.randint(0, screen_width - 300)  # 300 is the window width
    random_y = random.randint(0, screen_height - 200)  # Adjusted height for the image
    
    window.geometry(f'300x200+{random_x}+{random_y}')  # Set the window size and position

def create_window_image():
    """Load a random image from the 'images' folder and display it in the window."""
    window = Toplevel()  # Use Toplevel() for child window
    window.title("Hình ảnh em")
    images_folder = os.path.join(os.path.dirname(__file__), 'images')
    images = [img for img in os.listdir(images_folder) if img.endswith(('png', 'jpg', 'jpeg', 'gif'))]
    
    if images:
        random_image = random.choice(images)
        image_path = os.path.join(images_folder, random_image)
        
        # Open the image
        img = Image.open(image_path)
        
        # Resize the image to fit in the window while maintaining the aspect ratio
        max_size = (300, 200)  # Set your desired maximum size
        img.thumbnail(max_size)  # Resize while maintaining aspect ratio, using default resampling method
        
        tk_image = ImageTk.PhotoImage(img)
        
        # Display the image in a label
        label_image = ttk.Label(window, image=tk_image)
        label_image.image = tk_image  # Keep a reference to avoid garbage collection
        label_image.pack(padx=10, pady=10)  # Add padding above and below
        
        # Set the window size based on the resized image
        img_width, img_height = img.size
        window.geometry(f'{img_width}x{img_height + 50}')  # Add some space for the label
        window.update_idletasks()  # Update the window size
    else:
        # If no images are found, just create an empty label
        label_image = ttk.Label(window)  # Empty label for image
        label_image.pack(padx=10, pady=(0, 10))
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Random position ensuring the window is fully on the screen
    random_x = random.randint(0, screen_width - 300)  # 300 is the window width
    random_y = random.randint(0, screen_height - 200)  # Adjusted height for the image
    
    window.geometry(f'{img_width}x{img_height}+{random_x}+{random_y}') 

def create_windows(count=200, delay=200):
    if count > 0:
        create_window("Anh nhớ em!")
        create_window_image()
        root.after(delay, create_windows, count - 1, delay)

def start_creating_windows():
    # Initialize pygame for audio playback
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "tranbonho.wav"))
    pygame.mixer.music.play()
    
    create_windows()

def quit_program(event=None):
    """Handle quitting the program when Ctrl+Q is pressed."""
    root.quit()

# Create main application window
root = Tk()
root.title("Hello em!")
root.geometry("600x400")
root.resizable(False, False)

# Bind the Ctrl+Q shortcut to quit the program
root.bind('<Control-q>', quit_program)

# Center the window on the screen
x = (root.winfo_screenwidth() // 2) - 300
y = (root.winfo_screenheight() // 2) - 300
root.geometry(f'600x400+{x}+{y}')

# Set background image
bg_image_path = os.path.join(os.path.dirname(__file__), 'bg.jpg')
bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((600, 400), Image.LANCZOS))
ttk.Label(root, image=bg_image).place(relwidth=1, relheight=1)

# Use `tkFont` to set font for Button
custom_font = tkFont.Font(family="Helvetica", size=24, weight="bold")  # You can adjust the font as needed

# Create a custom button using `tk.Button` (for background color support)
start_button = Button(root, text="Start", fg="white", font=custom_font, bg="#FF69B4", command=start_creating_windows)
start_button.place(x=250, y=300)

# Start the Tkinter main loop
root.mainloop()
