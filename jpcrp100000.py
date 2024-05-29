from arelle import ModelManager
from arelle import Cntlr

class jpcrp100000:#企業内容等の開示に関する内閣府令 第十号様式 半期報告書
	CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo10SemiannualSecuritiesReportHeading = '' #企業内容等の開示に関する内閣府令 第十号様式 半期報告書 [目次項目]
	SemiAnnualConsolidatedFinancialStatementsEtcHeading = '' #中間連結財務諸表等 [目次項目]
	SemiAnnualConsolidatedFinancialStatementsHeading = '' #中間連結財務諸表 [目次項目]
	SemiAnnualConsolidatedBalanceSheetHeading = '' #中間連結貸借対照表 [目次項目]
	SemiAnnualConsolidatedBalanceSheetTextBlock = '' #中間連結貸借対照表 [テキストブロック]
	SemiAnnualConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading = '' #中間連結損益計算書及び中間連結包括利益計算書 [目次項目]
	SemiAnnualConsolidatedStatementOfIncomeHeading = '' #中間連結損益計算書 [目次項目]
	SemiAnnualConsolidatedStatementOfIncomeTextBlock = '' #中間連結損益計算書 [テキストブロック]
	SemiAnnualConsolidatedStatementOfComprehensiveIncomeHeading = '' #中間連結包括利益計算書 [目次項目]
	SemiAnnualConsolidatedStatementOfComprehensiveIncomeTextBlock = '' #中間連結包括利益計算書 [テキストブロック]
	SemiAnnualConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = '' #中間連結損益及び包括利益計算書 [目次項目]
	SemiAnnualConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = '' #中間連結損益及び包括利益計算書 [テキストブロック]
	SemiAnnualConsolidatedStatementOfChangesInEquityHeading = '' #中間連結株主資本等変動計算書 [目次項目]
	SemiAnnualConsolidatedStatementOfChangesInEquityTextBlock = '' #中間連結株主資本等変動計算書 [テキストブロック]
	SemiAnnualConsolidatedStatementOfCashFlowsHeading = '' #中間連結キャッシュ・フロー計算書 [目次項目]
	SemiAnnualConsolidatedStatementOfCashFlowsTextBlock = '' #中間連結キャッシュ・フロー計算書 [テキストブロック]
	SemiAnnualFinancialStatementsEtcHeading = '' #中間財務諸表等 [目次項目]
	SemiAnnualFinancialStatementsHeading = '' #中間財務諸表 [目次項目]
	SemiAnnualBalanceSheetHeading = '' #中間貸借対照表 [目次項目]
	SemiAnnualBalanceSheetTextBlock = '' #中間貸借対照表 [テキストブロック]
	SemiAnnualStatementOfIncomeHeading = '' #中間損益計算書 [目次項目]
	SemiAnnualStatementOfIncomeTextBlock = '' #中間損益計算書 [テキストブロック]
	SemiAnnualStatementOfChangesInEquityHeading = '' #中間株主資本等変動計算書 [目次項目]
	SemiAnnualStatementOfChangesInEquityTextBlock = '' #中間株主資本等変動計算書 [テキストブロック]
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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo10SemiannualSecuritiesReportHeading': #企業内容等の開示に関する内閣府令 第十号様式 半期報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo10SemiannualSecuritiesReportHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedFinancialStatementsEtcHeading': #中間連結財務諸表等 [目次項目]
				self.SemiAnnualConsolidatedFinancialStatementsEtcHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedFinancialStatementsHeading': #中間連結財務諸表 [目次項目]
				self.SemiAnnualConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedBalanceSheetHeading': #中間連結貸借対照表 [目次項目]
				self.SemiAnnualConsolidatedBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedBalanceSheetTextBlock': #中間連結貸借対照表 [テキストブロック]
				self.SemiAnnualConsolidatedBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading': #中間連結損益計算書及び中間連結包括利益計算書 [目次項目]
				self.SemiAnnualConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedStatementOfIncomeHeading': #中間連結損益計算書 [目次項目]
				self.SemiAnnualConsolidatedStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedStatementOfIncomeTextBlock': #中間連結損益計算書 [テキストブロック]
				self.SemiAnnualConsolidatedStatementOfIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedStatementOfComprehensiveIncomeHeading': #中間連結包括利益計算書 [目次項目]
				self.SemiAnnualConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedStatementOfComprehensiveIncomeTextBlock': #中間連結包括利益計算書 [テキストブロック]
				self.SemiAnnualConsolidatedStatementOfComprehensiveIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading': #中間連結損益及び包括利益計算書 [目次項目]
				self.SemiAnnualConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock': #中間連結損益及び包括利益計算書 [テキストブロック]
				self.SemiAnnualConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedStatementOfChangesInEquityHeading': #中間連結株主資本等変動計算書 [目次項目]
				self.SemiAnnualConsolidatedStatementOfChangesInEquityHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedStatementOfChangesInEquityTextBlock': #中間連結株主資本等変動計算書 [テキストブロック]
				self.SemiAnnualConsolidatedStatementOfChangesInEquityTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedStatementOfCashFlowsHeading': #中間連結キャッシュ・フロー計算書 [目次項目]
				self.SemiAnnualConsolidatedStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualConsolidatedStatementOfCashFlowsTextBlock': #中間連結キャッシュ・フロー計算書 [テキストブロック]
				self.SemiAnnualConsolidatedStatementOfCashFlowsTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualFinancialStatementsEtcHeading': #中間財務諸表等 [目次項目]
				self.SemiAnnualFinancialStatementsEtcHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualFinancialStatementsHeading': #中間財務諸表 [目次項目]
				self.SemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualBalanceSheetHeading': #中間貸借対照表 [目次項目]
				self.SemiAnnualBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualBalanceSheetTextBlock': #中間貸借対照表 [テキストブロック]
				self.SemiAnnualBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfIncomeHeading': #中間損益計算書 [目次項目]
				self.SemiAnnualStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfIncomeTextBlock': #中間損益計算書 [テキストブロック]
				self.SemiAnnualStatementOfIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfChangesInEquityHeading': #中間株主資本等変動計算書 [目次項目]
				self.SemiAnnualStatementOfChangesInEquityHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfChangesInEquityTextBlock': #中間株主資本等変動計算書 [テキストブロック]
				self.SemiAnnualStatementOfChangesInEquityTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfCashFlowsHeading': #中間キャッシュ・フロー計算書 [目次項目]
				self.SemiAnnualStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfCashFlowsTextBlock': #中間キャッシュ・フロー計算書 [テキストブロック]
				self.SemiAnnualStatementOfCashFlowsTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo10SemiannualSecuritiesReportHeading(self): #企業内容等の開示に関する内閣府令 第十号様式 半期報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo10SemiannualSecuritiesReportHeading

	def getSemiAnnualConsolidatedFinancialStatementsEtcHeading(self): #中間連結財務諸表等 [目次項目]
		return self.SemiAnnualConsolidatedFinancialStatementsEtcHeading

	def getSemiAnnualConsolidatedFinancialStatementsHeading(self): #中間連結財務諸表 [目次項目]
		return self.SemiAnnualConsolidatedFinancialStatementsHeading

	def getSemiAnnualConsolidatedBalanceSheetHeading(self): #中間連結貸借対照表 [目次項目]
		return self.SemiAnnualConsolidatedBalanceSheetHeading

	def getSemiAnnualConsolidatedBalanceSheetTextBlock(self): #中間連結貸借対照表 [テキストブロック]
		return self.SemiAnnualConsolidatedBalanceSheetTextBlock

	def getSemiAnnualConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading(self): #中間連結損益計算書及び中間連結包括利益計算書 [目次項目]
		return self.SemiAnnualConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading

	def getSemiAnnualConsolidatedStatementOfIncomeHeading(self): #中間連結損益計算書 [目次項目]
		return self.SemiAnnualConsolidatedStatementOfIncomeHeading

	def getSemiAnnualConsolidatedStatementOfIncomeTextBlock(self): #中間連結損益計算書 [テキストブロック]
		return self.SemiAnnualConsolidatedStatementOfIncomeTextBlock

	def getSemiAnnualConsolidatedStatementOfComprehensiveIncomeHeading(self): #中間連結包括利益計算書 [目次項目]
		return self.SemiAnnualConsolidatedStatementOfComprehensiveIncomeHeading

	def getSemiAnnualConsolidatedStatementOfComprehensiveIncomeTextBlock(self): #中間連結包括利益計算書 [テキストブロック]
		return self.SemiAnnualConsolidatedStatementOfComprehensiveIncomeTextBlock

	def getSemiAnnualConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading(self): #中間連結損益及び包括利益計算書 [目次項目]
		return self.SemiAnnualConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading

	def getSemiAnnualConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock(self): #中間連結損益及び包括利益計算書 [テキストブロック]
		return self.SemiAnnualConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock

	def getSemiAnnualConsolidatedStatementOfChangesInEquityHeading(self): #中間連結株主資本等変動計算書 [目次項目]
		return self.SemiAnnualConsolidatedStatementOfChangesInEquityHeading

	def getSemiAnnualConsolidatedStatementOfChangesInEquityTextBlock(self): #中間連結株主資本等変動計算書 [テキストブロック]
		return self.SemiAnnualConsolidatedStatementOfChangesInEquityTextBlock

	def getSemiAnnualConsolidatedStatementOfCashFlowsHeading(self): #中間連結キャッシュ・フロー計算書 [目次項目]
		return self.SemiAnnualConsolidatedStatementOfCashFlowsHeading

	def getSemiAnnualConsolidatedStatementOfCashFlowsTextBlock(self): #中間連結キャッシュ・フロー計算書 [テキストブロック]
		return self.SemiAnnualConsolidatedStatementOfCashFlowsTextBlock

	def getSemiAnnualFinancialStatementsEtcHeading(self): #中間財務諸表等 [目次項目]
		return self.SemiAnnualFinancialStatementsEtcHeading

	def getSemiAnnualFinancialStatementsHeading(self): #中間財務諸表 [目次項目]
		return self.SemiAnnualFinancialStatementsHeading

	def getSemiAnnualBalanceSheetHeading(self): #中間貸借対照表 [目次項目]
		return self.SemiAnnualBalanceSheetHeading

	def getSemiAnnualBalanceSheetTextBlock(self): #中間貸借対照表 [テキストブロック]
		return self.SemiAnnualBalanceSheetTextBlock

	def getSemiAnnualStatementOfIncomeHeading(self): #中間損益計算書 [目次項目]
		return self.SemiAnnualStatementOfIncomeHeading

	def getSemiAnnualStatementOfIncomeTextBlock(self): #中間損益計算書 [テキストブロック]
		return self.SemiAnnualStatementOfIncomeTextBlock

	def getSemiAnnualStatementOfChangesInEquityHeading(self): #中間株主資本等変動計算書 [目次項目]
		return self.SemiAnnualStatementOfChangesInEquityHeading

	def getSemiAnnualStatementOfChangesInEquityTextBlock(self): #中間株主資本等変動計算書 [テキストブロック]
		return self.SemiAnnualStatementOfChangesInEquityTextBlock

	def getSemiAnnualStatementOfCashFlowsHeading(self): #中間キャッシュ・フロー計算書 [目次項目]
		return self.SemiAnnualStatementOfCashFlowsHeading

	def getSemiAnnualStatementOfCashFlowsTextBlock(self): #中間キャッシュ・フロー計算書 [テキストブロック]
		return self.SemiAnnualStatementOfCashFlowsTextBlock
