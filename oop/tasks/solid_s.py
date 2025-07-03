class PDFReport:
    def generate(self):
        print("PDF generated")

class FileReport:
    def save(self, filename):
        print(f"Saved {filename}")

class CustomReport(PDFReport, FileReport):
    def __init__(self, title, content):
        self.title = title
        self.content = content