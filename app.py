import streamlit as st
from PIL import Image, ImageDraw

# Function to generate a simple image of a robot
def generate_robot_image():
    # Create a blank image with white background
    img = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw the robot's body
    draw.rectangle([50, 50, 150, 150], fill='gray', outline='black')
    
    # Draw the robot's head
    draw.rectangle([75, 20, 125, 70], fill='gray', outline='black')
    
    # Draw the robot's eyes
    draw.ellipse([85, 30, 95, 40], fill='black')
    draw.ellipse([105, 30, 115, 40], fill='black')
    
    # Draw the robot's mouth
    draw.rectangle([90, 50, 110, 55], fill='black')
    
    return img

# Function to generate a simple image of a cat
def generate_cat_image():
    # Create a blank image with white background
    img = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw the cat's body
    draw.ellipse([50, 100, 150, 180], fill='orange', outline='black')
    
    # Draw the cat's head
    draw.ellipse([75, 50, 125, 100], fill='orange', outline='black')
    
    # Draw the cat's ears
    draw.polygon([75, 50, 85, 20, 95, 50], fill='orange', outline='black')
    draw.polygon([125, 50, 115, 20, 105, 50], fill='orange', outline='black')
    
    # Draw the cat's eyes
    draw.ellipse([85, 60, 95, 70], fill='black')
    draw.ellipse([105, 60, 115, 70], fill='black')
    
    # Draw the cat's mouth
    draw.line([100, 75, 100, 85], fill='black')
    draw.arc([90, 80, 110, 90], start=0, end=180, fill='black')
    
    return img

# Streamlit interface
st.title("Image Generator")

# User input for the type of image to generate
image_type = st.selectbox("Select the type of image to generate", ["Robot", "Cat"])

# Generate and display the image based on user input
if st.button("Generate Image"):
    if image_type == "Robot":
        img = generate_robot_image()
    elif image_type == "Cat":
        img = generate_cat_image()
    
    st.image(img, caption=f"Generated {image_type} Image")
