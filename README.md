# Travelling Salesman Problem With Ant Colony Algorithm
Project ini bertujuan untuk mencari jarak terpendek untuk menyelesaikan travelling salesman problem menggunakan Algoritma Koloni Semut

Optimasi Koloni Semut berasal dari perilaku semut ketika mereka mengangkut makanan dari sumber ke sarang mereka. Mereka menemukan jalur terpendek antara dua titik dengan meninggalkan feromon di sepanjang jalur mereka. Pada awalnya semut menjelajahi banyak jalur untuk mencapai tujuannya, tetapi karena feromon menguap, jalur dengan banyak feromon menunjukkan bahwa semut ada di sana beberapa waktu yang lalu, sehingga jalur ini mungkin lebih pendek dari yang lain. Metode ini dapat diterapkan untuk mencari solusi yang baik untuk Traveling Salesman Problem misalnya yang dikenal dengan NP-hard problem. Seperti ditekankan, itu tidak menyelesaikan masalah dengan menemukan solusi terbaik, (yang dapat diperoleh dengan menggunakan algoritma Held-Karp) tetapi memberikan solusi yang dapat diterima dalam waktu yang dapat diterima (pengguna memperbaiki jumlah iterasi) untuk masalah dimensi besar . 

Berikut adalah deskripsi singkat dari algoritma Koloni Semut: 

    1. Grafik diinisialisasi dengan meninggalkan nilai yang sama dari feromon pada setiap busur (setiap node dari masalah terkait dengan semua node yang tersisa), dan
    semut secara acak ditugaskan untuk salah satu simpul. 
    
    2. Pada setiap iterasi, setiap semut menemukan solusi untuk masalah tersebut, dengan melewati setiap node dan kembali ke node awal.
    
    3. Untuk memilih di kota mana semut harus pergi, sebuah probabilitas diberikan ke setiap busur, yang mewakili daya tariknya (kombinasi nilai feromon dan jaraknya).
    Busur kemudian dipilih dengan menggambar sampel dari hukum probabilitas ini. 
    
    4. Pada akhir iterasi, pheromone pada setiap busur diperbarui: 
        - beberapa pheromone dihilangkan karena menguap(evaporates)
        - beberapa pheromone ditambahkan, bergantung pada jarak total yang ditempuh oleh setiap semut: semakin kecil jaraknya, semakin besar pheromone yang ditambahkan             di jalurnya . 
        
    5. Kriteria penghentian adalah jumlah iterasi (dapat berupa fakta bahwa solusi terbaik tidak berkembang selama n iterasi.

Parameter penting : 
- nilai pheromone yang menguap(evaporates) pada setiap iterasi 
- parameter alpha yang mengontrol pentingnya pheromone selama pemilihan node berikutnya 
- parameter beta yang mengontrol pentingnya jarak busur selama pemilihan yang sama 

# Menyelesaikan TSP di Indonesia 

Saya menggunakan Streamlit untuk membangun visualisasi yang bagus, di mana bisa dengan mudah menentukan parameter dan memeriksa dampak mereka pada solusi. Persyaratan (hanya streamlit untuk saat ini) dapat diinstal dengan pip install -r requirements.txt Kemudian, aplikasi dapat diakses dengan menjalankan streamlit run main.py 

Berikut adalah screenshoot yang menunjukkan evolusi feromon pada setiap busur (garis hitam) , jalur terbaik saat ini (berwarna merah) dan konvergensi jarak.
![1](https://user-images.githubusercontent.com/84274028/214821419-c5143c5e-cca3-456a-a552-96317a0acfc8.JPG)

