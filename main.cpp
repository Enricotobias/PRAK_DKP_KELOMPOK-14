#include <iostream>

using namespace std;

int main()
{
cout <<"\nIdentitas Kelompok :\n\n";
cout <<"RAMADHIN PUTRA FADHLI, 21120121140101, Kel.14, Shift 1 \n";
cout <<"SATRIA ADI PRATAMA, 21120121140154, Kel.14, Shift 1 \n";
cout <<"MUHAMMAD HAIDAR KHOLIL ATHALLAH, 21120121120036, Kel.14, Shift 1 \n";
cout <<"ENRICO TOBIAS, 21120121140113, Kel.14, Shift 1\n\n";

    string arr[2][4] =
{{"Mawar","Violet","Dendrum","Matahari"},{"500000","600000","650000","725000"}};
cout << "Harga Villa di Puncak" << endl;
cout << "==========================" << endl;
cout << "Villa " << arr[0][0] <<" seharga "<< arr[1][0] <<" rupiah per malam "<<endl;
cout << "Villa " << arr[0][1] <<" seharga "<< arr[1][1] <<" rupiah per malam "<<endl;
cout << "Villa " << arr[0][2] <<" seharga "<< arr[1][2] <<" rupiah per malam "<<endl;
cout << "Villa " << arr[0][3] <<" seharga "<< arr[1][3] <<" rupiah per malam "<<endl;
    return 0;
}
