from arelle import ModelManager
from arelle import Cntlr

class jpcrp110200:#企業内容等の開示に関する内閣府令 第十一号の二様式 発行登録書
	CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo112ShelfRegistrationStatementHeading = '' #企業内容等の開示に関する内閣府令 第十一号の二様式 発行登録書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	ShelfRegistrationNumberCoverPage = '' #発行登録番号、表紙
	DocumentTitleCoverPage = '' #提出書類、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	CompanyNameCoverPage = '' #会社名、表紙
	CompanyNameInEnglishCoverPage = '' #英訳名、表紙
	TitleAndNameOfRepresentativeCoverPage = '' #代表者の役職氏名、表紙
	AddressOfRegisteredHeadquarterCoverPage = '' #本店の所在の場所、表紙
	TelephoneNumberAddressOfRegisteredHeadquarterCoverPage = '' #電話番号、本店の所在の場所、表紙
	NameOfContactPersonAddressOfRegisteredHeadquarterCoverPage = '' #事務連絡者氏名、本店の所在の場所、表紙
	NearestPlaceOfContactCoverPage = '' #最寄りの連絡場所、表紙
	TelephoneNumberNearestPlaceOfContactCoverPage = '' #電話番号、最寄りの連絡場所、表紙
	NameOfContactPersonNearestPlaceOfContactCoverPage = '' #事務連絡者氏名、最寄りの連絡場所、表紙
	TypesOfSecuritiesToShelfRegisterForOfferingOrDistributionCoverPage = '' #発行登録の対象とした募集（売出）有価証券の種類、表紙
	PlannedPeriodOfIssueCoverPage = '' #発行予定期間、表紙
	PlannedAmountOfIssueOrLimitOnOutstandingBalanceCoverPageTextBlock = '' #発行予定額又は発行残高の上限、表紙 [テキストブロック]
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	FootnotesCoverPageTextBlock = '' #脚注、表紙 [テキストブロック]
	SecurityInformationHeading = '' #証券情報 [目次項目]
	ParticularsOfPublicOfferingHeading = '' #募集要項 [目次項目]
	ParticularsOfPublicOfferingTextBlock = '' #募集要項 [テキストブロック]
	NewIssuanceOfCommercialPapersHeading = '' #新規発行コマーシャル・ペーパー [目次項目]
	NewIssuanceOfCommercialPapersTextBlock = '' #新規発行コマーシャル・ペーパー [テキストブロック]
	UseOfNetProceedsFromNewIssuanceHeading = '' #新規発行による手取金の使途 [目次項目]
	UseOfNetProceedsFromNewIssuanceTextBlock = '' #新規発行による手取金の使途 [テキストブロック]
	ParticularsOfSecondaryDistributionHeading = '' #売出要項 [目次項目]
	ParticularsOfSecondaryDistributionTextBlock = '' #売出要項 [テキストブロック]
	SecondaryDistributionOfCommercialPapersHeading = '' #売出コマーシャル・ペーパー [目次項目]
	SecondaryDistributionOfCommercialPapersTextBlock = '' #売出コマーシャル・ペーパー [テキストブロック]
	TermsOfSecondaryDistributionHeading = '' #売出しの条件 [目次項目]
	TermsOfSecondaryDistributionTextBlock = '' #売出しの条件 [テキストブロック]
	SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading = '' #募集又は売出しに関する特別記載事項 [目次項目]
	SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock = '' #募集又は売出しに関する特別記載事項 [テキストブロック]
	OtherInformationSecurityInformationHeading = '' #その他の記載事項、証券情報 [目次項目]
	OtherInformationSecurityInformationTextBlock = '' #その他の記載事項、証券情報 [テキストブロック]
	ReferenceInformationHeading = '' #参照情報 [目次項目]
	ReferenceDocumentsHeading = '' #参照書類 [目次項目]
	AnnualSecuritiesReportAndAttachedDocumentsReferenceDocumentsHeading = '' #有価証券報告書及びその添付書類、参照書類 [目次項目]
	AnnualSecuritiesReportAndAttachedDocumentsReferenceDocumentsTextBlock = '' #有価証券報告書及びその添付書類、参照書類 [テキストブロック]
	QuarterlySecuritiesReportOrSemiAnnualSecuritiesReportReferenceDocumentsHeading = '' #四半期報告書又は半期報告書、参照書類 [目次項目]
	QuarterlySecuritiesReportOrSemiAnnualSecuritiesReportReferenceDocumentsTextBlock = '' #四半期報告書又は半期報告書、参照書類 [テキストブロック]
	ExtraordinarySecuritiesReportReferenceDocumentsHeading = '' #臨時報告書、参照書類 [目次項目]
	ExtraordinarySecuritiesReportReferenceDocumentsTextBlock = '' #臨時報告書、参照書類 [テキストブロック]
	AmendmentReportReferenceDocumentsHeading = '' #訂正報告書、参照書類 [目次項目]
	AmendmentReportReferenceDocumentsTextBlock = '' #訂正報告書、参照書類 [テキストブロック]
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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo112ShelfRegistrationStatementHeading': #企業内容等の開示に関する内閣府令 第十一号の二様式 発行登録書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo112ShelfRegistrationStatementHeading = fact.value

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

			elif fact.concept.qname.localName == 'CompanyNameCoverPage': #会社名、表紙
				self.CompanyNameCoverPage = fact.value

			elif fact.concept.qname.localName == 'CompanyNameInEnglishCoverPage': #英訳名、表紙
				self.CompanyNameInEnglishCoverPage = fact.value

			elif fact.concept.qname.localName == 'TitleAndNameOfRepresentativeCoverPage': #代表者の役職氏名、表紙
				self.TitleAndNameOfRepresentativeCoverPage = fact.value

			elif fact.concept.qname.localName == 'AddressOfRegisteredHeadquarterCoverPage': #本店の所在の場所、表紙
				self.AddressOfRegisteredHeadquarterCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberAddressOfRegisteredHeadquarterCoverPage': #電話番号、本店の所在の場所、表紙
				self.TelephoneNumberAddressOfRegisteredHeadquarterCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonAddressOfRegisteredHeadquarterCoverPage': #事務連絡者氏名、本店の所在の場所、表紙
				self.NameOfContactPersonAddressOfRegisteredHeadquarterCoverPage = fact.value

			elif fact.concept.qname.localName == 'NearestPlaceOfContactCoverPage': #最寄りの連絡場所、表紙
				self.NearestPlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberNearestPlaceOfContactCoverPage': #電話番号、最寄りの連絡場所、表紙
				self.TelephoneNumberNearestPlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonNearestPlaceOfContactCoverPage': #事務連絡者氏名、最寄りの連絡場所、表紙
				self.NameOfContactPersonNearestPlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'TypesOfSecuritiesToShelfRegisterForOfferingOrDistributionCoverPage': #発行登録の対象とした募集（売出）有価証券の種類、表紙
				self.TypesOfSecuritiesToShelfRegisterForOfferingOrDistributionCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlannedPeriodOfIssueCoverPage': #発行予定期間、表紙
				self.PlannedPeriodOfIssueCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlannedAmountOfIssueOrLimitOnOutstandingBalanceCoverPageTextBlock': #発行予定額又は発行残高の上限、表紙 [テキストブロック]
				self.PlannedAmountOfIssueOrLimitOnOutstandingBalanceCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'FootnotesCoverPageTextBlock': #脚注、表紙 [テキストブロック]
				self.FootnotesCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'SecurityInformationHeading': #証券情報 [目次項目]
				self.SecurityInformationHeading = fact.value

			elif fact.concept.qname.localName == 'ParticularsOfPublicOfferingHeading': #募集要項 [目次項目]
				self.ParticularsOfPublicOfferingHeading = fact.value

			elif fact.concept.qname.localName == 'ParticularsOfPublicOfferingTextBlock': #募集要項 [テキストブロック]
				self.ParticularsOfPublicOfferingTextBlock = fact.value

			elif fact.concept.qname.localName == 'NewIssuanceOfCommercialPapersHeading': #新規発行コマーシャル・ペーパー [目次項目]
				self.NewIssuanceOfCommercialPapersHeading = fact.value

			elif fact.concept.qname.localName == 'NewIssuanceOfCommercialPapersTextBlock': #新規発行コマーシャル・ペーパー [テキストブロック]
				self.NewIssuanceOfCommercialPapersTextBlock = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsFromNewIssuanceHeading': #新規発行による手取金の使途 [目次項目]
				self.UseOfNetProceedsFromNewIssuanceHeading = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsFromNewIssuanceTextBlock': #新規発行による手取金の使途 [テキストブロック]
				self.UseOfNetProceedsFromNewIssuanceTextBlock = fact.value

			elif fact.concept.qname.localName == 'ParticularsOfSecondaryDistributionHeading': #売出要項 [目次項目]
				self.ParticularsOfSecondaryDistributionHeading = fact.value

			elif fact.concept.qname.localName == 'ParticularsOfSecondaryDistributionTextBlock': #売出要項 [テキストブロック]
				self.ParticularsOfSecondaryDistributionTextBlock = fact.value

			elif fact.concept.qname.localName == 'SecondaryDistributionOfCommercialPapersHeading': #売出コマーシャル・ペーパー [目次項目]
				self.SecondaryDistributionOfCommercialPapersHeading = fact.value

			elif fact.concept.qname.localName == 'SecondaryDistributionOfCommercialPapersTextBlock': #売出コマーシャル・ペーパー [テキストブロック]
				self.SecondaryDistributionOfCommercialPapersTextBlock = fact.value

			elif fact.concept.qname.localName == 'TermsOfSecondaryDistributionHeading': #売出しの条件 [目次項目]
				self.TermsOfSecondaryDistributionHeading = fact.value

			elif fact.concept.qname.localName == 'TermsOfSecondaryDistributionTextBlock': #売出しの条件 [テキストブロック]
				self.TermsOfSecondaryDistributionTextBlock = fact.value

			elif fact.concept.qname.localName == 'SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading': #募集又は売出しに関する特別記載事項 [目次項目]
				self.SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading = fact.value

			elif fact.concept.qname.localName == 'SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock': #募集又は売出しに関する特別記載事項 [テキストブロック]
				self.SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationSecurityInformationHeading': #その他の記載事項、証券情報 [目次項目]
				self.OtherInformationSecurityInformationHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationSecurityInformationTextBlock': #その他の記載事項、証券情報 [テキストブロック]
				self.OtherInformationSecurityInformationTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReferenceInformationHeading': #参照情報 [目次項目]
				self.ReferenceInformationHeading = fact.value

			elif fact.concept.qname.localName == 'ReferenceDocumentsHeading': #参照書類 [目次項目]
				self.ReferenceDocumentsHeading = fact.value

			elif fact.concept.qname.localName == 'AnnualSecuritiesReportAndAttachedDocumentsReferenceDocumentsHeading': #有価証券報告書及びその添付書類、参照書類 [目次項目]
				self.AnnualSecuritiesReportAndAttachedDocumentsReferenceDocumentsHeading = fact.value

			elif fact.concept.qname.localName == 'AnnualSecuritiesReportAndAttachedDocumentsReferenceDocumentsTextBlock': #有価証券報告書及びその添付書類、参照書類 [テキストブロック]
				self.AnnualSecuritiesReportAndAttachedDocumentsReferenceDocumentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlySecuritiesReportOrSemiAnnualSecuritiesReportReferenceDocumentsHeading': #四半期報告書又は半期報告書、参照書類 [目次項目]
				self.QuarterlySecuritiesReportOrSemiAnnualSecuritiesReportReferenceDocumentsHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterlySecuritiesReportOrSemiAnnualSecuritiesReportReferenceDocumentsTextBlock': #四半期報告書又は半期報告書、参照書類 [テキストブロック]
				self.QuarterlySecuritiesReportOrSemiAnnualSecuritiesReportReferenceDocumentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ExtraordinarySecuritiesReportReferenceDocumentsHeading': #臨時報告書、参照書類 [目次項目]
				self.ExtraordinarySecuritiesReportReferenceDocumentsHeading = fact.value

			elif fact.concept.qname.localName == 'ExtraordinarySecuritiesReportReferenceDocumentsTextBlock': #臨時報告書、参照書類 [テキストブロック]
				self.ExtraordinarySecuritiesReportReferenceDocumentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AmendmentReportReferenceDocumentsHeading': #訂正報告書、参照書類 [目次項目]
				self.AmendmentReportReferenceDocumentsHeading = fact.value

			elif fact.concept.qname.localName == 'AmendmentReportReferenceDocumentsTextBlock': #訂正報告書、参照書類 [テキストブロック]
				self.AmendmentReportReferenceDocumentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'SupplementaryInformationAboutReferenceDocumentsHeading': #参照書類の補完情報 [目次項目]
				self.SupplementaryInformationAboutReferenceDocumentsHeading = fact.value

			elif fact.concept.qname.localName == 'SupplementaryInformationAboutReferenceDocumentsTextBlock': #参照書類の補完情報 [テキストブロック]
				self.SupplementaryInformationAboutReferenceDocumentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionOfReferenceDocumentsHeading': #参照書類を縦覧に供している場所 [目次項目]
				self.PlaceForPublicInspectionOfReferenceDocumentsHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionOfReferenceDocumentsTextBlock': #参照書類を縦覧に供している場所 [テキストブロック]
				self.PlaceForPublicInspectionOfReferenceDocumentsTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo112ShelfRegistrationStatementHeading(self): #企業内容等の開示に関する内閣府令 第十一号の二様式 発行登録書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo112ShelfRegistrationStatementHeading

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

	def getCompanyNameCoverPage(self): #会社名、表紙
		return self.CompanyNameCoverPage

	def getCompanyNameInEnglishCoverPage(self): #英訳名、表紙
		return self.CompanyNameInEnglishCoverPage

	def getTitleAndNameOfRepresentativeCoverPage(self): #代表者の役職氏名、表紙
		return self.TitleAndNameOfRepresentativeCoverPage

	def getAddressOfRegisteredHeadquarterCoverPage(self): #本店の所在の場所、表紙
		return self.AddressOfRegisteredHeadquarterCoverPage

	def getTelephoneNumberAddressOfRegisteredHeadquarterCoverPage(self): #電話番号、本店の所在の場所、表紙
		return self.TelephoneNumberAddressOfRegisteredHeadquarterCoverPage

	def getNameOfContactPersonAddressOfRegisteredHeadquarterCoverPage(self): #事務連絡者氏名、本店の所在の場所、表紙
		return self.NameOfContactPersonAddressOfRegisteredHeadquarterCoverPage

	def getNearestPlaceOfContactCoverPage(self): #最寄りの連絡場所、表紙
		return self.NearestPlaceOfContactCoverPage

	def getTelephoneNumberNearestPlaceOfContactCoverPage(self): #電話番号、最寄りの連絡場所、表紙
		return self.TelephoneNumberNearestPlaceOfContactCoverPage

	def getNameOfContactPersonNearestPlaceOfContactCoverPage(self): #事務連絡者氏名、最寄りの連絡場所、表紙
		return self.NameOfContactPersonNearestPlaceOfContactCoverPage

	def getTypesOfSecuritiesToShelfRegisterForOfferingOrDistributionCoverPage(self): #発行登録の対象とした募集（売出）有価証券の種類、表紙
		return self.TypesOfSecuritiesToShelfRegisterForOfferingOrDistributionCoverPage

	def getPlannedPeriodOfIssueCoverPage(self): #発行予定期間、表紙
		return self.PlannedPeriodOfIssueCoverPage

	def getPlannedAmountOfIssueOrLimitOnOutstandingBalanceCoverPageTextBlock(self): #発行予定額又は発行残高の上限、表紙 [テキストブロック]
		return self.PlannedAmountOfIssueOrLimitOnOutstandingBalanceCoverPageTextBlock

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getFootnotesCoverPageTextBlock(self): #脚注、表紙 [テキストブロック]
		return self.FootnotesCoverPageTextBlock

	def getSecurityInformationHeading(self): #証券情報 [目次項目]
		return self.SecurityInformationHeading

	def getParticularsOfPublicOfferingHeading(self): #募集要項 [目次項目]
		return self.ParticularsOfPublicOfferingHeading

	def getParticularsOfPublicOfferingTextBlock(self): #募集要項 [テキストブロック]
		return self.ParticularsOfPublicOfferingTextBlock

	def getNewIssuanceOfCommercialPapersHeading(self): #新規発行コマーシャル・ペーパー [目次項目]
		return self.NewIssuanceOfCommercialPapersHeading

	def getNewIssuanceOfCommercialPapersTextBlock(self): #新規発行コマーシャル・ペーパー [テキストブロック]
		return self.NewIssuanceOfCommercialPapersTextBlock

	def getUseOfNetProceedsFromNewIssuanceHeading(self): #新規発行による手取金の使途 [目次項目]
		return self.UseOfNetProceedsFromNewIssuanceHeading

	def getUseOfNetProceedsFromNewIssuanceTextBlock(self): #新規発行による手取金の使途 [テキストブロック]
		return self.UseOfNetProceedsFromNewIssuanceTextBlock

	def getParticularsOfSecondaryDistributionHeading(self): #売出要項 [目次項目]
		return self.ParticularsOfSecondaryDistributionHeading

	def getParticularsOfSecondaryDistributionTextBlock(self): #売出要項 [テキストブロック]
		return self.ParticularsOfSecondaryDistributionTextBlock

	def getSecondaryDistributionOfCommercialPapersHeading(self): #売出コマーシャル・ペーパー [目次項目]
		return self.SecondaryDistributionOfCommercialPapersHeading

	def getSecondaryDistributionOfCommercialPapersTextBlock(self): #売出コマーシャル・ペーパー [テキストブロック]
		return self.SecondaryDistributionOfCommercialPapersTextBlock

	def getTermsOfSecondaryDistributionHeading(self): #売出しの条件 [目次項目]
		return self.TermsOfSecondaryDistributionHeading

	def getTermsOfSecondaryDistributionTextBlock(self): #売出しの条件 [テキストブロック]
		return self.TermsOfSecondaryDistributionTextBlock

	def getSpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading(self): #募集又は売出しに関する特別記載事項 [目次項目]
		return self.SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading

	def getSpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock(self): #募集又は売出しに関する特別記載事項 [テキストブロック]
		return self.SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock

	def getOtherInformationSecurityInformationHeading(self): #その他の記載事項、証券情報 [目次項目]
		return self.OtherInformationSecurityInformationHeading

	def getOtherInformationSecurityInformationTextBlock(self): #その他の記載事項、証券情報 [テキストブロック]
		return self.OtherInformationSecurityInformationTextBlock

	def getReferenceInformationHeading(self): #参照情報 [目次項目]
		return self.ReferenceInformationHeading

	def getReferenceDocumentsHeading(self): #参照書類 [目次項目]
		return self.ReferenceDocumentsHeading

	def getAnnualSecuritiesReportAndAttachedDocumentsReferenceDocumentsHeading(self): #有価証券報告書及びその添付書類、参照書類 [目次項目]
		return self.AnnualSecuritiesReportAndAttachedDocumentsReferenceDocumentsHeading

	def getAnnualSecuritiesReportAndAttachedDocumentsReferenceDocumentsTextBlock(self): #有価証券報告書及びその添付書類、参照書類 [テキストブロック]
		return self.AnnualSecuritiesReportAndAttachedDocumentsReferenceDocumentsTextBlock

	def getQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportReferenceDocumentsHeading(self): #四半期報告書又は半期報告書、参照書類 [目次項目]
		return self.QuarterlySecuritiesReportOrSemiAnnualSecuritiesReportReferenceDocumentsHeading

	def getQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportReferenceDocumentsTextBlock(self): #四半期報告書又は半期報告書、参照書類 [テキストブロック]
		return self.QuarterlySecuritiesReportOrSemiAnnualSecuritiesReportReferenceDocumentsTextBlock

	def getExtraordinarySecuritiesReportReferenceDocumentsHeading(self): #臨時報告書、参照書類 [目次項目]
		return self.ExtraordinarySecuritiesReportReferenceDocumentsHeading

	def getExtraordinarySecuritiesReportReferenceDocumentsTextBlock(self): #臨時報告書、参照書類 [テキストブロック]
		return self.ExtraordinarySecuritiesReportReferenceDocumentsTextBlock

	def getAmendmentReportReferenceDocumentsHeading(self): #訂正報告書、参照書類 [目次項目]
		return self.AmendmentReportReferenceDocumentsHeading

	def getAmendmentReportReferenceDocumentsTextBlock(self): #訂正報告書、参照書類 [テキストブロック]
		return self.AmendmentReportReferenceDocumentsTextBlock

	def getSupplementaryInformationAboutReferenceDocumentsHeading(self): #参照書類の補完情報 [目次項目]
		return self.SupplementaryInformationAboutReferenceDocumentsHeading

	def getSupplementaryInformationAboutReferenceDocumentsTextBlock(self): #参照書類の補完情報 [テキストブロック]
		return self.SupplementaryInformationAboutReferenceDocumentsTextBlock

	def getPlaceForPublicInspectionOfReferenceDocumentsHeading(self): #参照書類を縦覧に供している場所 [目次項目]
		return self.PlaceForPublicInspectionOfReferenceDocumentsHeading

	def getPlaceForPublicInspectionOfReferenceDocumentsTextBlock(self): #参照書類を縦覧に供している場所 [テキストブロック]
		return self.PlaceForPublicInspectionOfReferenceDocumentsTextBlock
