# import library
from streamlit_tailwind import st_tw
from helpers import humanize_date
from utils import image_to_base64




def component_html_list(data, i, on_click=None):
    images = image_to_base64(data[1])
    descriptions = data[2]
    locations = data[3]
    dates = data[4]
    contactPersons = data[5]
    categorys = data[6]
    statuss = data[7]

    return st_tw(
        text="""
<div onclick={on_click} class="w-full max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 hover:bg-white-800">
    <img class="p-8 rounded-t-lg center" style="height:300px;" src={images} alt="product image" />
    <div class="px-5 pb-5">
        <h6 class="text-xl font-semibold tracking-tight text-gray-900 dark:text-white">{descriptions}</h6>
        <span class="text-l font-bold text-gray-900 dark:text-white mt-5 mb-5">{dates}</span> 
        <div class="flex items-center justify-between">
            <span class="text-l font-bold text-gray-900 dark:text-white"> {locations}</span>
            <span class="text-white bg-{color}-700  font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-{color}-600 ">{categorys}</span>
        </div>
    </div>
</div>
    """.format(
            images=images,
            descriptions=descriptions,
            locations=locations,
            dates=humanize_date(dates),
            contactPersons=contactPersons,
            categorys=categorys,
            statuss=statuss,
            color="blue" if categorys == "Penemuan" else "red",
            on_click=on_click,
        ),
        height=500,
        key=i,
    )


def component_html_detail(data, i):
    images = image_to_base64(data[1])
    descriptions = data[2]
    locations = data[3]
    dates = data[4]
    contactPersons = data[5]
    categorys = data[6]
    categoryBarang = data[7]

    return st_tw(
        # create detail page using tailwind css framework
        text="""
<div class="overflow-hidden bg-white py-24 sm:py-32 w-full">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2">
      <div class="lg:pr-8 lg:pt-4">
        <div class="lg:max-w-lg">
        <div class="flex items-center justify-between">
          <h2 class="text-base font-semibold leading-7 text-{color}-600 ">{categorys}</h2>
          <h2 class="text-base font-semibold leading-7 text-indigo-600">{categoryBarang}</h2>
          </div>
          <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Deskripsi Barang</p>
          <p class="mt-6 text-lg leading-8 text-gray-600">{descriptions}</p>
          <dl class="mt-10 max-w-xl space-y-8 text-base leading-7 text-gray-600 lg:max-w-none">
            <div class="relative pl-9">
              <dt class="inline font-semibold text-gray-900">
               <svg  class="absolute left-1 top-1 h-5 w-5 text-indigo-600" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
							<path d="M12.075,10.812c1.358-0.853,2.242-2.507,2.242-4.037c0-2.181-1.795-4.618-4.198-4.618S5.921,4.594,5.921,6.775c0,1.53,0.884,3.185,2.242,4.037c-3.222,0.865-5.6,3.807-5.6,7.298c0,0.23,0.189,0.42,0.42,0.42h14.273c0.23,0,0.42-0.189,0.42-0.42C17.676,14.619,15.297,11.677,12.075,10.812 M6.761,6.775c0-2.162,1.773-3.778,3.358-3.778s3.359,1.616,3.359,3.778c0,2.162-1.774,3.778-3.359,3.778S6.761,8.937,6.761,6.775 M3.415,17.69c0.218-3.51,3.142-6.297,6.704-6.297c3.562,0,6.486,2.787,6.705,6.297H3.415z"></path>
						</svg>
               Contact Person : 
              </dt>
              <dd class="inline">{contactPersons}</dd>
            </div>
            <div class="relative pl-9">
              <dt class="inline font-semibold text-gray-900">
                <svg class="absolute left-1 top-1 h-5 w-5 text-indigo-600" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
							<path d="M10,1.375c-3.17,0-5.75,2.548-5.75,5.682c0,6.685,5.259,11.276,5.483,11.469c0.152,0.132,0.382,0.132,0.534,0c0.224-0.193,5.481-4.784,5.483-11.469C15.75,3.923,13.171,1.375,10,1.375 M10,17.653c-1.064-1.024-4.929-5.127-4.929-10.596c0-2.68,2.212-4.861,4.929-4.861s4.929,2.181,4.929,4.861C14.927,12.518,11.063,16.627,10,17.653 M10,3.839c-1.815,0-3.286,1.47-3.286,3.286s1.47,3.286,3.286,3.286s3.286-1.47,3.286-3.286S11.815,3.839,10,3.839 M10,9.589c-1.359,0-2.464-1.105-2.464-2.464S8.641,4.661,10,4.661s2.464,1.105,2.464,2.464S11.359,9.589,10,9.589"></path>
						</svg>
                Lokasi Terakhir : 
              </dt>
              <dd class="inline">{locations}</dd>
            </div>
            <div class="relative pl-9">
              <dt class="inline font-semibold text-gray-900">
                 <svg class="absolute left-1 top-1 h-5 w-5 text-indigo-600" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
							<path d="M10.25,2.375c-4.212,0-7.625,3.413-7.625,7.625s3.413,7.625,7.625,7.625s7.625-3.413,7.625-7.625S14.462,2.375,10.25,2.375M10.651,16.811v-0.403c0-0.221-0.181-0.401-0.401-0.401s-0.401,0.181-0.401,0.401v0.403c-3.443-0.201-6.208-2.966-6.409-6.409h0.404c0.22,0,0.401-0.181,0.401-0.401S4.063,9.599,3.843,9.599H3.439C3.64,6.155,6.405,3.391,9.849,3.19v0.403c0,0.22,0.181,0.401,0.401,0.401s0.401-0.181,0.401-0.401V3.19c3.443,0.201,6.208,2.965,6.409,6.409h-0.404c-0.22,0-0.4,0.181-0.4,0.401s0.181,0.401,0.4,0.401h0.404C16.859,13.845,14.095,16.609,10.651,16.811 M12.662,12.412c-0.156,0.156-0.409,0.159-0.568,0l-2.127-2.129C9.986,10.302,9.849,10.192,9.849,10V5.184c0-0.221,0.181-0.401,0.401-0.401s0.401,0.181,0.401,0.401v4.651l2.011,2.008C12.818,12.001,12.818,12.256,12.662,12.412"></path>
						</svg>
                Tanggal Kejadian :
              </dt>
              <dd class="inline">{dates}</dd>
            </div>
          </dl>
            <p class="mt-6 text-lg leading-8 text-gray-600">Jika Anda menemukan barang yang hilang, identifikasi dengan cermat, catat waktu dan tempat temuan, dan periksa informasi kontak pemilik. Jika informasi tersebut tidak tersedia, gunakan media sosial atau pemberitahuan publik. Jika upaya ini tidak berhasil, serahkan barang ke kantor kepolisian dengan bukti identifikasi. Berikan informasi kontak Anda dan pertimbangkan keamanan privasi pemilik. Dengan langkah-langkah ini, Anda dapat meningkatkan kemungkinan barang dikembalikan dengan efisien kepada pemiliknya.</p>
        </div>
      </div>
      <img src="{images}" alt="Product screenshot" class="rounded-xl shadow-xl ring-1 ring-gray-400/10  md:-ml-4 lg:-ml-0" width="2432" height="1442">
    </div>
  </div>
</div>

      """.format(
            images=images,
            descriptions=descriptions,
            locations=locations,
            dates=humanize_date(dates),
            contactPersons=contactPersons,
            categorys=categorys,
            categoryBarang=categoryBarang,
            color="blue" if categorys == "Penemuan" else "red",
        ),
        key=i,
        height=800,
    )
