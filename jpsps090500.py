from arelle import ModelManager
from arelle import Cntlr

class jpsps090500:#特定有価証券の内容等の開示に関する内閣府令 第九号の五様式 有価証券報告書
	CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo95AnnualSecuritiesReportHeading = '' #特定有価証券の内容等の開示に関する内閣府令 第九号の五様式 有価証券報告書 [目次項目]
	FinancialInformationOfPartnershipEtcHeading = '' #組合等の経理状況 [目次項目]
	FinancialStatementsHeading = '' #財務諸表 [目次項目]
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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo95AnnualSecuritiesReportHeading': #特定有価証券の内容等の開示に関する内閣府令 第九号の五様式 有価証券報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo95AnnualSecuritiesReportHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationOfPartnershipEtcHeading': #組合等の経理状況 [目次項目]
				self.FinancialInformationOfPartnershipEtcHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialStatementsHeading': #財務諸表 [目次項目]
				self.FinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'BalanceSheetHeading': #貸借対照表 [目次項目]
				self.BalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'BalanceSheetTextBlock': #貸借対照表 [テキストブロック]
				self.BalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfIncomeHeading': #損益計算書 [目次項目]
				self.StatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfIncomeTextBlock': #損益計算書 [テキストブロック]
				self.StatementOfIncomeTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo95AnnualSecuritiesReportHeading(self): #特定有価証券の内容等の開示に関する内閣府令 第九号の五様式 有価証券報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo95AnnualSecuritiesReportHeading

	def getFinancialInformationOfPartnershipEtcHeading(self): #組合等の経理状況 [目次項目]
		return self.FinancialInformationOfPartnershipEtcHeading

	def getFinancialStatementsHeading(self): #財務諸表 [目次項目]
		return self.FinancialStatementsHeading

	def getBalanceSheetHeading(self): #貸借対照表 [目次項目]
		return self.BalanceSheetHeading

	def getBalanceSheetTextBlock(self): #貸借対照表 [テキストブロック]
		return self.BalanceSheetTextBlock

	def getStatementOfIncomeHeading(self): #損益計算書 [目次項目]
		return self.StatementOfIncomeHeading

	def getStatementOfIncomeTextBlock(self): #損益計算書 [テキストブロック]
		return self.StatementOfIncomeTextBlock
