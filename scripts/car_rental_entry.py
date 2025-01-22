import sys
import os

# Get the absolute path of the project root and add 'src' to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.normpath(os.path.join(current_dir, "..", "src"))  # Cross-platform path handling
sys.path.insert(0, src_path)  # Ensure 'src' is in sys.path

from rental_services.login import login  # Now it should work

def main():
    """Main function for car rental script."""
    print("Starting Car Rental Application...")
    login()

if __name__ == "__main__":
    main()
