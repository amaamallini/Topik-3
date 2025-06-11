import sys
import csv
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton,
    QTextEdit, QVBoxLayout, QWidget, QHBoxLayout, QAction, QMessageBox
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class AplikasiPasien(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Data Pasien")
        self.setGeometry(300, 100, 600, 500)
        self.data_pasien = []

        self.init_ui()
        self.init_menu()

    def init_ui(self):
        # Widget pusat
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        # ===== INPUT FORM =====
        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Nama Pasien")

        self.input_sakit = QLineEdit()
        self.input_sakit.setPlaceholderText("Keluhan Pasien")

        self.input_jam = QLineEdit()
        self.input_jam.setPlaceholderText("Jam Periksa (ex: 10:00)")

        main_layout.addWidget(QLabel("Form Input Pasien"))
        main_layout.addWidget(self.input_nama)
        main_layout.addWidget(self.input_sakit)
        main_layout.addWidget(self.input_jam)

        # ===== TOMBOL =====
        tombol_layout = QHBoxLayout()
        self.btn_tambah = QPushButton("➕ Tambah Pasien")
        self.btn_hapus = QPushButton("🗑 Hapus Semua")
        self.btn_simpan = QPushButton("💾 Simpan ke File")
        self.btn_muat = QPushButton("📂 Muat dari File")

        tombol_layout.addWidget(self.btn_tambah)
        tombol_layout.addWidget(self.btn_hapus)
        tombol_layout.addWidget(self.btn_simpan)
        tombol_layout.addWidget(self.btn_muat)

        main_layout.addLayout(tombol_layout)

        # ===== OUTPUT =====
        self.output_teks = QTextEdit()
        self.output_teks.setReadOnly(True)
        main_layout.addWidget(QLabel("📋 Daftar Pasien"))
        main_layout.addWidget(self.output_teks)

        # Event handling
        self.btn_tambah.clicked.connect(self.tambah_pasien)
        self.btn_hapus.clicked.connect(self.hapus_data)
        self.btn_simpan.clicked.connect(self.simpan_data)
        self.btn_muat.clicked.connect(self.muat_data)

        central_widget.setLayout(main_layout)

    def init_menu(self):
        # Menu Bar
        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu("File")
        exit_action = QAction("Keluar", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Help Menu
        help_menu = menu_bar.addMenu("Bantuan")
        about_action = QAction("Tentang", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def tambah_pasien(self):
        nama = self.input_nama.text().strip()
        sakit = self.input_sakit.text().strip()
        jam = self.input_jam.text().strip()

        if not nama or not sakit or not jam:
            QMessageBox.warning(self, "Input Tidak Lengkap", "Mohon isi semua kolom.")
            return

        self.data_pasien.append([nama, sakit, jam])
        self.update_output()
        self.input_nama.clear()
        self.input_sakit.clear()
        self.input_jam.clear()

    def update_output(self):
        self.output_teks.clear()
        for i, (nama, sakit, jam) in enumerate(self.data_pasien, 1):
            self.output_teks.append(f"{i}. Nama: {nama}, Sakit: {sakit}, Jam: {jam}")

    def hapus_data(self):
        if self.data_pasien:
            confirm = QMessageBox.question(
                self, "Konfirmasi", "Yakin ingin menghapus semua data?",
                QMessageBox.Yes | QMessageBox.No
            )
            if confirm == QMessageBox.Yes:
                self.data_pasien.clear()
                self.update_output()
        else:
            QMessageBox.information(self, "Info", "Data pasien masih kosong.")

    def simpan_data(self):
        try:
            with open("data_pasien.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Nama", "Sakit", "Jam"])
                writer.writerows(self.data_pasien)
            QMessageBox.information(self, "Berhasil", "Data berhasil disimpan ke file.")
        except Exception as e:
            QMessageBox.critical(self, "Gagal", f"Gagal menyimpan file: {e}")

    def muat_data(self):
        if not os.path.exists("data_pasien.csv"):
            QMessageBox.warning(self, "File Tidak Ada", "File data_pasien.csv tidak ditemukan.")
            return

        try:
            with open("data_pasien.csv", "r") as file:
                reader = csv.reader(file)
                next(reader)  # lewati header
                self.data_pasien = [row for row in reader]
                self.update_output()
            QMessageBox.information(self, "Berhasil", "Data berhasil dimuat dari file.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal memuat data: {e}")

    def show_about(self):
        QMessageBox.information(
            self,
            "Tentang Aplikasi",
            "🩺 Aplikasi Data Pasien\nDibuat dengan PyQt5\nFitur lengkap dan tampilan menyerupai aplikasi modern."
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AplikasiPasien()
    window.show()
    sys.exit(app.exec_())

