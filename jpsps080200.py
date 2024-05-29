from arelle import ModelManager
from arelle import Cntlr

class jpsps080200:#特定有価証券の内容等の開示に関する内閣府令 第八号の二様式 有価証券報告書
	CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo82AnnualSecuritiesReportHeading = '' #特定有価証券の内容等の開示に関する内閣府令 第八号の二様式 有価証券報告書 [目次項目]
	InformationAboutIssuerAndPartiesInvolvedHeading = '' #発行者及び関係法人情報 [目次項目]
	InformationAboutIssuerHeading = '' #発行者の状況 [目次項目]
	FinancialInformationHeading = '' #経理の状況 [目次項目]
	BalanceSheetHeading = '' #貸借対照表 [目次項目]
	BalanceSheetTextBlock = '' #貸借対照表 [テキストブロック]
	StatementOfIncomeHeading = '' #損益計算書 [目次項目]
	StatementOfIncomeTextBlock = '' #損益計算書 [テキストブロック]
	StatementOfMembersEquityHeading = '' #社員資本等変動計算書 [目次項目]
	StatementOfMembersEquityTextBlock = '' #社員資本等変動計算書 [テキストブロック]
	StatementOfCashFlowsHeading = '' #キャッシュ・フロー計算書 [目次項目]
	StatementOfCashFlowsTextBlock = '' #キャッシュ・フロー計算書 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo82AnnualSecuritiesReportHeading': #特定有価証券の内容等の開示に関する内閣府令 第八号の二様式 有価証券報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo82AnnualSecuritiesReportHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIssuerAndPartiesInvolvedHeading': #発行者及び関係法人情報 [目次項目]
				self.InformationAboutIssuerAndPartiesInvolvedHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIssuerHeading': #発行者の状況 [目次項目]
				self.InformationAboutIssuerHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationHeading': #経理の状況 [目次項目]
				self.FinancialInformationHeading = fact.value

			elif fact.concept.qname.localName == 'BalanceSheetHeading': #貸借対照表 [目次項目]
				self.BalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'BalanceSheetTextBlock': #貸借対照表 [テキストブロック]
				self.BalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfIncomeHeading': #損益計算書 [目次項目]
				self.StatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfIncomeTextBlock': #損益計算書 [テキストブロック]
				self.StatementOfIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfMembersEquityHeading': #社員資本等変動計算書 [目次項目]
				self.StatementOfMembersEquityHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfMembersEquityTextBlock': #社員資本等変動計算書 [テキストブロック]
				self.StatementOfMembersEquityTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashFlowsHeading': #キャッシュ・フロー計算書 [目次項目]
				self.StatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashFlowsTextBlock': #キャッシュ・フロー計算書 [テキストブロック]
				self.StatementOfCashFlowsTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo82AnnualSecuritiesReportHeading(self): #特定有価証券の内容等の開示に関する内閣府令 第八号の二様式 有価証券報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo82AnnualSecuritiesReportHeading

	def getInformationAboutIssuerAndPartiesInvolvedHeading(self): #発行者及び関係法人情報 [目次項目]
		return self.InformationAboutIssuerAndPartiesInvolvedHeading

	def getInformationAboutIssuerHeading(self): #発行者の状況 [目次項目]
		return self.InformationAboutIssuerHeading

	def getFinancialInformationHeading(self): #経理の状況 [目次項目]
		return self.FinancialInformationHeading

	def getBalanceSheetHeading(self): #貸借対照表 [目次項目]
		return self.BalanceSheetHeading

	def getBalanceSheetTextBlock(self): #貸借対照表 [テキストブロック]
		return self.BalanceSheetTextBlock

	def getStatementOfIncomeHeading(self): #損益計算書 [目次項目]
		return self.StatementOfIncomeHeading

	def getStatementOfIncomeTextBlock(self): #損益計算書 [テキストブロック]
		return self.StatementOfIncomeTextBlock

	def getStatementOfMembersEquityHeading(self): #社員資本等変動計算書 [目次項目]
		return self.StatementOfMembersEquityHeading

	def getStatementOfMembersEquityTextBlock(self): #社員資本等変動計算書 [テキストブロック]
		return self.StatementOfMembersEquityTextBlock

	def getStatementOfCashFlowsHeading(self): #キャッシュ・フロー計算書 [目次項目]
		return self.StatementOfCashFlowsHeading

	def getStatementOfCashFlowsTextBlock(self): #キャッシュ・フロー計算書 [テキストブロック]
		return self.StatementOfCashFlowsTextBlock
