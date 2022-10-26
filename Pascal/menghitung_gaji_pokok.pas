program menghitung_gaji_pokok;
var
    tjg, mk, gapok, gatot: real;
begin
    write('masukan masa kerja anda : ');readln(mk);
    write('masukan gaji pokok anda : ');readln(gapok);
    if mk > 3 then
        tjg := 0.2 * gapok
    else
        tjg := 0.1 * gapok;
    gatot := gapok+tjg;
    writeln('gaji total anda adalah ', gatot:1:2);
    readln();
end.