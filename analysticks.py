import os
import zipfile
from arelle import ModelManager
from arelle import Cntlr
import pandas as pd
from pathlib import Path
import glob
import inspect



from jpcrp030200 import jpcrp030200

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

    kubota = jpcrp030200(xbrl_file)
    
    edinetcodedlinfo_filepath = '.\\EdinetcodeDlInfo.csv'
    edinet_info_list = makeEdinetCompInfoList(edinetcodedlinfo_filepath)
    
    kubota.setInfo(edinet_info_list)
    
    # print('会社名',kubota.getCompanyNameCoverPage())
    # print('従業員数',kubota.getNumberOfEmployees())
    # print('売上高',kubota.getNetSales())
    # print('資本金',kubota.getCapitalStockSummaryOfBusinessResults())
    # print('潜在株式調整後１株当たり当期純利益',kubota.getDilutedEarningsPerShareSummaryOfBusinessResults())
    # print('自己資本比率',kubota.getEquityToAssetRatioSummaryOfBusinessResults())   

    for m in inspect.getmembers(kubota):
        print(m)
    

    
if __name__ == "__main__":
    main()