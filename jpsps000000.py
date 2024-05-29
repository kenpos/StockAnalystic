from arelle import ModelManager
from arelle import Cntlr

class jpsps000000:#特定有価証券の内容等の開示に関する内閣府令 臨時報告書
	CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesExtraordinarySecuritiesReportHeading = '' #特定有価証券の内容等の開示に関する内閣府令 臨時報告書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	FundNameCoverPage = '' #ファンド名、表紙
	IssuerNameCoverPage = '' #発行者名、表紙
	TitleAndNameOfRepresentativeCoverPage = '' #代表者の役職氏名、表紙
	AddressOfRegisteredHeadquarterCoverPage = '' #本店の所在の場所、表紙
	NameOfContactPersonCoverPage = '' #事務連絡者氏名、表紙
	PlaceOfContactCoverPage = '' #連絡場所、表紙
	TelephoneNumberCoverPage = '' #電話番号、表紙
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	ReasonForFilingHeading = '' #提出理由 [目次項目]
	ReasonForFilingTextBlock = '' #提出理由 [テキストブロック]
	BodyOfReportHeading = '' #報告内容 [目次項目]
	PublicOfferingOrSecondaryDistributionOfSpecifiedSecuritiesOutsideJapanTextBlock = '' #本邦以外の地域における特定有価証券の募集又は売出 [テキストブロック]
	ChangesInMajorPartiesInvolvedTextBlock = '' #主要な関係法人の異動の決定又は異動 [テキストブロック]
	MajorChangesInInvestmentManagementPolicyEtcTextBlock = '' #ファンドの運用に関する基本方針又は運用体制等の重要な変更 [テキストブロック]
	EndOfTrustAccountingPeriodWithinSpecifiedPeriodTextBlock = '' #特定期間内における信託計算期間の到来 [テキストブロック]
	SignificantDisasterTextBlock = '' #重要な災害の発生 [テキストブロック]
	CommencementOrResolutionOfLitigationTextBlock = '' #訴訟の提起又は解決 [テキストブロック]
	DecisionOnAbsorptionTypeMergerOfInvestmentCorporationTextBlock = '' #投資法人の吸収合併の決定 [テキストブロック]
	DecisionOnConsolidationTypeMergerOfInvestmentCorporationTextBlock = '' #投資法人の新設合併の決定 [テキストブロック]
	MergerOfInvestmentTrustTextBlock = '' #投資信託の併合 [テキストブロック]
	PetitionEtcForCommencementOfBankruptcyProceedingsTextBlock = '' #破産手続開始の申立て等 [テキストブロック]
	LikelihoodOfUncollectibleOrDelinquentAccountsTextBlock = '' #取立不能又は取立遅延債権のおそれ [テキストブロック]
	EventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsTextBlock = '' #財政状態、経営成績及びキャッシュ・フローの状況に著しい影響を与える事象 [テキストブロック]
	CancelationOfRegistrationOrOrderForSuspensionOfBusinessEtcTextBlock = '' #登録の取消し又は業務の停止の処分等 [テキストブロック]
	DecisionOnDissolutionEtcTextBlock = '' #解散の決定等 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesExtraordinarySecuritiesReportHeading': #特定有価証券の内容等の開示に関する内閣府令 臨時報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesExtraordinarySecuritiesReportHeading = fact.value

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

			elif fact.concept.qname.localName == 'FundNameCoverPage': #ファンド名、表紙
				self.FundNameCoverPage = fact.value

			elif fact.concept.qname.localName == 'IssuerNameCoverPage': #発行者名、表紙
				self.IssuerNameCoverPage = fact.value

			elif fact.concept.qname.localName == 'TitleAndNameOfRepresentativeCoverPage': #代表者の役職氏名、表紙
				self.TitleAndNameOfRepresentativeCoverPage = fact.value

			elif fact.concept.qname.localName == 'AddressOfRegisteredHeadquarterCoverPage': #本店の所在の場所、表紙
				self.AddressOfRegisteredHeadquarterCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonCoverPage': #事務連絡者氏名、表紙
				self.NameOfContactPersonCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceOfContactCoverPage': #連絡場所、表紙
				self.PlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberCoverPage': #電話番号、表紙
				self.TelephoneNumberCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReasonForFilingHeading': #提出理由 [目次項目]
				self.ReasonForFilingHeading = fact.value

			elif fact.concept.qname.localName == 'ReasonForFilingTextBlock': #提出理由 [テキストブロック]
				self.ReasonForFilingTextBlock = fact.value

			elif fact.concept.qname.localName == 'BodyOfReportHeading': #報告内容 [目次項目]
				self.BodyOfReportHeading = fact.value

			elif fact.concept.qname.localName == 'PublicOfferingOrSecondaryDistributionOfSpecifiedSecuritiesOutsideJapanTextBlock': #本邦以外の地域における特定有価証券の募集又は売出 [テキストブロック]
				self.PublicOfferingOrSecondaryDistributionOfSpecifiedSecuritiesOutsideJapanTextBlock = fact.value

			elif fact.concept.qname.localName == 'ChangesInMajorPartiesInvolvedTextBlock': #主要な関係法人の異動の決定又は異動 [テキストブロック]
				self.ChangesInMajorPartiesInvolvedTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorChangesInInvestmentManagementPolicyEtcTextBlock': #ファンドの運用に関する基本方針又は運用体制等の重要な変更 [テキストブロック]
				self.MajorChangesInInvestmentManagementPolicyEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'EndOfTrustAccountingPeriodWithinSpecifiedPeriodTextBlock': #特定期間内における信託計算期間の到来 [テキストブロック]
				self.EndOfTrustAccountingPeriodWithinSpecifiedPeriodTextBlock = fact.value

			elif fact.concept.qname.localName == 'SignificantDisasterTextBlock': #重要な災害の発生 [テキストブロック]
				self.SignificantDisasterTextBlock = fact.value

			elif fact.concept.qname.localName == 'CommencementOrResolutionOfLitigationTextBlock': #訴訟の提起又は解決 [テキストブロック]
				self.CommencementOrResolutionOfLitigationTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnAbsorptionTypeMergerOfInvestmentCorporationTextBlock': #投資法人の吸収合併の決定 [テキストブロック]
				self.DecisionOnAbsorptionTypeMergerOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnConsolidationTypeMergerOfInvestmentCorporationTextBlock': #投資法人の新設合併の決定 [テキストブロック]
				self.DecisionOnConsolidationTypeMergerOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'MergerOfInvestmentTrustTextBlock': #投資信託の併合 [テキストブロック]
				self.MergerOfInvestmentTrustTextBlock = fact.value

			elif fact.concept.qname.localName == 'PetitionEtcForCommencementOfBankruptcyProceedingsTextBlock': #破産手続開始の申立て等 [テキストブロック]
				self.PetitionEtcForCommencementOfBankruptcyProceedingsTextBlock = fact.value

			elif fact.concept.qname.localName == 'LikelihoodOfUncollectibleOrDelinquentAccountsTextBlock': #取立不能又は取立遅延債権のおそれ [テキストブロック]
				self.LikelihoodOfUncollectibleOrDelinquentAccountsTextBlock = fact.value

			elif fact.concept.qname.localName == 'EventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsTextBlock': #財政状態、経営成績及びキャッシュ・フローの状況に著しい影響を与える事象 [テキストブロック]
				self.EventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsTextBlock = fact.value

			elif fact.concept.qname.localName == 'CancelationOfRegistrationOrOrderForSuspensionOfBusinessEtcTextBlock': #登録の取消し又は業務の停止の処分等 [テキストブロック]
				self.CancelationOfRegistrationOrOrderForSuspensionOfBusinessEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnDissolutionEtcTextBlock': #解散の決定等 [テキストブロック]
				self.DecisionOnDissolutionEtcTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesExtraordinarySecuritiesReportHeading(self): #特定有価証券の内容等の開示に関する内閣府令 臨時報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesExtraordinarySecuritiesReportHeading

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

	def getFundNameCoverPage(self): #ファンド名、表紙
		return self.FundNameCoverPage

	def getIssuerNameCoverPage(self): #発行者名、表紙
		return self.IssuerNameCoverPage

	def getTitleAndNameOfRepresentativeCoverPage(self): #代表者の役職氏名、表紙
		return self.TitleAndNameOfRepresentativeCoverPage

	def getAddressOfRegisteredHeadquarterCoverPage(self): #本店の所在の場所、表紙
		return self.AddressOfRegisteredHeadquarterCoverPage

	def getNameOfContactPersonCoverPage(self): #事務連絡者氏名、表紙
		return self.NameOfContactPersonCoverPage

	def getPlaceOfContactCoverPage(self): #連絡場所、表紙
		return self.PlaceOfContactCoverPage

	def getTelephoneNumberCoverPage(self): #電話番号、表紙
		return self.TelephoneNumberCoverPage

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getReasonForFilingHeading(self): #提出理由 [目次項目]
		return self.ReasonForFilingHeading

	def getReasonForFilingTextBlock(self): #提出理由 [テキストブロック]
		return self.ReasonForFilingTextBlock

	def getBodyOfReportHeading(self): #報告内容 [目次項目]
		return self.BodyOfReportHeading

	def getPublicOfferingOrSecondaryDistributionOfSpecifiedSecuritiesOutsideJapanTextBlock(self): #本邦以外の地域における特定有価証券の募集又は売出 [テキストブロック]
		return self.PublicOfferingOrSecondaryDistributionOfSpecifiedSecuritiesOutsideJapanTextBlock

	def getChangesInMajorPartiesInvolvedTextBlock(self): #主要な関係法人の異動の決定又は異動 [テキストブロック]
		return self.ChangesInMajorPartiesInvolvedTextBlock

	def getMajorChangesInInvestmentManagementPolicyEtcTextBlock(self): #ファンドの運用に関する基本方針又は運用体制等の重要な変更 [テキストブロック]
		return self.MajorChangesInInvestmentManagementPolicyEtcTextBlock

	def getEndOfTrustAccountingPeriodWithinSpecifiedPeriodTextBlock(self): #特定期間内における信託計算期間の到来 [テキストブロック]
		return self.EndOfTrustAccountingPeriodWithinSpecifiedPeriodTextBlock

	def getSignificantDisasterTextBlock(self): #重要な災害の発生 [テキストブロック]
		return self.SignificantDisasterTextBlock

	def getCommencementOrResolutionOfLitigationTextBlock(self): #訴訟の提起又は解決 [テキストブロック]
		return self.CommencementOrResolutionOfLitigationTextBlock

	def getDecisionOnAbsorptionTypeMergerOfInvestmentCorporationTextBlock(self): #投資法人の吸収合併の決定 [テキストブロック]
		return self.DecisionOnAbsorptionTypeMergerOfInvestmentCorporationTextBlock

	def getDecisionOnConsolidationTypeMergerOfInvestmentCorporationTextBlock(self): #投資法人の新設合併の決定 [テキストブロック]
		return self.DecisionOnConsolidationTypeMergerOfInvestmentCorporationTextBlock

	def getMergerOfInvestmentTrustTextBlock(self): #投資信託の併合 [テキストブロック]
		return self.MergerOfInvestmentTrustTextBlock

	def getPetitionEtcForCommencementOfBankruptcyProceedingsTextBlock(self): #破産手続開始の申立て等 [テキストブロック]
		return self.PetitionEtcForCommencementOfBankruptcyProceedingsTextBlock

	def getLikelihoodOfUncollectibleOrDelinquentAccountsTextBlock(self): #取立不能又は取立遅延債権のおそれ [テキストブロック]
		return self.LikelihoodOfUncollectibleOrDelinquentAccountsTextBlock

	def getEventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsTextBlock(self): #財政状態、経営成績及びキャッシュ・フローの状況に著しい影響を与える事象 [テキストブロック]
		return self.EventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsTextBlock

	def getCancelationOfRegistrationOrOrderForSuspensionOfBusinessEtcTextBlock(self): #登録の取消し又は業務の停止の処分等 [テキストブロック]
		return self.CancelationOfRegistrationOrOrderForSuspensionOfBusinessEtcTextBlock

	def getDecisionOnDissolutionEtcTextBlock(self): #解散の決定等 [テキストブロック]
		return self.DecisionOnDissolutionEtcTextBlock
