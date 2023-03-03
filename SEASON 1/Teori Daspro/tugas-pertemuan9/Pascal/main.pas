program main;
uses sysutils;
// deklarasi variabel
var
    dataMahasiswa: array of array of string;
    tambah, nama, nim, prodi, tempatLahir, tanggallahir: string;
    i, n: integer;
begin
    // assignment data mahasiswa default
    n := 3;
    setlength(dataMahasiswa,5,n);
    dataMahasiswa[0][1]:='Yoga Agustiansyah'; dataMahasiswa[0][2]:='Udin Gambut';
    dataMahasiswa[1][1]:='2206050'; dataMahasiswa[1][2]:='2101234';
    dataMahasiswa[2][1]:='Teknik Informatika'; dataMahasiswa[2][2]:='Teknik Informatika';
    dataMahasiswa[3][1]:='Garut'; dataMahasiswa[3][2]:='Sumedang';
    dataMahasiswa[4][1]:='22 Agustus 2002'; dataMahasiswa[4][2]:='25 Desember 2002';
    // menampilkan data mahasiswa default
    writeln('       ---Daftar Mahasiswa---');
for i := 1 to n-1 do
    begin
        writeln(i);
        writeln('Nama                   : ', dataMahasiswa[0][i]);
        writeln('NIM                    : ', dataMahasiswa[1][i]);
        writeln('Program Studi          : ', dataMahasiswa[2][i]);
        writeln('Tempat, Tanggal Lahir  : ', dataMahasiswa[3][i], ', ', dataMahasiswa[4][i]);
        writeln();
    end;
    // konfirmasi apakah data mahasiswa ingin ditambah atau tidak
    write('Ingin menambah daftar mahasiswa(Y/t)? ');readln(tambah);
    tambah:=AnsiLowerCase(tambah);
    // penambahan data mahasiswa jika ingin ditambah
while tambah = 'y' do
    begin
        write('Masukan Nama             : ');readln(nama);
        write('Masukan NIM              : ');readln(nim);
        write('Masukan Program Studi    : ');readln(prodi);
        write('Masukan Tempat Lahir     : ');readln(tempatLahir);
        write('Masukan Tanggal Lahir    : ');readln(tanggallahir);
        writeln();
        dataMahasiswa[0][n] := nama;
        dataMahasiswa[1][n] := nim;
        dataMahasiswa[2][n] := prodi;
        dataMahasiswa[3][n] := tempatLahir;
        dataMahasiswa[4][n] := tanggallahir;
        n := n+1;
        // konfirmasi apakah data mahasiswa ingin ditambah lagi atau tidak
        write('Ingin menambah daftar mahasiswa lagi(Y/t)? ');readln(tambah);
        tambah:=AnsiLowerCase(tambah);
        writeln();
    end;
    // menampilkan data mahasiswa terbaru
    writeln('       ---Daftar Mahasiswa Baru---');
for i := 1 to n-1 do
    begin
        writeln(i);
        writeln('Nama                   : ', dataMahasiswa[0][i]);
        writeln('NIM                    : ', dataMahasiswa[1][i]);
        writeln('Program Studi          : ', dataMahasiswa[2][i]);
        writeln('Tempat, Tanggal Lahir  : ', dataMahasiswa[3][i], ', ', dataMahasiswa[4][i]);
        writeln();
    end;
end.