from arelle import ModelManager
from arelle import Cntlr

class jpsps040303:#特定有価証券の内容等の開示に関する内閣府令 第四号の三の三様式 有価証券届出書
	CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo433SecuritiesRegistrationStatementHeading = '' #特定有価証券の内容等の開示に関する内閣府令 第四号の三の三様式 有価証券届出書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	IssuerNameCoverPage = '' #発行者名、表紙
	TitleAndNameOfRepresentativeCoverPage = '' #代表者の役職氏名、表紙
	AddressOfRegisteredHeadquarterCoverPage = '' #本店の所在の場所、表紙
	NameOfContactPersonCoverPage = '' #事務連絡者氏名、表紙
	TelephoneNumberCoverPage = '' #電話番号、表紙
	NameOfInvestmentCorporationRelatedToDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPage = '' #届出の対象とした募集（売出）内国投資証券に係る投資法人の名称、表紙
	LegalFormAndAmountOfDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPageTextBlock = '' #届出の対象とした募集（売出）内国投資証券の形態及び金額、表紙 [テキストブロック]
	MattersSpecificToStabilizingOperationCoverPageTextBlock = '' #安定操作に関する事項、表紙 [テキストブロック]
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	SecurityInformationHeading = '' #証券情報 [目次項目]
	DomesticInvestmentSecuritiesOtherThanInvestmentCorporationBondsHeading = '' #内国投資証券（新投資口予約権証券及び投資法人債券を除く。） [目次項目]
	DomesticInvestmentSecuritiesOtherThanInvestmentUnitAcquisitionRightsAndInvestmentCorporationBondsTextBlock = '' #内国投資証券（新投資口予約権証券及び投資法人債券を除く。） [テキストブロック]
	PublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #募集内国投資証券 [目次項目]
	NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #投資法人の名称、募集内国投資証券 [目次項目]
	NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #投資法人の名称、募集内国投資証券 [テキストブロック]
	LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #内国投資証券の形態等、募集内国投資証券 [目次項目]
	LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #内国投資証券の形態等、募集内国投資証券 [テキストブロック]
	NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #発行数、募集内国投資証券 [目次項目]
	NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #発行数、募集内国投資証券 [テキストブロック]
	TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #発行価額の総額、募集内国投資証券 [目次項目]
	TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #発行価額の総額、募集内国投資証券 [テキストブロック]
	PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #発行価格、募集内国投資証券 [目次項目]
	PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #発行価格、募集内国投資証券 [テキストブロック]
	ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #申込手数料、募集内国投資証券 [目次項目]
	ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #申込手数料、募集内国投資証券 [テキストブロック]
	ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #申込単位、募集内国投資証券 [目次項目]
	ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #申込単位、募集内国投資証券 [テキストブロック]
	ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #申込期間、募集内国投資証券 [目次項目]
	ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #申込期間、募集内国投資証券 [テキストブロック]
	ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #申込証拠金、募集内国投資証券 [目次項目]
	ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #申込証拠金、募集内国投資証券 [テキストブロック]
	PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #申込取扱場所、募集内国投資証券 [目次項目]
	PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #申込取扱場所、募集内国投資証券 [テキストブロック]
	DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #払込期日、募集内国投資証券 [目次項目]
	DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #払込期日、募集内国投資証券 [テキストブロック]
	PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #払込取扱場所、募集内国投資証券 [目次項目]
	PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #払込取扱場所、募集内国投資証券 [テキストブロック]
	OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #引受け等の概要、募集内国投資証券 [目次項目]
	OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #引受け等の概要、募集内国投資証券 [テキストブロック]
	BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #振替機関に関する事項、募集内国投資証券 [目次項目]
	BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #振替機関に関する事項、募集内国投資証券 [テキストブロック]
	UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #手取金の使途、募集内国投資証券 [目次項目]
	UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #手取金の使途、募集内国投資証券 [テキストブロック]
	OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #その他、募集内国投資証券 [目次項目]
	OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #その他、募集内国投資証券 [テキストブロック]
	SecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #売出内国投資証券 [目次項目]
	NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #投資法人の名称、売出内国投資証券 [目次項目]
	NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #投資法人の名称、売出内国投資証券 [テキストブロック]
	LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #内国投資証券の形態等、売出内国投資証券 [目次項目]
	LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #内国投資証券の形態等、売出内国投資証券 [テキストブロック]
	NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #売出数、売出内国投資証券 [目次項目]
	NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #売出数、売出内国投資証券 [テキストブロック]
	TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #売出価額の総額、売出内国投資証券 [目次項目]
	TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #売出価額の総額、売出内国投資証券 [テキストブロック]
	PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #売出価格、売出内国投資証券 [目次項目]
	PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #売出価格、売出内国投資証券 [テキストブロック]
	ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #申込手数料、売出内国投資証券 [目次項目]
	ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #申込手数料、売出内国投資証券 [テキストブロック]
	ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #申込単位、売出内国投資証券 [目次項目]
	ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #申込単位、売出内国投資証券 [テキストブロック]
	ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #申込期間、売出内国投資証券 [目次項目]
	ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #申込期間、売出内国投資証券 [テキストブロック]
	ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #申込証拠金、売出内国投資証券 [目次項目]
	ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #申込証拠金、売出内国投資証券 [テキストブロック]
	PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #申込取扱場所、売出内国投資証券 [目次項目]
	PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #申込取扱場所、売出内国投資証券 [テキストブロック]
	SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #受渡期日、売出内国投資証券 [目次項目]
	SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #受渡期日、売出内国投資証券 [テキストブロック]
	PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #払込取扱場所、売出内国投資証券 [目次項目]
	PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #払込取扱場所、売出内国投資証券 [テキストブロック]
	OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #引受け等の概要、売出内国投資証券 [目次項目]
	OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #引受け等の概要、売出内国投資証券 [テキストブロック]
	BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #振替機関に関する事項、売出内国投資証券 [目次項目]
	BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #振替機関に関する事項、売出内国投資証券 [テキストブロック]
	UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #手取金の使途、売出内国投資証券 [目次項目]
	UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #手取金の使途、売出内国投資証券 [テキストブロック]
	OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #その他、売出内国投資証券 [目次項目]
	OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #その他、売出内国投資証券 [テキストブロック]
	SubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権証券 [目次項目]
	InvestmentUnitAcquisitionRightsTextBlock = '' #新投資口予約権証券 [テキストブロック]
	NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #投資法人の名称、新投資口予約権証券 [目次項目]
	NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #投資法人の名称、新投資口予約権証券 [テキストブロック]
	LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権証券の形態等 [目次項目]
	LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権証券の形態等 [テキストブロック]
	NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #発行数、新投資口予約権証券 [目次項目]
	NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #発行数、新投資口予約権証券 [テキストブロック]
	DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #割当日、新投資口予約権証券 [目次項目]
	DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #割当日、新投資口予約権証券 [テキストブロック]
	ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の内容 [目次項目]
	ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の内容 [テキストブロック]
	LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の目的となる内国投資証券の形態等 [目次項目]
	LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の目的となる内国投資証券の形態等 [テキストブロック]
	NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の目的となる内国投資証券の数 [目次項目]
	NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の目的となる内国投資証券の数 [テキストブロック]
	AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedHeading = '' #新投資口予約権の行使時の払込金額 [目次項目]
	AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedTextBlock = '' #新投資口予約権の行使時の払込金額 [テキストブロック]
	TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedHeading = '' #新投資口予約権の行使により発行する内国投資証券の発行価額の総額 [目次項目]
	TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedTextBlock = '' #新投資口予約権の行使により発行する内国投資証券の発行価額の総額 [テキストブロック]
	ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の行使期間 [目次項目]
	ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の行使期間 [テキストブロック]
	CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の行使請求の受付場所、取次場所及び払込取扱場所 [目次項目]
	CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の行使請求の受付場所、取次場所及び払込取扱場所 [テキストブロック]
	TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の行使の条件 [目次項目]
	TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の行使の条件 [テキストブロック]
	ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #自己新投資口予約権の取得の事由及び取得の条件 [目次項目]
	ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #自己新投資口予約権の取得の事由及び取得の条件 [テキストブロック]
	InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の譲渡に関する事項 [目次項目]
	InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の譲渡に関する事項 [テキストブロック]
	OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #引受け等の概要、新投資口予約権証券 [目次項目]
	OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #引受け等の概要、新投資口予約権証券 [テキストブロック]
	BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #振替機関に関する事項、新投資口予約権証券 [目次項目]
	BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #振替機関に関する事項、新投資口予約権証券 [テキストブロック]
	UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #手取金の使途、新投資口予約権証券 [目次項目]
	UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #手取金の使途、新投資口予約権証券 [テキストブロック]
	OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #その他、新投資口予約権証券 [目次項目]
	OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #その他、新投資口予約権証券 [テキストブロック]
	InvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #投資法人債券（短期投資法人債を除く。） [目次項目]
	InvestmentCorporationBondsOtherThanShortTermOnesTextBlock = '' #投資法人債券（短期投資法人債を除く。） [テキストブロック]
	SecurityTitlesHeading = '' #銘柄 [目次項目]
	SecurityTitlesTextBlock = '' #銘柄 [テキストブロック]
	LegalFormEtcOfInvestmentCorporationBondsHeading = '' #投資法人債券の形態等 [目次項目]
	LegalFormEtcOfInvestmentCorporationBondsTextBlock = '' #投資法人債券の形態等 [テキストブロック]
	TotalFaceValueHeading = '' #券面総額 [目次項目]
	TotalFaceValueTextBlock = '' #券面総額 [テキストブロック]
	AmountOfEachOfInvestmentCorporationBondsHeading = '' #各投資法人債の金額 [目次項目]
	AmountOfEachOfInvestmentCorporationBondsTextBlock = '' #各投資法人債の金額 [テキストブロック]
	TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #発行（売出）価額の総額、投資法人債券（短期投資法人債を除く。） [目次項目]
	TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #発行（売出）価額の総額、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #発行（売出）価格、投資法人債券（短期投資法人債を除く。） [目次項目]
	PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #発行（売出）価格、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	InterestRateHeading = '' #利率 [目次項目]
	InterestRateTextBlock = '' #利率 [テキストブロック]
	DateAndMethodOfInterestPaymentHeading = '' #利払日及び利息支払の方法 [目次項目]
	DateAndMethodOfInterestPaymentTextBlock = '' #利払日及び利息支払の方法 [テキストブロック]
	DateAndMethodOfRedemptionHeading = '' #償還期限及び償還の方法 [目次項目]
	DateAndMethodOfRedemptionTextBlock = '' #償還期限及び償還の方法 [テキストブロック]
	MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #募集の方法、投資法人債券（短期投資法人債を除く。） [目次項目]
	MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #募集の方法、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #申込証拠金、投資法人債券（短期投資法人債を除く。） [目次項目]
	ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #申込証拠金、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #申込期間、投資法人債券（短期投資法人債を除く。） [目次項目]
	ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #申込期間、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #申込取扱場所、投資法人債券（短期投資法人債を除く。） [目次項目]
	PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #申込取扱場所、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #払込期日、投資法人債券（短期投資法人債を除く。） [目次項目]
	DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #払込期日、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #払込取扱場所、投資法人債券（短期投資法人債を除く。） [目次項目]
	PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #払込取扱場所、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #引受け等の概要、投資法人債券（短期投資法人債を除く。） [目次項目]
	OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #引受け等の概要、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	AdministratorOfInvestmentCorporationBondsHeading = '' #投資法人債管理者又は投資法人債の管理会社 [目次項目]
	AdministratorOfInvestmentCorporationBondsTextBlock = '' #投資法人債管理者又は投資法人債の管理会社 [テキストブロック]
	BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #振替機関に関する事項、投資法人債券（短期投資法人債を除く。） [目次項目]
	BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #振替機関に関する事項、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	RegistrationDateAndRegistrationNumberOfInvestmentCorporationHeading = '' #投資法人の登録年月日及び登録番号 [目次項目]
	RegistrationDateAndRegistrationNumberOfInvestmentCorporationTextBlock = '' #投資法人の登録年月日及び登録番号 [テキストブロック]
	UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #手取金の使途、投資法人債券（短期投資法人債を除く。） [目次項目]
	UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #手取金の使途、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #その他、投資法人債券（短期投資法人債を除く。） [目次項目]
	OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #その他、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	ShortTermInvestmentCorporationBondsHeading = '' #短期投資法人債 [目次項目]
	ShortTermInvestmentCorporationBondsTextBlock = '' #短期投資法人債 [テキストブロック]
	TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsHeading = '' #発行（売出）短期投資法人債の総額 [目次項目]
	TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsTextBlock = '' #発行（売出）短期投資法人債の総額 [テキストブロック]
	TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading = '' #発行（売出）価額の総額、短期投資法人債 [目次項目]
	TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock = '' #発行（売出）価額の総額、短期投資法人債 [テキストブロック]
	PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading = '' #発行（売出）価格、短期投資法人債 [目次項目]
	PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock = '' #発行（売出）価格、短期投資法人債 [テキストブロック]
	LimitOnAmountOfIssueHeading = '' #発行限度額 [目次項目]
	LimitOnAmountOfIssueTextBlock = '' #発行限度額 [テキストブロック]
	RemainingBalanceOfLimitOnAmountOfIssueHeading = '' #発行限度額残高 [目次項目]
	RemainingBalanceOfLimitOnAmountOfIssueTextBlock = '' #発行限度額残高 [テキストブロック]
	DueDateOfPaymentHeading = '' #支払期日 [目次項目]
	DueDateOfPaymentTextBlock = '' #支払期日 [テキストブロック]
	PlaceForPaymentHeading = '' #支払場所 [目次項目]
	PlaceForPaymentTextBlock = '' #支払場所 [テキストブロック]
	BookEntryTransferInstitutionShortTermInvestmentCorporationBondsHeading = '' #振替機関に関する事項、短期投資法人債 [目次項目]
	BookEntryTransferInstitutionShortTermInvestmentCorporationBondsTextBlock = '' #振替機関に関する事項、短期投資法人債 [テキストブロック]
	FinancialInstitutionProvidingBackupLineHeading = '' #バックアップラインの設定金融機関 [目次項目]
	FinancialInstitutionProvidingBackupLineTextBlock = '' #バックアップラインの設定金融機関 [テキストブロック]
	DescriptionOfBackupLineHeading = '' #バックアップラインの設定内容 [目次項目]
	DescriptionOfBackupLineTextBlock = '' #バックアップラインの設定内容 [テキストブロック]
	RatingHeading = '' #取得格付 [目次項目]
	RatingTextBlock = '' #取得格付 [テキストブロック]
	SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading = '' #募集又は売出しに関する特別記載事項 [目次項目]
	SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock = '' #募集又は売出しに関する特別記載事項 [テキストブロック]
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
	SpecialInformationHeading = '' #特別情報 [目次項目]
	OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesHeading = '' #内国投資証券事務の概要 [目次項目]
	OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesTextBlock = '' #内国投資証券事務の概要 [テキストブロック]
	OtherInformationSpecialInformationHeading = '' #その他、特別情報 [目次項目]
	OtherInformationSpecialInformationTextBlock = '' #その他、特別情報 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo433SecuritiesRegistrationStatementHeading': #特定有価証券の内容等の開示に関する内閣府令 第四号の三の三様式 有価証券届出書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo433SecuritiesRegistrationStatementHeading = fact.value

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

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationRelatedToDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPage': #届出の対象とした募集（売出）内国投資証券に係る投資法人の名称、表紙
				self.NameOfInvestmentCorporationRelatedToDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPage = fact.value

			elif fact.concept.qname.localName == 'LegalFormAndAmountOfDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPageTextBlock': #届出の対象とした募集（売出）内国投資証券の形態及び金額、表紙 [テキストブロック]
				self.LegalFormAndAmountOfDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'MattersSpecificToStabilizingOperationCoverPageTextBlock': #安定操作に関する事項、表紙 [テキストブロック]
				self.MattersSpecificToStabilizingOperationCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'SecurityInformationHeading': #証券情報 [目次項目]
				self.SecurityInformationHeading = fact.value

			elif fact.concept.qname.localName == 'DomesticInvestmentSecuritiesOtherThanInvestmentCorporationBondsHeading': #内国投資証券（新投資口予約権証券及び投資法人債券を除く。） [目次項目]
				self.DomesticInvestmentSecuritiesOtherThanInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'DomesticInvestmentSecuritiesOtherThanInvestmentUnitAcquisitionRightsAndInvestmentCorporationBondsTextBlock': #内国投資証券（新投資口予約権証券及び投資法人債券を除く。） [テキストブロック]
				self.DomesticInvestmentSecuritiesOtherThanInvestmentUnitAcquisitionRightsAndInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PublicOfferingOfDomesticInvestmentSecuritiesHeading': #募集内国投資証券 [目次項目]
				self.PublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesHeading': #投資法人の名称、募集内国投資証券 [目次項目]
				self.NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #投資法人の名称、募集内国投資証券 [テキストブロック]
				self.NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesHeading': #内国投資証券の形態等、募集内国投資証券 [目次項目]
				self.LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #内国投資証券の形態等、募集内国投資証券 [テキストブロック]
				self.LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesHeading': #発行数、募集内国投資証券 [目次項目]
				self.NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #発行数、募集内国投資証券 [テキストブロック]
				self.NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading': #発行価額の総額、募集内国投資証券 [目次項目]
				self.TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #発行価額の総額、募集内国投資証券 [テキストブロック]
				self.TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading': #発行価格、募集内国投資証券 [目次項目]
				self.PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #発行価格、募集内国投資証券 [テキストブロック]
				self.PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesHeading': #申込手数料、募集内国投資証券 [目次項目]
				self.ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #申込手数料、募集内国投資証券 [テキストブロック]
				self.ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesHeading': #申込単位、募集内国投資証券 [目次項目]
				self.ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #申込単位、募集内国投資証券 [テキストブロック]
				self.ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesHeading': #申込期間、募集内国投資証券 [目次項目]
				self.ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #申込期間、募集内国投資証券 [テキストブロック]
				self.ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesHeading': #申込証拠金、募集内国投資証券 [目次項目]
				self.ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #申込証拠金、募集内国投資証券 [テキストブロック]
				self.ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesHeading': #申込取扱場所、募集内国投資証券 [目次項目]
				self.PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #申込取扱場所、募集内国投資証券 [テキストブロック]
				self.PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading': #払込期日、募集内国投資証券 [目次項目]
				self.DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #払込期日、募集内国投資証券 [テキストブロック]
				self.DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading': #払込取扱場所、募集内国投資証券 [目次項目]
				self.PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #払込取扱場所、募集内国投資証券 [テキストブロック]
				self.PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesHeading': #引受け等の概要、募集内国投資証券 [目次項目]
				self.OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #引受け等の概要、募集内国投資証券 [テキストブロック]
				self.OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesHeading': #振替機関に関する事項、募集内国投資証券 [目次項目]
				self.BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #振替機関に関する事項、募集内国投資証券 [テキストブロック]
				self.BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesHeading': #手取金の使途、募集内国投資証券 [目次項目]
				self.UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #手取金の使途、募集内国投資証券 [テキストブロック]
				self.UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesHeading': #その他、募集内国投資証券 [目次項目]
				self.OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #その他、募集内国投資証券 [テキストブロック]
				self.OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'SecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #売出内国投資証券 [目次項目]
				self.SecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #投資法人の名称、売出内国投資証券 [目次項目]
				self.NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #投資法人の名称、売出内国投資証券 [テキストブロック]
				self.NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #内国投資証券の形態等、売出内国投資証券 [目次項目]
				self.LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #内国投資証券の形態等、売出内国投資証券 [テキストブロック]
				self.LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #売出数、売出内国投資証券 [目次項目]
				self.NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #売出数、売出内国投資証券 [テキストブロック]
				self.NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #売出価額の総額、売出内国投資証券 [目次項目]
				self.TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #売出価額の総額、売出内国投資証券 [テキストブロック]
				self.TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #売出価格、売出内国投資証券 [目次項目]
				self.PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #売出価格、売出内国投資証券 [テキストブロック]
				self.PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #申込手数料、売出内国投資証券 [目次項目]
				self.ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #申込手数料、売出内国投資証券 [テキストブロック]
				self.ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #申込単位、売出内国投資証券 [目次項目]
				self.ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #申込単位、売出内国投資証券 [テキストブロック]
				self.ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #申込期間、売出内国投資証券 [目次項目]
				self.ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #申込期間、売出内国投資証券 [テキストブロック]
				self.ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #申込証拠金、売出内国投資証券 [目次項目]
				self.ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #申込証拠金、売出内国投資証券 [テキストブロック]
				self.ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #申込取扱場所、売出内国投資証券 [目次項目]
				self.PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #申込取扱場所、売出内国投資証券 [テキストブロック]
				self.PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #受渡期日、売出内国投資証券 [目次項目]
				self.SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #受渡期日、売出内国投資証券 [テキストブロック]
				self.SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #払込取扱場所、売出内国投資証券 [目次項目]
				self.PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #払込取扱場所、売出内国投資証券 [テキストブロック]
				self.PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #引受け等の概要、売出内国投資証券 [目次項目]
				self.OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #引受け等の概要、売出内国投資証券 [テキストブロック]
				self.OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #振替機関に関する事項、売出内国投資証券 [目次項目]
				self.BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #振替機関に関する事項、売出内国投資証券 [テキストブロック]
				self.BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #手取金の使途、売出内国投資証券 [目次項目]
				self.UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #手取金の使途、売出内国投資証券 [テキストブロック]
				self.UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #その他、売出内国投資証券 [目次項目]
				self.OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #その他、売出内国投資証券 [テキストブロック]
				self.OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'SubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権証券 [目次項目]
				self.SubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'InvestmentUnitAcquisitionRightsTextBlock': #新投資口予約権証券 [テキストブロック]
				self.InvestmentUnitAcquisitionRightsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationHeading': #投資法人の名称、新投資口予約権証券 [目次項目]
				self.NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #投資法人の名称、新投資口予約権証券 [テキストブロック]
				self.NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権証券の形態等 [目次項目]
				self.LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権証券の形態等 [テキストブロック]
				self.LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationHeading': #発行数、新投資口予約権証券 [目次項目]
				self.NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #発行数、新投資口予約権証券 [テキストブロック]
				self.NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationHeading': #割当日、新投資口予約権証券 [目次項目]
				self.DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #割当日、新投資口予約権証券 [テキストブロック]
				self.DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の内容 [目次項目]
				self.ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の内容 [テキストブロック]
				self.ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の目的となる内国投資証券の形態等 [目次項目]
				self.LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の目的となる内国投資証券の形態等 [テキストブロック]
				self.LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の目的となる内国投資証券の数 [目次項目]
				self.NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の目的となる内国投資証券の数 [テキストブロック]
				self.NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedHeading': #新投資口予約権の行使時の払込金額 [目次項目]
				self.AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedHeading = fact.value

			elif fact.concept.qname.localName == 'AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedTextBlock': #新投資口予約権の行使時の払込金額 [テキストブロック]
				self.AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedHeading': #新投資口予約権の行使により発行する内国投資証券の発行価額の総額 [目次項目]
				self.TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedHeading = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedTextBlock': #新投資口予約権の行使により発行する内国投資証券の発行価額の総額 [テキストブロック]
				self.TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedTextBlock = fact.value

			elif fact.concept.qname.localName == 'ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の行使期間 [目次項目]
				self.ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の行使期間 [テキストブロック]
				self.ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の行使請求の受付場所、取次場所及び払込取扱場所 [目次項目]
				self.CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の行使請求の受付場所、取次場所及び払込取扱場所 [テキストブロック]
				self.CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の行使の条件 [目次項目]
				self.TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の行使の条件 [テキストブロック]
				self.TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationHeading': #自己新投資口予約権の取得の事由及び取得の条件 [目次項目]
				self.ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #自己新投資口予約権の取得の事由及び取得の条件 [テキストブロック]
				self.ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の譲渡に関する事項 [目次項目]
				self.InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の譲渡に関する事項 [テキストブロック]
				self.InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationHeading': #引受け等の概要、新投資口予約権証券 [目次項目]
				self.OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #引受け等の概要、新投資口予約権証券 [テキストブロック]
				self.OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationHeading': #振替機関に関する事項、新投資口予約権証券 [目次項目]
				self.BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #振替機関に関する事項、新投資口予約権証券 [テキストブロック]
				self.BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationHeading': #手取金の使途、新投資口予約権証券 [目次項目]
				self.UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #手取金の使途、新投資口予約権証券 [テキストブロック]
				self.UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationHeading': #その他、新投資口予約権証券 [目次項目]
				self.OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #その他、新投資口予約権証券 [テキストブロック]
				self.OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'InvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #投資法人債券（短期投資法人債を除く。） [目次項目]
				self.InvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'InvestmentCorporationBondsOtherThanShortTermOnesTextBlock': #投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.InvestmentCorporationBondsOtherThanShortTermOnesTextBlock = fact.value

			elif fact.concept.qname.localName == 'SecurityTitlesHeading': #銘柄 [目次項目]
				self.SecurityTitlesHeading = fact.value

			elif fact.concept.qname.localName == 'SecurityTitlesTextBlock': #銘柄 [テキストブロック]
				self.SecurityTitlesTextBlock = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfInvestmentCorporationBondsHeading': #投資法人債券の形態等 [目次項目]
				self.LegalFormEtcOfInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfInvestmentCorporationBondsTextBlock': #投資法人債券の形態等 [テキストブロック]
				self.LegalFormEtcOfInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalFaceValueHeading': #券面総額 [目次項目]
				self.TotalFaceValueHeading = fact.value

			elif fact.concept.qname.localName == 'TotalFaceValueTextBlock': #券面総額 [テキストブロック]
				self.TotalFaceValueTextBlock = fact.value

			elif fact.concept.qname.localName == 'AmountOfEachOfInvestmentCorporationBondsHeading': #各投資法人債の金額 [目次項目]
				self.AmountOfEachOfInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'AmountOfEachOfInvestmentCorporationBondsTextBlock': #各投資法人債の金額 [テキストブロック]
				self.AmountOfEachOfInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #発行（売出）価額の総額、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #発行（売出）価額の総額、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #発行（売出）価格、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #発行（売出）価格、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'InterestRateHeading': #利率 [目次項目]
				self.InterestRateHeading = fact.value

			elif fact.concept.qname.localName == 'InterestRateTextBlock': #利率 [テキストブロック]
				self.InterestRateTextBlock = fact.value

			elif fact.concept.qname.localName == 'DateAndMethodOfInterestPaymentHeading': #利払日及び利息支払の方法 [目次項目]
				self.DateAndMethodOfInterestPaymentHeading = fact.value

			elif fact.concept.qname.localName == 'DateAndMethodOfInterestPaymentTextBlock': #利払日及び利息支払の方法 [テキストブロック]
				self.DateAndMethodOfInterestPaymentTextBlock = fact.value

			elif fact.concept.qname.localName == 'DateAndMethodOfRedemptionHeading': #償還期限及び償還の方法 [目次項目]
				self.DateAndMethodOfRedemptionHeading = fact.value

			elif fact.concept.qname.localName == 'DateAndMethodOfRedemptionTextBlock': #償還期限及び償還の方法 [テキストブロック]
				self.DateAndMethodOfRedemptionTextBlock = fact.value

			elif fact.concept.qname.localName == 'MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #募集の方法、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #募集の方法、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #申込証拠金、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #申込証拠金、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #申込期間、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #申込期間、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #申込取扱場所、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #申込取扱場所、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #払込期日、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #払込期日、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #払込取扱場所、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #払込取扱場所、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #引受け等の概要、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #引受け等の概要、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AdministratorOfInvestmentCorporationBondsHeading': #投資法人債管理者又は投資法人債の管理会社 [目次項目]
				self.AdministratorOfInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'AdministratorOfInvestmentCorporationBondsTextBlock': #投資法人債管理者又は投資法人債の管理会社 [テキストブロック]
				self.AdministratorOfInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #振替機関に関する事項、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #振替機関に関する事項、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'RegistrationDateAndRegistrationNumberOfInvestmentCorporationHeading': #投資法人の登録年月日及び登録番号 [目次項目]
				self.RegistrationDateAndRegistrationNumberOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'RegistrationDateAndRegistrationNumberOfInvestmentCorporationTextBlock': #投資法人の登録年月日及び登録番号 [テキストブロック]
				self.RegistrationDateAndRegistrationNumberOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #手取金の使途、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #手取金の使途、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #その他、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #その他、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ShortTermInvestmentCorporationBondsHeading': #短期投資法人債 [目次項目]
				self.ShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'ShortTermInvestmentCorporationBondsTextBlock': #短期投資法人債 [テキストブロック]
				self.ShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsHeading': #発行（売出）短期投資法人債の総額 [目次項目]
				self.TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsTextBlock': #発行（売出）短期投資法人債の総額 [テキストブロック]
				self.TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading': #発行（売出）価額の総額、短期投資法人債 [目次項目]
				self.TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock': #発行（売出）価額の総額、短期投資法人債 [テキストブロック]
				self.TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading': #発行（売出）価格、短期投資法人債 [目次項目]
				self.PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock': #発行（売出）価格、短期投資法人債 [テキストブロック]
				self.PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'LimitOnAmountOfIssueHeading': #発行限度額 [目次項目]
				self.LimitOnAmountOfIssueHeading = fact.value

			elif fact.concept.qname.localName == 'LimitOnAmountOfIssueTextBlock': #発行限度額 [テキストブロック]
				self.LimitOnAmountOfIssueTextBlock = fact.value

			elif fact.concept.qname.localName == 'RemainingBalanceOfLimitOnAmountOfIssueHeading': #発行限度額残高 [目次項目]
				self.RemainingBalanceOfLimitOnAmountOfIssueHeading = fact.value

			elif fact.concept.qname.localName == 'RemainingBalanceOfLimitOnAmountOfIssueTextBlock': #発行限度額残高 [テキストブロック]
				self.RemainingBalanceOfLimitOnAmountOfIssueTextBlock = fact.value

			elif fact.concept.qname.localName == 'DueDateOfPaymentHeading': #支払期日 [目次項目]
				self.DueDateOfPaymentHeading = fact.value

			elif fact.concept.qname.localName == 'DueDateOfPaymentTextBlock': #支払期日 [テキストブロック]
				self.DueDateOfPaymentTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentHeading': #支払場所 [目次項目]
				self.PlaceForPaymentHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentTextBlock': #支払場所 [テキストブロック]
				self.PlaceForPaymentTextBlock = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionShortTermInvestmentCorporationBondsHeading': #振替機関に関する事項、短期投資法人債 [目次項目]
				self.BookEntryTransferInstitutionShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionShortTermInvestmentCorporationBondsTextBlock': #振替機関に関する事項、短期投資法人債 [テキストブロック]
				self.BookEntryTransferInstitutionShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'FinancialInstitutionProvidingBackupLineHeading': #バックアップラインの設定金融機関 [目次項目]
				self.FinancialInstitutionProvidingBackupLineHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInstitutionProvidingBackupLineTextBlock': #バックアップラインの設定金融機関 [テキストブロック]
				self.FinancialInstitutionProvidingBackupLineTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBackupLineHeading': #バックアップラインの設定内容 [目次項目]
				self.DescriptionOfBackupLineHeading = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBackupLineTextBlock': #バックアップラインの設定内容 [テキストブロック]
				self.DescriptionOfBackupLineTextBlock = fact.value

			elif fact.concept.qname.localName == 'RatingHeading': #取得格付 [目次項目]
				self.RatingHeading = fact.value

			elif fact.concept.qname.localName == 'RatingTextBlock': #取得格付 [テキストブロック]
				self.RatingTextBlock = fact.value

			elif fact.concept.qname.localName == 'SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading': #募集又は売出しに関する特別記載事項 [目次項目]
				self.SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading = fact.value

			elif fact.concept.qname.localName == 'SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock': #募集又は売出しに関する特別記載事項 [テキストブロック]
				self.SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock = fact.value

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

			elif fact.concept.qname.localName == 'SpecialInformationHeading': #特別情報 [目次項目]
				self.SpecialInformationHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesHeading': #内国投資証券事務の概要 [目次項目]
				self.OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesTextBlock': #内国投資証券事務の概要 [テキストブロック]
				self.OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationSpecialInformationHeading': #その他、特別情報 [目次項目]
				self.OtherInformationSpecialInformationHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationSpecialInformationTextBlock': #その他、特別情報 [テキストブロック]
				self.OtherInformationSpecialInformationTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo433SecuritiesRegistrationStatementHeading(self): #特定有価証券の内容等の開示に関する内閣府令 第四号の三の三様式 有価証券届出書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo433SecuritiesRegistrationStatementHeading

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

	def getNameOfInvestmentCorporationRelatedToDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPage(self): #届出の対象とした募集（売出）内国投資証券に係る投資法人の名称、表紙
		return self.NameOfInvestmentCorporationRelatedToDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPage

	def getLegalFormAndAmountOfDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPageTextBlock(self): #届出の対象とした募集（売出）内国投資証券の形態及び金額、表紙 [テキストブロック]
		return self.LegalFormAndAmountOfDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPageTextBlock

	def getMattersSpecificToStabilizingOperationCoverPageTextBlock(self): #安定操作に関する事項、表紙 [テキストブロック]
		return self.MattersSpecificToStabilizingOperationCoverPageTextBlock

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getSecurityInformationHeading(self): #証券情報 [目次項目]
		return self.SecurityInformationHeading

	def getDomesticInvestmentSecuritiesOtherThanInvestmentCorporationBondsHeading(self): #内国投資証券（新投資口予約権証券及び投資法人債券を除く。） [目次項目]
		return self.DomesticInvestmentSecuritiesOtherThanInvestmentCorporationBondsHeading

	def getDomesticInvestmentSecuritiesOtherThanInvestmentUnitAcquisitionRightsAndInvestmentCorporationBondsTextBlock(self): #内国投資証券（新投資口予約権証券及び投資法人債券を除く。） [テキストブロック]
		return self.DomesticInvestmentSecuritiesOtherThanInvestmentUnitAcquisitionRightsAndInvestmentCorporationBondsTextBlock

	def getPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #募集内国投資証券 [目次項目]
		return self.PublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getNameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #投資法人の名称、募集内国投資証券 [目次項目]
		return self.NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getNameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #投資法人の名称、募集内国投資証券 [テキストブロック]
		return self.NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getLegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #内国投資証券の形態等、募集内国投資証券 [目次項目]
		return self.LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getLegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #内国投資証券の形態等、募集内国投資証券 [テキストブロック]
		return self.LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getNumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #発行数、募集内国投資証券 [目次項目]
		return self.NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getNumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #発行数、募集内国投資証券 [テキストブロック]
		return self.NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getTotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #発行価額の総額、募集内国投資証券 [目次項目]
		return self.TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getTotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #発行価額の総額、募集内国投資証券 [テキストブロック]
		return self.TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getPriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #発行価格、募集内国投資証券 [目次項目]
		return self.PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getPriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #発行価格、募集内国投資証券 [テキストブロック]
		return self.PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #申込手数料、募集内国投資証券 [目次項目]
		return self.ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #申込手数料、募集内国投資証券 [テキストブロック]
		return self.ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #申込単位、募集内国投資証券 [目次項目]
		return self.ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #申込単位、募集内国投資証券 [テキストブロック]
		return self.ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #申込期間、募集内国投資証券 [目次項目]
		return self.ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #申込期間、募集内国投資証券 [テキストブロック]
		return self.ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #申込証拠金、募集内国投資証券 [目次項目]
		return self.ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #申込証拠金、募集内国投資証券 [テキストブロック]
		return self.ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getPlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #申込取扱場所、募集内国投資証券 [目次項目]
		return self.PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getPlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #申込取扱場所、募集内国投資証券 [テキストブロック]
		return self.PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getDueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #払込期日、募集内国投資証券 [目次項目]
		return self.DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getDueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #払込期日、募集内国投資証券 [テキストブロック]
		return self.DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getPlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #払込取扱場所、募集内国投資証券 [目次項目]
		return self.PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getPlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #払込取扱場所、募集内国投資証券 [テキストブロック]
		return self.PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getOverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #引受け等の概要、募集内国投資証券 [目次項目]
		return self.OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getOverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #引受け等の概要、募集内国投資証券 [テキストブロック]
		return self.OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getBookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #振替機関に関する事項、募集内国投資証券 [目次項目]
		return self.BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getBookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #振替機関に関する事項、募集内国投資証券 [テキストブロック]
		return self.BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getUseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #手取金の使途、募集内国投資証券 [目次項目]
		return self.UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getUseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #手取金の使途、募集内国投資証券 [テキストブロック]
		return self.UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getOtherInformationPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #その他、募集内国投資証券 [目次項目]
		return self.OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getOtherInformationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #その他、募集内国投資証券 [テキストブロック]
		return self.OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #売出内国投資証券 [目次項目]
		return self.SecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getNameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #投資法人の名称、売出内国投資証券 [目次項目]
		return self.NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getNameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #投資法人の名称、売出内国投資証券 [テキストブロック]
		return self.NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getLegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #内国投資証券の形態等、売出内国投資証券 [目次項目]
		return self.LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getLegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #内国投資証券の形態等、売出内国投資証券 [テキストブロック]
		return self.LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getNumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #売出数、売出内国投資証券 [目次項目]
		return self.NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getNumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #売出数、売出内国投資証券 [テキストブロック]
		return self.NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getTotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #売出価額の総額、売出内国投資証券 [目次項目]
		return self.TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getTotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #売出価額の総額、売出内国投資証券 [テキストブロック]
		return self.TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getPriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #売出価格、売出内国投資証券 [目次項目]
		return self.PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getPriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #売出価格、売出内国投資証券 [テキストブロック]
		return self.PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #申込手数料、売出内国投資証券 [目次項目]
		return self.ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #申込手数料、売出内国投資証券 [テキストブロック]
		return self.ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #申込単位、売出内国投資証券 [目次項目]
		return self.ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #申込単位、売出内国投資証券 [テキストブロック]
		return self.ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #申込期間、売出内国投資証券 [目次項目]
		return self.ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #申込期間、売出内国投資証券 [テキストブロック]
		return self.ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #申込証拠金、売出内国投資証券 [目次項目]
		return self.ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #申込証拠金、売出内国投資証券 [テキストブロック]
		return self.ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getPlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #申込取扱場所、売出内国投資証券 [目次項目]
		return self.PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getPlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #申込取扱場所、売出内国投資証券 [テキストブロック]
		return self.PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getSettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #受渡期日、売出内国投資証券 [目次項目]
		return self.SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getSettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #受渡期日、売出内国投資証券 [テキストブロック]
		return self.SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getPlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #払込取扱場所、売出内国投資証券 [目次項目]
		return self.PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getPlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #払込取扱場所、売出内国投資証券 [テキストブロック]
		return self.PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getOverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #引受け等の概要、売出内国投資証券 [目次項目]
		return self.OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getOverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #引受け等の概要、売出内国投資証券 [テキストブロック]
		return self.OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getBookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #振替機関に関する事項、売出内国投資証券 [目次項目]
		return self.BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getBookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #振替機関に関する事項、売出内国投資証券 [テキストブロック]
		return self.BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getUseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #手取金の使途、売出内国投資証券 [目次項目]
		return self.UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getUseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #手取金の使途、売出内国投資証券 [テキストブロック]
		return self.UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getOtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #その他、売出内国投資証券 [目次項目]
		return self.OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getOtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #その他、売出内国投資証券 [テキストブロック]
		return self.OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権証券 [目次項目]
		return self.SubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getInvestmentUnitAcquisitionRightsTextBlock(self): #新投資口予約権証券 [テキストブロック]
		return self.InvestmentUnitAcquisitionRightsTextBlock

	def getNameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #投資法人の名称、新投資口予約権証券 [目次項目]
		return self.NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getNameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #投資法人の名称、新投資口予約権証券 [テキストブロック]
		return self.NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getLegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権証券の形態等 [目次項目]
		return self.LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getLegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権証券の形態等 [テキストブロック]
		return self.LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getNumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #発行数、新投資口予約権証券 [目次項目]
		return self.NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getNumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #発行数、新投資口予約権証券 [テキストブロック]
		return self.NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getDateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #割当日、新投資口予約権証券 [目次項目]
		return self.DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getDateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #割当日、新投資口予約権証券 [テキストブロック]
		return self.DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の内容 [目次項目]
		return self.ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の内容 [テキストブロック]
		return self.ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getLegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の目的となる内国投資証券の形態等 [目次項目]
		return self.LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getLegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の目的となる内国投資証券の形態等 [テキストブロック]
		return self.LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getNumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の目的となる内国投資証券の数 [目次項目]
		return self.NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getNumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の目的となる内国投資証券の数 [テキストブロック]
		return self.NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getAmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedHeading(self): #新投資口予約権の行使時の払込金額 [目次項目]
		return self.AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedHeading

	def getAmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedTextBlock(self): #新投資口予約権の行使時の払込金額 [テキストブロック]
		return self.AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedTextBlock

	def getTotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedHeading(self): #新投資口予約権の行使により発行する内国投資証券の発行価額の総額 [目次項目]
		return self.TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedHeading

	def getTotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedTextBlock(self): #新投資口予約権の行使により発行する内国投資証券の発行価額の総額 [テキストブロック]
		return self.TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedTextBlock

	def getExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の行使期間 [目次項目]
		return self.ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の行使期間 [テキストブロック]
		return self.ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getCustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の行使請求の受付場所、取次場所及び払込取扱場所 [目次項目]
		return self.CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getCustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の行使請求の受付場所、取次場所及び払込取扱場所 [テキストブロック]
		return self.CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getTermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の行使の条件 [目次項目]
		return self.TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getTermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の行使の条件 [テキストブロック]
		return self.TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #自己新投資口予約権の取得の事由及び取得の条件 [目次項目]
		return self.ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #自己新投資口予約権の取得の事由及び取得の条件 [テキストブロック]
		return self.ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getInformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の譲渡に関する事項 [目次項目]
		return self.InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getInformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の譲渡に関する事項 [テキストブロック]
		return self.InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getOverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #引受け等の概要、新投資口予約権証券 [目次項目]
		return self.OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getOverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #引受け等の概要、新投資口予約権証券 [テキストブロック]
		return self.OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getBookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #振替機関に関する事項、新投資口予約権証券 [目次項目]
		return self.BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getBookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #振替機関に関する事項、新投資口予約権証券 [テキストブロック]
		return self.BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getUseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #手取金の使途、新投資口予約権証券 [目次項目]
		return self.UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getUseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #手取金の使途、新投資口予約権証券 [テキストブロック]
		return self.UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getOtherInformationSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #その他、新投資口予約権証券 [目次項目]
		return self.OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getOtherInformationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #その他、新投資口予約権証券 [テキストブロック]
		return self.OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.InvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getInvestmentCorporationBondsOtherThanShortTermOnesTextBlock(self): #投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.InvestmentCorporationBondsOtherThanShortTermOnesTextBlock

	def getSecurityTitlesHeading(self): #銘柄 [目次項目]
		return self.SecurityTitlesHeading

	def getSecurityTitlesTextBlock(self): #銘柄 [テキストブロック]
		return self.SecurityTitlesTextBlock

	def getLegalFormEtcOfInvestmentCorporationBondsHeading(self): #投資法人債券の形態等 [目次項目]
		return self.LegalFormEtcOfInvestmentCorporationBondsHeading

	def getLegalFormEtcOfInvestmentCorporationBondsTextBlock(self): #投資法人債券の形態等 [テキストブロック]
		return self.LegalFormEtcOfInvestmentCorporationBondsTextBlock

	def getTotalFaceValueHeading(self): #券面総額 [目次項目]
		return self.TotalFaceValueHeading

	def getTotalFaceValueTextBlock(self): #券面総額 [テキストブロック]
		return self.TotalFaceValueTextBlock

	def getAmountOfEachOfInvestmentCorporationBondsHeading(self): #各投資法人債の金額 [目次項目]
		return self.AmountOfEachOfInvestmentCorporationBondsHeading

	def getAmountOfEachOfInvestmentCorporationBondsTextBlock(self): #各投資法人債の金額 [テキストブロック]
		return self.AmountOfEachOfInvestmentCorporationBondsTextBlock

	def getTotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #発行（売出）価額の総額、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getTotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #発行（売出）価額の総額、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getPriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #発行（売出）価格、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getPriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #発行（売出）価格、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getInterestRateHeading(self): #利率 [目次項目]
		return self.InterestRateHeading

	def getInterestRateTextBlock(self): #利率 [テキストブロック]
		return self.InterestRateTextBlock

	def getDateAndMethodOfInterestPaymentHeading(self): #利払日及び利息支払の方法 [目次項目]
		return self.DateAndMethodOfInterestPaymentHeading

	def getDateAndMethodOfInterestPaymentTextBlock(self): #利払日及び利息支払の方法 [テキストブロック]
		return self.DateAndMethodOfInterestPaymentTextBlock

	def getDateAndMethodOfRedemptionHeading(self): #償還期限及び償還の方法 [目次項目]
		return self.DateAndMethodOfRedemptionHeading

	def getDateAndMethodOfRedemptionTextBlock(self): #償還期限及び償還の方法 [テキストブロック]
		return self.DateAndMethodOfRedemptionTextBlock

	def getMethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #募集の方法、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getMethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #募集の方法、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #申込証拠金、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #申込証拠金、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #申込期間、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #申込期間、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getPlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #申込取扱場所、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getPlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #申込取扱場所、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getDueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #払込期日、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getDueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #払込期日、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getPlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #払込取扱場所、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getPlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #払込取扱場所、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getOverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #引受け等の概要、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getOverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #引受け等の概要、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getAdministratorOfInvestmentCorporationBondsHeading(self): #投資法人債管理者又は投資法人債の管理会社 [目次項目]
		return self.AdministratorOfInvestmentCorporationBondsHeading

	def getAdministratorOfInvestmentCorporationBondsTextBlock(self): #投資法人債管理者又は投資法人債の管理会社 [テキストブロック]
		return self.AdministratorOfInvestmentCorporationBondsTextBlock

	def getBookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #振替機関に関する事項、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getBookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #振替機関に関する事項、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getRegistrationDateAndRegistrationNumberOfInvestmentCorporationHeading(self): #投資法人の登録年月日及び登録番号 [目次項目]
		return self.RegistrationDateAndRegistrationNumberOfInvestmentCorporationHeading

	def getRegistrationDateAndRegistrationNumberOfInvestmentCorporationTextBlock(self): #投資法人の登録年月日及び登録番号 [テキストブロック]
		return self.RegistrationDateAndRegistrationNumberOfInvestmentCorporationTextBlock

	def getUseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #手取金の使途、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getUseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #手取金の使途、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getOtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #その他、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getOtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #その他、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getShortTermInvestmentCorporationBondsHeading(self): #短期投資法人債 [目次項目]
		return self.ShortTermInvestmentCorporationBondsHeading

	def getShortTermInvestmentCorporationBondsTextBlock(self): #短期投資法人債 [テキストブロック]
		return self.ShortTermInvestmentCorporationBondsTextBlock

	def getTotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsHeading(self): #発行（売出）短期投資法人債の総額 [目次項目]
		return self.TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsHeading

	def getTotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsTextBlock(self): #発行（売出）短期投資法人債の総額 [テキストブロック]
		return self.TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsTextBlock

	def getTotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading(self): #発行（売出）価額の総額、短期投資法人債 [目次項目]
		return self.TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading

	def getTotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock(self): #発行（売出）価額の総額、短期投資法人債 [テキストブロック]
		return self.TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock

	def getPriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading(self): #発行（売出）価格、短期投資法人債 [目次項目]
		return self.PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading

	def getPriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock(self): #発行（売出）価格、短期投資法人債 [テキストブロック]
		return self.PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock

	def getLimitOnAmountOfIssueHeading(self): #発行限度額 [目次項目]
		return self.LimitOnAmountOfIssueHeading

	def getLimitOnAmountOfIssueTextBlock(self): #発行限度額 [テキストブロック]
		return self.LimitOnAmountOfIssueTextBlock

	def getRemainingBalanceOfLimitOnAmountOfIssueHeading(self): #発行限度額残高 [目次項目]
		return self.RemainingBalanceOfLimitOnAmountOfIssueHeading

	def getRemainingBalanceOfLimitOnAmountOfIssueTextBlock(self): #発行限度額残高 [テキストブロック]
		return self.RemainingBalanceOfLimitOnAmountOfIssueTextBlock

	def getDueDateOfPaymentHeading(self): #支払期日 [目次項目]
		return self.DueDateOfPaymentHeading

	def getDueDateOfPaymentTextBlock(self): #支払期日 [テキストブロック]
		return self.DueDateOfPaymentTextBlock

	def getPlaceForPaymentHeading(self): #支払場所 [目次項目]
		return self.PlaceForPaymentHeading

	def getPlaceForPaymentTextBlock(self): #支払場所 [テキストブロック]
		return self.PlaceForPaymentTextBlock

	def getBookEntryTransferInstitutionShortTermInvestmentCorporationBondsHeading(self): #振替機関に関する事項、短期投資法人債 [目次項目]
		return self.BookEntryTransferInstitutionShortTermInvestmentCorporationBondsHeading

	def getBookEntryTransferInstitutionShortTermInvestmentCorporationBondsTextBlock(self): #振替機関に関する事項、短期投資法人債 [テキストブロック]
		return self.BookEntryTransferInstitutionShortTermInvestmentCorporationBondsTextBlock

	def getFinancialInstitutionProvidingBackupLineHeading(self): #バックアップラインの設定金融機関 [目次項目]
		return self.FinancialInstitutionProvidingBackupLineHeading

	def getFinancialInstitutionProvidingBackupLineTextBlock(self): #バックアップラインの設定金融機関 [テキストブロック]
		return self.FinancialInstitutionProvidingBackupLineTextBlock

	def getDescriptionOfBackupLineHeading(self): #バックアップラインの設定内容 [目次項目]
		return self.DescriptionOfBackupLineHeading

	def getDescriptionOfBackupLineTextBlock(self): #バックアップラインの設定内容 [テキストブロック]
		return self.DescriptionOfBackupLineTextBlock

	def getRatingHeading(self): #取得格付 [目次項目]
		return self.RatingHeading

	def getRatingTextBlock(self): #取得格付 [テキストブロック]
		return self.RatingTextBlock

	def getSpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading(self): #募集又は売出しに関する特別記載事項 [目次項目]
		return self.SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading

	def getSpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock(self): #募集又は売出しに関する特別記載事項 [テキストブロック]
		return self.SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock

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

	def getSpecialInformationHeading(self): #特別情報 [目次項目]
		return self.SpecialInformationHeading

	def getOverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesHeading(self): #内国投資証券事務の概要 [目次項目]
		return self.OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesHeading

	def getOverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesTextBlock(self): #内国投資証券事務の概要 [テキストブロック]
		return self.OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesTextBlock

	def getOtherInformationSpecialInformationHeading(self): #その他、特別情報 [目次項目]
		return self.OtherInformationSpecialInformationHeading

	def getOtherInformationSpecialInformationTextBlock(self): #その他、特別情報 [テキストブロック]
		return self.OtherInformationSpecialInformationTextBlock
