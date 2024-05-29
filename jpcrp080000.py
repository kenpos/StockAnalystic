from arelle import ModelManager
from arelle import Cntlr

class jpcrp080000:#企業内容等の開示に関する内閣府令 第八号様式 有価証券報告書
	CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo8AnnualSecuritiesReportHeading = '' #企業内容等の開示に関する内閣府令 第八号様式 有価証券報告書 [目次項目]
	ConsolidatedFinancialStatementsEtcHeading = '' #連結財務諸表等 [目次項目]
	ConsolidatedFinancialStatementsHeading = '' #連結財務諸表 [目次項目]
	ConsolidatedBalanceSheetHeading = '' #連結貸借対照表 [目次項目]
	ConsolidatedBalanceSheetTextBlock = '' #連結貸借対照表 [テキストブロック]
	ConsolidatedBalanceSheetUSGAAPTextBlock = '' #連結貸借対照表 （US GAAP） [テキストブロック]
	ConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading = '' #連結損益計算書及び連結包括利益計算書 [目次項目]
	ConsolidatedStatementOfIncomeHeading = '' #連結損益計算書 [目次項目]
	ConsolidatedStatementOfIncomeTextBlock = '' #連結損益計算書 [テキストブロック]
	ConsolidatedStatementOfIncomeUSGAAPTextBlock = '' #連結損益計算書（US GAAP） [テキストブロック]
	ConsolidatedStatementOfComprehensiveIncomeHeading = '' #連結包括利益計算書 [目次項目]
	ConsolidatedStatementOfComprehensiveIncomeTextBlock = '' #連結包括利益計算書 [テキストブロック]
	ConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock = '' #連結包括利益計算書（US GAAP） [テキストブロック]
	ConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = '' #連結損益及び包括利益計算書 [目次項目]
	ConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = '' #連結損益及び包括利益計算書 [テキストブロック]
	ConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock = '' #連結損益及び包括利益計算書（US GAAP） [テキストブロック]
	ConsolidatedStatementOfChangesInEquityHeading = '' #連結株主資本等変動計算書 [目次項目]
	ConsolidatedStatementOfChangesInEquityTextBlock = '' #連結株主資本等変動計算書 [テキストブロック]
	ConsolidatedStatementOfEquityUSGAAPTextBlock = '' #連結資本勘定計算書（US GAAP） [テキストブロック]
	ConsolidatedStatementOfCashFlowsHeading = '' #連結キャッシュ・フロー計算書 [目次項目]
	ConsolidatedStatementOfCashFlowsTextBlock = '' #連結キャッシュ・フロー計算書 [テキストブロック]
	ConsolidatedStatementOfCashFlowsUSGAAPTextBlock = '' #連結キャッシュ・フロー計算書（US GAAP） [テキストブロック]
	FinancialStatementsEtcHeading = '' #財務諸表等 [目次項目]
	FinancialStatementsHeading = '' #財務諸表 [目次項目]
	BalanceSheetHeading = '' #貸借対照表 [目次項目]
	BalanceSheetTextBlock = '' #貸借対照表 [テキストブロック]
	StatementOfIncomeHeading = '' #損益計算書 [目次項目]
	StatementOfIncomeTextBlock = '' #損益計算書 [テキストブロック]
	DetailedScheduleOfManufacturingCostTextBlock = '' #製造原価明細書 [テキストブロック]
	DetailedScheduleOfCostOfSalesTextBlock = '' #売上原価明細書 [テキストブロック]
	DetailedScheduleOfOperatingExpensesForRailwayBusinessTextBlock = '' #鉄道事業営業費明細表 [テキストブロック]
	DetailedScheduleOfOperatingExpensesForMotorwayBusinessTextBlock = '' #自動車道事業営業費明細表 [テキストブロック]
	DetailedScheduleOfOperatingExpensesTelecommunicationsBusinessTextBlock = '' #電気通信事業営業費用明細表 [テキストブロック]
	DetailedScheduleOfElectricUtilityOperatingExpensesTextBlock = '' #電気事業営業費用明細表 [テキストブロック]
	DetailedScheduleOfOperatingExpensesGASTextBlock = '' #営業費明細表、ガス事業 [テキストブロック]
	DetailedScheduleOfOperatingExpensesNonOperatingExpensesExtraordinaryLossesEtcForHighwayBusinessTextBlock = '' #高速道路事業営業費用、営業外費用及び特別損失等明細表 [テキストブロック]
	DetailedScheduleOfOperatingExpensesEDUTextBlock = '' #事業費用明細表、学校法人 [テキストブロック]
	StatementOfChangesInEquityHeading = '' #株主資本等変動計算書 [目次項目]
	StatementOfChangesInEquityTextBlock = '' #株主資本等変動計算書 [テキストブロック]
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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo8AnnualSecuritiesReportHeading': #企業内容等の開示に関する内閣府令 第八号様式 有価証券報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo8AnnualSecuritiesReportHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedFinancialStatementsEtcHeading': #連結財務諸表等 [目次項目]
				self.ConsolidatedFinancialStatementsEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedFinancialStatementsHeading': #連結財務諸表 [目次項目]
				self.ConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedBalanceSheetHeading': #連結貸借対照表 [目次項目]
				self.ConsolidatedBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedBalanceSheetTextBlock': #連結貸借対照表 [テキストブロック]
				self.ConsolidatedBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedBalanceSheetUSGAAPTextBlock': #連結貸借対照表 （US GAAP） [テキストブロック]
				self.ConsolidatedBalanceSheetUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading': #連結損益計算書及び連結包括利益計算書 [目次項目]
				self.ConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfIncomeHeading': #連結損益計算書 [目次項目]
				self.ConsolidatedStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfIncomeTextBlock': #連結損益計算書 [テキストブロック]
				self.ConsolidatedStatementOfIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfIncomeUSGAAPTextBlock': #連結損益計算書（US GAAP） [テキストブロック]
				self.ConsolidatedStatementOfIncomeUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeHeading': #連結包括利益計算書 [目次項目]
				self.ConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeTextBlock': #連結包括利益計算書 [テキストブロック]
				self.ConsolidatedStatementOfComprehensiveIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock': #連結包括利益計算書（US GAAP） [テキストブロック]
				self.ConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading': #連結損益及び包括利益計算書 [目次項目]
				self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock': #連結損益及び包括利益計算書 [テキストブロック]
				self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock': #連結損益及び包括利益計算書（US GAAP） [テキストブロック]
				self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfChangesInEquityHeading': #連結株主資本等変動計算書 [目次項目]
				self.ConsolidatedStatementOfChangesInEquityHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfChangesInEquityTextBlock': #連結株主資本等変動計算書 [テキストブロック]
				self.ConsolidatedStatementOfChangesInEquityTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfEquityUSGAAPTextBlock': #連結資本勘定計算書（US GAAP） [テキストブロック]
				self.ConsolidatedStatementOfEquityUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfCashFlowsHeading': #連結キャッシュ・フロー計算書 [目次項目]
				self.ConsolidatedStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfCashFlowsTextBlock': #連結キャッシュ・フロー計算書 [テキストブロック]
				self.ConsolidatedStatementOfCashFlowsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfCashFlowsUSGAAPTextBlock': #連結キャッシュ・フロー計算書（US GAAP） [テキストブロック]
				self.ConsolidatedStatementOfCashFlowsUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'FinancialStatementsEtcHeading': #財務諸表等 [目次項目]
				self.FinancialStatementsEtcHeading = fact.value

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

			elif fact.concept.qname.localName == 'DetailedScheduleOfManufacturingCostTextBlock': #製造原価明細書 [テキストブロック]
				self.DetailedScheduleOfManufacturingCostTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfCostOfSalesTextBlock': #売上原価明細書 [テキストブロック]
				self.DetailedScheduleOfCostOfSalesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfOperatingExpensesForRailwayBusinessTextBlock': #鉄道事業営業費明細表 [テキストブロック]
				self.DetailedScheduleOfOperatingExpensesForRailwayBusinessTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfOperatingExpensesForMotorwayBusinessTextBlock': #自動車道事業営業費明細表 [テキストブロック]
				self.DetailedScheduleOfOperatingExpensesForMotorwayBusinessTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfOperatingExpensesTelecommunicationsBusinessTextBlock': #電気通信事業営業費用明細表 [テキストブロック]
				self.DetailedScheduleOfOperatingExpensesTelecommunicationsBusinessTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfElectricUtilityOperatingExpensesTextBlock': #電気事業営業費用明細表 [テキストブロック]
				self.DetailedScheduleOfElectricUtilityOperatingExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfOperatingExpensesGASTextBlock': #営業費明細表、ガス事業 [テキストブロック]
				self.DetailedScheduleOfOperatingExpensesGASTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfOperatingExpensesNonOperatingExpensesExtraordinaryLossesEtcForHighwayBusinessTextBlock': #高速道路事業営業費用、営業外費用及び特別損失等明細表 [テキストブロック]
				self.DetailedScheduleOfOperatingExpensesNonOperatingExpensesExtraordinaryLossesEtcForHighwayBusinessTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfOperatingExpensesEDUTextBlock': #事業費用明細表、学校法人 [テキストブロック]
				self.DetailedScheduleOfOperatingExpensesEDUTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfChangesInEquityHeading': #株主資本等変動計算書 [目次項目]
				self.StatementOfChangesInEquityHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfChangesInEquityTextBlock': #株主資本等変動計算書 [テキストブロック]
				self.StatementOfChangesInEquityTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashFlowsHeading': #キャッシュ・フロー計算書 [目次項目]
				self.StatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashFlowsTextBlock': #キャッシュ・フロー計算書 [テキストブロック]
				self.StatementOfCashFlowsTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo8AnnualSecuritiesReportHeading(self): #企業内容等の開示に関する内閣府令 第八号様式 有価証券報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo8AnnualSecuritiesReportHeading

	def getConsolidatedFinancialStatementsEtcHeading(self): #連結財務諸表等 [目次項目]
		return self.ConsolidatedFinancialStatementsEtcHeading

	def getConsolidatedFinancialStatementsHeading(self): #連結財務諸表 [目次項目]
		return self.ConsolidatedFinancialStatementsHeading

	def getConsolidatedBalanceSheetHeading(self): #連結貸借対照表 [目次項目]
		return self.ConsolidatedBalanceSheetHeading

	def getConsolidatedBalanceSheetTextBlock(self): #連結貸借対照表 [テキストブロック]
		return self.ConsolidatedBalanceSheetTextBlock

	def getConsolidatedBalanceSheetUSGAAPTextBlock(self): #連結貸借対照表 （US GAAP） [テキストブロック]
		return self.ConsolidatedBalanceSheetUSGAAPTextBlock

	def getConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading(self): #連結損益計算書及び連結包括利益計算書 [目次項目]
		return self.ConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading

	def getConsolidatedStatementOfIncomeHeading(self): #連結損益計算書 [目次項目]
		return self.ConsolidatedStatementOfIncomeHeading

	def getConsolidatedStatementOfIncomeTextBlock(self): #連結損益計算書 [テキストブロック]
		return self.ConsolidatedStatementOfIncomeTextBlock

	def getConsolidatedStatementOfIncomeUSGAAPTextBlock(self): #連結損益計算書（US GAAP） [テキストブロック]
		return self.ConsolidatedStatementOfIncomeUSGAAPTextBlock

	def getConsolidatedStatementOfComprehensiveIncomeHeading(self): #連結包括利益計算書 [目次項目]
		return self.ConsolidatedStatementOfComprehensiveIncomeHeading

	def getConsolidatedStatementOfComprehensiveIncomeTextBlock(self): #連結包括利益計算書 [テキストブロック]
		return self.ConsolidatedStatementOfComprehensiveIncomeTextBlock

	def getConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock(self): #連結包括利益計算書（US GAAP） [テキストブロック]
		return self.ConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock

	def getConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading(self): #連結損益及び包括利益計算書 [目次項目]
		return self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading

	def getConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock(self): #連結損益及び包括利益計算書 [テキストブロック]
		return self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock

	def getConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock(self): #連結損益及び包括利益計算書（US GAAP） [テキストブロック]
		return self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock

	def getConsolidatedStatementOfChangesInEquityHeading(self): #連結株主資本等変動計算書 [目次項目]
		return self.ConsolidatedStatementOfChangesInEquityHeading

	def getConsolidatedStatementOfChangesInEquityTextBlock(self): #連結株主資本等変動計算書 [テキストブロック]
		return self.ConsolidatedStatementOfChangesInEquityTextBlock

	def getConsolidatedStatementOfEquityUSGAAPTextBlock(self): #連結資本勘定計算書（US GAAP） [テキストブロック]
		return self.ConsolidatedStatementOfEquityUSGAAPTextBlock

	def getConsolidatedStatementOfCashFlowsHeading(self): #連結キャッシュ・フロー計算書 [目次項目]
		return self.ConsolidatedStatementOfCashFlowsHeading

	def getConsolidatedStatementOfCashFlowsTextBlock(self): #連結キャッシュ・フロー計算書 [テキストブロック]
		return self.ConsolidatedStatementOfCashFlowsTextBlock

	def getConsolidatedStatementOfCashFlowsUSGAAPTextBlock(self): #連結キャッシュ・フロー計算書（US GAAP） [テキストブロック]
		return self.ConsolidatedStatementOfCashFlowsUSGAAPTextBlock

	def getFinancialStatementsEtcHeading(self): #財務諸表等 [目次項目]
		return self.FinancialStatementsEtcHeading

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

	def getDetailedScheduleOfManufacturingCostTextBlock(self): #製造原価明細書 [テキストブロック]
		return self.DetailedScheduleOfManufacturingCostTextBlock

	def getDetailedScheduleOfCostOfSalesTextBlock(self): #売上原価明細書 [テキストブロック]
		return self.DetailedScheduleOfCostOfSalesTextBlock

	def getDetailedScheduleOfOperatingExpensesForRailwayBusinessTextBlock(self): #鉄道事業営業費明細表 [テキストブロック]
		return self.DetailedScheduleOfOperatingExpensesForRailwayBusinessTextBlock

	def getDetailedScheduleOfOperatingExpensesForMotorwayBusinessTextBlock(self): #自動車道事業営業費明細表 [テキストブロック]
		return self.DetailedScheduleOfOperatingExpensesForMotorwayBusinessTextBlock

	def getDetailedScheduleOfOperatingExpensesTelecommunicationsBusinessTextBlock(self): #電気通信事業営業費用明細表 [テキストブロック]
		return self.DetailedScheduleOfOperatingExpensesTelecommunicationsBusinessTextBlock

	def getDetailedScheduleOfElectricUtilityOperatingExpensesTextBlock(self): #電気事業営業費用明細表 [テキストブロック]
		return self.DetailedScheduleOfElectricUtilityOperatingExpensesTextBlock

	def getDetailedScheduleOfOperatingExpensesGASTextBlock(self): #営業費明細表、ガス事業 [テキストブロック]
		return self.DetailedScheduleOfOperatingExpensesGASTextBlock

	def getDetailedScheduleOfOperatingExpensesNonOperatingExpensesExtraordinaryLossesEtcForHighwayBusinessTextBlock(self): #高速道路事業営業費用、営業外費用及び特別損失等明細表 [テキストブロック]
		return self.DetailedScheduleOfOperatingExpensesNonOperatingExpensesExtraordinaryLossesEtcForHighwayBusinessTextBlock

	def getDetailedScheduleOfOperatingExpensesEDUTextBlock(self): #事業費用明細表、学校法人 [テキストブロック]
		return self.DetailedScheduleOfOperatingExpensesEDUTextBlock

	def getStatementOfChangesInEquityHeading(self): #株主資本等変動計算書 [目次項目]
		return self.StatementOfChangesInEquityHeading

	def getStatementOfChangesInEquityTextBlock(self): #株主資本等変動計算書 [テキストブロック]
		return self.StatementOfChangesInEquityTextBlock

	def getStatementOfCashFlowsHeading(self): #キャッシュ・フロー計算書 [目次項目]
		return self.StatementOfCashFlowsHeading

	def getStatementOfCashFlowsTextBlock(self): #キャッシュ・フロー計算書 [テキストブロック]
		return self.StatementOfCashFlowsTextBlock
