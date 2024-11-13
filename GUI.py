import tkinter as tk  # Mengimpor modul tkinter untuk GUI
from tkinter import messagebox  # Mengimpor messagebox dari tkinter untuk menampilkan pesan kesalahan

# Fungsi untuk mengambil nilai dari setiap kotak input dan melakukan validasi
def hasil_prediksi():
    try:
        # Iterasi setiap entry di list entries untuk mengambil nilai input
        for entry in entries:
            nilai = int(entry.get())  # Mengonversi nilai input ke integer
            # Memastikan nilai input berada dalam rentang 0 hingga 100
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        # Menampilkan hasil prediksi jika semua nilai valid
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        # Menampilkan pesan kesalahan jika ada input yang tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100")

# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Judul jendela
root.geometry("500x600")  # Ukuran jendela
root.configure(bg="#BF00FF")  # Warna latar belakang jendela

# Membuat label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Candara", 10, "bold"), bg="#BF00FF")
judul_label.pack(pady=20)  # Menambahkan padding di atas dan di bawah label

# Membuat frame untuk menampung input nilai
frame_input = tk.Frame(root, bg="#BF00FF")
frame_input.pack(pady=10)  # Padding antara frame dan elemen lain di jendela

# Membuat 10 kotak input untuk nilai mata pelajaran
entries = []  # List untuk menyimpan objek Entry (kotak input)
for i in range(10):
    # Membuat label untuk setiap mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", font=("Candara", 10, "bold"), bg="#BF00FF")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Menempatkan label dalam grid

    # Membuat kotak input untuk setiap mata pelajaran
    entry = tk.Entry(frame_input, width=10, font=("Candara", 10))
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menempatkan kotak input dalam grid
    entries.append(entry)  # Menambahkan kotak input ke dalam list entries

# Membuat tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Candara", 10, "bold"), bg="#BF00FF")
prediksi_button.pack(pady=30)  # Menambahkan padding antara tombol dan elemen lainnya

# Membuat label kosong untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Candara", 10, "italic", "bold"), fg="red", bg="#BF00FF")
hasil_label.pack(pady=20)  # Padding antara label hasil dan elemen lainnya

# Menjalankan aplikasi (event loop)
root.mainloop()
