program teoremaPythagoras;
var a, b: integer;
sisiMiring: real;

begin
writeln('menghtung sisi miring segitiga siku-siku');
write('Masukan panjang sisi a ');readln(a);
write('Masukan panjang sisi b ');readln(b);
sisiMiring :=sqrt(sqr(a)+sqr(b));
writeln('Panjang sisi miring segitiga siku-siku dengan panjang sisi a ', a, ' dan panjang sisi b ', b, ' adalah ',sisiMiring:3:2);
end.