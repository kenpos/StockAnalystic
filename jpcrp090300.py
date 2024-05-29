from arelle import ModelManager
from arelle import Cntlr

class jpcrp090300:#企業内容等の開示に関する内閣府令 第九号の三様式 四半期報告書
	CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo93QuarterlySecuritiesReportHeading = '' #企業内容等の開示に関する内閣府令 第九号の三様式 四半期報告書 [目次項目]
	QuarterlyConsolidatedFinancialStatementsHeading = '' #四半期連結財務諸表 [目次項目]
	QuarterlyConsolidatedBalanceSheetHeading = '' #四半期連結貸借対照表 [目次項目]
	QuarterlyConsolidatedBalanceSheetTextBlock = '' #四半期連結貸借対照表 [テキストブロック]
	QuarterlyConsolidatedBalanceSheetUSGAAPTextBlock = '' #四半期連結貸借対照表（US GAAP） [テキストブロック]
	QuarterlyConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading = '' #四半期連結損益計算書及び四半期連結包括利益計算書 [目次項目]
	QuarterlyConsolidatedStatementOfIncomeHeading = '' #四半期連結損益計算書 [目次項目]
	YearToQuarterEndConsolidatedStatementOfIncomeHeading = '' #四半期連結累計期間、四半期連結損益計算書 [目次項目]
	YearToQuarterEndConsolidatedStatementOfIncomeTextBlock = '' #四半期連結累計期間、四半期連結損益計算書 [テキストブロック]
	YearToQuarterEndConsolidatedStatementOfIncomeUSGAAPTextBlock = '' #四半期連結累計期間、四半期連結損益計算書（US GAAP） [テキストブロック]
	QuarterPeriodConsolidatedStatementOfIncomeHeading = '' #四半期連結会計期間、四半期連結損益計算書 [目次項目]
	QuarterPeriodConsolidatedStatementOfIncomeTextBlock = '' #四半期連結会計期間、四半期連結損益計算書 [テキストブロック]
	QuarterPeriodConsolidatedStatementOfIncomeUSGAAPTextBlock = '' #四半期連結会計期間、四半期連結損益計算書（US GAAP） [テキストブロック]
	QuarterlyConsolidatedStatementOfComprehensiveIncomeHeading = '' #四半期連結包括利益計算書 [目次項目]
	YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeHeading = '' #四半期連結累計期間、四半期連結包括利益計算書 [目次項目]
	YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock = '' #四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック]
	YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock = '' #四半期連結累計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]
	QuarterPeriodConsolidatedStatementOfComprehensiveIncomeHeading = '' #四半期連結会計期間、四半期連結包括利益計算書 [目次項目]
	QuarterPeriodConsolidatedStatementOfComprehensiveIncomeTextBlock = '' #四半期連結会計期間、四半期連結包括利益計算書 [テキストブロック]
	QuarterPeriodConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock = '' #四半期連結会計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]
	QuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = '' #四半期連結損益及び包括利益計算書 [目次項目]
	YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = '' #四半期連結累計期間、四半期連結損益及び包括利益計算書 [目次項目]
	YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = '' #四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック]
	YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock = '' #四半期連結累計期間、四半期連結損益及び包括利益計算書（US GAAP） [テキストブロック]
	QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = '' #四半期連結会計期間、四半期連結損益及び包括利益計算書 [目次項目]
	QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = '' #四半期連結会計期間、四半期連結損益及び包括利益計算書 [テキストブロック]
	QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock = '' #四半期連結会計期間、四半期連結損益及び包括利益計算書（US GAAP） [テキストブロック]
	QuarterlyConsolidatedStatementOfCashFlowsHeading = '' #四半期連結キャッシュ・フロー計算書 [目次項目]
	QuarterlyConsolidatedStatementOfCashFlowsTextBlock = '' #四半期連結キャッシュ・フロー計算書 [テキストブロック]
	QuarterlyConsolidatedStatementOfCashFlowsUSGAAPTextBlock = '' #四半期連結キャッシュ・フロー計算書（US GAAP） [テキストブロック]
	QuarterlyFinancialStatementsHeading = '' #四半期財務諸表 [目次項目]
	QuarterlyBalanceSheetHeading = '' #四半期貸借対照表 [目次項目]
	QuarterlyBalanceSheetTextBlock = '' #四半期貸借対照表 [テキストブロック]
	QuarterlyStatementOfIncomeHeading = '' #四半期損益計算書 [目次項目]
	YearToQuarterEndStatementOfIncomeHeading = '' #四半期累計期間、四半期損益計算書 [目次項目]
	YearToQuarterEndStatementOfIncomeTextBlock = '' #四半期累計期間、四半期損益計算書 [テキストブロック]
	QuarterPeriodStatementOfIncomeHeading = '' #四半期会計期間、四半期損益計算書 [目次項目]
	QuarterPeriodStatementOfIncomeTextBlock = '' #四半期会計期間、四半期損益計算書 [テキストブロック]
	QuarterlyStatementOfCashFlowsHeading = '' #四半期キャッシュ・フロー計算書 [目次項目]
	QuarterlyStatementOfCashFlowsTextBlock = '' #四半期キャッシュ・フロー計算書 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo93QuarterlySecuritiesReportHeading': #企業内容等の開示に関する内閣府令 第九号の三様式 四半期報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo93QuarterlySecuritiesReportHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedFinancialStatementsHeading': #四半期連結財務諸表 [目次項目]
				self.QuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedBalanceSheetHeading': #四半期連結貸借対照表 [目次項目]
				self.QuarterlyConsolidatedBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedBalanceSheetTextBlock': #四半期連結貸借対照表 [テキストブロック]
				self.QuarterlyConsolidatedBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedBalanceSheetUSGAAPTextBlock': #四半期連結貸借対照表（US GAAP） [テキストブロック]
				self.QuarterlyConsolidatedBalanceSheetUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading': #四半期連結損益計算書及び四半期連結包括利益計算書 [目次項目]
				self.QuarterlyConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedStatementOfIncomeHeading': #四半期連結損益計算書 [目次項目]
				self.QuarterlyConsolidatedStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfIncomeHeading': #四半期連結累計期間、四半期連結損益計算書 [目次項目]
				self.YearToQuarterEndConsolidatedStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfIncomeTextBlock': #四半期連結累計期間、四半期連結損益計算書 [テキストブロック]
				self.YearToQuarterEndConsolidatedStatementOfIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfIncomeUSGAAPTextBlock': #四半期連結累計期間、四半期連結損益計算書（US GAAP） [テキストブロック]
				self.YearToQuarterEndConsolidatedStatementOfIncomeUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfIncomeHeading': #四半期連結会計期間、四半期連結損益計算書 [目次項目]
				self.QuarterPeriodConsolidatedStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfIncomeTextBlock': #四半期連結会計期間、四半期連結損益計算書 [テキストブロック]
				self.QuarterPeriodConsolidatedStatementOfIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfIncomeUSGAAPTextBlock': #四半期連結会計期間、四半期連結損益計算書（US GAAP） [テキストブロック]
				self.QuarterPeriodConsolidatedStatementOfIncomeUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedStatementOfComprehensiveIncomeHeading': #四半期連結包括利益計算書 [目次項目]
				self.QuarterlyConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeHeading': #四半期連結累計期間、四半期連結包括利益計算書 [目次項目]
				self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock': #四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック]
				self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock': #四半期連結累計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]
				self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfComprehensiveIncomeHeading': #四半期連結会計期間、四半期連結包括利益計算書 [目次項目]
				self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfComprehensiveIncomeTextBlock': #四半期連結会計期間、四半期連結包括利益計算書 [テキストブロック]
				self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock': #四半期連結会計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]
				self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading': #四半期連結損益及び包括利益計算書 [目次項目]
				self.QuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading': #四半期連結累計期間、四半期連結損益及び包括利益計算書 [目次項目]
				self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock': #四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック]
				self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock': #四半期連結累計期間、四半期連結損益及び包括利益計算書（US GAAP） [テキストブロック]
				self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading': #四半期連結会計期間、四半期連結損益及び包括利益計算書 [目次項目]
				self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock': #四半期連結会計期間、四半期連結損益及び包括利益計算書 [テキストブロック]
				self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock': #四半期連結会計期間、四半期連結損益及び包括利益計算書（US GAAP） [テキストブロック]
				self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedStatementOfCashFlowsHeading': #四半期連結キャッシュ・フロー計算書 [目次項目]
				self.QuarterlyConsolidatedStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedStatementOfCashFlowsTextBlock': #四半期連結キャッシュ・フロー計算書 [テキストブロック]
				self.QuarterlyConsolidatedStatementOfCashFlowsTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedStatementOfCashFlowsUSGAAPTextBlock': #四半期連結キャッシュ・フロー計算書（US GAAP） [テキストブロック]
				self.QuarterlyConsolidatedStatementOfCashFlowsUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlyFinancialStatementsHeading': #四半期財務諸表 [目次項目]
				self.QuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterlyBalanceSheetHeading': #四半期貸借対照表 [目次項目]
				self.QuarterlyBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterlyBalanceSheetTextBlock': #四半期貸借対照表 [テキストブロック]
				self.QuarterlyBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlyStatementOfIncomeHeading': #四半期損益計算書 [目次項目]
				self.QuarterlyStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndStatementOfIncomeHeading': #四半期累計期間、四半期損益計算書 [目次項目]
				self.YearToQuarterEndStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndStatementOfIncomeTextBlock': #四半期累計期間、四半期損益計算書 [テキストブロック]
				self.YearToQuarterEndStatementOfIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodStatementOfIncomeHeading': #四半期会計期間、四半期損益計算書 [目次項目]
				self.QuarterPeriodStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodStatementOfIncomeTextBlock': #四半期会計期間、四半期損益計算書 [テキストブロック]
				self.QuarterPeriodStatementOfIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlyStatementOfCashFlowsHeading': #四半期キャッシュ・フロー計算書 [目次項目]
				self.QuarterlyStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterlyStatementOfCashFlowsTextBlock': #四半期キャッシュ・フロー計算書 [テキストブロック]
				self.QuarterlyStatementOfCashFlowsTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo93QuarterlySecuritiesReportHeading(self): #企業内容等の開示に関する内閣府令 第九号の三様式 四半期報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo93QuarterlySecuritiesReportHeading

	def getQuarterlyConsolidatedFinancialStatementsHeading(self): #四半期連結財務諸表 [目次項目]
		return self.QuarterlyConsolidatedFinancialStatementsHeading

	def getQuarterlyConsolidatedBalanceSheetHeading(self): #四半期連結貸借対照表 [目次項目]
		return self.QuarterlyConsolidatedBalanceSheetHeading

	def getQuarterlyConsolidatedBalanceSheetTextBlock(self): #四半期連結貸借対照表 [テキストブロック]
		return self.QuarterlyConsolidatedBalanceSheetTextBlock

	def getQuarterlyConsolidatedBalanceSheetUSGAAPTextBlock(self): #四半期連結貸借対照表（US GAAP） [テキストブロック]
		return self.QuarterlyConsolidatedBalanceSheetUSGAAPTextBlock

	def getQuarterlyConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading(self): #四半期連結損益計算書及び四半期連結包括利益計算書 [目次項目]
		return self.QuarterlyConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading

	def getQuarterlyConsolidatedStatementOfIncomeHeading(self): #四半期連結損益計算書 [目次項目]
		return self.QuarterlyConsolidatedStatementOfIncomeHeading

	def getYearToQuarterEndConsolidatedStatementOfIncomeHeading(self): #四半期連結累計期間、四半期連結損益計算書 [目次項目]
		return self.YearToQuarterEndConsolidatedStatementOfIncomeHeading

	def getYearToQuarterEndConsolidatedStatementOfIncomeTextBlock(self): #四半期連結累計期間、四半期連結損益計算書 [テキストブロック]
		return self.YearToQuarterEndConsolidatedStatementOfIncomeTextBlock

	def getYearToQuarterEndConsolidatedStatementOfIncomeUSGAAPTextBlock(self): #四半期連結累計期間、四半期連結損益計算書（US GAAP） [テキストブロック]
		return self.YearToQuarterEndConsolidatedStatementOfIncomeUSGAAPTextBlock

	def getQuarterPeriodConsolidatedStatementOfIncomeHeading(self): #四半期連結会計期間、四半期連結損益計算書 [目次項目]
		return self.QuarterPeriodConsolidatedStatementOfIncomeHeading

	def getQuarterPeriodConsolidatedStatementOfIncomeTextBlock(self): #四半期連結会計期間、四半期連結損益計算書 [テキストブロック]
		return self.QuarterPeriodConsolidatedStatementOfIncomeTextBlock

	def getQuarterPeriodConsolidatedStatementOfIncomeUSGAAPTextBlock(self): #四半期連結会計期間、四半期連結損益計算書（US GAAP） [テキストブロック]
		return self.QuarterPeriodConsolidatedStatementOfIncomeUSGAAPTextBlock

	def getQuarterlyConsolidatedStatementOfComprehensiveIncomeHeading(self): #四半期連結包括利益計算書 [目次項目]
		return self.QuarterlyConsolidatedStatementOfComprehensiveIncomeHeading

	def getYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeHeading(self): #四半期連結累計期間、四半期連結包括利益計算書 [目次項目]
		return self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeHeading

	def getYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock(self): #四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック]
		return self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock

	def getYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock(self): #四半期連結累計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]
		return self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock

	def getQuarterPeriodConsolidatedStatementOfComprehensiveIncomeHeading(self): #四半期連結会計期間、四半期連結包括利益計算書 [目次項目]
		return self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeHeading

	def getQuarterPeriodConsolidatedStatementOfComprehensiveIncomeTextBlock(self): #四半期連結会計期間、四半期連結包括利益計算書 [テキストブロック]
		return self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeTextBlock

	def getQuarterPeriodConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock(self): #四半期連結会計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]
		return self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock

	def getQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading(self): #四半期連結損益及び包括利益計算書 [目次項目]
		return self.QuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading

	def getYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading(self): #四半期連結累計期間、四半期連結損益及び包括利益計算書 [目次項目]
		return self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading

	def getYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock(self): #四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック]
		return self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock

	def getYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock(self): #四半期連結累計期間、四半期連結損益及び包括利益計算書（US GAAP） [テキストブロック]
		return self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock

	def getQuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading(self): #四半期連結会計期間、四半期連結損益及び包括利益計算書 [目次項目]
		return self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading

	def getQuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock(self): #四半期連結会計期間、四半期連結損益及び包括利益計算書 [テキストブロック]
		return self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock

	def getQuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock(self): #四半期連結会計期間、四半期連結損益及び包括利益計算書（US GAAP） [テキストブロック]
		return self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock

	def getQuarterlyConsolidatedStatementOfCashFlowsHeading(self): #四半期連結キャッシュ・フロー計算書 [目次項目]
		return self.QuarterlyConsolidatedStatementOfCashFlowsHeading

	def getQuarterlyConsolidatedStatementOfCashFlowsTextBlock(self): #四半期連結キャッシュ・フロー計算書 [テキストブロック]
		return self.QuarterlyConsolidatedStatementOfCashFlowsTextBlock

	def getQuarterlyConsolidatedStatementOfCashFlowsUSGAAPTextBlock(self): #四半期連結キャッシュ・フロー計算書（US GAAP） [テキストブロック]
		return self.QuarterlyConsolidatedStatementOfCashFlowsUSGAAPTextBlock

	def getQuarterlyFinancialStatementsHeading(self): #四半期財務諸表 [目次項目]
		return self.QuarterlyFinancialStatementsHeading

	def getQuarterlyBalanceSheetHeading(self): #四半期貸借対照表 [目次項目]
		return self.QuarterlyBalanceSheetHeading

	def getQuarterlyBalanceSheetTextBlock(self): #四半期貸借対照表 [テキストブロック]
		return self.QuarterlyBalanceSheetTextBlock

	def getQuarterlyStatementOfIncomeHeading(self): #四半期損益計算書 [目次項目]
		return self.QuarterlyStatementOfIncomeHeading

	def getYearToQuarterEndStatementOfIncomeHeading(self): #四半期累計期間、四半期損益計算書 [目次項目]
		return self.YearToQuarterEndStatementOfIncomeHeading

	def getYearToQuarterEndStatementOfIncomeTextBlock(self): #四半期累計期間、四半期損益計算書 [テキストブロック]
		return self.YearToQuarterEndStatementOfIncomeTextBlock

	def getQuarterPeriodStatementOfIncomeHeading(self): #四半期会計期間、四半期損益計算書 [目次項目]
		return self.QuarterPeriodStatementOfIncomeHeading

	def getQuarterPeriodStatementOfIncomeTextBlock(self): #四半期会計期間、四半期損益計算書 [テキストブロック]
		return self.QuarterPeriodStatementOfIncomeTextBlock

	def getQuarterlyStatementOfCashFlowsHeading(self): #四半期キャッシュ・フロー計算書 [目次項目]
		return self.QuarterlyStatementOfCashFlowsHeading

	def getQuarterlyStatementOfCashFlowsTextBlock(self): #四半期キャッシュ・フロー計算書 [テキストブロック]
		return self.QuarterlyStatementOfCashFlowsTextBlock
