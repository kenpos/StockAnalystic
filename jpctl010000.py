from arelle import ModelManager
from arelle import Cntlr

class jpctl010000:#財務計算に関する書類その他の情報の適正性を確保するための体制に関する内閣府令 第一号様式 内部統制報告書
	CabinetOfficeOrdinanceOnSystemForEnsuringAppropriatenessOfFinancialAndOtherDocumentsFormNo1InternalControlReportHeading = '' #財務計算に関する書類その他の情報の適正性を確保するための体制に関する内閣府令 第一号様式 内部統制報告書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	ClauseOfStipulationCoverPage = '' #根拠条文、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	CompanyNameCoverPage = '' #会社名、表紙
	CompanyNameInEnglishCoverPage = '' #英訳名、表紙
	TitleAndNameOfRepresentativeCoverPage = '' #代表者の役職氏名、表紙
	TitleAndNameOfChiefFinancialOfficerCoverPage = '' #最高財務責任者の役職氏名、表紙
	AddressOfRegisteredHeadquarterCoverPage = '' #本店の所在の場所、表紙
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	BasicFrameworkOfInternalControlRelatedToFinancialReportingHeading = '' #財務報告に係る内部統制の基本的枠組みに関する事項 [目次項目]
	BasicFrameworkOfInternalControlRelatedToFinancialReportingTextBlock = '' #財務報告に係る内部統制の基本的枠組みに関する事項 [テキストブロック]
	ScopeDateAndProceduresForEvaluationHeading = '' #評価の範囲、基準日及び評価手続に関する事項 [目次項目]
	ScopeDateAndProceduresForEvaluationTextBlock = '' #評価の範囲、基準日及び評価手続に関する事項 [テキストブロック]
	ResultOfEvaluationHeading = '' #評価結果に関する事項 [目次項目]
	ResultOfEvaluationTextBlock = '' #評価結果に関する事項 [テキストブロック]
	SupplementaryInformationHeading = '' #付記事項 [目次項目]
	SupplementaryInformationTextBlock = '' #付記事項 [テキストブロック]
	OtherInformationForSpecialAttentionHeading = '' #特記事項 [目次項目]
	OtherInformationForSpecialAttentionTextBlock = '' #特記事項 [テキストブロック]
	IndependentAuditorsReportHeading = '' #独立監査人の報告書 [目次項目]
	IndependentAuditorsReportTextBlock = '' #独立監査人の報告書 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnSystemForEnsuringAppropriatenessOfFinancialAndOtherDocumentsFormNo1InternalControlReportHeading': #財務計算に関する書類その他の情報の適正性を確保するための体制に関する内閣府令 第一号様式 内部統制報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnSystemForEnsuringAppropriatenessOfFinancialAndOtherDocumentsFormNo1InternalControlReportHeading = fact.value

			elif fact.concept.qname.localName == 'CoverPageHeading': #表紙 [目次項目]
				self.CoverPageHeading = fact.value

			elif fact.concept.qname.localName == 'CoverPageHeading': #表紙 [目次項目]
				self.CoverPageHeading = fact.value

			elif fact.concept.qname.localName == 'DocumentTitleCoverPage': #提出書類、表紙
				self.DocumentTitleCoverPage = fact.value

			elif fact.concept.qname.localName == 'ClauseOfStipulationCoverPage': #根拠条文、表紙
				self.ClauseOfStipulationCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceOfFilingCoverPage': #提出先、表紙
				self.PlaceOfFilingCoverPage = fact.value

			elif fact.concept.qname.localName == 'FilingDateCoverPage': #提出日、表紙
				self.FilingDateCoverPage = fact.value

			elif fact.concept.qname.localName == 'CompanyNameCoverPage': #会社名、表紙
				self.CompanyNameCoverPage = fact.value

			elif fact.concept.qname.localName == 'CompanyNameInEnglishCoverPage': #英訳名、表紙
				self.CompanyNameInEnglishCoverPage = fact.value

			elif fact.concept.qname.localName == 'TitleAndNameOfRepresentativeCoverPage': #代表者の役職氏名、表紙
				self.TitleAndNameOfRepresentativeCoverPage = fact.value

			elif fact.concept.qname.localName == 'TitleAndNameOfChiefFinancialOfficerCoverPage': #最高財務責任者の役職氏名、表紙
				self.TitleAndNameOfChiefFinancialOfficerCoverPage = fact.value

			elif fact.concept.qname.localName == 'AddressOfRegisteredHeadquarterCoverPage': #本店の所在の場所、表紙
				self.AddressOfRegisteredHeadquarterCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'BasicFrameworkOfInternalControlRelatedToFinancialReportingHeading': #財務報告に係る内部統制の基本的枠組みに関する事項 [目次項目]
				self.BasicFrameworkOfInternalControlRelatedToFinancialReportingHeading = fact.value

			elif fact.concept.qname.localName == 'BasicFrameworkOfInternalControlRelatedToFinancialReportingTextBlock': #財務報告に係る内部統制の基本的枠組みに関する事項 [テキストブロック]
				self.BasicFrameworkOfInternalControlRelatedToFinancialReportingTextBlock = fact.value

			elif fact.concept.qname.localName == 'ScopeDateAndProceduresForEvaluationHeading': #評価の範囲、基準日及び評価手続に関する事項 [目次項目]
				self.ScopeDateAndProceduresForEvaluationHeading = fact.value

			elif fact.concept.qname.localName == 'ScopeDateAndProceduresForEvaluationTextBlock': #評価の範囲、基準日及び評価手続に関する事項 [テキストブロック]
				self.ScopeDateAndProceduresForEvaluationTextBlock = fact.value

			elif fact.concept.qname.localName == 'ResultOfEvaluationHeading': #評価結果に関する事項 [目次項目]
				self.ResultOfEvaluationHeading = fact.value

			elif fact.concept.qname.localName == 'ResultOfEvaluationTextBlock': #評価結果に関する事項 [テキストブロック]
				self.ResultOfEvaluationTextBlock = fact.value

			elif fact.concept.qname.localName == 'SupplementaryInformationHeading': #付記事項 [目次項目]
				self.SupplementaryInformationHeading = fact.value

			elif fact.concept.qname.localName == 'SupplementaryInformationTextBlock': #付記事項 [テキストブロック]
				self.SupplementaryInformationTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationForSpecialAttentionHeading': #特記事項 [目次項目]
				self.OtherInformationForSpecialAttentionHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationForSpecialAttentionTextBlock': #特記事項 [テキストブロック]
				self.OtherInformationForSpecialAttentionTextBlock = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportHeading': #独立監査人の報告書 [目次項目]
				self.IndependentAuditorsReportHeading = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportTextBlock': #独立監査人の報告書 [テキストブロック]
				self.IndependentAuditorsReportTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnSystemForEnsuringAppropriatenessOfFinancialAndOtherDocumentsFormNo1InternalControlReportHeading(self): #財務計算に関する書類その他の情報の適正性を確保するための体制に関する内閣府令 第一号様式 内部統制報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnSystemForEnsuringAppropriatenessOfFinancialAndOtherDocumentsFormNo1InternalControlReportHeading

	def getCoverPageHeading(self): #表紙 [目次項目]
		return self.CoverPageHeading

	def getCoverPageHeading(self): #表紙 [目次項目]
		return self.CoverPageHeading

	def getDocumentTitleCoverPage(self): #提出書類、表紙
		return self.DocumentTitleCoverPage

	def getClauseOfStipulationCoverPage(self): #根拠条文、表紙
		return self.ClauseOfStipulationCoverPage

	def getPlaceOfFilingCoverPage(self): #提出先、表紙
		return self.PlaceOfFilingCoverPage

	def getFilingDateCoverPage(self): #提出日、表紙
		return self.FilingDateCoverPage

	def getCompanyNameCoverPage(self): #会社名、表紙
		return self.CompanyNameCoverPage

	def getCompanyNameInEnglishCoverPage(self): #英訳名、表紙
		return self.CompanyNameInEnglishCoverPage

	def getTitleAndNameOfRepresentativeCoverPage(self): #代表者の役職氏名、表紙
		return self.TitleAndNameOfRepresentativeCoverPage

	def getTitleAndNameOfChiefFinancialOfficerCoverPage(self): #最高財務責任者の役職氏名、表紙
		return self.TitleAndNameOfChiefFinancialOfficerCoverPage

	def getAddressOfRegisteredHeadquarterCoverPage(self): #本店の所在の場所、表紙
		return self.AddressOfRegisteredHeadquarterCoverPage

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getBasicFrameworkOfInternalControlRelatedToFinancialReportingHeading(self): #財務報告に係る内部統制の基本的枠組みに関する事項 [目次項目]
		return self.BasicFrameworkOfInternalControlRelatedToFinancialReportingHeading

	def getBasicFrameworkOfInternalControlRelatedToFinancialReportingTextBlock(self): #財務報告に係る内部統制の基本的枠組みに関する事項 [テキストブロック]
		return self.BasicFrameworkOfInternalControlRelatedToFinancialReportingTextBlock

	def getScopeDateAndProceduresForEvaluationHeading(self): #評価の範囲、基準日及び評価手続に関する事項 [目次項目]
		return self.ScopeDateAndProceduresForEvaluationHeading

	def getScopeDateAndProceduresForEvaluationTextBlock(self): #評価の範囲、基準日及び評価手続に関する事項 [テキストブロック]
		return self.ScopeDateAndProceduresForEvaluationTextBlock

	def getResultOfEvaluationHeading(self): #評価結果に関する事項 [目次項目]
		return self.ResultOfEvaluationHeading

	def getResultOfEvaluationTextBlock(self): #評価結果に関する事項 [テキストブロック]
		return self.ResultOfEvaluationTextBlock

	def getSupplementaryInformationHeading(self): #付記事項 [目次項目]
		return self.SupplementaryInformationHeading

	def getSupplementaryInformationTextBlock(self): #付記事項 [テキストブロック]
		return self.SupplementaryInformationTextBlock

	def getOtherInformationForSpecialAttentionHeading(self): #特記事項 [目次項目]
		return self.OtherInformationForSpecialAttentionHeading

	def getOtherInformationForSpecialAttentionTextBlock(self): #特記事項 [テキストブロック]
		return self.OtherInformationForSpecialAttentionTextBlock

	def getIndependentAuditorsReportHeading(self): #独立監査人の報告書 [目次項目]
		return self.IndependentAuditorsReportHeading

	def getIndependentAuditorsReportTextBlock(self): #独立監査人の報告書 [テキストブロック]
		return self.IndependentAuditorsReportTextBlock
