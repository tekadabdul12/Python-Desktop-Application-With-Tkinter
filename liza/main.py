from tkinter import *
import sqlite3
from tkinter import ttk
root = Tk()
root.title('Rumah Sakit')
root.geometry('1500x500')
conn = sqlite3.connect('Apotek.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS data (\n    no_Register text,\n    no_rekam_medis text,\n    nama text,\n    alamat text,\n    kota text,\n    Jenis_kelamin text,\n    tanggal_masuk text,\n    kelas_perawatan text,\n    golongan_darah text,\n    pendidikan text,\n    perkawinan text,\n    agama text\n    )\n    ')
conn.commit()
conn.close()
Mylabel1 = Label(root, text='Form Pendaftaran')

def update(rows):
    id = 1
    for x in tabel.get_children():
        tabel.delete(x)
    else:
        for i in rows:
            print(i)
            tabel.insert('', 'end', text=id, values=i)
            id += 1


def simpan():
    conn = sqlite3.connect('Apotek.db')
    c = conn.cursor()
    c.execute('INSERT INTO data VALUES (:entry1, :entry2, :entry3, :entry4, :entry5, :entry6, :entry7, :entry8, :entry9, :entry10, :entry11, :entry12)', {'entry1':entry1.get(),
     'entry2':entry2.get(),
     'entry3':entry3.get(),
     'entry4':entry4.get(),
     'entry5':entry5.get(),
     'entry6':entry6.get(),
     'entry7':entry7.get(),
     'entry8':entry8.get(),
     'entry9':entry9.get(),
     'entry10':entry10.get(),
     'entry11':entry11.get(),
     'entry12':entry12.get()})
    if entry1.get() == '':
        print('eror')
    else:
        conn.commit()
        tampil()
        conn.close()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    entry8.delete(0, END)
    entry9.delete(0, END)
    entry10.delete(0, END)
    entry11.delete(0, END)
    entry12.delete(0, END)


def hapus():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    entry8.delete(0, END)
    entry9.delete(0, END)
    entry10.delete(0, END)
    entry11.delete(0, END)
    entry12.delete(0, END)


def delete():
    conn = sqlite3.connect('Apotek.db')
    c = conn.cursor()
    c.execute('DELETE FROM data WHERE no_Register = :a', {'a': entry1.get()})
    hapus()
    conn.commit()
    tampil()
    conn.close()


def munculkan():
    hapus()
    selected = tabel.focus()
    values = tabel.item(selected, 'values')
    entry1.insert(0, values[0])
    entry2.insert(0, values[1])
    entry3.insert(0, values[2])
    entry4.insert(0, values[3])
    entry5.insert(0, values[4])
    entry6.insert(0, values[5])
    entry7.insert(0, values[6])
    entry8.insert(0, values[7])
    entry9.insert(0, values[8])
    entry10.insert(0, values[9])
    entry11.insert(0, values[10])
    entry12.insert(0, values[11])
    print(values)


def edit():
    conn = sqlite3.connect('Apotek.db')
    c = conn.cursor()
    c.execute('UPDATE data SET no_Register = :entry1, no_rekam_medis =:entry2 ,nama=:entry3,alamat=:entry4,kota=:entry5,Jenis_kelamin=:entry6,tanggal_masuk=:entry7,kelas_perawatan=:entry8,golongan_darah=:entry9,pendidikan=:entry10,perkawinan=:entry11,agama = :entry12 WHERE no_register = :entry1 ', {'entry1':entry1.get(),
     'entry2':entry2.get(),
     'entry3':entry3.get(),
     'entry4':entry4.get(),
     'entry5':entry5.get(),
     'entry6':entry6.get(),
     'entry7':entry7.get(),
     'entry8':entry8.get(),
     'entry9':entry9.get(),
     'entry10':entry10.get(),
     'entry11':entry11.get(),
     'entry12':entry12.get()})
    hapus()
    conn.commit()
    tampil()
    conn.close()


def click(e):
    munculkan()


def tampil():
    conn = sqlite3.connect('Apotek.db')
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    rows = c.fetchall()
    update(rows)
    conn.commit()
    conn.close()


button_ok = Button(root, text='Simpan', command=simpan, padx=8)
button_cancel = Button(root, text='Hapus', padx=10, command=delete)
button_tampil = Button(root, text='Tampil', command=tampil, padx=10)
button_edit = Button(root, text='Update data', command=edit, padx=10)
label_register = Label(root, text='No. Register', padx=20)
label_norekammedis = Label(root, text='rekam medis', padx=20)
label_NamaPasien = Label(root, text='NamaPasien', padx=20)
label_Alamat = Label(root, text='Alamat', padx=20)
label_Kota = Label(root, text='Kota', padx=20)
label_JenisKelamin = Label(root, text='Jenis kelamin', padx=20)
label_TanggalMasuk = Label(root, text='Tanggal Masuk', padx=20)
label_KelasPerawatan = Label(root, text='Kelas Perawatan', padx=20)
label_GolonganDarah = Label(root, text='Golongan Darah', padx=20)
label_Pendidikan = Label(root, text='Pendidikan', padx=20)
label_Perkwainan = Label(root, text='Perkawinan', padx=20)
label_Agama = Label(root, text='Agama', padx=20)
Label(root, text=':').grid(row=1, column=1)
Label(root, text=':').grid(row=2, column=1)
Label(root, text=':').grid(row=3, column=1)
Label(root, text=':').grid(row=4, column=1)
Label(root, text=':').grid(row=5, column=1)
Label(root, text=':').grid(row=6, column=1)
Label(root, text=':').grid(row=7, column=1)
Label(root, text=':').grid(row=8, column=1)
Label(root, text=':').grid(row=9, column=1)
Label(root, text=':').grid(row=10, column=1)
Label(root, text=':').grid(row=11, column=1)
Label(root, text=':').grid(row=12, column=1)
entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)
entry5 = Entry(root)
entry6 = Entry(root)
entry7 = Entry(root)
entry8 = Entry(root)
entry9 = Entry(root)
entry10 = Entry(root)
entry11 = Entry(root)
entry12 = Entry(root)
Mylabel1.grid(row=0, columnspan=18, pady=20, sticky='n')
label_register.grid(row=1, column=0, sticky='w')
label_norekammedis.grid(row=2, column=0, sticky='w')
label_NamaPasien.grid(row=3, column=0, sticky='w')
label_Alamat.grid(row=4, column=0, sticky='w')
label_Kota.grid(row=5, column=0, sticky='w')
label_JenisKelamin.grid(row=6, column=0, sticky='w')
label_TanggalMasuk.grid(row=7, column=0, sticky='w')
label_KelasPerawatan.grid(row=8, column=0, sticky='w')
Label(root, text=' ').grid(row=1, column=3, rowspan=7, padx=20)
label_GolonganDarah.grid(row=9, column=0, sticky='w')
label_Pendidikan.grid(row=10, column=0, sticky='w')
label_Perkwainan.grid(row=11, column=0, sticky='w')
label_Agama.grid(row=12, column=0, sticky='w')
button_ok.grid(row=14, column=0, pady=(40, 0))
button_edit.grid(row=15, column=0)
button_tampil.grid(row=14, column=2, pady=(40, 0))
button_cancel.grid(row=15, column=2)
button_ok.config(width=10)
button_cancel.config(width=10)
button_tampil.config(width=10)
entry1.grid(row=1, column=2)
entry2.grid(row=2, column=2)
entry3.grid(row=3, column=2)
entry4.grid(row=4, column=2)
entry5.grid(row=5, column=2)
entry6.grid(row=6, column=2)
entry7.grid(row=7, column=2)
entry8.grid(row=8, column=2)
entry9.grid(row=9, column=2)
entry10.grid(row=10, column=2)
entry11.grid(row=11, column=2)
entry12.grid(row=12, column=2)
tabel = ttk.Treeview(root, height=17)
tabel['column'] = ('No. register', 'rekam_medis', 'nama', 'Alamat', 'kota', 'JenisKelamin',
                   'tanggal', 'kelas', 'golongan_darah', 'pendidikan', 'perkawinan',
                   'agama')
tabel.column('#0', anchor=W, width=45)
tabel.column('No. register', anchor=CENTER, width=100)
tabel.column('rekam_medis', anchor=CENTER, width=100)
tabel.column('nama', anchor=CENTER, width=120)
tabel.column('Alamat', anchor=CENTER, width=100)
tabel.column('kota', anchor=CENTER, width=70)
tabel.column('JenisKelamin', anchor=CENTER, width=80)
tabel.column('tanggal', anchor=CENTER, width=100)
tabel.column('kelas', anchor=CENTER, width=50)
tabel.column('golongan_darah', anchor=CENTER, width=100)
tabel.column('pendidikan', anchor=CENTER, width=100)
tabel.column('perkawinan', anchor=CENTER, width=100)
tabel.column('agama', anchor=CENTER, width=60)
tabel.heading('#0', text='NO.')
tabel.heading('No. register', text='No. register')
tabel.heading('rekam_medis', text='Rekam Medis')
tabel.heading('nama', text='Nama')
tabel.heading('Alamat', text='Alamat')
tabel.heading('kota', text='kota')
tabel.heading('JenisKelamin', text='Jenis Kelamin')
tabel.heading('tanggal', text='tanggal')
tabel.heading('kelas', text='kelas')
tabel.heading('golongan_darah', text='golongan darah')
tabel.heading('pendidikan', text='pendidikan')
tabel.heading('perkawinan', text='perkawinan')
tabel.heading('agama', text='agama')
tabel.grid(row=1, rowspan=17, column=4, columnspan=15, pady=0)
tampil()
tabel.bind('<ButtonRelease-1>', click)
root.mainloop()