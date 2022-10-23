program menghitung_energi_kinetik;
var 
    v, m: integer;
    ek: double;
begin
    writeln('Menghitung Energi Kinetik');
    write('Masukan massa benda (Kg) '); readln(m);
    write('Masukan kecepatan benda (m/s) '); readln(v);
    ek := 0.5*m*v*v;
    writeln('Energi kinetik benda dengan massa ',m,' dan kecepatan ',v,' adalah ',ek:5:2,' joule');
end.