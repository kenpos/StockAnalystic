import os
import zipfile
from arelle import ModelManager
from arelle import Cntlr
import pandas as pd
from pathlib import Path
import glob

class CompanyData:
    edinet_company_info_list = []
    edinet_code = ""  # EDINETCODE
    company_name_jp = ""  # 企業名
    industry_code = ""  # 業種
    DilutedEarningsPerShareSummaryOfBusinessResults = ""#潜在株式調整後１株当たり当期純利益
    EquityToAssetRatioSummaryOfBusinessResults = ""#自己資本比率
    CapitalStockSummaryOfBusinessResults ="" #資本金
    model_xbrl =""
    
    def __init__(self,xbrl_file):
        ctrl = Cntlr.Cntlr()
        model_manager = ModelManager.initialize(ctrl)
        self.model_xbrl = model_manager.load(xbrl_file)
        
    def setCompanyInfo(self,edinet_info_list):
        for fact in self.model_xbrl.facts:
            print(fact)
            
            if fact.concept.qname.localName == 'EDINETCodeDEI':
                self.edinet_code = fact.value
                for code_name in edinet_info_list:
                    if code_name[0] == self.edinet_code:
                        self.industry_code = code_name[1]
                        break
            elif fact.concept.qname.localName == 'CompanyNameCoverPage': #企業名
                self.company_name_jp = fact.value
            elif fact.concept.qname.localName == 'CapitalStockSummaryOfBusinessResults':#資本金
                self.CapitalStockSummaryOfBusinessResults = fact.value
            elif fact.concept.qname.localName == 'DilutedEarningsPerShareSummaryOfBusinessResults': #自己資本比率
                self.DilutedEarningsPerShareSummaryOfBusinessResults = fact.value
            elif fact.concept.qname.localName == 'EquityToAssetRatioSummaryOfBusinessResults': #
                self.EquityToAssetRatioSummaryOfBusinessResults = fact.value

    def getCompanyName(self):
        return self.company_name_jp
    
    def getIndastoryCode(self):
        return self.industry_code
    
    def getCompanyInfo(self):
        return [self.edinet_code,self.industry_code,self.company_name_jp]

    def getBusinessResult(self):
        return self.DilutedEarningsPerShareSummaryOfBusinessResults

    def getCapitalStockSummaryOfBusinessResults(self):
        return self.CapitalStockSummaryOfBusinessResults

    def getSummary(self):
        return self.EquityToAssetRatioSummaryOfBusinessResults
    
def makeEdinetCompInfoList(edinetcodedlinfo_filepath):
    edinet_info = pd.read_csv(edinetcodedlinfo_filepath, skiprows=1,
                                 encoding='cp932')
    edinet_info = edinet_info[["ＥＤＩＮＥＴコード", "提出者業種"]]
    edinet_info_list = edinet_info.values.tolist()
    return edinet_info_list


def main():
    # ZIPファイルのパス
    zip_file_path = 'S100FFK6_有価証券報告書_株式会社　クボタ.zip'

    # 一時フォルダを作成
    temp_dir = 'temp'
    os.makedirs(temp_dir, exist_ok=True)

    # ZIPファイルを一時フォルダに展開
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        zip_file.extractall(temp_dir)
    
    xbrl_file = glob.glob(temp_dir+'/**/PublicDoc/*.xbrl')[0]
    # print(files[0])
    
    # xbrl_file = getXBRLFilePath(temp_dir)

    kubota = CompanyData(xbrl_file)
    
    edinetcodedlinfo_filepath = '.\\EdinetcodeDlInfo.csv'
    edinet_info_list = makeEdinetCompInfoList(edinetcodedlinfo_filepath)
    
    kubota.setCompanyInfo(edinet_info_list)
    
    # print('会社名',kubota.getCompanyName())
    # print('資本金',kubota.getCapitalStockSummaryOfBusinessResults())
    # print('潜在株式調整後１株当たり当期純利益',kubota.getBusinessResult())
    # print('自己資本比率',kubota.getSummary())

    

if __name__ == "__main__":
    main()