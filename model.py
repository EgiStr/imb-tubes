import pandas as pd
import uuid


def load_data():
    df = pd.read_csv("./data/main.csv")
    return df


class CrudDateset:
    def __init__(self, df):
        self.df = df
        self.categoryBarang = [
            "Handphone",
            "Laptop",
            "Dompet",
            "Kunci",
            "Kacamata",
            "Tas",
            "Buku",
            "Motor",
            "Surat-surat",
            "Kartu",
            "Tumbler",
            "Lainnya",
        ]
        self.location = [
            "Kantin RK",
            "Kantin BKL",
            "Galeri Labtek 3",
            "Galeri Gedung B",
            "Perpustakaan GKU1",
            "Perpustakaan GKU2",
            "Gedung A",
            "Gedung B",
            "Gedung C",
            "Gedung D",
            "Gedung E",
            "Gedung F",
            "Labtek 1",
            "Labtek 2",
            "Labtek 3",
            "Labtek 5/OZT",
            "Asrama TB1",
            "Asrama TB2",
            "Asrama TB3",
            "Asrama TB4",
            "GKU1",
            "GKU2",
            "Embung A",
            "Embung B",
            "Embung C",
            "Embung D",
            "Embung E",
            "Kebun Raya",
            "Masjid Baitul Ilmi",
            "Masjid At-tanwir",
            "Belwis",
            "Airan",
            "Gerbang Barat",
            "Lainnya",
        ]
        self.category = ["Penemuan", "Kehilangan"]

    def add_data(
        self,
        image,
        description,
        location,
        date,
        contactPerson,
        category,
        categoryBarang,
    ):
        uuid_1 = str(uuid.uuid4())
        id = str(uuid_1)

        new_data = pd.DataFrame(
            [
                [
                    id,
                    image,
                    description,
                    location,
                    date,
                    contactPerson,
                    category,
                    categoryBarang,
                    "",
                ]
            ],
            columns=self.df.columns,
        )
        self.df = pd.concat([self.df, new_data], ignore_index=True)
        self.save_data()
        return self.df

    def edit_data(
        self,
        index,
        image,
        description,
        location,
        date,
        contactPerson,
        category,
    ):
        self.df.loc[index] = [
            image,
            description,
            location,
            date,
            contactPerson,
            category,
        ]
        self.save_data()
        return self.df

    def delete_data_by_index(self, index):
        self.df = self.df[self.df.loc[index].uuid != self.df.uuid]
        self.save_data()
        self.df = load_data()
        return self.df

    def add_comment(self, index, comment):
        # get comment from data where index is index
        # check is comment is not None and comment is nan
        if (
            pd.isna(self.df.loc[index]["comment"])
            or self.df.loc[index]["comment"] == ""
        ):
            # if comment is None or comment is nan then replace comment with new comment
            self.df.iloc[index, 8] = comment
        else:
            # if comment is not None or comment is not nan then add new comment to the old comment

            # replace comment with new comment
            self.df.iloc[index, 8] = self.df.loc[index]["comment"] + f",{comment}"

        self.save_data()

    def detail_data(self, index):
        return self.df.loc[index]

    def save_data(self):
        self.df.to_csv("data/main.csv", index=False)

