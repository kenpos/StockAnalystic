from arelle import ModelManager
from arelle import Cntlr

class jpsps150300:#特定有価証券の内容等の開示に関する内閣府令 第十五号の三様式 発行登録書
	CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo153ShelfRegistrationStatementHeading = '' #特定有価証券の内容等の開示に関する内閣府令 第十五号の三様式 発行登録書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	ShelfRegistrationNumberCoverPage = '' #発行登録番号、表紙
	DocumentTitleCoverPage = '' #提出書類、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	IssuerNameCoverPage = '' #発行者名、表紙
	TitleAndNameOfRepresentativeCoverPage = '' #代表者の役職氏名、表紙
	AddressOfRegisteredHeadquarterCoverPage = '' #本店の所在の場所、表紙
	NameOfContactPersonCoverPage = '' #事務連絡者氏名、表紙
	TelephoneNumberCoverPage = '' #電話番号、表紙
	NameOfInvestmentCorporationRelatedToDomesticInvestmentCorporationBondsToShelfRegisterForOfferingOrDistributionCoverPage = '' #発行登録の対象とした募集（売出）短期投資法人債に係る投資法人の名称、表紙
	PlannedPeriodOfIssueCoverPage = '' #発行予定期間、表紙
	PlannedAmountOfIssueOrLimitOnOutstandingBalanceCoverPage = '' #発行予定額又は発行残高の上限、表紙
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	SecurityInformationHeading = '' #証券情報 [目次項目]
	ParticularsOfPublicOfferingShelfRegistrationStatementHeading = '' #募集要項、発行登録書 [目次項目]
	ShortTermInvestmentCorporationBondsShelfRegistrationStatementHeading = '' #短期投資法人債、発行登録書 [目次項目]
	ShortTermInvestmentCorporationBondsShelfRegistrationStatementTextBlock = '' #短期投資法人債、発行登録書 [テキストブロック]
	OtherInformationShelfRegistrationStatementHeading = '' #その他の記載事項、発行登録書 [目次項目]
	OtherInformationShelfRegistrationStatementTextBlock = '' #その他の記載事項、発行登録書 [テキストブロック]
	ReferenceInformationHeading = '' #参照情報 [目次項目]
	ReferenceDocumentsHeading = '' #参照書類 [目次項目]
	AnnualSecuritiesReportAndAttachedDocumentsHeading = '' #有価証券報告書及びその添付書類 [目次項目]
	AnnualSecuritiesReportAndAttachedDocumentsTextBlock = '' #有価証券報告書及びその添付書類 [テキストブロック]
	SemiAnnualSecuritiesReportHeading = '' #半期報告書 [目次項目]
	SemiAnnualSecuritiesReportTextBlock = '' #半期報告書 [テキストブロック]
	ExtraordinarySecuritiesReportHeading = '' #臨時報告書 [目次項目]
	ExtraordinarySecuritiesReportTextBlock = '' #臨時報告書 [テキストブロック]
	AmendmentReportHeading = '' #訂正報告書 [目次項目]
	AmendmentReportTextBlock = '' #訂正報告書 [テキストブロック]
	SupplementaryInformationAboutReferenceDocumentsHeading = '' #参照書類の補完情報 [目次項目]
	SupplementaryInformationAboutReferenceDocumentsTextBlock = '' #参照書類の補完情報 [テキストブロック]
	PlaceForPublicInspectionOfReferenceDocumentsHeading = '' #参照書類を縦覧に供している場所 [目次項目]
	PlaceForPublicInspectionOfReferenceDocumentsTextBlock = '' #参照書類を縦覧に供している場所 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo153ShelfRegistrationStatementHeading': #特定有価証券の内容等の開示に関する内閣府令 第十五号の三様式 発行登録書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo153ShelfRegistrationStatementHeading = fact.value

			elif fact.concept.qname.localName == 'CoverPageHeading': #表紙 [目次項目]
				self.CoverPageHeading = fact.value

			elif fact.concept.qname.localName == 'CoverPageHeading': #表紙 [目次項目]
				self.CoverPageHeading = fact.value

			elif fact.concept.qname.localName == 'ShelfRegistrationNumberCoverPage': #発行登録番号、表紙
				self.ShelfRegistrationNumberCoverPage = fact.value

			elif fact.concept.qname.localName == 'DocumentTitleCoverPage': #提出書類、表紙
				self.DocumentTitleCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceOfFilingCoverPage': #提出先、表紙
				self.PlaceOfFilingCoverPage = fact.value

			elif fact.concept.qname.localName == 'FilingDateCoverPage': #提出日、表紙
				self.FilingDateCoverPage = fact.value

			elif fact.concept.qname.localName == 'IssuerNameCoverPage': #発行者名、表紙
				self.IssuerNameCoverPage = fact.value

			elif fact.concept.qname.localName == 'TitleAndNameOfRepresentativeCoverPage': #代表者の役職氏名、表紙
				self.TitleAndNameOfRepresentativeCoverPage = fact.value

			elif fact.concept.qname.localName == 'AddressOfRegisteredHeadquarterCoverPage': #本店の所在の場所、表紙
				self.AddressOfRegisteredHeadquarterCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonCoverPage': #事務連絡者氏名、表紙
				self.NameOfContactPersonCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberCoverPage': #電話番号、表紙
				self.TelephoneNumberCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationRelatedToDomesticInvestmentCorporationBondsToShelfRegisterForOfferingOrDistributionCoverPage': #発行登録の対象とした募集（売出）短期投資法人債に係る投資法人の名称、表紙
				self.NameOfInvestmentCorporationRelatedToDomesticInvestmentCorporationBondsToShelfRegisterForOfferingOrDistributionCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlannedPeriodOfIssueCoverPage': #発行予定期間、表紙
				self.PlannedPeriodOfIssueCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlannedAmountOfIssueOrLimitOnOutstandingBalanceCoverPage': #発行予定額又は発行残高の上限、表紙
				self.PlannedAmountOfIssueOrLimitOnOutstandingBalanceCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'SecurityInformationHeading': #証券情報 [目次項目]
				self.SecurityInformationHeading = fact.value

			elif fact.concept.qname.localName == 'ParticularsOfPublicOfferingShelfRegistrationStatementHeading': #募集要項、発行登録書 [目次項目]
				self.ParticularsOfPublicOfferingShelfRegistrationStatementHeading = fact.value

			elif fact.concept.qname.localName == 'ShortTermInvestmentCorporationBondsShelfRegistrationStatementHeading': #短期投資法人債、発行登録書 [目次項目]
				self.ShortTermInvestmentCorporationBondsShelfRegistrationStatementHeading = fact.value

			elif fact.concept.qname.localName == 'ShortTermInvestmentCorporationBondsShelfRegistrationStatementTextBlock': #短期投資法人債、発行登録書 [テキストブロック]
				self.ShortTermInvestmentCorporationBondsShelfRegistrationStatementTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationShelfRegistrationStatementHeading': #その他の記載事項、発行登録書 [目次項目]
				self.OtherInformationShelfRegistrationStatementHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationShelfRegistrationStatementTextBlock': #その他の記載事項、発行登録書 [テキストブロック]
				self.OtherInformationShelfRegistrationStatementTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReferenceInformationHeading': #参照情報 [目次項目]
				self.ReferenceInformationHeading = fact.value

			elif fact.concept.qname.localName == 'ReferenceDocumentsHeading': #参照書類 [目次項目]
				self.ReferenceDocumentsHeading = fact.value

			elif fact.concept.qname.localName == 'AnnualSecuritiesReportAndAttachedDocumentsHeading': #有価証券報告書及びその添付書類 [目次項目]
				self.AnnualSecuritiesReportAndAttachedDocumentsHeading = fact.value

			elif fact.concept.qname.localName == 'AnnualSecuritiesReportAndAttachedDocumentsTextBlock': #有価証券報告書及びその添付書類 [テキストブロック]
				self.AnnualSecuritiesReportAndAttachedDocumentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualSecuritiesReportHeading': #半期報告書 [目次項目]
				self.SemiAnnualSecuritiesReportHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualSecuritiesReportTextBlock': #半期報告書 [テキストブロック]
				self.SemiAnnualSecuritiesReportTextBlock = fact.value

			elif fact.concept.qname.localName == 'ExtraordinarySecuritiesReportHeading': #臨時報告書 [目次項目]
				self.ExtraordinarySecuritiesReportHeading = fact.value

			elif fact.concept.qname.localName == 'ExtraordinarySecuritiesReportTextBlock': #臨時報告書 [テキストブロック]
				self.ExtraordinarySecuritiesReportTextBlock = fact.value

			elif fact.concept.qname.localName == 'AmendmentReportHeading': #訂正報告書 [目次項目]
				self.AmendmentReportHeading = fact.value

			elif fact.concept.qname.localName == 'AmendmentReportTextBlock': #訂正報告書 [テキストブロック]
				self.AmendmentReportTextBlock = fact.value

			elif fact.concept.qname.localName == 'SupplementaryInformationAboutReferenceDocumentsHeading': #参照書類の補完情報 [目次項目]
				self.SupplementaryInformationAboutReferenceDocumentsHeading = fact.value

			elif fact.concept.qname.localName == 'SupplementaryInformationAboutReferenceDocumentsTextBlock': #参照書類の補完情報 [テキストブロック]
				self.SupplementaryInformationAboutReferenceDocumentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionOfReferenceDocumentsHeading': #参照書類を縦覧に供している場所 [目次項目]
				self.PlaceForPublicInspectionOfReferenceDocumentsHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionOfReferenceDocumentsTextBlock': #参照書類を縦覧に供している場所 [テキストブロック]
				self.PlaceForPublicInspectionOfReferenceDocumentsTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo153ShelfRegistrationStatementHeading(self): #特定有価証券の内容等の開示に関する内閣府令 第十五号の三様式 発行登録書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo153ShelfRegistrationStatementHeading

	def getCoverPageHeading(self): #表紙 [目次項目]
		return self.CoverPageHeading

	def getCoverPageHeading(self): #表紙 [目次項目]
		return self.CoverPageHeading

	def getShelfRegistrationNumberCoverPage(self): #発行登録番号、表紙
		return self.ShelfRegistrationNumberCoverPage

	def getDocumentTitleCoverPage(self): #提出書類、表紙
		return self.DocumentTitleCoverPage

	def getPlaceOfFilingCoverPage(self): #提出先、表紙
		return self.PlaceOfFilingCoverPage

	def getFilingDateCoverPage(self): #提出日、表紙
		return self.FilingDateCoverPage

	def getIssuerNameCoverPage(self): #発行者名、表紙
		return self.IssuerNameCoverPage

	def getTitleAndNameOfRepresentativeCoverPage(self): #代表者の役職氏名、表紙
		return self.TitleAndNameOfRepresentativeCoverPage

	def getAddressOfRegisteredHeadquarterCoverPage(self): #本店の所在の場所、表紙
		return self.AddressOfRegisteredHeadquarterCoverPage

	def getNameOfContactPersonCoverPage(self): #事務連絡者氏名、表紙
		return self.NameOfContactPersonCoverPage

	def getTelephoneNumberCoverPage(self): #電話番号、表紙
		return self.TelephoneNumberCoverPage

	def getNameOfInvestmentCorporationRelatedToDomesticInvestmentCorporationBondsToShelfRegisterForOfferingOrDistributionCoverPage(self): #発行登録の対象とした募集（売出）短期投資法人債に係る投資法人の名称、表紙
		return self.NameOfInvestmentCorporationRelatedToDomesticInvestmentCorporationBondsToShelfRegisterForOfferingOrDistributionCoverPage

	def getPlannedPeriodOfIssueCoverPage(self): #発行予定期間、表紙
		return self.PlannedPeriodOfIssueCoverPage

	def getPlannedAmountOfIssueOrLimitOnOutstandingBalanceCoverPage(self): #発行予定額又は発行残高の上限、表紙
		return self.PlannedAmountOfIssueOrLimitOnOutstandingBalanceCoverPage

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getSecurityInformationHeading(self): #証券情報 [目次項目]
		return self.SecurityInformationHeading

	def getParticularsOfPublicOfferingShelfRegistrationStatementHeading(self): #募集要項、発行登録書 [目次項目]
		return self.ParticularsOfPublicOfferingShelfRegistrationStatementHeading

	def getShortTermInvestmentCorporationBondsShelfRegistrationStatementHeading(self): #短期投資法人債、発行登録書 [目次項目]
		return self.ShortTermInvestmentCorporationBondsShelfRegistrationStatementHeading

	def getShortTermInvestmentCorporationBondsShelfRegistrationStatementTextBlock(self): #短期投資法人債、発行登録書 [テキストブロック]
		return self.ShortTermInvestmentCorporationBondsShelfRegistrationStatementTextBlock

	def getOtherInformationShelfRegistrationStatementHeading(self): #その他の記載事項、発行登録書 [目次項目]
		return self.OtherInformationShelfRegistrationStatementHeading

	def getOtherInformationShelfRegistrationStatementTextBlock(self): #その他の記載事項、発行登録書 [テキストブロック]
		return self.OtherInformationShelfRegistrationStatementTextBlock

	def getReferenceInformationHeading(self): #参照情報 [目次項目]
		return self.ReferenceInformationHeading

	def getReferenceDocumentsHeading(self): #参照書類 [目次項目]
		return self.ReferenceDocumentsHeading

	def getAnnualSecuritiesReportAndAttachedDocumentsHeading(self): #有価証券報告書及びその添付書類 [目次項目]
		return self.AnnualSecuritiesReportAndAttachedDocumentsHeading

	def getAnnualSecuritiesReportAndAttachedDocumentsTextBlock(self): #有価証券報告書及びその添付書類 [テキストブロック]
		return self.AnnualSecuritiesReportAndAttachedDocumentsTextBlock

	def getSemiAnnualSecuritiesReportHeading(self): #半期報告書 [目次項目]
		return self.SemiAnnualSecuritiesReportHeading

	def getSemiAnnualSecuritiesReportTextBlock(self): #半期報告書 [テキストブロック]
		return self.SemiAnnualSecuritiesReportTextBlock

	def getExtraordinarySecuritiesReportHeading(self): #臨時報告書 [目次項目]
		return self.ExtraordinarySecuritiesReportHeading

	def getExtraordinarySecuritiesReportTextBlock(self): #臨時報告書 [テキストブロック]
		return self.ExtraordinarySecuritiesReportTextBlock

	def getAmendmentReportHeading(self): #訂正報告書 [目次項目]
		return self.AmendmentReportHeading

	def getAmendmentReportTextBlock(self): #訂正報告書 [テキストブロック]
		return self.AmendmentReportTextBlock

	def getSupplementaryInformationAboutReferenceDocumentsHeading(self): #参照書類の補完情報 [目次項目]
		return self.SupplementaryInformationAboutReferenceDocumentsHeading

	def getSupplementaryInformationAboutReferenceDocumentsTextBlock(self): #参照書類の補完情報 [テキストブロック]
		return self.SupplementaryInformationAboutReferenceDocumentsTextBlock

	def getPlaceForPublicInspectionOfReferenceDocumentsHeading(self): #参照書類を縦覧に供している場所 [目次項目]
		return self.PlaceForPublicInspectionOfReferenceDocumentsHeading

	def getPlaceForPublicInspectionOfReferenceDocumentsTextBlock(self): #参照書類を縦覧に供している場所 [テキストブロック]
		return self.PlaceForPublicInspectionOfReferenceDocumentsTextBlock
