#!/usr/bin/python
# -*- encoding: utf-8 -*-
import json as j

from pond.factory.fish_factory import FishFactory
from pond.seed.fish_company import FishCompany

FISH_COMPANY_SEED = 'fish_company'

FISH_COMPANY_DICT = {
    'id': None,
    'gmt_create': None,
    'gmt_modified': None,
    'code': None,
    'short_name': '$.data.company.org_short_name_cn',
    'company_name': '$.data.company.org_name_cn',
    'country_region': '$.data.company.provincial_name',
    'business_mode': '$.data.company.classi_name',
    'main_business': '$.data.company.main_operation_business',
    'company_desc': '$.data.company.org_cn_introduction',
    'establish_date': '$.data.company.established_date',
    'employees': '$.data.company.staff_num',
    'listing_date': '$.data.company.listed_date',
    'shares_offered': '$.data.company.actual_issue_vol',
    'initial_price': '$.data.company.issue_price',
    'initial_pe': '$.data.company.pe_after_issuing'
}

if __name__ == '__main__':
    company = FishCompany()

    url = company.build_url('SH600613')
    header = company.build_header('SH600613')

    val = '{"data":{"company":{"org_id":"02600613","org_name_cn":"上海神奇制药投资管理股份有限公司","org_short_name_cn":"神奇制药","org_name_en":"Shanghai Shenqi Pharmaceutical Investment Management Co.,Ltd.","org_short_name_en":"Shenqi","main_operation_business":"药品的研发、生产与销售。","operating_scope":"　　在国家法律允许和政策鼓励的范围内进行投资管理（以医药领域为主）。【依法须经批准的项目，经相关部门批准后方可开展经营活动】","district_encode":"310115","org_cn_introduction":"上海神奇制药投资管理股份有限公司的主营业务为药品的研发、生产与销售。主要产品包括斑蝥酸钠维生素B6注射液、斑蝥酸钠注射液、枇杷止咳颗粒、强力枇杷露、枇杷止咳胶囊、金乌骨通胶囊、珊瑚癣净、精乌胶囊、全天麻胶囊、银丹心泰滴丸等。公司“神奇”品牌具有超过30年的经营历史,是获国家工商总局评定的“中国驰名商标”,多次荣登荣获世界品牌实验室中国500强最具价值品牌排行榜、中国医药最具影响力“中国制造100强”、“中国医药行业成长50强”等荣誉称号。中国非处方药协会公布的“2019年度中国非处方药生产企业综合统计排名”,公司综合统计排名第82名;子公司金桥药业产品“珊瑚癣净”位列2019年度中国非处方药产品综合统计排名皮肤科类药物第8名;子公司神奇药业产品“枇杷止咳颗粒/胶囊”位列2019年度中国非处方药产品综合统计排名止咳化痰平喘类药物第13名。","legal_representative":"张芝庭","general_manager":"冯斌","secretary":"吴克兢","established_date":711734400000,"reg_asset":5.34071628E8,"staff_num":1371,"telephone":"86-21-53750009","postcode":"200003","fax":"86-21-53750010","email":"shanghaiys@126.com","org_website":"www.gzsq.com","reg_address_cn":"上海市浦东新区上川路995号","reg_address_en":"","office_address_cn":"上海市浦东新区威海路128号长发大厦613室","office_address_en":"","currency_encode":"019001","currency":"CNY","listed_date":714240000000,"provincial_name":"上海市","actual_controller":"文邦英 (25.48%)，张芝庭 (20.12%)","classi_name":"民营企业","pre_name_cn":"上海永生投资管理股份有限公司","chairman":"张芝庭","executives_nums":12,"actual_issue_vol":500000.0,"issue_price":72.0,"actual_rc_net_amt":3.6E7,"pe_after_issuing":null,"online_success_rate_of_issue":null,"affiliate_industry":{"ind_code":"BK0040","ind_name":"化学制药"}}},"error_code":0,"error_description":""}'

    fatctory = FishFactory()
    num = fatctory.build(j.loads(val), FISH_COMPANY_DICT, FISH_COMPANY_SEED)
    print("num={}".format(num))
    # res = get(url, header)
    # print(res)
