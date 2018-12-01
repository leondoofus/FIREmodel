data = [
[4.483107391501312, 4.135526440235811, 4.128499070246824, 3.8611926278307074, 3.789415507677336, 4.61796327280122, 4.214854469955894, 4.1017418441776545, 4.41273544756358, 4.078128011219022, 4.3146895444951925, 4.891633888262774, 4.66503669370181, 3.8189748124784666, 4.2784174437251705, 3.809852677885878],
[ 5.076054409176738, 4.565947097827657, 3.5754026266456975, 4.2396869959190795, 4.057851281508084, 4.0571836610722505, 3.9004287745337844, 4.059988312876029, 4.031234196426477, 4.445584813090578, 3.8308807918100634, 4.330709031002035, 3.9475512623532243, 3.4495173256136678, 4.878340782968199, 3.9267957671848426],
[ 3.4523245421071618, 4.066365186449523, 4.223520949540391, 4.023587091890294, 3.9464102876549245, 3.89390395397923, 4.724666745917876, 4.21468862247549, 3.62312774638115, 4.834785764326352, 4.866442346726199, 3.7114834097324296, 3.7551282260849663, 4.539630193738906, 4.152766869474522, 4.197387172074625],
[ 4.285992247035193, 4.623354800244606, 4.104890285314164, 4.180809514963188, 4.034965168758269, 3.9963567386919827, 4.165782275733801, 3.8617657198764106, 4.673127406254207, 3.866275160727792, 4.8671580143712685, 4.25455235075586, 3.8791091831100064, 3.980123026945849, 4.509746310773751, 4.334419923336675],
[ 4.882072938147038, 4.338616221378667, 3.7714822998453466, 4.725593953234827, 4.596719679110889, 4.220327285875957, 4.845069528182132, 3.748813043233917, 4.26600066839936, 5.078770196110943, 4.236791483707452, 3.862244917563913, 4.185712325872535, 4.139167125714052, 4.692476806000251, 3.92097229531301],
[ 4.002265305519049, 4.033691278570131, 3.571446470932743, 4.151304545151137, 4.232117643806267, 3.591265144827066, 3.8052341983442313, 3.9212003996893694, 3.9950975941499194, 4.432459078211723, 3.877984973913565, 4.517672236759195, 3.753009786621323, 4.0164843175287785, 4.445983184720155, 4.380777627403263],
[ 4.096408622338807, 4.734610069105986, 3.5673408257494486, 3.7896476608794445, 4.088619318017491, 4.46863616423136, 4.378922964310411, 4.452343835276579, 4.32097746476842, 4.121971742339296, 4.10343334423607, 3.8393677009880722, 3.6942371530072156, 4.530381317851801, 4.286248742876447, 3.9679218848725912],
[ 4.64891983699306, 3.9476686661550318, 3.823174541789976, 4.055728592073444, 3.92674154166886, 4.306863773188583, 4.367393283221031, 4.106560415029543, 3.8877405066859434, 4.62573993473997, 4.167206216750058, 3.88722572200295, 4.333197765490486, 4.347575205547673, 4.139492275740583, 4.539594359839124],
[ 4.131651494475639, 4.508089447426791, 4.499817352025486, 4.291070248735914, 4.003288811782832, 4.1940764840790665, 3.644005004432784, 3.4764916530981513, 4.031634042383282, 4.0707724959647145, 4.8336993574316525, 4.365587494219857, 4.06411622205105, 4.642104951583973, 4.687322636948887, 4.630173550672311],
[ 4.203397616260286, 4.784340670127891, 4.5158639995955685, 3.269946398222364, 4.396540143100107, 3.8354428980638042, 4.065596005345782, 3.779561983633356, 4.166424007582134, 4.498158226833953, 4.140888930986359, 4.417417614608764, 4.087082759181699, 4.942118272030865, 4.014273208443781, 3.8223289288458466],
[ 4.046084798756851, 3.4911044002814586, 4.585614744910825, 4.4303959288657335, 3.5557905412841366, 4.445697009377638, 4.3114465888616325, 4.159892114132674, 4.733094048153438, 4.1452838060927935, 3.8219874119730926, 4.0478979307227885, 5.0456042929925085, 4.3564291882704245, 3.7225577405917982, 4.507504760617302],
[ 4.363299061678408, 3.9394960445447285, 4.387699583734263, 4.080026969915672, 4.393162915611939, 3.856658720389929, 4.540507803586599, 4.17831752423029, 4.04204165925376, 4.390421067766381, 3.946285270578448, 3.897640157601302, 4.536952451274031, 4.257478172165749, 4.118805767055729, 4.166230633831709],
[ 3.9726044378532968, 3.8402681529841503, 4.3890666372116796, 5.159806951924015, 4.393576435275857, 4.9346074240099, 4.391116729080493, 3.59324298842515, 3.709544027588702, 4.383758290605594, 4.164667197010372, 4.300208375254002, 4.642888579700364, 4.832026701589605, 4.743904785624302, 4.75298906115183],
[ 3.6582179075212533, 3.9535834440041873, 3.324205850246484, 4.706357167065285, 4.150179712686102, 3.849120432564375, 3.9441798650062947, 4.44967185715453, 4.395930593707166, 4.49121758891977, 4.754749897647867, 4.395032155920302, 4.252573521554572, 4.049780516299967, 4.18890700028484, 3.9377373792142145],
[ 3.9300552811415717, 3.8626981645510896, 3.4521880373619775, 4.6398343220693, 3.7639014891621985, 4.3907276605962835, 3.6266569446938557, 4.29943487666796, 4.016863170960525, 4.363485334949513, 3.797695023715953, 4.317746034145651, 5.0638803019064325, 4.018460805411385, 4.7988027290437545, 4.55535799860842],
[ 4.876559545932908, 3.9616752633087673, 4.587109062506198, 3.675021433576506, 4.576459776404849, 4.613199987882562, 3.8875993263604416, 4.02633835953164, 4.267409135403116, 4.0796178494088196, 4.388852564720643, 3.9829055693806907, 4.591856952221804, 4.495017297670131, 4.442756237511827, 3.883665088896574]
]