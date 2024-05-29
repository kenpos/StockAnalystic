from arelle import ModelManager
from arelle import Cntlr

class jptoi030000:#発行者による上場株券等の公開買付けの開示に関する内閣府令 第三号様式 公開買付撤回届出書
	CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForListedShareCertificatesEtcByIssuerFormNo3WrittenWithdrawalOfTenderOfferHeading = '' #発行者による上場株券等の公開買付けの開示に関する内閣府令 第三号様式 公開買付撤回届出書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	FullNameOrNameOfFilerOfNotificationCoverPage = '' #届出者の名称、表紙
	ResidentialAddressOrLocationOfFilerOfNotificationCoverPage = '' #届出者の住所又は所在地、表紙
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
	NameOfSubjectCompanyHeading = '' #対象者名 [目次項目]
	NameOfSubjectCompanyTextBlock = '' #対象者名 [テキストブロック]
	ClassesOfListedShareCertificatesEtcRelatedToPurchaseEtcHeading = '' #買付け等に係る上場株券等の種類 [目次項目]
	ClassesOfListedShareCertificatesEtcRelatedToPurchaseEtcTextBlock = '' #買付け等に係る上場株券等の種類 [テキストブロック]
	TenderOfferPeriodHeading = '' #公開買付期間 [目次項目]
	TenderOfferPeriodTextBlock = '' #公開買付期間 [テキストブロック]
	OfficialOrPublicAnnouncementOfWithdrawalEtcHeading = '' #撤回等の公告又は公表 [目次項目]
	DateOfOfficialOrPublicAnnouncementHeading = '' #公告又は公表日 [目次項目]
	DateOfOfficialOrPublicAnnouncementTextBlock = '' #公告又は公表日 [テキストブロック]
	NameOfNewspaperContainingOfficialAnnouncementOrMethodsOfPublicAnnouncementHeading = '' #公告掲載新聞名又は公表の方法 [目次項目]
	NameOfNewspaperContainingOfficialAnnouncementOrMethodsOfPublicAnnouncementTextBlock = '' #公告掲載新聞名又は公表の方法 [テキストブロック]
	ReasonForWithdrawalEtcHeading = '' #撤回等の理由 [目次項目]
	ReasonForWithdrawalEtcTextBlock = '' #撤回等の理由 [テキストブロック]
	HowToReturnListedShareCertificatesEtcWithdrawalHeading = '' #上場株券等の返還方法、撤回 [目次項目]
	HowAndWhereListedShareCertificatesEtcAreToBeHandedOverHeading = '' #上場株券等の返還方法及び返還場所 [目次項目]
	HowAndWhereListedShareCertificatesEtcAreToBeHandedOverTextBlock = '' #上場株券等の返還方法及び返還場所 [テキストブロック]
	DateOfCommencementOfReturnHeading = '' #返還の開始日 [目次項目]
	DateOfCommencementOfReturnTextBlock = '' #返還の開始日 [テキストブロック]
	NameAndAddressOfRegisteredHeadquarterOfFinancialInstrumentsBusinessOperatorBankEtcToHandleReturnOfListedShareCertificatesEtcHeading = '' #上場株券等の返還を行う金融商品取引業者・銀行等の名称及び所在地 [目次項目]
	NameAndAddressOfRegisteredHeadquarterOfFinancialInstrumentsBusinessOperatorBankEtcToHandleReturnOfListedShareCertificatesEtcTextBlock = '' #上場株券等の返還を行う金融商品取引業者・銀行等の名称及び所在地 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForListedShareCertificatesEtcByIssuerFormNo3WrittenWithdrawalOfTenderOfferHeading': #発行者による上場株券等の公開買付けの開示に関する内閣府令 第三号様式 公開買付撤回届出書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForListedShareCertificatesEtcByIssuerFormNo3WrittenWithdrawalOfTenderOfferHeading = fact.value

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

			elif fact.concept.qname.localName == 'FullNameOrNameOfFilerOfNotificationCoverPage': #届出者の名称、表紙
				self.FullNameOrNameOfFilerOfNotificationCoverPage = fact.value

			elif fact.concept.qname.localName == 'ResidentialAddressOrLocationOfFilerOfNotificationCoverPage': #届出者の住所又は所在地、表紙
				self.ResidentialAddressOrLocationOfFilerOfNotificationCoverPage = fact.value

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

			elif fact.concept.qname.localName == 'NameOfSubjectCompanyHeading': #対象者名 [目次項目]
				self.NameOfSubjectCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfSubjectCompanyTextBlock': #対象者名 [テキストブロック]
				self.NameOfSubjectCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'ClassesOfListedShareCertificatesEtcRelatedToPurchaseEtcHeading': #買付け等に係る上場株券等の種類 [目次項目]
				self.ClassesOfListedShareCertificatesEtcRelatedToPurchaseEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ClassesOfListedShareCertificatesEtcRelatedToPurchaseEtcTextBlock': #買付け等に係る上場株券等の種類 [テキストブロック]
				self.ClassesOfListedShareCertificatesEtcRelatedToPurchaseEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'TenderOfferPeriodHeading': #公開買付期間 [目次項目]
				self.TenderOfferPeriodHeading = fact.value

			elif fact.concept.qname.localName == 'TenderOfferPeriodTextBlock': #公開買付期間 [テキストブロック]
				self.TenderOfferPeriodTextBlock = fact.value

			elif fact.concept.qname.localName == 'OfficialOrPublicAnnouncementOfWithdrawalEtcHeading': #撤回等の公告又は公表 [目次項目]
				self.OfficialOrPublicAnnouncementOfWithdrawalEtcHeading = fact.value

			elif fact.concept.qname.localName == 'DateOfOfficialOrPublicAnnouncementHeading': #公告又は公表日 [目次項目]
				self.DateOfOfficialOrPublicAnnouncementHeading = fact.value

			elif fact.concept.qname.localName == 'DateOfOfficialOrPublicAnnouncementTextBlock': #公告又は公表日 [テキストブロック]
				self.DateOfOfficialOrPublicAnnouncementTextBlock = fact.value

			elif fact.concept.qname.localName == 'NameOfNewspaperContainingOfficialAnnouncementOrMethodsOfPublicAnnouncementHeading': #公告掲載新聞名又は公表の方法 [目次項目]
				self.NameOfNewspaperContainingOfficialAnnouncementOrMethodsOfPublicAnnouncementHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfNewspaperContainingOfficialAnnouncementOrMethodsOfPublicAnnouncementTextBlock': #公告掲載新聞名又は公表の方法 [テキストブロック]
				self.NameOfNewspaperContainingOfficialAnnouncementOrMethodsOfPublicAnnouncementTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReasonForWithdrawalEtcHeading': #撤回等の理由 [目次項目]
				self.ReasonForWithdrawalEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ReasonForWithdrawalEtcTextBlock': #撤回等の理由 [テキストブロック]
				self.ReasonForWithdrawalEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'HowToReturnListedShareCertificatesEtcWithdrawalHeading': #上場株券等の返還方法、撤回 [目次項目]
				self.HowToReturnListedShareCertificatesEtcWithdrawalHeading = fact.value

			elif fact.concept.qname.localName == 'HowAndWhereListedShareCertificatesEtcAreToBeHandedOverHeading': #上場株券等の返還方法及び返還場所 [目次項目]
				self.HowAndWhereListedShareCertificatesEtcAreToBeHandedOverHeading = fact.value

			elif fact.concept.qname.localName == 'HowAndWhereListedShareCertificatesEtcAreToBeHandedOverTextBlock': #上場株券等の返還方法及び返還場所 [テキストブロック]
				self.HowAndWhereListedShareCertificatesEtcAreToBeHandedOverTextBlock = fact.value

			elif fact.concept.qname.localName == 'DateOfCommencementOfReturnHeading': #返還の開始日 [目次項目]
				self.DateOfCommencementOfReturnHeading = fact.value

			elif fact.concept.qname.localName == 'DateOfCommencementOfReturnTextBlock': #返還の開始日 [テキストブロック]
				self.DateOfCommencementOfReturnTextBlock = fact.value

			elif fact.concept.qname.localName == 'NameAndAddressOfRegisteredHeadquarterOfFinancialInstrumentsBusinessOperatorBankEtcToHandleReturnOfListedShareCertificatesEtcHeading': #上場株券等の返還を行う金融商品取引業者・銀行等の名称及び所在地 [目次項目]
				self.NameAndAddressOfRegisteredHeadquarterOfFinancialInstrumentsBusinessOperatorBankEtcToHandleReturnOfListedShareCertificatesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'NameAndAddressOfRegisteredHeadquarterOfFinancialInstrumentsBusinessOperatorBankEtcToHandleReturnOfListedShareCertificatesEtcTextBlock': #上場株券等の返還を行う金融商品取引業者・銀行等の名称及び所在地 [テキストブロック]
				self.NameAndAddressOfRegisteredHeadquarterOfFinancialInstrumentsBusinessOperatorBankEtcToHandleReturnOfListedShareCertificatesEtcTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfTenderOfferForListedShareCertificatesEtcByIssuerFormNo3WrittenWithdrawalOfTenderOfferHeading(self): #発行者による上場株券等の公開買付けの開示に関する内閣府令 第三号様式 公開買付撤回届出書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForListedShareCertificatesEtcByIssuerFormNo3WrittenWithdrawalOfTenderOfferHeading

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

	def getFullNameOrNameOfFilerOfNotificationCoverPage(self): #届出者の名称、表紙
		return self.FullNameOrNameOfFilerOfNotificationCoverPage

	def getResidentialAddressOrLocationOfFilerOfNotificationCoverPage(self): #届出者の住所又は所在地、表紙
		return self.ResidentialAddressOrLocationOfFilerOfNotificationCoverPage

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

	def getNameOfSubjectCompanyHeading(self): #対象者名 [目次項目]
		return self.NameOfSubjectCompanyHeading

	def getNameOfSubjectCompanyTextBlock(self): #対象者名 [テキストブロック]
		return self.NameOfSubjectCompanyTextBlock

	def getClassesOfListedShareCertificatesEtcRelatedToPurchaseEtcHeading(self): #買付け等に係る上場株券等の種類 [目次項目]
		return self.ClassesOfListedShareCertificatesEtcRelatedToPurchaseEtcHeading

	def getClassesOfListedShareCertificatesEtcRelatedToPurchaseEtcTextBlock(self): #買付け等に係る上場株券等の種類 [テキストブロック]
		return self.ClassesOfListedShareCertificatesEtcRelatedToPurchaseEtcTextBlock

	def getTenderOfferPeriodHeading(self): #公開買付期間 [目次項目]
		return self.TenderOfferPeriodHeading

	def getTenderOfferPeriodTextBlock(self): #公開買付期間 [テキストブロック]
		return self.TenderOfferPeriodTextBlock

	def getOfficialOrPublicAnnouncementOfWithdrawalEtcHeading(self): #撤回等の公告又は公表 [目次項目]
		return self.OfficialOrPublicAnnouncementOfWithdrawalEtcHeading

	def getDateOfOfficialOrPublicAnnouncementHeading(self): #公告又は公表日 [目次項目]
		return self.DateOfOfficialOrPublicAnnouncementHeading

	def getDateOfOfficialOrPublicAnnouncementTextBlock(self): #公告又は公表日 [テキストブロック]
		return self.DateOfOfficialOrPublicAnnouncementTextBlock

	def getNameOfNewspaperContainingOfficialAnnouncementOrMethodsOfPublicAnnouncementHeading(self): #公告掲載新聞名又は公表の方法 [目次項目]
		return self.NameOfNewspaperContainingOfficialAnnouncementOrMethodsOfPublicAnnouncementHeading

	def getNameOfNewspaperContainingOfficialAnnouncementOrMethodsOfPublicAnnouncementTextBlock(self): #公告掲載新聞名又は公表の方法 [テキストブロック]
		return self.NameOfNewspaperContainingOfficialAnnouncementOrMethodsOfPublicAnnouncementTextBlock

	def getReasonForWithdrawalEtcHeading(self): #撤回等の理由 [目次項目]
		return self.ReasonForWithdrawalEtcHeading

	def getReasonForWithdrawalEtcTextBlock(self): #撤回等の理由 [テキストブロック]
		return self.ReasonForWithdrawalEtcTextBlock

	def getHowToReturnListedShareCertificatesEtcWithdrawalHeading(self): #上場株券等の返還方法、撤回 [目次項目]
		return self.HowToReturnListedShareCertificatesEtcWithdrawalHeading

	def getHowAndWhereListedShareCertificatesEtcAreToBeHandedOverHeading(self): #上場株券等の返還方法及び返還場所 [目次項目]
		return self.HowAndWhereListedShareCertificatesEtcAreToBeHandedOverHeading

	def getHowAndWhereListedShareCertificatesEtcAreToBeHandedOverTextBlock(self): #上場株券等の返還方法及び返還場所 [テキストブロック]
		return self.HowAndWhereListedShareCertificatesEtcAreToBeHandedOverTextBlock

	def getDateOfCommencementOfReturnHeading(self): #返還の開始日 [目次項目]
		return self.DateOfCommencementOfReturnHeading

	def getDateOfCommencementOfReturnTextBlock(self): #返還の開始日 [テキストブロック]
		return self.DateOfCommencementOfReturnTextBlock

	def getNameAndAddressOfRegisteredHeadquarterOfFinancialInstrumentsBusinessOperatorBankEtcToHandleReturnOfListedShareCertificatesEtcHeading(self): #上場株券等の返還を行う金融商品取引業者・銀行等の名称及び所在地 [目次項目]
		return self.NameAndAddressOfRegisteredHeadquarterOfFinancialInstrumentsBusinessOperatorBankEtcToHandleReturnOfListedShareCertificatesEtcHeading

	def getNameAndAddressOfRegisteredHeadquarterOfFinancialInstrumentsBusinessOperatorBankEtcToHandleReturnOfListedShareCertificatesEtcTextBlock(self): #上場株券等の返還を行う金融商品取引業者・銀行等の名称及び所在地 [テキストブロック]
		return self.NameAndAddressOfRegisteredHeadquarterOfFinancialInstrumentsBusinessOperatorBankEtcToHandleReturnOfListedShareCertificatesEtcTextBlock
