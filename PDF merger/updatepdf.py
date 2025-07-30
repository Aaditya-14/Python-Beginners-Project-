import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger Tool")
        self.root.geometry("400x300")
        self.pdf_files = []

        # Heading
        tk.Label(root, text="Merge Your PDF Files", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Select button
        self.select_btn = tk.Button(root, text="Select PDF Files", command=self.select_pdfs)
        self.select_btn.pack(pady=10)

        # Listbox to show selected PDFs
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        # Merge button
        self.merge_btn = tk.Button(root, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_btn.pack(pady=10)

    def select_pdfs(self):
        files = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF Files", "*.pdf")])
        if files:
            self.pdf_files = files
            self.listbox.delete(0, tk.END)
            for file in self.pdf_files:
                self.listbox.insert(tk.END, file.split("/")[-1])

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showerror("No Files", "Please select at least two PDF files to merge.")
            return

        merger = PdfWriter()
        for pdf in self.pdf_files:
            merger.append(pdf)

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Save Merged PDF As")
        if save_path:
            merger.write(save_path)
            merger.close()
            messagebox.showinfo("Success", f"PDFs merged and saved as:\n{save_path}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
