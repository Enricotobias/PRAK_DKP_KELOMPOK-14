package com.example;

import java.util.*;
/*
Identitas Kelompok :
 RAMADHIN PUTRA FADHLI, 21120121140101, Kel.14 (Shift 1)
 SATRIA ADI PRATAMA, 21120121140154, Kel.14 (Shift 1)
 MUHAMMAD HAIDAR KHOLIL ATHALLAH, 21120121120036, Kel.14 (Shift 1)
 ENRICO TOBIAS, 21120121140113, Kel.14 (Shift 1)
 */
class TugasModul4_Kel14 {
        public static float hitung (float tugas, float uts, float uas){
                float total_nilai = (float) ((0.15 * tugas) + (0.35 * uts) + (0.50 * uas));
                return total_nilai;
        }
        public static void printNilai (String pelajaran){
                System.out.println("\nMasukkan nilai pelajaran " + pelajaran + " anda (0-100)");
        }
        static String cetakRapor () {
                return "\nRapor Nilai Akhir Semester Anda : " ;
        }

        public static void main(String[] args) {
                int[] nilai = new int[6];
                Scanner input = new Scanner(System.in);

                System.out.println("-----------------------------------------");
                System.out.println("|Simulasi Penilaian Rapor Akhir Semester|");
                System.out.println("-----------------------------------------");

                float hasil_IPA = 0, hasil_BIN = 0, hasil_IPS = 0, hasil_MAT =0, hasil_BI= 0;
