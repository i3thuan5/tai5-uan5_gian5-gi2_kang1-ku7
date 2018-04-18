'''
Created on 2018年4月12日

@author: wenli
'''


聲對照表 = {
    'p': 'p', 'ph': 'ph', 'm': 'm', 'b': 'b',
    't': 't', 'th': 'th', 'n': 'n', 'l': 'l',
    'k': 'k', 'kh': 'kh', 'ng': 'ng', 'g': 'g',
    'ts': 'ch', 'tsh': 'chh', 's': 's', 'j': 'j',
    'h': 'h', '': '',
}

韻對照表 = {
    'a': 'a', 'am': 'am', 'an': 'an', 'ang': 'ang',
    'ah': 'ah', 'ap': 'ap', 'at': 'at', 'ak': 'ak',
    'ann': 'aⁿ', 'annh': 'ahⁿ',

    'ai': 'ai',
    'aih': 'aih',
    'ainn': 'aiⁿ', 'ainnh': 'aihⁿ',

    'au': 'au',
    'auh': 'auh', 'aunn': 'auⁿ', 'aunnh': 'auhⁿ',

    'e': 'e',
    'eh': 'eh',
    'enn': 'eⁿ', 'ennh': 'ehⁿ',

    'ia': 'ia', 'iam': 'iam', 'ian': 'ian', 'iang': 'iang',
    'iah': 'iah', 'iap': 'iap', 'iat': 'iat', 'iak': 'iak',
    'iann': 'iaⁿ', 'iannh': 'iahⁿ',

    'iau': 'iau',
    'iauh': 'iauh',
    'iaunn': 'iauⁿ', 'iaunnh': 'iauhⁿ',

    'i': 'i', 'im': 'im', 'in': 'in', 'ing': 'ing',
    'ih': 'ih', 'ip': 'ip', 'it': 'it', 'ik': 'ik',
    'inn': 'iⁿ', 'innh': 'ihⁿ',

    'io': 'io',
    'ioh': 'ioh',

    # 寫法上不存在-ook, -oong, -oonn
    # 臺羅手冊：-ok, -ong, -onn的-o為-oo的簡寫，因為該音節不存在o和oo的差別
    'ioo': '', 'iong': 'iong',
    'iooh': '', 'iok': 'iok',
    'ionn': 'ioⁿ',

    'iu': 'iu',
    # TODO: 不會有iut
    'iuh': 'iuh',  # 'iut': 'iut',
    'iunn': 'iuⁿ', 'iunnh': 'iuhⁿ',

    'm': 'm', 'ng': 'ng',
    'mh': 'mh', 'ngh': 'ngh',

    'o': 'o',
    'oh': 'oh', 'op': 'op',

    # TODO: 確認om是唸oo
    'oo': '', 'om': 'om', 'ong': 'ong',
    'ooh': '', 'ok': 'ok',
    'onn': 'oⁿ', 'onnh': 'ohⁿ',

    # TODO: 不會有oi
    #     'oi': '', 'oih': '',

    'ua': 'oa', 'uan': 'oan',
    # TODO: 不會有oak、oap
    'uah': 'oah', 'uat': 'oat',  # 'uak': 'oak',
    'uann': 'oaⁿ', 'uannh': 'oahⁿ',

    'uai': 'oai',
    'uaih': 'oaih',
    'uainn': 'oaiⁿ', 'uainnh': 'oaihⁿ',

    'ue': 'oe',
    'ueh': 'oeh',
    'uenn': 'oeⁿ', 'uennh': 'oehⁿ',

    'ui': 'ui',
    'uih': 'uih',
    'uinn': 'uiⁿ', 'uinnh': 'uihⁿ',

    'u': 'u', 'un': 'un',
    'uh': 'uh', 'ut': 'ut',

    #     # 下跤是次方言
    #     'or': '', 'orh': '', 'ior': '', 'iorh': '',
    #     'eng': '',
    #     'ee': '', 'eeh': '', 'uee': '',  # 有問題
    #     'ir': '', 'irh': '', 'irp': '', 'irt': '', 'irk': '',  # 有問題
    #     'irm': '', 'irn': '', 'irng': '', 'irinn': '',  # 有問題
    #     'er': '', 'erh': '', 'erm': '', 'erm': '',
    #     'ere': '', 'ereh': '',
    #     'ie': '', 'uang': '',
}

調對照表 = {
    '1': '1', '7': '7', '3': '3', '2': '2', '5': '5',
    '8': '8', '4': '4', '10': '10', '9': '9',
    '6': '6', '0': '0',
}
