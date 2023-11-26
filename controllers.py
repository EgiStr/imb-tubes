from component import component_html_detail, component_html_list
import streamlit as st
import pandas as pd
from utils import get_preview_image, upload_image_to_folder

class Auth:
    def __init__(self):
        self.username = "admin"
        self.password = "bukain123"

        
    def login(self):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == self.username and password == self.password:
                st.session_state["authentication_status"] = True
                st.session_state["name"] = username
                st.success("Login Success")
                st.balloons()
                st.session_state["route"] = "dashboard"
                st.rerun()
            else:
                st.error("Username or Password is wrong")
                st.session_state["authentication_status"] = False
                st.session_state["name"] = None

    def logout(self):
        st.session_state["authentication_status"] = False
        st.session_state["name"] = None
        st.session_state["route"] = "Home"
        st.success("Logout Success")
        st.balloons()
        st.rerun()
       


class ListDataController:
    def __init__(self, crud,auth):
        self.crud = crud
        self.auth = auth

    def detail_data(self):
        data = self.crud.detail_data(st.session_state["index"])
        st.write(component_html_detail(data, st.session_state["index"]))
        self.add_comment()
        self.show_comment(data)
 
    def show_comment(self, data):
        # check if comment is not None and comment is not empty
        if pd.isna(data[8]) or data[8] == "":
            # split comment by comma
            comments = []
        else:
            comments = data[8].split(",")
        # reverse comment to show the latest comment
        comments.reverse()

        for comment in comments:
            st.write(comment)
            st.write("=========================================")
            st.write("")

    def add_comment(self):
        st.subheader("Tambah Komentar")
        comment = st.text_input("Komentar")
        if st.button("Submit"):
            self.crud.add_comment(st.session_state["index"], comment)
            st.success("Komentar Ditambahkan")
            st.balloons()
            st.rerun()

    def list_data(self):
        # check if route is Home then show list of data
        if st.session_state["route"] == "Home":
            st.subheader("List Data")
            data = self.crud.df
            # filter data description
            filter = st.text_input("Filter")
            if filter != "":
                data = data[data.iloc[:, 2].str.contains(filter)]

            category = st.selectbox("Category", ["All", "Penemuan", "Kehilangan"])
            if category != "All":
                data = data[data.iloc[:, 6] == category]

            location = st.selectbox("Location", ["All"] + self.crud.location)
            if location != "All":
                data = data[data.iloc[:, 4] == location]

            for num, (i, row) in enumerate(data.iterrows()):
                # create layout to show list of data with 3 column 5 row
                if num % 3 == 0:
                    col1, col2, col3 = st.columns(3)

                if num % 3 == 0:
                    with col1:
                        component_html_list(row, i)
                        # create button to open modal
                        if st.button(f"Open{i}"):
                            st.session_state["index"] = i
                            st.session_state["route"] = "Detail Laporan"

                elif num % 3 == 1:
                    with col2:
                        component_html_list(row, i)
                        if st.button(f"Open{i}"):
                            st.session_state["index"] = i
                            st.session_state["route"] = "Detail Laporan"

                elif num % 3 == 2:
                    with col3:
                        component_html_list(row, i)
                        if st.button(f"Open{i}"):
                            st.session_state["index"] = i
                            st.session_state["route"] = "Detail Laporan"

    def add_data(self):
        st.subheader("Tambah Data")
        image = st.file_uploader("Image", type=["png", "jpeg", "jpg"])

        if image is not None:
            image_html = get_preview_image(image)
            st.write(image_html, unsafe_allow_html=True)

        img = upload_image_to_folder(image)

        description = st.text_input("Description")
        location = st.selectbox("Location", self.crud.location)
        date = st.date_input("Date")
        contactPerson = st.text_input("Contact Person")
        category = st.selectbox("Category", self.crud.category)
        if category == "Penemuan":
            st.write("""Untuk menjaga barang-barang yang ditemukan dengan tepat, diharapkan kepada pengguna website untuk aktif bertanya kepada orang yang menemukan barang tersebut. Berkomunikasi dengan pertanyaan yang tepat dapat membantu identifikasi pemilik asli dan memastikan barang tersebut kembali ke tangan yang benar. Gunakan pertanyaan seperti "Apakah ada tanda pengenal di dalamnya?" atau "Bisakah Anda memberikan deskripsi lebih lanjut mengenai barang yang Anda temukan?" Untuk menghindari kehilangan barang yang bernilai, melibatkan diri dalam proses pertanyaan dapat menjadi langkah yang sangat penting dan edukatif.""")
        elif category == "Kehilangan":
            st.write("""
1. Laporkan Kehilangan dengan Detail:
    Beri pengguna informasi tentang pentingnya segera melaporkan kehilangan barang dengan memberikan detail yang lengkap. Jelaskan bahwa semakin lengkap informasinya, semakin besar kemungkinan barang tersebut dapat ditemukan.
2. Deskripsikan Barang dengan Jelas:
    memberikan deskripsi yang sangat jelas dan detail mengenai barang yang hilang. Ini termasuk warna, bentuk, merek, atau ciri khusus lainnya yang dapat membantu orang lain mengidentifikasi barang tersebut.
3. Perbarui Informasi:
    Tekankan pentingnya untuk memperbarui informasi jika ada perkembangan dalam pencarian. Jika barang tersebut telah ditemukan, minta pengguna untuk memberi tahu agar informasi di website dapat diperbarui.
""")
        categoryBarang = st.selectbox("Category Barang", self.crud.categoryBarang)
        if category == "Penemuan" and categoryBarang == "Handphone":
            st.write("""
                     Berikut adalah langkah-langkah yang dapat dilakukan untuk menemukan pemilik asli handphone yang ditemukan:
                    1. Apakah Anda dapat membuka pesan atau kontak darurat di handphone tersebut?
                    2. Bisakah Anda memberikan deskripsi ringtone atau nada dering yang biasa digunakan?
                    3. Apakah ada aplikasi atau widget yang mungkin dapat memberikan petunjuk tentang pemiliknya?
                    4. Apakah Anda tahu operator seluler atau penyedia layanan handphone tersebut?
                    5. Apakah ada nomor darurat yang dapat dihubungi tanpa membuka kunci handphone?
                    """)
        elif category == "Penemuan" and categoryBarang == "Dompet":
            st.write("""
                     Berikut adalah langkah-langkah yang dapat dilakukan untuk menemukan pemilik asli dompet yang ditemukan:
                     1. Apakah ada kartu identitas atau kartu nama dengan nama pemilik di dalam dompet?
                     2. Bisakah Anda memberikan deskripsi uang tunai atau mata uang yang ada di dalam dompet?
                     3. Apakah ada kartu keanggotaan atau kartu kredit yang dapat dihubungi untuk mengidentifikasi pemilik?
                     4. Apakah Anda tahu apakah dompet tersebut memiliki nilai sentimental atau barang berharga lain di dalamnya?
                     5. Apakah ada foto atau tanda pengenal lain yang dapat membantu mengidentifikasi pemilik dompet?
                        """)    
        elif category == "Penemuan" and categoryBarang == "Kunci":
            st.write("""
                     Berikut adalah langkah-langkah yang dapat dilakukan untuk menemukan pemilik asli kunci yang ditemukan:
                    1. Apakah ada tanda pengenal pada kunci atau gantungan kunci?
                    2. Apakah Anda tahu kunci untuk apa atau di mana digunakan?
                    3. Apakah ada kode atau nomor yang tercetak pada kunci?
                    4. Apakah Anda tahu apakah kunci tersebut memiliki nilai sentimental atau barang berharga lainnya?
                     """)
        elif category == "Penemuan" and categoryBarang == "Kacamata":
            st.write("""
                 Berikut adalah langkah-langkah yang dapat dilakukan untuk menemukan pemilik asli kacamata yang ditemukan:
                1. Apakah ada resep kacamata di dalam kotak atau kantung kacamata?
                2. Bisakah Anda memberikan deskripsi bingkai dan lensa kacamata?
                3. Apakah ada tanda-tanda perbaikan atau penyesuaian pada kacamata?
                4. Apakah ada kartu garansi atau informasi pembelian di dalam kotak?
                5. Apakah ada tanda-tanda pemakaian atau goresan pada lensa atau bingkai?
                    """)
        elif category == "Penemuan" and categoryBarang == "Tas":
            st.write("""
                 Berikut adalah langkah-langkah yang dapat dilakukan untuk menemukan pemilik asli tas yang ditemukan:
                1. Apakah ada tanda pengenal atau dokumen dalam tas?
                2. Apakah Anda tahu barang apa saja yang biasanya ada di dalam tas tersebut?
                3. Bisakah Anda memberikan deskripsi desain atau warna tas?
                4. Apakah ada bau khusus atau barang yang mencirikan pemilik di dalam tas?
                5. Apakah ada tanda-tanda pemakaian atau keausan pada tas?
                    """)
        elif category == "Penemuan" and categoryBarang == "Buku":
            st.write("""
                 Berikut adalah langkah-langkah yang dapat dilakukan untuk menemukan pemilik asli buku yang ditemukan:
                1. Apakah ada nama atau tanda pengenal di buku tersebut?
                2. Bisakah Anda memberikan deskripsi isi buku atau halaman terakhir yang dibaca?
                3. Apakah ada catatan atau coretan di dalam buku yang dapat membantu mengidentifikasi pemilik?
                4. Apakah ada tanda-tanda pemakaian buku seperti lipatan halaman atau spidol?
                5. Apakah ada tanda buku yang menunjukkan tempat pembelian atau kepemilikan pribadi?
                    """)
        elif category == "Penemuan" and categoryBarang == "Motor":
            st.write("""
                 Berikut adalah langkah-langkah yang dapat dilakukan untuk menemukan pemilik asli motor yang ditemukan:
                1. Apakah ada tanda pengenal atau dokumen di dalam motor?
                2. Bisakah Anda memberikan deskripsi desain atau warna motor?
                3. Apakah ada tanda-tanda perbaikan atau penyesuaian pada motor?
                4. Apakah ada kartu garansi atau informasi pembelian di dalam motor?
                5. Apakah ada tanda-tanda pemakaian atau goresan pada motor?
                 6. Apakah ada surat-surat kendaraan motor?
                    """)
        elif category == "Penemuan" and categoryBarang == "Kartu":
            st.write("""
                 Berikut adalah langkah-langkah yang dapat dilakukan untuk menemukan pemilik asli kartu yang ditemukan:
                - Apakah ada kartu identitas atau kartu keanggotaan di dalamnya?
                - Apakah Anda tahu fungsi atau tempat penerbitan kartu tersebut?
                - Bisakah Anda memberikan deskripsi desain dan warna kartu?
                - Apakah ada nama atau tanda pengenal yang mencirikan pemilik pada kartu?
                - Apakah ada nomor telepon atau informasi kontak lainnya pada kartu?
                    """)
        elif category == "Penemuan" and categoryBarang == "Tumbler":
            st.write("""
                 Berikut adalah langkah-langkah yang dapat dilakukan untuk menemukan pemilik asli tumbler yang ditemukan:
                 - Apakah ada stiker atau tanda pengenal di tumbler tersebut?
                - Bisakah Anda memberikan deskripsi desain atau warna tumbler?
                - Apakah ada bekas minuman atau aroma tertentu di dalam tumbler?
                - Apakah ada tanda-tanda pemakaian atau keausan pada tumbler?
                - Apakah ada nomor seri atau informasi pembelian yang dapat membantu mengidentifikasi 
                    """)
        elif category == "Penemuan" and categoryBarang == "Lainnya":
            st.write("""
                 Berikut adalah langkah-langkah yang dapat dilakukan untuk menemukan pemilik asli barang lainnya yang ditemukan:
                - Apakah ada tanda pengenal atau dokumen di dalam barang tersebut?
                - Bisakah Anda memberikan deskripsi desain atau warna barang tersebut?
                - Apakah ada tanda-tanda pemakaian atau keausan pada barang tersebut?
                - Apakah ada nomor seri atau informasi pembelian yang dapat membantu mengidentifikasi pemilik?
                - Apakah ada ciri khusus atau tanda pengenal pada barang tersebut?
                - Apakah ada stiker atau label yang mencirikan pemilik?
                - Bisakah Anda memberikan deskripsi fisik dan fungsi barang tersebut?
                - Apakah ada petunjuk penggunaan atau panduan yang dapat memberikan petunjuk tentang pemilik?
                - Apakah ada hubungan barang tersebut dengan lokasi atau acara tertentu yang dapat membantu mengidentifikasi pemilik
                    """)
        
        
        
        # validate data 
        if self.validate_data([img,description,location,date,contactPerson,category,categoryBarang]):
            
            if st.button("Submit"):
                self.crud.add_data(
                    img,
                    description,
                    location,
                    date,
                    contactPerson,
                    category,
                    categoryBarang,
                )
                # get index of the last data
                st.session_state["index"] = len(self.crud.df) - 1
                st.success("Data Added")
                st.balloons()
                st.session_state["route"] = "Detail Laporan"
                st.rerun()

    def statistic_data(self):
        if st.session_state["route"] == "Statistic Data":
            st.subheader("Statistic Data")

            data = self.crud.df
            # create month and year column from date column
            data["month"] = pd.to_datetime(data.iloc[:, 4]).dt.month
            data["year"] = pd.to_datetime(data.iloc[:, 4]).dt.year

            data_penemuan = data[data.iloc[:, 6] == "Penemuan"]
            data_kehilangan = data[data.iloc[:, 6] == "Kehilangan"]

            st.subheader("Statistic Data Penemuan dan Kehilangan")
            st.write("Jumlah Penemuan : ", len(data_penemuan))
            st.write("Jumlah Kehilangan : ", len(data_kehilangan))
            st.write("Jumlah Total : ", len(data))

            st.subheader("Statistic Data Penemuan dan Kehilangan Per Bulan")
            st.line_chart(data.iloc[:, 9].value_counts())

            # create layout to show statistic data
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Statistic Data Penemuan dengan Location")
                st.bar_chart(data_penemuan.iloc[:, 3].value_counts())

                # create statistic data by category with bar chart
                st.subheader("Statistic Data Penemuan dengan Category")
                st.bar_chart(data_penemuan.iloc[:, 7].value_counts())

            with col2:
                st.subheader("Statistic Data Kehilangan dengan Location")
                st.bar_chart(data_kehilangan.iloc[:, 3].value_counts())

                # create statistic data by category with bar chart
                st.subheader("Statistic Data Kehilangan dengan Category")
                st.bar_chart(data_kehilangan.iloc[:, 7].value_counts())
    
    def validate_data(self,data):
        if data[1] == "":
            st.error("Image is required")
            return False
        
        if data[2] == "":
            st.error("Description is required")
            return False
        
        # check if contact person is valid format 08xxxxxxxxxx|628xxxxxxxxxx|+628xxxxxxxxxx|08xxxxxxxxx|628xxxxxxxxx|+628xxxxxxxxx
        # with regex
        import re
        regex = r"^(?:\+?62|0)[8]{1}[0-9]{8,11}$"
        if not re.match(regex, data[4]):
            st.error("Contact Person is not valid")
            return False
        


        

        return True
    

    def about(self):
        st.subheader("About")
        st.write(
            "TemuBarang is web app that will help people to find their lost item or help people to find the owner of the item they found in the public place (institut teknologi sumatera)"
        )
        st.write("TemuBarang app features: ")
        st.write("1. list of lost\found item that has been reported")
        st.write(
            "2. Detail of lost\found item (image, description, location, date, contactPerson,category, status, etc)"
        )
        st.write("3. form to report lost\found item")
        st.write("4. Search lost\found item by category, location, date, status, etc")
        st.write(
            "5. Statistic of lost\found item (number of lost\found item, number of lost\found item by category, number of lost\found item by location, number of lost\found item by date, number of lost\found item by status, etc) "
        )

    def dashboard(self):
        # check if authentication status is true then show dashboard else show login page 
        st.subheader("Dashboard")
        # say hello to user
        st.write(f"Hello {st.session_state['name']}")
        data = self.crud.df
        # filter data description
        filter = st.text_input("Filter")
        if filter != "":
            data = data[data.iloc[:, 2].str.contains(filter)]

        category = st.selectbox("Category", ["All", "Penemuan", "Kehilangan"])
        if category != "All":
            data = data[data.iloc[:, 6] == category]

        location = st.selectbox("Location", ["All"] + self.crud.location)
        if location != "All":
            data = data[data.iloc[:, 4] == location]

        for num, (i, row) in enumerate(data.iterrows()):
            # create layout to show list of data with 3 column 5 row
            if num % 3 == 0:
                col1, col2, col3 = st.columns(3)

            if num % 3 == 0:
                with col1:
                    component_html_list(row, i)
                    # create button to open modal
                    if st.button(f"Open{i}"):
                        st.session_state["index"] = i
                        st.session_state["route"] = "Detail Laporan"
                    if st.button(f"Delete{i}"):
                        self.crud.delete_data_by_index(i)
                        st.success("Data Deleted")
                        st.balloons()
                        st.rerun()
    

            elif num % 3 == 1:
                with col2:
                    component_html_list(row, i)
                    if st.button(f"Open{i}"):
                        st.session_state["index"] = i
                        st.session_state["route"] = "Detail Laporan"
                    if st.button(f"Delete{i}"):
                        self.crud.delete_data_by_index(i)
                        st.success("Data Deleted")
                        st.balloons()
                        st.rerun()

            elif num % 3 == 2:
                with col3:
                    component_html_list(row, i)
                    if st.button(f"Open{i}"):
                        st.session_state["index"] = i
                        st.session_state["route"] = "Detail Laporan"
                    if st.button(f"Delete{i}"):
                        self.crud.delete_data_by_index(i)
                        st.success("Data Deleted")
                        st.balloons()
                        st.rerun()
     

    def login(self):
        self.auth.login()
    
    def logout(self):
        self.auth.logout()

