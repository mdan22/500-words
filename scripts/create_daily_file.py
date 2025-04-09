import os
from datetime import datetime
import sys

class DailyWritingGenerator:
    def __init__(self, base_folder):
        """Initialize with the folder where files should be created."""
        self.base_folder = base_folder
        self.ensure_folder_exists()

    def ensure_folder_exists(self):
        """Create the base folder if it doesn't exist."""
        os.makedirs(self.base_folder, exist_ok=True)

    def get_current_day_number(self):
        """Calculate the next day number based on existing files."""
        existing_files = [f for f in os.listdir(self.base_folder) 
                         if f.startswith('day-') and f.endswith('.md')]
        
        if not existing_files:
            return 1
        
        # Extract numbers from existing files
        day_numbers = []
        for file in existing_files:
            try:
                number = int(file.replace('day-', '').replace('.md', ''))
                day_numbers.append(number)
            except ValueError:
                continue
        
        return max(day_numbers) + 1 if day_numbers else 1

    def file_created_today(self):
        """Check if a file was already created today."""
        today = datetime.now().date()
        
        for file in os.listdir(self.base_folder):
            if file.startswith('day-') and file.endswith('.md'):
                file_path = os.path.join(self.base_folder, file)
                file_date = datetime.fromtimestamp(os.stat(file_path).st_mtime).date()
                if file_date == today:
                    return True
        return False

    def create_daily_file(self):
        """Create the daily writing file if it hasn't been created today."""
        if self.file_created_today():
            return False

        day_number = self.get_current_day_number()
        filename = f"day-{day_number}.md"
        file_path = os.path.join(self.base_folder, filename)

        content = f"500 Words Challenge - Day {day_number}\n\n"
        
        with open(file_path, 'w') as f:
            f.write(content)
        
        return True

if __name__ == "__main__":
    # Get the project root directory (one level up from scripts folder)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    # Set writing folder to the "writing" subdirectory
    WRITING_FOLDER = os.path.join(project_root, "writing")
    
    generator = DailyWritingGenerator(WRITING_FOLDER)
    file_created = generator.create_daily_file()
    sys.exit(0 if file_created else 1)