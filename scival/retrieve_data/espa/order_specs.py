orders = {"original": [{'tm4_collection': {
    'inputs': ['LT04_L1TP_030031_19890420_20161002_01_T1'],
    'products': ['l1', 'source_metadata', 'toa', 'sr', 'bt',
                 'sr_ndvi', 'sr_ndmi', 'sr_nbr', 'sr_nbr2',
                 'sr_savi', 'sr_msavi', 'sr_evi']
},
    'format': 'envi',
    'note': 'Test1',
    'resize': {
        'pixel_size': 500,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'utm': {
            'zone': 14,
            'zone_ns': 'north'
        }
    },
    'image_extents': {
        'north': 4653099.046333,
        'south': 4603245.749171,
        'east': 537599.784776,
        'west': 443877.992818,
        'units': 'meters'
    },
    'resampling_method': 'cc'

}, {'tm4_collection': {
    'inputs': ['LT04_L1TP_030031_19890420_20161002_01_T1'],
    'products': ['source_metadata', 'toa', 'sr', 'bt',
                 'sr_ndvi', 'sr_ndmi', 'sr_nbr', 'sr_nbr2',
                 'sr_savi', 'sr_msavi', 'sr_evi', 'st']
},
    'format': 'gtiff',
    'note': 'Test2',
    'projection': {
        'utm': {
            'zone': 14,
            'zone_ns': 'north'
        }
    },
    'image_extents': {
        'north': 4673018.374,
        'south': 4569036.916,
        'east': 59119.194,
        'west': 51371.027,
        'units': 'meters'
    },
    'resampling_method': 'cc'

}, {'tm5_collection': {
    'inputs': ['LT05_L1TP_187021_20070917_20161112_01_T1'],
    'products': ['l1, sr, swe, st, sr_ndmi']
},
    'format': 'envi',
    'note': 'Test1',
    'resize': {
        'pixel_size': 0.005,
        'pixel_size_units': 'dd'
    },
    'projection': {
        'lonlat': None
    },
    'resampling_method': 'bil'

}, {'etm7_collection': {
    'inputs': ['LE07_L1GT_210117_20130302_20161125_01_T2'],
    'products': ['l1', 'toa']
},
    'format': 'gtiff',
    'note': 'Test1',
    'resize': {
        'pixel_size': 500,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'utm': {
            'zone': 17,
            'zone_ns': 'south'
        }
    },
    'resampling_method': 'nn'

}, {'etm7_collection': {
    'inputs': ['LE07_L1GT_210117_20130302_20161125_01_T2'],
    'products': ['l1', 'source_metadata', 'sr']
},
    'format': 'envi',
    'note': 'Test2',
    'resize': {
        'pixel_size': 0.0025,
        'pixel_size_units': 'dd'
    },
    'projection': {
        'lonlat': None
    },
    'resampling_method': 'nn'

}, {'etm7_collection': {
    'inputs': ['LE07_L1GT_210117_20130302_20161125_01_T2'],
    'products': ['l1', 'toa']
},
    'format': 'envi',
    'note': 'Test3',
    'resize': {
        'pixel_size': 500,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'ps': {
            'false_easting': 0,
            'false_northing': 0,
            'latitude_true_scale': -70,
            'longitudinal_pole': 0
        }
    },
    'resampling_method': 'nn'

}, {'etm7_collection': {
    'inputs': ['LE07_L1GT_210117_20130302_20161125_01_T2'],
    'products': ['sr_ndvi', 'sr_ndmi', 'sr_nbr', 'sr_nbr2',
                 'sr_savi', 'sr_msavi', 'sr_evi']
},
    'format': 'gtiff',
    'note': 'Test4',
    'resize': {
        'pixel_size': 500,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'ps': {
            'false_easting': 0,
            'false_northing': 0,
            'latitude_true_scale': -90,
            'longitudinal_pole': 0
        }
    },
    'resampling_method': 'nn'

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_039037_20080712_20160922_01_T1'],
    'products': ['l1', 'source_metadata', 'sr']
},
    'format': 'gtiff',
    'note': 'Test1',
    'resize': {
        'pixel_size': 0.0025,
        'pixel_size_units': 'dd'
    },
    'projection': {
        'lonlat': None
    },
    'resampling_method': 'nn'

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_039037_20080712_20160922_01_T1'],
    'products': ['l1', 'bt']
},
    'format': 'envi',
    'note': 'Test2',
    'resize': {
        'pixel_size': 500,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'utm': {
            'zone': 11,
            'zone_ns': 'north'
        }
    },
    'resampling_method': 'nn'

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_039037_20080712_20160922_01_T1'],
    'products': ['sr']
},
    'format': 'gtiff',
    'note': 'Test3',
    'resize': {
        'pixel_size': 500,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'sinu': {
            'central_meridian': 0,
            'false_easting': 0,
            'false_northing': 0
        }
    },
    'resampling_method': 'nn'

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_039037_20080712_20160922_01_T1'],
    'products': ['sr']
},
    'format': 'gtiff',
    'note': 'Test4',
    'resize': {
        'pixel_size': 500,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'aea': {
            'central_meridian': -96,
            'datum': 'nad83',
            'false_easting': 0,
            'false_northing': 0,
            'latitude_of_origin': 23,
            'standard_parallel_1': 29.5,
            'standard_parallel_2': 45.5
        }
    },
    'resampling_method': 'nn'

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_039037_20080712_20160922_01_T1'],
    'products': ['source_metadata']
},
    'format': 'gtiff',
    'note': 'Test5',

}, {'oli8_collection': {
    'inputs': ['LC08_L1TP_125030_20150414_20170410_01_T1'],
    'products': ['sr', 'st', 'swe', 'toa']
},
    'format': 'gtiff',
    'note': 'Test1',
    'resize': {
        'pixel_size': 35,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'utm': {
            'zone': 50,
            'zone_ns': 'north'
        }
    },
    'resampling_method': 'cc'

}, {'tm5_collection': {
    'inputs': ['LT05_L1TP_010054_20110312_20161209_01_T1'],
    'products': ['l1', 'toa']
},
    'format': 'envi',
    'note': 'Test1',
    'resize': {
        'pixel_size': 500,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'utm': {
            'zone': 18,
            'zone_ns': 'north'
        }
    },
    'resampling_method': 'nn'

}, {'tm5_collection': {
    'inputs': ['LT05_L1TP_010054_20110312_20161209_01_T1'],
    'products': ['l1', 'source_metadata', 'sr']
},
    'format': 'gtiff',
    'note': 'Test2',
    'resize': {
        'pixel_size': 0.0025,
        'pixel_size_units': 'dd'
    },
    'projection': {
        'lonlat': None
    },
    'resampling_method': 'nn'

}, {'tm5_collection': {
    'inputs': ['LT05_L1TP_010054_20110312_20161209_01_T1'],
    'products': ['l1', 'bt', 'st']
},
    'format': 'envi',
    'note': 'Test3',
    'resize': {
        'pixel_size': 500,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'utm': {
            'zone': 18,
            'zone_ns': 'north'
        }
    },
    'resampling_method': 'nn'

}, {'tm5_collection': {
    'inputs': ['LT05_L1TP_010054_20110312_20161209_01_T1'],
    'products': ['sr_ndvi', 'sr_ndmi', 'sr_nbr', 'sr_nbr2',
                 'sr_savi', 'sr_msavi', 'sr_evi']
},
    'format': 'envi',
    'note': 'Test4',
    'resize': {
        'pixel_size': 500,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'sinu': {
            'central_meridian': -76.6,
            'false_easting': 0,
            'false_northing': 0
        }
    },
    'resampling_method': 'nn'

}, {'tm5_collection': {
    'inputs': ['LT05_L1TP_010054_20110312_20161209_01_T1'],
    'products': ['swe']
},
    'format': 'gtiff',
    'note': 'Test5',

}, {'mod09ga': {
    'inputs': ['MOD09GA.A2001024.h20v17.005.2006351175917',
               'MOD09GA.A2001024.h20v17.006.2015140115718'],
    'products': ['l1']
},
    'format': 'envi',
    'note': 'Test1',
    'resize': {
        'pixel_size': 250,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'utm': {
            'zone': 58,
            'zone_ns': 'south'
        }
    },
    'resampling_method': 'cc'

}, {'mod09ga': {
    'inputs': ['MOD09GA.A2001024.h20v17.005.2006351175917',
               'MOD09GA.A2001024.h20v17.006.2015140115718'],
    'products': ['l1']
},
    'format': 'gtiff',
    'note': 'Test2',
    'resize': {
        'pixel_size': 250,
        'pixel_size_units': 'meters'
    },
    'image_extents': {
        'west': -150000,
        'north': 1100200,
        'east': 124685.981,
        'south': 951765.809,
        'units': 'meters'
    },
    'projection': {
        'ps': {
            'false_easting': 0,
            'false_northing': 0,
            'latitude_true_scale': -80,
            'longitudinal_pole': 160
        }
    },
    'resampling_method': 'cc'

}, {'myd13q1': {
    'inputs': ['MYD13Q1.A2002185.h19v05.006.2015149070403'],
    'products': ['l1']
},
    'tm5_collection': {
        'inputs': ['LT05_L1TP_182034_20020628_20161207_01_T1'],
        'products': ['l1', 'sr_ndvi', 'sr_evi']
    },
    'format': 'envi',
    'note': 'Test1',
    'resize': {
        'pixel_size': 250,
        'pixel_size_units': 'meters'
    },
    'image_extents': {
        'west': 188945.952,
        'north': 4260854.770,
        'east': 344521.263,
        'south': 4149729.547,
        'units': 'meters'
    },
    'projection': {
        'utm': {
            'zone': 35,
            'zone_ns': 'north'
        }
    },
    'resampling_method': 'bil'

}, {'myd13q1': {
    'inputs': ['MYD13Q1.A2002185.h19v05.006.2015149070403'],
    'products': ['l1', 'stats']
},
    'tm5_collection': {
        'inputs': ['LT05_L1TP_182034_20020628_20161207_01_T1'],
        'products': ['l1', 'swe', 'sr_ndvi', 'stats']
    },
    'format': 'gtiff',
    'note': 'Test2',
    'resize': {
        'pixel_size': 250,
        'pixel_size_units': 'meters'
    },
    'image_extents': {
        'west': 1190082.308,
        'north': 1019317.137,
        'east': 1335074.265,
        'south': 907662.747,
        'units': 'meters'
    },
    'projection': {
        'aea': {
            'central_meridian': 10,
            'datum': 'nad27',
            'false_easting': 0,
            'false_northing': 0,
            'latitude_of_origin': 30,
            'standard_parallel_1': 43,
            'standard_parallel_2': 62
        }
    },
    'resampling_method': 'cc'

}, {'myd13q1': {
    'inputs': ['MYD13Q1.A2002185.h19v05.006.2015149070403'],
    'products': ['l1', 'stats']
},
    'tm5_collection': {
        'inputs': ['LT05_L1TP_182034_20020628_20161207_01_T1'],
        'products': ['l1', 'st', 'sr_ndvi', 'stats']
    },
    'format': 'envi',
    'note': 'Test3',
    'resize': {
        'pixel_size': 100,
        'pixel_size_units': 'meters'
    },
    'image_extents': {
        'west': 2048288.867,
        'north': 4254354.005,
        'east': 2217357.955,
        'south': 4095074.520,
        'units': 'meters'
    },
    'projection': {
        'sinu': {
            'central_meridian': 0,
            'false_easting': 0,
            'false_northing': 0
        }
    },
    'resampling_method': 'nn'

}, {'myd13q1': {
    'inputs': ['MYD13Q1.A2002185.h19v05.006.2015149070403'],
    'products': ['l1', 'stats']
},
    'tm5_collection': {
        'inputs': ['LT05_L1TP_182034_20020628_20161207_01_T1'],
        'products': ['l1', 'sr_ndvi', 'stats']
    },
    'format': 'gtiff',
    'note': 'Test4',
    'resize': {
        'pixel_size': 0.005,
        'pixel_size_units': 'dd'
    },
    'image_extents': {
        'west': 23.495342,
        'north': 38.425612,
        'east': 25.011058,
        'south': 37.021730,
        'units': 'dd'
    },
    'projection': {
        'lonlat': None
    },
    'resampling_method': 'nn'

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_028031_20041227_20160925_01_T1'],
    'products': ['sr']
},
    'format': 'gtiff',
    'note': 'Test1',
    'image_extents': {
        'west': 706149.668,
        'north': 4666748.241,
        'east': 777223.101,
        'south': 4595959.102,
        'units': 'meters'
    },
    'projection': {
        'utm': {
            'zone': 14,
            'zone_ns': 'north'
        }
    }

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_047027_20131014_20170308_01_T1'],
    'products': ['sr', 'toa', 'sr_ndvi']
},
    'format': 'envi',
    'note': 'Test1',

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_047027_20131014_20170308_01_T1'],
    'products': ['source_metadata', 'bt', 'sr_ndvi', 'sr_ndmi',
                 'sr_nbr', 'sr_nbr2', 'sr_savi', 'sr_msavi',
                 'sr_evi']
},
    'format': 'gtiff',
    'note': 'Test2',
    'resize': {
        'pixel_size': 0.0025,
        'pixel_size_units': 'dd'
    },
    'image_extents': {
        'west': -124.184902,
        'north': 48.110315,
        'east': -122.977087,
        'south': 47.296540,
        'units': 'dd'
    },
    'projection': {
        'lonlat': None
    },
    'resampling_method': 'cc'

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_047027_20131014_20170308_01_T1'],
    'products': ['l1']
},
    'format': 'hdf-eos2',
    'note': 'Test3',
    'resize': {
        'pixel_size': 2000,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'aea': {
            'latitude_of_origin': 23,
            'datum': 'nad83',
            'central_meridian': -96,
            'standard_parallel_1': 29.5,
            'standard_parallel_2': 45.5,
            'false_easting': 0,
            'false_northing': 0
        }
    },
    'resampling_method': 'bil'

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_047027_20131014_20170308_01_T1'],
    'products': ['sr', 'swe']
},
    'format': 'hdf-eos2',
    'note': 'Test4',
    'resize': {
        'pixel_size': 1500,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'sinu': {
            'central_meridian': 0,
            'false_easting': 0,
            'false_northing': 0
        }
    },
    'resampling_method': 'nn'

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_047027_20131014_20170308_01_T1'],
    'products': ['toa']
},
    'format': 'envi',
    'note': 'Test5',
    'resize': {
        'pixel_size': 2000,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'utm': {
            'zone': 11,
            'zone_ns': 'north'
        }
    },
    'resampling_method': 'cc'

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_033029_20140727_20170304_01_T1'],
    'products': ['l1', 'sr_ndvi', 'sr_evi', 'stats']
},
    'mod13q1': {
        'inputs': ['MOD13Q1.A2014209.h10v04.006.2015289032142'],
        'products': ['l1', 'stats']
    },
    'format': 'gtiff',
    'note': 'Test1',
    'resize': {
        'pixel_size': 0.0025,
        'pixel_size_units': 'dd'
    },
    'projection': {
        'lonlat': None
    },
    'image_extents': {
        'west': -104.050254,
        'north': 44.485869,
        'east': -103.294537,
        'south': 43.954773,
        'units': 'dd'
    },
    'resampling_method': 'nn'

}, {'olitirs8': {
    'inputs': ['LC08_L1GT_044116_20131126_20170428_01_T2'],
    'products': ['sr', 'toa', 'swe', 'bt']
},
    'format': 'envi',
    'note': 'Test1'

}, {'olitirs8': {
    'inputs': ['LC08_L1TP_131018_20130418_20170505_01_T2'],
    'products': ['sr', 'toa', 'sr_ndvi']
},
    'format': 'gtiff',
    'note': 'Test1'

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_014035_20150615_20160902_01_T1'],
    'products': ['toa', 'pixel_qa', 'st']
},
    'format': 'envi',
    'note': 'Test1',

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_089079_20150815_20161022_01_T1'],
    'products': ['toa', 'sr']
},
    'format': 'envi',
    'note': 'Test1',

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_089079_20150815_20161022_01_T1'],
    'products': ['toa', 'sr']
},
    'format': 'gtiff',
    'note': 'Test2',
    'projection': {
        'utm': {
            'zone': 56,
            'zone_ns': 'south'
        }
    },
    'image_extents': {
        'west': 350000,
        'north': -3120000,
        'east': 398000,
        'south': -3160000,
        'units': 'meters'
    },
    'resampling_method': 'nn'

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_022033_20140228_20160905_01_T1'],
    'products': ['pixel_qa', 'sr', 'st', 'swe']
},
    'format': 'gtiff',
    'note': 'Test1',

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_200025_20000831_20170210_01_T1'],
    'products': ['source_metadata', 'sr', 'swe', 'sr_ndvi']
},
    'format': 'envi',
    'note': 'Test1'

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_002071_20151126_20170401_01_T1'],
    'products': ['swe']
},
    'format': 'gtiff',
    'note': 'Test1',

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_195021_20150907_20161021_01_T1'],
    'products': ['sr_ndvi', 'sr']
},
    'format': 'netcdf',
    'note': 'Test1'

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_195021_20150907_20161021_01_T1'],
    'products': ['toa', 'bt', 'sr_evi', 'swe']
},
    'format': 'netcdf',
    'note': 'Test2',
    'projection': {
        'lonlat': None
    },
    'resize': {
        'pixel_size': 0.004,
        'pixel_size_units': 'dd'
    },
    'image_extents': {
        'west': 12,
        'north': 56,
        'east': 13,
        'south': 55.5,
        'units': 'dd'
    },
    'resampling_method': 'cc'

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_194021_20150908_20170404_01_T1'],
    'products': ['toa']
},
    'format': 'netcdf',
    'note': 'Test1'

}, {'olitirs8_collection': {
    'inputs': ['LO08_L1GT_211113_20140304_20170425_01_T2'],
    'products': ['toa', 'sr']
},
    'format': 'geotiff',
    'projection': {
        'ps': {
            'false_easting': 0,
            'false_northing': 0,
            'latitude_true_scale': -70,
            'longitudinal_pole': 0
        }
    },
}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_022032_20130828_20170309_01_T1'],
    'products': ['source_metadata', 'pixel_qa', 'st', 'sr_evi']
},
    'format': 'hdf-eos2',
    'note': 'Test1'

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_140027_20151016_20170403_01_T1'],
    'products': ['swe', 'toa', 'stats']
},
    'format': 'envi',
    'note': 'Test1',

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1GT_066017_20130917_20170308_01_T2'],
    'products': ['l1', 'st', 'stats']
},
    'format': 'gtiff',
    'note': 'Test1',
    'projection': {
        'lonlat': None
    },
    'resize': {
        'pixel_size': 0.0004,
        'pixel_size_units': 'dd'
    },
    'image_extents': {
        'west': -147.3,
        'north': 61.3,
        'east': -146,
        'south': 61,
        'units': 'dd'
    },
    'resampling_method': 'cc'

}, {'tm4_collection': {
    'inputs': ['LT04_L1TP_035027_19890712_20161001_01_T1'],
    'products': ['source_metadata', 'pixel_qa', 'bt', 'st', 'sr_nbr']
},
    'format': 'envi',
    'note': 'Test1'
}, {'tm4_collection': {
    'inputs': ['LT04_L1TP_029046_19920523_20170124_01_T1'],
    'products': ['st', 'swe', 'source_metadata', 'sr', 'stats']
},
    'format': 'envi',
    'note': 'Test1',
    'resize': {
        'pixel_size': 60,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'aea': {
            'central_meridian': -105,
            'datum': 'wgs84',
            'false_easting': 0,
            'false_northing': 0,
            'latitude_of_origin': 24,
            'standard_parallel_1': 14.5,
            'standard_parallel_2': 32.5
        }
    },
    'resampling_method': 'bil'

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_013009_20130720_20161122_01_T1'],
    'products': ['pixel_qa', 'st', 'sr_ndvi', 'swe']
},
    'format': 'hdf-eos2',
    'note': 'Test1',
    'projection': {
        'ps': {
            'false_easting': 0,
            'false_northing': 0,
            'latitude_true_scale': 70,
            'longitudinal_pole': 45
        }
    },

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_033032_20161020_20170219_01_T1'],
    'products': ['sr']
},
    'format': 'netcdf',
    'note': 'Test1',

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_033032_20161020_20170219_01_T1'],
    'products': ['sr', 'sr_ndvi', 'sr_ndmi', 'sr_nbr', 'sr_nbr2',
                 'sr_savi', 'sr_msavi', 'sr_evi', 'stats']
},
    'format': 'netcdf',
    'note': 'Test2',

}, {'myd11a1': {
    'inputs': ['MYD11A1.A2017069.h16v02.006.2017073045736'],
    'products': ['l1', 'stats']
},
    'format': 'netcdf',
    'note': 'Test1',
    'resize': {
        'pixel_size': 500,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'ps': {
            'false_easting': 0,
            'false_northing': 0,
            'latitude_true_scale': 70,
            'longitudinal_pole': 45
        }
    },
    'resampling_method': 'bil'

}, {'mod11a1': {
    'inputs': ['MOD11A1.A2009341.h22v06.006.2016024083416'],
    'products': ['l1', 'stats']
},
    'format': 'hdf-eos2',
    'note': 'Test1',
    'resize': {
        'pixel_size': 1000,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'sinu': {
            'central_meridian': 0,
            'false_easting': 0,
            'false_northing': 0
        }
    },
    'resampling_method': 'cc'

}, {'myd11a1': {
    'inputs': ['MYD11A1.A2006282.h22v16.006.2015299134539'],
    'products': ['l1', 'stats']
},
    'format': 'envi',
    'note': 'Test1',
    'resize': {
        'pixel_size': 0.03,
        'pixel_size_units': 'dd'
    },
    'projection': {
        'lonlat': None
    },
    'image_extents': {
        'north': -73.9,
        'south': -76.5,
        'east': 165.0,
        'west': 159.8,
        'units': 'dd'
    },
    'resampling_method': 'nn'

}, {'mod11a1': {
    'inputs': ['MOD11A1.A2006270.h08v05.005.2008120032130'],
    'products': ['l1', 'stats']
},
    'format': 'gtiff',
    'note': 'Test1',
    'resize': {
        'pixel_size': 500,
        'pixel_size_units': 'meters'
    },
    'projection': {
        'aea': {
            'central_meridian': -96,
            'datum': 'nad83',
            'false_easting': 0,
            'false_northing': 0,
            'latitude_of_origin': 23,
            'standard_parallel_1': 29.5,
            'standard_parallel_2': 45.5
        }
    },
    'resampling_method': 'cc'

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_035038_20130331_20170313_01_T1'],
    'products': ['sr', 'st']
},
    'format': 'gtiff',
    'note': 'Test1'

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_032032_20160522_20170223_01_T1'],
    'products': ['st']
},
    'format': 'gtiff',
    'note': 'Test1'

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_023027_20170227_20170325_01_T1'],
    'products': ['sr']
},
    'format': 'gtiff',
    'note': 'Test1',

    'projection': {
        'lonlat': None
    }

}, {'etm7_collection': {
    'inputs': ['LE07_L1TP_016042_20130319_20160908_01_T1'],
    'products': ['sr']
},
    'format': 'gtiff',
    'note': 'Test1',

    'projection': {
        'aea': {
            'central_meridian': -96,
            'datum': 'nad83',
            'false_easting': 0,
            'false_northing': 0,
            'latitude_of_origin': 23,
            'standard_parallel_1': 29.5,
            'standard_parallel_2': 45.5
        }
    },
    'resampling_method': 'nn'

}, {'myd13a1': {
    'inputs': ['MYD13A1.A2012265.h17v08.006.2015249154919'],
    'products': ['l1']
},
    'format': 'gtiff',
    'note': 'Test1'

}, {'myd13a2': {
    'inputs': ['MYD13A2.A2009057.h17v04.006.2015187064142'],
    'products': ['l1']
},
    'format': 'netcdf',
    'note': 'Test1',

    'projection': {
        'aea': {
            'central_meridian': 10,
            'datum': 'wgs84',
            'false_easting': 0,
            'false_northing': 0,
            'latitude_of_origin': 30,
            'standard_parallel_1': 43,
            'standard_parallel_2': 62
        }
    }

}, {'mod13a3': {
    'inputs': ['MOD13A3.A2001335.h30v08.006.2015146102643'],
    'products': ['l1']
},
    'format': 'hdf-eos2',
    'note': 'Test1',

    'resize': {
        'pixel_size': 0.04,
        'pixel_size_units': 'dd'
    },

    'projection': {
        'lonlat': None
    }

}, {'mod09a1': {
    'inputs': ['MOD09A1.A2007145.h25v06.006.2015131231048'],
    'products': ['l1']
},
    'format': 'netcdf',
    'note': 'Test1',

    'projection': {
        'aea': {
            'central_meridian': 83,
            'datum': 'nad27',
            'false_easting': 0,
            'false_northing': 0,
            'latitude_of_origin': 20,
            'standard_parallel_1': 22,
            'standard_parallel_2': 28
        }
    },
    'resampling_method': 'nn'

}, {'myd09gq': {
    'inputs': ['MYD09GQ.A2003072.h22v08.006.2015157022119'],
    'products': ['l1'],
},
    'format': 'gtiff',
    'note': 'Test1',

    'projection': {
        'sinu': {
            'central_meridian': 15,
            'false_easting': 0,
            'false_northing': 0
        }
    },
    'resampling_method': 'bil'

}, {'myd09q1': {
    'inputs': ['MYD09Q1.A2007305.h25v07.006.2015168104534'],
    'products': ['l1'],
},
    'format': 'envi',
    'note': 'Test1',

}, {'olitirs8_collection': {
    'inputs': ['LC08_L1TP_015035_20140713_20170304_01_T1'],
    'products': ['l1', 'st', 'swe']
},
    'format': 'gtiff',
    'note': 'Test1'
}],

    # ***********************************
    # ***** END OF ORIGINAL ORDERS ******
    # ***********************************

    "test": [{
        'olitirs8_collection': {
            'inputs': ['LC08_L1TP_015035_20140713_20170304_01_T1'],
            'products': ['sr', 'l1']
        },
        'format': 'gtiff',
        'note': 'test_0'
    }], "LT5_MYD13Q1": [{'myd13q1': {
        'inputs': ['MYD13Q1.A2002185.h19v05.006.2015149070403'],
        'products': ['l1']
    },
        'tm5_collection': {
            'inputs': ['LT05_L1TP_182034_20020628_20161207_01_T1'],
            'products': ['l1', 'sr_ndvi', 'sr_evi']
        },
        'format': 'envi',
        'note': 'Test1',
        'resize': {
            'pixel_size': 250,
            'pixel_size_units': 'meters'
        },
        'image_extents': {
            'west': 188945.952,
            'north': 4260854.770,
            'east': 344521.263,
            'south': 4149729.547,
            'units': 'meters'
        },
        'projection': {
            'utm': {
                'zone': 35,
                'zone_ns': 'north'
            }
        },
        'resampling_method': 'bil'

    }, {'myd13q1': {
        'inputs': ['MYD13Q1.A2002185.h19v05.006.2015149070403'],
        'products': ['l1', 'stats']
    },
        'tm5_collection': {
            'inputs': ['LT05_L1TP_182034_20020628_20161207_01_T1'],
            'products': ['l1', 'swe', 'sr_ndvi', 'stats']
        },
        'format': 'gtiff',
        'note': 'Test2',
        'resize': {
            'pixel_size': 250,
            'pixel_size_units': 'meters'
        },
        'image_extents': {
            'west': 1190082.308,
            'north': 1019317.137,
            'east': 1335074.265,
            'south': 907662.747,
            'units': 'meters'
        },
        'projection': {
            'aea': {
                'central_meridian': 10,
                'datum': 'nad27',
                'false_easting': 0,
                'false_northing': 0,
                'latitude_of_origin': 30,
                'standard_parallel_1': 43,
                'standard_parallel_2': 62
            }
        },
        'resampling_method': 'cc'

    }, {'myd13q1': {
        'inputs': ['MYD13Q1.A2002185.h19v05.006.2015149070403'],
        'products': ['l1', 'stats']
    },
        'tm5_collection': {
            'inputs': ['LT05_L1TP_182034_20020628_20161207_01_T1'],
            'products': ['l1', 'st', 'sr_ndvi', 'stats']
        },
        'format': 'envi',
        'note': 'Test3',
        'resize': {
            'pixel_size': 100,
            'pixel_size_units': 'meters'
        },
        'image_extents': {
            'west': 2048288.867,
            'north': 4254354.005,
            'east': 2217357.955,
            'south': 4095074.520,
            'units': 'meters'
        },
        'projection': {
            'sinu': {
                'central_meridian': 0,
                'false_easting': 0,
                'false_northing': 0
            }
        },
        'resampling_method': 'nn'

    }, {'myd13q1': {
        'inputs': ['MYD13Q1.A2002185.h19v05.006.2015149070403'],
        'products': ['l1', 'stats']
    },
        'tm5_collection': {
            'inputs': ['LT05_L1TP_182034_20020628_20161207_01_T1'],
            'products': ['l1', 'sr_ndvi', 'stats']
        },
        'format': 'gtiff',
        'note': 'Test4',
        'resize': {
            'pixel_size': 0.005,
            'pixel_size_units': 'dd'
        },
        'image_extents': {
            'west': 23.495342,
            'north': 38.425612,
            'east': 25.011058,
            'south': 37.021730,
            'units': 'dd'
        },
        'projection': {
            'lonlat': None
        },
        'resampling_method': 'nn'

    }], "LE07_L1TP_089079_20150815": [{'etm7_collection': {
        'inputs': ['LE07_L1TP_089079_20150815_20161022_01_T1'],
        'products': ['toa', 'sr']
    },
        'format': 'envi',
        'note': 'Test1',

        # Should fail - all fill
    }, {'etm7_collection': {
        'inputs': ['LE07_L1TP_089079_20150815_20161022_01_T1'],
        'products': ['toa', 'sr']
    },
        'format': 'gtiff',
        'note': 'Test2',
        'projection': {
            'utm': {
                'zone': 56,
                'zone_ns': 'south'
            }
        },
        'image_extents': {
            'west': 350000,
            'north': -3120000,
            'east': 398000,
            'south': -3160000,
            'units': 'meters'
        },
        'resampling_method': 'nn'

    }], "LT5_L1TP_010054_test3": [{'tm5_collection': {
        'inputs': ['LT05_L1TP_010054_20110312_20161209_01_T1'],
        'products': ['l1', 'bt', 'st']
    },
        'format': 'envi',
        'note': 'Test3',
        'resize': {
            'pixel_size': 500,
            'pixel_size_units': 'meters'
        },
        'projection': {
            'utm': {
                'zone': 18,
                'zone_ns': 'north'
            }
        },
        'resampling_method': 'nn'

    }], "LT5_L1TP_010054_test4": [{'tm5_collection': {
        'inputs': ['LT05_L1TP_010054_20110312_20161209_01_T1'],
        'products': ['sr_ndvi', 'sr_ndmi', 'sr_nbr', 'sr_nbr2',
                     'sr_savi', 'sr_msavi', 'sr_evi']
    },
        'format': 'envi',
        'note': 'Test4',
        'resize': {
            'pixel_size': 500,
            'pixel_size_units': 'meters'
        },
        'projection': {
            'sinu': {
                'central_meridian': -76.6,
                'false_easting': 0,
                'false_northing': 0
            }
        },
        'resampling_method': 'nn'

    }], "LT5_L1TP_010054_test5": [{'tm5_collection': {
        'inputs': ['LT05_L1TP_010054_20110312_20161209_01_T1'],
        'products': ['swe']
    },
        'format': 'gtiff',
        'note': 'Test5',

    }], "LE07_t4": [{'etm7_collection': {
        'inputs': ['LE07_L1TP_039037_20080712_20160922_01_T1'],
        'products': ['sr']
    },
        'format': 'gtiff',
        'note': 'Test4',
        'resize': {
            'pixel_size': 500,
            'pixel_size_units': 'meters'
        },
        'projection': {
            'aea': {
                'central_meridian': -96,
                'datum': 'nad83',
                'false_easting': 0,
                'false_northing': 0,
                'latitude_of_origin': 23,
                'standard_parallel_1': 29.5,
                'standard_parallel_2': 45.5
            }
        },
        'resampling_method': 'nn'

    }], "LE07_T2": [{'etm7_collection': {
        'inputs': ['LE07_L1TP_039037_20080712_20160922_01_T1'],
        'products': ['l1', 'bt']
    },
        'format': 'envi',
        'note': 'Test2',
        'resize': {
            'pixel_size': 500,
            'pixel_size_units': 'meters'
        },
        'projection': {
            'utm': {
                'zone': 11,
                'zone_ns': 'north'
            }
        },
        'resampling_method': 'nn'

    }], "LE07_L1GT_T2": [{'etm7_collection': {
        'inputs': ['LE07_L1GT_210117_20130302_20161125_01_T2'],
        'products': ['l1', 'source_metadata', 'sr']
    },
        'format': 'envi',
        'note': 'Test2',
        'resize': {
            'pixel_size': 0.0025,
            'pixel_size_units': 'dd'
        },
        'projection': {
            'lonlat': None
        },
        'resampling_method': 'nn'

    }], "reruns": [{'etm7_collection': {
        'inputs': ['LE07_L1TP_200025_20000831_20170210_01_T1'],
        'products': ['source_metadata', 'sr', 'swe', 'sr_ndvi']
    },
        'format': 'envi',
        'note': 'Test1'

    }, {'etm7_collection': {
        'inputs': ['LE07_L1TP_195021_20150907_20161021_01_T1'],
        'products': ['toa', 'bt', 'sr_evi', 'swe']
    },
        'format': 'netcdf',
        'note': 'Test2',
        'projection': {
            'lonlat': None
        },
        'resize': {
            'pixel_size': 0.004,
            'pixel_size_units': 'dd'
        },
        'image_extents': {
            'west': 12,
            'north': 56,
            'east': 13,
            'south': 55.5,
            'units': 'dd'
        },
        'resampling_method': 'cc'

    }, {'olitirs8_collection': {
        'inputs': ['LC08_L1TP_047027_20131014_20170308_01_T1'],
        'products': ['toa']
    },
        'format': 'envi',
        'note': 'Test5',
        'resize': {
            'pixel_size': 2000,
            'pixel_size_units': 'meters'
        },
        'projection': {
            'utm': {
                'zone': 11,
                'zone_ns': 'north'
            }
        },
        'resampling_method': 'cc'

    }, {'olitirs8_collection': {
        'inputs': ['LC08_L1TP_047027_20131014_20170308_01_T1'],
        'products': ['l1']
    },
        'format': 'hdf-eos2',
        'note': 'Test3',
        'resize': {
            'pixel_size': 2000,
            'pixel_size_units': 'meters'
        },
        'projection': {
            'aea': {
                'latitude_of_origin': 23,
                'datum': 'nad83',
                'central_meridian': -96,
                'standard_parallel_1': 29.5,
                'standard_parallel_2': 45.5,
                'false_easting': 0,
                'false_northing': 0
            }
        },
        'resampling_method': 'bil'

    }, {'olitirs8_collection': {
        'inputs': ['LC08_L1TP_047027_20131014_20170308_01_T1'],
        'products': ['sr', 'toa', 'sr_ndvi']
    },
        'format': 'envi',
        'note': 'Test1',

    }, {'etm7_collection': {
        'inputs': ['LE07_L1GT_210117_20130302_20161125_01_T2'],
        'products': ['sr_ndvi', 'sr_ndmi', 'sr_nbr', 'sr_nbr2',
                     'sr_savi', 'sr_msavi', 'sr_evi']
    },
        'format': 'gtiff',
        'note': 'Test4',
        'resize': {
            'pixel_size': 500,
            'pixel_size_units': 'meters'
        },
        'projection': {
            'ps': {
                'false_easting': 0,
                'false_northing': 0,
                'latitude_true_scale': -90,
                'longitudinal_pole': 0
            }
        },
        'resampling_method': 'nn'

    }], "L8_retry": [{'olitirs8_collection': {
        'inputs': ['LC08_L1TP_047027_20131014_20170308_01_T1'],
        'products': ['sr', 'toa', 'sr_ndvi']
    },
        'format': 'envi',
        'note': 'Test1',

        # ***********************
        # ***** BRIDGE TEST *****
        # ***********************

    }], "bridge_test": [{"olitirs8_collection": {
        "inputs": ["LC08_L1TP_015035_20140713_20170304_01_T1",
                   "LC08_L1TP_022032_20130828_20170309_01_T1",
                   "LC08_L1TP_032032_20160522_20170223_01_T1",
                   "LC08_L1TP_035038_20130331_20170313_01_T1",
                   "LC08_L1TP_047027_20131014_20170308_01_T1",
                   "LC08_L1GT_066017_20130917_20170308_01_T2"],

        "products": ["sr", "st", "swe"]
    },
        "format": "gtiff",
        "note": "LC08"},

        {"etm7_collection": {
            "inputs": ["LE07_L1TP_022033_20140228_20160905_01_T1"],
            "products": ["sr", "st", "swe"]
        },
            "format": "gtiff",
            "note": "LE07"},

        {"tm4_collection": {
            "inputs": ["LT04_L1TP_035027_19890712_20161001_01_T1"],
            "products": ["sr", "st", "swe"]
        },
            "format": "gtiff",
            "note": "LT04"
        }

    ], "bridge_test_full": [{"olitirs8_collection": {
        "inputs": ["LC08_L1TP_015035_20140713_20170304_01_T1",
                   "LC08_L1TP_022032_20130828_20170309_01_T1",
                   "LC08_L1TP_032032_20160522_20170223_01_T1",
                   "LC08_L1TP_035038_20130331_20170313_01_T1",
                   "LC08_L1TP_047027_20131014_20170308_01_T1",
                   "LC08_L1GT_066017_20130917_20170308_01_T2"],

        "products": ["sr", "st", "swe", "toa", "bt"]
    },
        "format": "gtiff",
        "note": "utmLC08"},

        {"etm7_collection": {
            "inputs": ["LE07_L1TP_022033_20140228_20160905_01_T1"],
            "products": ["sr", "st", "swe", "toa", "bt"]
        },
            "format": "gtiff",
            "note": "utmLE07"},

        {"tm4_collection": {
            "inputs": ["LT04_L1TP_035027_19890712_20161001_01_T1"],
            "products": ["sr", "st", "swe", "toa", "bt"]
        },
            "format": "gtiff",
            "note": "utmLT04"
        }

    ],     "bridge_test_albers": [{"olitirs8_collection": {
        "inputs": ["LC08_L1TP_015035_20140713_20170304_01_T1",
                   "LC08_L1TP_022032_20130828_20170309_01_T1",
                   "LC08_L1TP_032032_20160522_20170223_01_T1",
                   "LC08_L1TP_035038_20130331_20170313_01_T1",
                   "LC08_L1TP_047027_20131014_20170308_01_T1",
                   "LC08_L1GT_066017_20130917_20170308_01_T2"],

        "products": ["sr", "st", "swe", "toa", "bt"]
    },
        "format": "gtiff",
        "note": "btest",
        'projection': {
                          'aea': {
                              'central_meridian': -96,
                              'datum': 'wgs84',
                              'false_easting': 0,
                              'false_northing': 0,
                              'latitude_of_origin': 23,
                              'standard_parallel_1': 29.5,
                              'standard_parallel_2': 45.5
                          }
                      }},

        {"etm7_collection": {
            "inputs": ["LE07_L1TP_022033_20140228_20160905_01_T1"],
            "products": ["sr", "st", "swe", "toa", "bt"]
        },
            "format": "gtiff",
            "note": "btest",
        'projection': {
                          'aea': {
                              'central_meridian': -96,
                              'datum': 'wgs84',
                              'false_easting': 0,
                              'false_northing': 0,
                              'latitude_of_origin': 23,
                              'standard_parallel_1': 29.5,
                              'standard_parallel_2': 45.5
                          }
                      }},

        {"tm4_collection": {
            "inputs": ["LT04_L1TP_035027_19890712_20161001_01_T1"],
            "products": ["sr", "st", "swe", "toa", "bt"]
        },
            "format": "gtiff",
            "note": "btest",
            'projection': {
                'aea': {
                    'central_meridian': -96,
                    'datum': 'wgs84',
                    'false_easting': 0,
                    'false_northing': 0,
                    'latitude_of_origin': 23,
                    'standard_parallel_1': 29.5,
                    'standard_parallel_2': 45.5
                }
            }

        }

    ]
}
