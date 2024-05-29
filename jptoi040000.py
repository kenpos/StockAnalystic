from arelle import ModelManager
from arelle import Cntlr

class jptoi040000:#発行者による上場株券等の公開買付けの開示に関する内閣府令 第四号様式 公開買付報告書
	CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForListedShareCertificatesEtcByIssuerFormNo4TenderOfferReportHeading = '' #発行者による上場株券等の公開買付けの開示に関する内閣府令 第四号様式 公開買付報告書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	NameOfFilerCoverPage = '' #報告者の名称、表紙
	LocationOfFilerCoverPage = '' #報告者の所在地、表紙
	NearestPlaceOfContactCoverPage = '' #最寄りの連絡場所、表紙
	TelephoneNumberCoverPage = '' #電話番号、表紙
	NameOfContactPersonCoverPage = '' #事務連絡者氏名、表紙
	NameOfLegalRepresentativeCoverPage = '' #代理人の氏名又は名称、表紙
	NameOfLegalRepresentativeCoverPageNA = '' #代理人の氏名又は名称、表紙（該当なし）
	ResidentialAddressOrLocationOfLegalRepresentativeCoverPage = '' #代理人の住所又は所在地、表紙
	ResidentialAddressOrLocationOfLegalRepresentativeCoverPageNA = '' #代理人の住所又は所在地、表紙（該当なし）
	NearestPlaceOfContactLegalRepresentativeCoverPage = '' #最寄りの連絡場所、代理人、表紙
	NearestPlaceOfContactLegalRepresentativeCoverPageNA = '' #最寄りの連絡場所、代理人、表紙（該当なし）
	TelephoneNumberLegalRepresentativeCoverPage = '' #電話番号、代理人、表紙
	TelephoneNumberLegalRepresentativeCoverPageNA = '' #電話番号、代理人、表紙（該当なし）
	NameOfContactPersonLegalRepresentativeCoverPage = '' #事務連絡者氏名、代理人、表紙
	NameOfContactPersonLegalRepresentativeCoverPageNA = '' #事務連絡者氏名、代理人、表紙（該当なし）
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	PlaceForPublicInspectionCoverPageNA = '' #縦覧に供する場所、表紙（該当なし）
	NotesCoverPageTextBlock = '' #脚注、表紙 [テキストブロック]
	InformationOfTenderOfferHeading = '' #公開買付けの内容 [目次項目]
	ClassesOfShareCertificatesRelatedToListedShareCertificatesEtcRelatedToPurchaseEtcHeading = '' #買付け等に係る上場株券等の種類、公開買付報告書 [目次項目]
	ClassesOfShareCertificatesRelatedToListedShareCertificatesEtcRelatedToPurchaseEtcTextBlock = '' #買付け等に係る上場株券等の種類、公開買付報告書 [テキストブロック]
	TenderOfferPeriodHeading = '' #公開買付期間 [目次項目]
	TenderOfferPeriodTextBlock = '' #公開買付期間 [テキストブロック]
	ResultOfPurchaseEtcHeading = '' #買付け等の結果 [目次項目]
	DateOfOfficialAnnouncementOfTenderOfferAndNameOfNewspaperContainingItHeading = '' #公開買付けの結果の公告日及び公告掲載新聞名 [目次項目]
	DateOfOfficialAnnouncementOfTenderOfferAndNameOfNewspaperContainingItTextBlock = '' #公開買付けの結果の公告日及び公告掲載新聞名 [テキストブロック]
	NumberOfListedShareCertificatesEtcAcquiredByPurchaseEtcHeading = '' #買付け等を行った上場株券等の数 [目次項目]
	NumberOfListedShareCertificatesEtcAcquiredByPurchaseEtcTextBlock = '' #買付け等を行った上場株券等の数 [テキストブロック]
	CalculationForPurchaseEtcByMethodOfProportionalDistributionHeading = '' #あん分比例方式により買付け等を行う場合の計算 [目次項目]
	CalculationForPurchaseEtcByMethodOfProportionalDistributionTextBlock = '' #あん分比例方式により買付け等を行う場合の計算 [テキストブロック]
	CalculationForPurchaseEtcByMethodOfProportionalDistributionNA = '' #あん分比例方式により買付け等を行う場合の計算（該当なし）

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForListedShareCertificatesEtcByIssuerFormNo4TenderOfferReportHeading': #発行者による上場株券等の公開買付けの開示に関する内閣府令 第四号様式 公開買付報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForListedShareCertificatesEtcByIssuerFormNo4TenderOfferReportHeading = fact.value

			elif fact.concept.qname.localName == 'CoverPageHeading': #表紙 [目次項目]
				self.CoverPageHeading = fact.value

			elif fact.concept.qname.localName == 'CoverPageHeading': #表紙 [目次項目]
				self.CoverPageHeading = fact.value

			elif fact.concept.qname.localName == 'DocumentTitleCoverPage': #提出書類、表紙
				self.DocumentTitleCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceOfFilingCoverPage': #提出先、表紙
				self.PlaceOfFilingCoverPage = fact.value

			elif fact.concept.qname.localName == 'FilingDateCoverPage': #提出日、表紙
				self.FilingDateCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfFilerCoverPage': #報告者の名称、表紙
				self.NameOfFilerCoverPage = fact.value

			elif fact.concept.qname.localName == 'LocationOfFilerCoverPage': #報告者の所在地、表紙
				self.LocationOfFilerCoverPage = fact.value

			elif fact.concept.qname.localName == 'NearestPlaceOfContactCoverPage': #最寄りの連絡場所、表紙
				self.NearestPlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberCoverPage': #電話番号、表紙
				self.TelephoneNumberCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonCoverPage': #事務連絡者氏名、表紙
				self.NameOfContactPersonCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfLegalRepresentativeCoverPage': #代理人の氏名又は名称、表紙
				self.NameOfLegalRepresentativeCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfLegalRepresentativeCoverPageNA': #代理人の氏名又は名称、表紙（該当なし）
				self.NameOfLegalRepresentativeCoverPageNA = fact.value

			elif fact.concept.qname.localName == 'ResidentialAddressOrLocationOfLegalRepresentativeCoverPage': #代理人の住所又は所在地、表紙
				self.ResidentialAddressOrLocationOfLegalRepresentativeCoverPage = fact.value

			elif fact.concept.qname.localName == 'ResidentialAddressOrLocationOfLegalRepresentativeCoverPageNA': #代理人の住所又は所在地、表紙（該当なし）
				self.ResidentialAddressOrLocationOfLegalRepresentativeCoverPageNA = fact.value

			elif fact.concept.qname.localName == 'NearestPlaceOfContactLegalRepresentativeCoverPage': #最寄りの連絡場所、代理人、表紙
				self.NearestPlaceOfContactLegalRepresentativeCoverPage = fact.value

			elif fact.concept.qname.localName == 'NearestPlaceOfContactLegalRepresentativeCoverPageNA': #最寄りの連絡場所、代理人、表紙（該当なし）
				self.NearestPlaceOfContactLegalRepresentativeCoverPageNA = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberLegalRepresentativeCoverPage': #電話番号、代理人、表紙
				self.TelephoneNumberLegalRepresentativeCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberLegalRepresentativeCoverPageNA': #電話番号、代理人、表紙（該当なし）
				self.TelephoneNumberLegalRepresentativeCoverPageNA = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonLegalRepresentativeCoverPage': #事務連絡者氏名、代理人、表紙
				self.NameOfContactPersonLegalRepresentativeCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonLegalRepresentativeCoverPageNA': #事務連絡者氏名、代理人、表紙（該当なし）
				self.NameOfContactPersonLegalRepresentativeCoverPageNA = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageNA': #縦覧に供する場所、表紙（該当なし）
				self.PlaceForPublicInspectionCoverPageNA = fact.value

			elif fact.concept.qname.localName == 'NotesCoverPageTextBlock': #脚注、表紙 [テキストブロック]
				self.NotesCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationOfTenderOfferHeading': #公開買付けの内容 [目次項目]
				self.InformationOfTenderOfferHeading = fact.value

			elif fact.concept.qname.localName == 'ClassesOfShareCertificatesRelatedToListedShareCertificatesEtcRelatedToPurchaseEtcHeading': #買付け等に係る上場株券等の種類、公開買付報告書 [目次項目]
				self.ClassesOfShareCertificatesRelatedToListedShareCertificatesEtcRelatedToPurchaseEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ClassesOfShareCertificatesRelatedToListedShareCertificatesEtcRelatedToPurchaseEtcTextBlock': #買付け等に係る上場株券等の種類、公開買付報告書 [テキストブロック]
				self.ClassesOfShareCertificatesRelatedToListedShareCertificatesEtcRelatedToPurchaseEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'TenderOfferPeriodHeading': #公開買付期間 [目次項目]
				self.TenderOfferPeriodHeading = fact.value

			elif fact.concept.qname.localName == 'TenderOfferPeriodTextBlock': #公開買付期間 [テキストブロック]
				self.TenderOfferPeriodTextBlock = fact.value

			elif fact.concept.qname.localName == 'ResultOfPurchaseEtcHeading': #買付け等の結果 [目次項目]
				self.ResultOfPurchaseEtcHeading = fact.value

			elif fact.concept.qname.localName == 'DateOfOfficialAnnouncementOfTenderOfferAndNameOfNewspaperContainingItHeading': #公開買付けの結果の公告日及び公告掲載新聞名 [目次項目]
				self.DateOfOfficialAnnouncementOfTenderOfferAndNameOfNewspaperContainingItHeading = fact.value

			elif fact.concept.qname.localName == 'DateOfOfficialAnnouncementOfTenderOfferAndNameOfNewspaperContainingItTextBlock': #公開買付けの結果の公告日及び公告掲載新聞名 [テキストブロック]
				self.DateOfOfficialAnnouncementOfTenderOfferAndNameOfNewspaperContainingItTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfListedShareCertificatesEtcAcquiredByPurchaseEtcHeading': #買付け等を行った上場株券等の数 [目次項目]
				self.NumberOfListedShareCertificatesEtcAcquiredByPurchaseEtcHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfListedShareCertificatesEtcAcquiredByPurchaseEtcTextBlock': #買付け等を行った上場株券等の数 [テキストブロック]
				self.NumberOfListedShareCertificatesEtcAcquiredByPurchaseEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'CalculationForPurchaseEtcByMethodOfProportionalDistributionHeading': #あん分比例方式により買付け等を行う場合の計算 [目次項目]
				self.CalculationForPurchaseEtcByMethodOfProportionalDistributionHeading = fact.value

			elif fact.concept.qname.localName == 'CalculationForPurchaseEtcByMethodOfProportionalDistributionTextBlock': #あん分比例方式により買付け等を行う場合の計算 [テキストブロック]
				self.CalculationForPurchaseEtcByMethodOfProportionalDistributionTextBlock = fact.value

			elif fact.concept.qname.localName == 'CalculationForPurchaseEtcByMethodOfProportionalDistributionNA': #あん分比例方式により買付け等を行う場合の計算（該当なし）
				self.CalculationForPurchaseEtcByMethodOfProportionalDistributionNA = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfTenderOfferForListedShareCertificatesEtcByIssuerFormNo4TenderOfferReportHeading(self): #発行者による上場株券等の公開買付けの開示に関する内閣府令 第四号様式 公開買付報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForListedShareCertificatesEtcByIssuerFormNo4TenderOfferReportHeading

	def getCoverPageHeading(self): #表紙 [目次項目]
		return self.CoverPageHeading

	def getCoverPageHeading(self): #表紙 [目次項目]
		return self.CoverPageHeading

	def getDocumentTitleCoverPage(self): #提出書類、表紙
		return self.DocumentTitleCoverPage

	def getPlaceOfFilingCoverPage(self): #提出先、表紙
		return self.PlaceOfFilingCoverPage

	def getFilingDateCoverPage(self): #提出日、表紙
		return self.FilingDateCoverPage

	def getNameOfFilerCoverPage(self): #報告者の名称、表紙
		return self.NameOfFilerCoverPage

	def getLocationOfFilerCoverPage(self): #報告者の所在地、表紙
		return self.LocationOfFilerCoverPage

	def getNearestPlaceOfContactCoverPage(self): #最寄りの連絡場所、表紙
		return self.NearestPlaceOfContactCoverPage

	def getTelephoneNumberCoverPage(self): #電話番号、表紙
		return self.TelephoneNumberCoverPage

	def getNameOfContactPersonCoverPage(self): #事務連絡者氏名、表紙
		return self.NameOfContactPersonCoverPage

	def getNameOfLegalRepresentativeCoverPage(self): #代理人の氏名又は名称、表紙
		return self.NameOfLegalRepresentativeCoverPage

	def getNameOfLegalRepresentativeCoverPageNA(self): #代理人の氏名又は名称、表紙（該当なし）
		return self.NameOfLegalRepresentativeCoverPageNA

	def getResidentialAddressOrLocationOfLegalRepresentativeCoverPage(self): #代理人の住所又は所在地、表紙
		return self.ResidentialAddressOrLocationOfLegalRepresentativeCoverPage

	def getResidentialAddressOrLocationOfLegalRepresentativeCoverPageNA(self): #代理人の住所又は所在地、表紙（該当なし）
		return self.ResidentialAddressOrLocationOfLegalRepresentativeCoverPageNA

	def getNearestPlaceOfContactLegalRepresentativeCoverPage(self): #最寄りの連絡場所、代理人、表紙
		return self.NearestPlaceOfContactLegalRepresentativeCoverPage

	def getNearestPlaceOfContactLegalRepresentativeCoverPageNA(self): #最寄りの連絡場所、代理人、表紙（該当なし）
		return self.NearestPlaceOfContactLegalRepresentativeCoverPageNA

	def getTelephoneNumberLegalRepresentativeCoverPage(self): #電話番号、代理人、表紙
		return self.TelephoneNumberLegalRepresentativeCoverPage

	def getTelephoneNumberLegalRepresentativeCoverPageNA(self): #電話番号、代理人、表紙（該当なし）
		return self.TelephoneNumberLegalRepresentativeCoverPageNA

	def getNameOfContactPersonLegalRepresentativeCoverPage(self): #事務連絡者氏名、代理人、表紙
		return self.NameOfContactPersonLegalRepresentativeCoverPage

	def getNameOfContactPersonLegalRepresentativeCoverPageNA(self): #事務連絡者氏名、代理人、表紙（該当なし）
		return self.NameOfContactPersonLegalRepresentativeCoverPageNA

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getPlaceForPublicInspectionCoverPageNA(self): #縦覧に供する場所、表紙（該当なし）
		return self.PlaceForPublicInspectionCoverPageNA

	def getNotesCoverPageTextBlock(self): #脚注、表紙 [テキストブロック]
		return self.NotesCoverPageTextBlock

	def getInformationOfTenderOfferHeading(self): #公開買付けの内容 [目次項目]
		return self.InformationOfTenderOfferHeading

	def getClassesOfShareCertificatesRelatedToListedShareCertificatesEtcRelatedToPurchaseEtcHeading(self): #買付け等に係る上場株券等の種類、公開買付報告書 [目次項目]
		return self.ClassesOfShareCertificatesRelatedToListedShareCertificatesEtcRelatedToPurchaseEtcHeading

	def getClassesOfShareCertificatesRelatedToListedShareCertificatesEtcRelatedToPurchaseEtcTextBlock(self): #買付け等に係る上場株券等の種類、公開買付報告書 [テキストブロック]
		return self.ClassesOfShareCertificatesRelatedToListedShareCertificatesEtcRelatedToPurchaseEtcTextBlock

	def getTenderOfferPeriodHeading(self): #公開買付期間 [目次項目]
		return self.TenderOfferPeriodHeading

	def getTenderOfferPeriodTextBlock(self): #公開買付期間 [テキストブロック]
		return self.TenderOfferPeriodTextBlock

	def getResultOfPurchaseEtcHeading(self): #買付け等の結果 [目次項目]
		return self.ResultOfPurchaseEtcHeading

	def getDateOfOfficialAnnouncementOfTenderOfferAndNameOfNewspaperContainingItHeading(self): #公開買付けの結果の公告日及び公告掲載新聞名 [目次項目]
		return self.DateOfOfficialAnnouncementOfTenderOfferAndNameOfNewspaperContainingItHeading

	def getDateOfOfficialAnnouncementOfTenderOfferAndNameOfNewspaperContainingItTextBlock(self): #公開買付けの結果の公告日及び公告掲載新聞名 [テキストブロック]
		return self.DateOfOfficialAnnouncementOfTenderOfferAndNameOfNewspaperContainingItTextBlock

	def getNumberOfListedShareCertificatesEtcAcquiredByPurchaseEtcHeading(self): #買付け等を行った上場株券等の数 [目次項目]
		return self.NumberOfListedShareCertificatesEtcAcquiredByPurchaseEtcHeading

	def getNumberOfListedShareCertificatesEtcAcquiredByPurchaseEtcTextBlock(self): #買付け等を行った上場株券等の数 [テキストブロック]
		return self.NumberOfListedShareCertificatesEtcAcquiredByPurchaseEtcTextBlock

	def getCalculationForPurchaseEtcByMethodOfProportionalDistributionHeading(self): #あん分比例方式により買付け等を行う場合の計算 [目次項目]
		return self.CalculationForPurchaseEtcByMethodOfProportionalDistributionHeading

	def getCalculationForPurchaseEtcByMethodOfProportionalDistributionTextBlock(self): #あん分比例方式により買付け等を行う場合の計算 [テキストブロック]
		return self.CalculationForPurchaseEtcByMethodOfProportionalDistributionTextBlock

	def getCalculationForPurchaseEtcByMethodOfProportionalDistributionNA(self): #あん分比例方式により買付け等を行う場合の計算（該当なし）
		return self.CalculationForPurchaseEtcByMethodOfProportionalDistributionNA
