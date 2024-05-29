from arelle import ModelManager
from arelle import Cntlr

class jpsps110200:#特定有価証券の内容等の開示に関する内閣府令 第十一号の二様式 半期報告書
	CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo112SemiannualSecuritiesReportHeading = '' #特定有価証券の内容等の開示に関する内閣府令 第十一号の二様式 半期報告書 [目次項目]
	InformationAboutIssuerAndPartiesInvolvedHeading = '' #発行者及び関係法人情報 [目次項目]
	InformationAboutIssuerHeading = '' #発行者の状況 [目次項目]
	FinancialInformationHeading = '' #経理の状況 [目次項目]
	SemiAnnualBalanceSheetHeading = '' #中間貸借対照表 [目次項目]
	SemiAnnualBalanceSheetTextBlock = '' #中間貸借対照表 [テキストブロック]
	SemiAnnualStatementOfIncomeHeading = '' #中間損益計算書 [目次項目]
	SemiAnnualStatementOfIncomeTextBlock = '' #中間損益計算書 [テキストブロック]
	SemiAnnualStatementOfMembersEquityHeading = '' #中間社員資本等変動計算書 [目次項目]
	SemiAnnualStatementOfMembersEquityTextBlock = '' #中間社員資本等変動計算書 [テキストブロック]
	SemiAnnualStatementOfCashFlowsHeading = '' #中間キャッシュ・フロー計算書 [目次項目]
	SemiAnnualStatementOfCashFlowsTextBlock = '' #中間キャッシュ・フロー計算書 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo112SemiannualSecuritiesReportHeading': #特定有価証券の内容等の開示に関する内閣府令 第十一号の二様式 半期報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo112SemiannualSecuritiesReportHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIssuerAndPartiesInvolvedHeading': #発行者及び関係法人情報 [目次項目]
				self.InformationAboutIssuerAndPartiesInvolvedHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIssuerHeading': #発行者の状況 [目次項目]
				self.InformationAboutIssuerHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationHeading': #経理の状況 [目次項目]
				self.FinancialInformationHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualBalanceSheetHeading': #中間貸借対照表 [目次項目]
				self.SemiAnnualBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualBalanceSheetTextBlock': #中間貸借対照表 [テキストブロック]
				self.SemiAnnualBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfIncomeHeading': #中間損益計算書 [目次項目]
				self.SemiAnnualStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfIncomeTextBlock': #中間損益計算書 [テキストブロック]
				self.SemiAnnualStatementOfIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfMembersEquityHeading': #中間社員資本等変動計算書 [目次項目]
				self.SemiAnnualStatementOfMembersEquityHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfMembersEquityTextBlock': #中間社員資本等変動計算書 [テキストブロック]
				self.SemiAnnualStatementOfMembersEquityTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfCashFlowsHeading': #中間キャッシュ・フロー計算書 [目次項目]
				self.SemiAnnualStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfCashFlowsTextBlock': #中間キャッシュ・フロー計算書 [テキストブロック]
				self.SemiAnnualStatementOfCashFlowsTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo112SemiannualSecuritiesReportHeading(self): #特定有価証券の内容等の開示に関する内閣府令 第十一号の二様式 半期報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo112SemiannualSecuritiesReportHeading

	def getInformationAboutIssuerAndPartiesInvolvedHeading(self): #発行者及び関係法人情報 [目次項目]
		return self.InformationAboutIssuerAndPartiesInvolvedHeading

	def getInformationAboutIssuerHeading(self): #発行者の状況 [目次項目]
		return self.InformationAboutIssuerHeading

	def getFinancialInformationHeading(self): #経理の状況 [目次項目]
		return self.FinancialInformationHeading

	def getSemiAnnualBalanceSheetHeading(self): #中間貸借対照表 [目次項目]
		return self.SemiAnnualBalanceSheetHeading

	def getSemiAnnualBalanceSheetTextBlock(self): #中間貸借対照表 [テキストブロック]
		return self.SemiAnnualBalanceSheetTextBlock

	def getSemiAnnualStatementOfIncomeHeading(self): #中間損益計算書 [目次項目]
		return self.SemiAnnualStatementOfIncomeHeading

	def getSemiAnnualStatementOfIncomeTextBlock(self): #中間損益計算書 [テキストブロック]
		return self.SemiAnnualStatementOfIncomeTextBlock

	def getSemiAnnualStatementOfMembersEquityHeading(self): #中間社員資本等変動計算書 [目次項目]
		return self.SemiAnnualStatementOfMembersEquityHeading

	def getSemiAnnualStatementOfMembersEquityTextBlock(self): #中間社員資本等変動計算書 [テキストブロック]
		return self.SemiAnnualStatementOfMembersEquityTextBlock

	def getSemiAnnualStatementOfCashFlowsHeading(self): #中間キャッシュ・フロー計算書 [目次項目]
		return self.SemiAnnualStatementOfCashFlowsHeading

	def getSemiAnnualStatementOfCashFlowsTextBlock(self): #中間キャッシュ・フロー計算書 [テキストブロック]
		return self.SemiAnnualStatementOfCashFlowsTextBlock
