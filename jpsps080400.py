from arelle import ModelManager
from arelle import Cntlr

class jpsps080400:#特定有価証券の内容等の開示に関する内閣府令 第八号の四様式 有価証券報告書
	CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo84AnnualSecuritiesReportHeading = '' #特定有価証券の内容等の開示に関する内閣府令 第八号の四様式 有価証券報告書 [目次項目]
	InformationAboutSpecificTrustPropertyHeading = '' #特定信託財産情報 [目次項目]
	FinancialInformationAboutSpecificTrustPropertyHeading = '' #特定信託財産の経理状況 [目次項目]
	BalanceSheetHeading = '' #貸借対照表 [目次項目]
	BalanceSheetTextBlock = '' #貸借対照表 [テキストブロック]
	StatementOfIncomeHeading = '' #損益計算書 [目次項目]
	StatementOfIncomeTextBlock = '' #損益計算書 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo84AnnualSecuritiesReportHeading': #特定有価証券の内容等の開示に関する内閣府令 第八号の四様式 有価証券報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo84AnnualSecuritiesReportHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutSpecificTrustPropertyHeading': #特定信託財産情報 [目次項目]
				self.InformationAboutSpecificTrustPropertyHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationAboutSpecificTrustPropertyHeading': #特定信託財産の経理状況 [目次項目]
				self.FinancialInformationAboutSpecificTrustPropertyHeading = fact.value

			elif fact.concept.qname.localName == 'BalanceSheetHeading': #貸借対照表 [目次項目]
				self.BalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'BalanceSheetTextBlock': #貸借対照表 [テキストブロック]
				self.BalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfIncomeHeading': #損益計算書 [目次項目]
				self.StatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfIncomeTextBlock': #損益計算書 [テキストブロック]
				self.StatementOfIncomeTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo84AnnualSecuritiesReportHeading(self): #特定有価証券の内容等の開示に関する内閣府令 第八号の四様式 有価証券報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo84AnnualSecuritiesReportHeading

	def getInformationAboutSpecificTrustPropertyHeading(self): #特定信託財産情報 [目次項目]
		return self.InformationAboutSpecificTrustPropertyHeading

	def getFinancialInformationAboutSpecificTrustPropertyHeading(self): #特定信託財産の経理状況 [目次項目]
		return self.FinancialInformationAboutSpecificTrustPropertyHeading

	def getBalanceSheetHeading(self): #貸借対照表 [目次項目]
		return self.BalanceSheetHeading

	def getBalanceSheetTextBlock(self): #貸借対照表 [テキストブロック]
		return self.BalanceSheetTextBlock

	def getStatementOfIncomeHeading(self): #損益計算書 [目次項目]
		return self.StatementOfIncomeHeading

	def getStatementOfIncomeTextBlock(self): #損益計算書 [テキストブロック]
		return self.StatementOfIncomeTextBlock
