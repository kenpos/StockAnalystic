from arelle import ModelManager
from arelle import Cntlr

class jpsps110400:#特定有価証券の内容等の開示に関する内閣府令 第十一号の四様式 半期報告書
	CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo114SemiannualSecuritiesReportHeading = '' #特定有価証券の内容等の開示に関する内閣府令 第十一号の四様式 半期報告書 [目次項目]
	FinancialInformationAboutSpecificTrustPropertyHeading = '' #特定信託財産の経理状況 [目次項目]
	SemiAnnualBalanceSheetHeading = '' #中間貸借対照表 [目次項目]
	SemiAnnualBalanceSheetTextBlock = '' #中間貸借対照表 [テキストブロック]
	SemiAnnualStatementOfIncomeHeading = '' #中間損益計算書 [目次項目]
	SemiAnnualStatementOfIncomeTextBlock = '' #中間損益計算書 [テキストブロック]

	def __init__(self,xbrl_file):
		ctrl = Cntlr.Cntlr()
		model_manager = ModelManager.initialize(ctrl)
		self.model_xbrl = model_manager.load(xbrl_file)
	def setInfo(self, edinet_info_list):
		for fact in self.model_xbrl.facts:
			if fact.concept.qname.localName == 'EDINETCodeDEI':
				self.edinet_code = fact.value
				for code_name in edinet_info_list:
					if code_name[0] == self.edinet_code:
						self.industry_code = code_name[1]
						break
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo114SemiannualSecuritiesReportHeading': #特定有価証券の内容等の開示に関する内閣府令 第十一号の四様式 半期報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo114SemiannualSecuritiesReportHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationAboutSpecificTrustPropertyHeading': #特定信託財産の経理状況 [目次項目]
				self.FinancialInformationAboutSpecificTrustPropertyHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualBalanceSheetHeading': #中間貸借対照表 [目次項目]
				self.SemiAnnualBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualBalanceSheetTextBlock': #中間貸借対照表 [テキストブロック]
				self.SemiAnnualBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfIncomeHeading': #中間損益計算書 [目次項目]
				self.SemiAnnualStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfIncomeTextBlock': #中間損益計算書 [テキストブロック]
				self.SemiAnnualStatementOfIncomeTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo114SemiannualSecuritiesReportHeading(self): #特定有価証券の内容等の開示に関する内閣府令 第十一号の四様式 半期報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo114SemiannualSecuritiesReportHeading

	def getFinancialInformationAboutSpecificTrustPropertyHeading(self): #特定信託財産の経理状況 [目次項目]
		return self.FinancialInformationAboutSpecificTrustPropertyHeading

	def getSemiAnnualBalanceSheetHeading(self): #中間貸借対照表 [目次項目]
		return self.SemiAnnualBalanceSheetHeading

	def getSemiAnnualBalanceSheetTextBlock(self): #中間貸借対照表 [テキストブロック]
		return self.SemiAnnualBalanceSheetTextBlock

	def getSemiAnnualStatementOfIncomeHeading(self): #中間損益計算書 [目次項目]
		return self.SemiAnnualStatementOfIncomeHeading

	def getSemiAnnualStatementOfIncomeTextBlock(self): #中間損益計算書 [テキストブロック]
		return self.SemiAnnualStatementOfIncomeTextBlock
