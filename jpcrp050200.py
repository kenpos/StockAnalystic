from arelle import ModelManager
from arelle import Cntlr

class jpcrp050200:#企業内容等の開示に関する内閣府令 第五号の二様式 半期報告書
	CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo52SemiannualSecuritiesReportHeading = '' #企業内容等の開示に関する内閣府令 第五号の二様式 半期報告書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	SemiAnnualAccountingPeriodCoverPage = '' #中間会計期間、表紙
	CompanyNameCoverPage = '' #会社名、表紙
	CompanyNameInEnglishCoverPage = '' #英訳名、表紙
	TitleAndNameOfRepresentativeCoverPage = '' #代表者の役職氏名、表紙
	AddressOfRegisteredHeadquarterCoverPage = '' #本店の所在の場所、表紙
	TelephoneNumberAddressOfRegisteredHeadquarterCoverPage = '' #電話番号、本店の所在の場所、表紙
	NameOfContactPersonAddressOfRegisteredHeadquarterCoverPage = '' #事務連絡者氏名、本店の所在の場所、表紙
	NearestPlaceOfContactCoverPage = '' #最寄りの連絡場所、表紙
	TelephoneNumberNearestPlaceOfContactCoverPage = '' #電話番号、最寄りの連絡場所、表紙
	NameOfContactPersonNearestPlaceOfContactCoverPage = '' #事務連絡者氏名、最寄りの連絡場所、表紙
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	FootnotesCoverPageTextBlock = '' #脚注、表紙 [テキストブロック]
	CompanyInformationHeading = '' #企業情報 [目次項目]
	OverviewOfCompanyHeading = '' #企業の概況 [目次項目]
	SummaryOfBusinessResultsHeading = '' #主要な経営指標等の推移 [目次項目]
	BusinessResultsOfReportingCompanyHeading = '' #提出会社の経営指標等 [目次項目]
	BusinessResultsOfReportingCompanyTextBlock = '' #提出会社の経営指標等 [テキストブロック]
	BusinessResultsOfReportingCompanyHeading = '' #提出会社の経営指標等 [目次項目]
	BusinessResultsOfReportingCompanyTable = '' #提出会社の経営指標等 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	BusinessResultsOfReportingCompanyLineItems = '' #提出会社の経営指標等 [表示項目]
	NetSalesSummaryOfBusinessResults = '' #売上高、経営指標等
	RevenueKeyFinancialData = '' #売上収益、経営指標等
	OperatingRevenue1SummaryOfBusinessResults = '' #営業収益、経営指標等
	OperatingRevenue2SummaryOfBusinessResults = '' #営業収入、経営指標等
	GrossOperatingRevenueSummaryOfBusinessResults = '' #営業総収入、経営指標等
	OrdinaryIncomeSummaryOfBusinessResults = '' #経常収益、経営指標等
	NetPremiumsWrittenSummaryOfBusinessResultsINS = '' #正味収入保険料、経営指標等、保険業
	OrdinaryIncomeLossSummaryOfBusinessResults = '' #経常利益又は経常損失（△）、経営指標等
	NetIncomeLossSummaryOfBusinessResults = '' #当期純利益又は当期純損失（△）、経営指標等
	NetLossRatioSummaryOfBusinessResultsINS = '' #正味損害率、経営指標等、保険業
	NetOperatingExpenseRatioSummaryOfBusinessResultsINS = '' #正味事業費率、経営指標等、保険業
	InterestAndDividendIncomeSummaryOfBusinessResultsINS = '' #利息及び配当金収入、経営指標等、保険業
	InvestmentAssetsYieldIncomeYieldSummaryOfBusinessResultsINS = '' #運用資産利回り（インカム利回り）、経営指標等、保険業
	InvestmentYieldRealizedYieldSummaryOfBusinessResultsINS = '' #資産運用利回り（実現利回り）、経営指標等、保険業
	EquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSummaryOfBusinessResults = '' #持分法を適用した場合の投資利益又は投資損失（△）、経営指標等
	CapitalStockSummaryOfBusinessResults = '' #資本金、経営指標等
	TotalNumberOfIssuedSharesSummaryOfBusinessResults = '' #発行済株式総数（普通株式）、経営指標等
	NetAssetsSummaryOfBusinessResults = '' #純資産額、経営指標等
	TotalAssetsSummaryOfBusinessResults = '' #総資産額、経営指標等
	DepositsSummaryOfBusinessResults = '' #預金残高、経営指標等
	LoansAndBillsDiscountedSummaryOfBusinessResults = '' #貸出金残高、経営指標等
	SecuritiesSummaryOfBusinessResults = '' #有価証券残高、経営指標等
	NetAssetsPerShareSummaryOfBusinessResults = '' #１株当たり純資産額、経営指標等
	DividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり配当額、経営指標等
	InterimDividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり中間配当額、経営指標等
	FirstQuarterDividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり第１四半期配当額、経営指標等
	SecondQuarterDividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり第２四半期配当額、経営指標等
	ThirdQuarterDividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり第３四半期配当額、経営指標等
	FourthQuarterDividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり第４四半期配当額、経営指標等
	FifthQuarterDividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり第５四半期配当額、経営指標等
	BasicEarningsLossPerShareSummaryOfBusinessResults = '' #１株当たり当期純利益又は当期純損失（△）、経営指標等
	DilutedEarningsPerShareSummaryOfBusinessResults = '' #潜在株式調整後１株当たり当期純利益、経営指標等
	EquityToAssetRatioSummaryOfBusinessResults = '' #自己資本比率、経営指標等
	CapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults = '' #自己資本比率（国際統一基準）、経営指標等
	CapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults = '' #自己資本比率（国内基準）、経営指標等
	CapitalAdequacyRatioBISStandardSummaryOfBusinessResults = '' #自己資本比率（第一基準）、経営指標等
	CapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults = '' #自己資本比率（第二基準）、経営指標等
	RateOfReturnOnEquitySummaryOfBusinessResults = '' #自己資本利益率、経営指標等
	PriceEarningsRatioSummaryOfBusinessResults = '' #株価収益率、経営指標等
	PayoutRatioSummaryOfBusinessResults = '' #配当性向、経営指標等
	NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults = '' #営業活動によるキャッシュ・フロー、経営指標等
	NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults = '' #投資活動によるキャッシュ・フロー、経営指標等
	NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults = '' #財務活動によるキャッシュ・フロー、経営指標等
	CashAndCashEquivalentsSummaryOfBusinessResults = '' #現金及び現金同等物の残高、経営指標等
	NumberOfEmployees = '' #従業員数
	AverageNumberOfTemporaryWorkers = '' #平均臨時雇用人員
	TotalShareholderReturn = '' #株主総利回り
	TotalReturnOnSharePriceIndex = '' #株価指数における総利回り
	DescriptionOfBusinessHeading = '' #事業の内容 [目次項目]
	DescriptionOfBusinessTextBlock = '' #事業の内容 [テキストブロック]
	InformationAboutSharesEtcHeading = '' #株式等の状況 [目次項目]
	TotalNumberOfSharesEtcHeading = '' #株式の総数等 [目次項目]
	TotalNumberOfSharesHeading = '' #株式の総数 [目次項目]
	TotalNumberOfSharesTextBlock = '' #株式の総数 [テキストブロック]
	IssuedSharesTotalNumberOfSharesEtcHeading = '' #発行済株式、株式の総数等 [目次項目]
	IssuedSharesTotalNumberOfSharesEtcTextBlock = '' #発行済株式、株式の総数等 [テキストブロック]
	SubscriptionRightsToSharesEtcHeading = '' #新株予約権等の状況 [目次項目]
	DetailsOfEmployeeShareOptionProgramHeading = '' #ストックオプション制度の内容 [目次項目]
	DetailsOfEmployeeShareOptionProgramTextBlock = '' #ストックオプション制度の内容 [テキストブロック]
	OtherInformationOnShareAcquisitionRightsHeading = '' #その他の新株予約権等の状況 [目次項目]
	OtherInformationOnShareAcquisitionRightsTextBlock = '' #その他の新株予約権等の状況 [テキストブロック]
	ExercisesEtcOfMovingStrikeConvertibleBondsEtcHeading = '' #行使価額修正条項付新株予約権付社債券等の行使状況等 [目次項目]
	ExercisesEtcOfMovingStrikeConvertibleBondsEtcTextBlock = '' #行使価額修正条項付新株予約権付社債券等の行使状況等 [テキストブロック]
	ChangesInNumberOfIssuedSharesStatedCapitalEtcHeading = '' #発行済株式総数、資本金等の推移 [目次項目]
	ChangesInNumberOfIssuedSharesStatedCapitalEtcTextBlock = '' #発行済株式総数、資本金等の推移 [テキストブロック]
	MajorShareholdersHeading = '' #大株主の状況 [目次項目]
	MajorShareholdersTextBlock = '' #大株主の状況 [テキストブロック]
	MajorShareholdersHeading = '' #大株主の状況 [目次項目]
	MajorShareholdersTable = '' #大株主の状況 [表]
	MajorShareholdersAxis = '' #大株主 [軸]
	MajorShareholdersMember = '' #大株主 [メンバー] ※ディメンションデフォルト
	No1MajorShareholdersMember = '' #第1位、大株主 [メンバー]
	No2MajorShareholdersMember = '' #第2位、大株主 [メンバー]
	No3MajorShareholdersMember = '' #第3位、大株主 [メンバー]
	No4MajorShareholdersMember = '' #第4位、大株主 [メンバー]
	No5MajorShareholdersMember = '' #第5位、大株主 [メンバー]
	No6MajorShareholdersMember = '' #第6位、大株主 [メンバー]
	No7MajorShareholdersMember = '' #第7位、大株主 [メンバー]
	No8MajorShareholdersMember = '' #第8位、大株主 [メンバー]
	No9MajorShareholdersMember = '' #第9位、大株主 [メンバー]
	No10MajorShareholdersMember = '' #第10位、大株主 [メンバー]
	No11MajorShareholdersMember = '' #第11位、大株主 [メンバー]
	No12MajorShareholdersMember = '' #第12位、大株主 [メンバー]
	No13MajorShareholdersMember = '' #第13位、大株主 [メンバー]
	No14MajorShareholdersMember = '' #第14位、大株主 [メンバー]
	No15MajorShareholdersMember = '' #第15位、大株主 [メンバー]
	MajorShareholdersLineItems = '' #大株主の状況 [表示項目]
	NameMajorShareholders = '' #氏名又は名称、大株主の状況
	AddressMajorShareholders = '' #住所、大株主の状況
	NumberOfSharesHeld = '' #所有株式数
	ShareholdingRatio = '' #発行済株式（自己株式を除く。）の総数に対する所有株式数の割合
	MajorShareholdersHeading = '' #大株主の状況 [目次項目]
	MajorShareholdersVotingRightsTable = '' #所有株式に係る議決権上位者の状況 [表]
	MajorShareholdersVotingRightsAxis = '' #議決権上位 [軸]
	MajorShareholdersVotingRightsMember = '' #議決権上位 [メンバー] ※ディメンションデフォルト
	No1MajorShareholdersVotingRightsMember = '' #第1位、議決権上位 [メンバー]
	No2MajorShareholdersVotingRightsMember = '' #第2位、議決権上位 [メンバー]
	No3MajorShareholdersVotingRightsMember = '' #第3位、議決権上位 [メンバー]
	No4MajorShareholdersVotingRightsMember = '' #第4位、議決権上位 [メンバー]
	No5MajorShareholdersVotingRightsMember = '' #第5位、議決権上位 [メンバー]
	No6MajorShareholdersVotingRightsMember = '' #第6位、議決権上位 [メンバー]
	No7MajorShareholdersVotingRightsMember = '' #第7位、議決権上位 [メンバー]
	No8MajorShareholdersVotingRightsMember = '' #第8位、議決権上位 [メンバー]
	No9MajorShareholdersVotingRightsMember = '' #第9位、議決権上位 [メンバー]
	No10MajorShareholdersVotingRightsMember = '' #第10位、議決権上位 [メンバー]
	No11MajorShareholdersVotingRightsMember = '' #第11位、議決権上位 [メンバー]
	No12MajorShareholdersVotingRightsMember = '' #第12位、議決権上位 [メンバー]
	No13MajorShareholdersVotingRightsMember = '' #第13位、議決権上位 [メンバー]
	No14MajorShareholdersVotingRightsMember = '' #第14位、議決権上位 [メンバー]
	No15MajorShareholdersVotingRightsMember = '' #第15位、議決権上位 [メンバー]
	MajorShareholdersVotingRightsLineItems = '' #所有株式に係る議決権上位者の状況 [表示項目]
	NameMajorShareholdersVotingRights = '' #氏名又は名称、所有株式に係る議決権上位者の状況
	AddressMajorShareholdersVotingRights = '' #住所、所有株式に係る議決権上位者の状況
	NumberOfVotingRightsHeld = '' #所有議決権数（個）
	RatioOfVotingRightsHeld = '' #総株主の議決権に対する所有議決権数の割合
	VotingRightsHeading = '' #議決権の状況 [目次項目]
	VotingRightsTextBlock = '' #議決権の状況 [テキストブロック]
	IssuedSharesVotingRightsHeading = '' #発行済株式、議決権の状況 [目次項目]
	IssuedSharesVotingRightsTextBlock = '' #発行済株式、議決権の状況 [テキストブロック]
	TreasurySharesEtcHeading = '' #自己株式等 [目次項目]
	TreasurySharesEtcTextBlock = '' #自己株式等 [テキストブロック]
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	InformationAboutOfficersTextBlock = '' #役員の状況 [テキストブロック]
	InformationAboutEmployeesHeading = '' #従業員の状況 [目次項目]
	InformationAboutEmployeesTextBlock = '' #従業員の状況 [テキストブロック]
	OverviewOfBusinessHeading = '' #事業の状況 [目次項目]
	BusinessPolicyBusinessEnvironmentIssuesToAddressEtcHeading = '' #経営方針、経営環境及び対処すべき課題等 [目次項目]
	BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock = '' #経営方針、経営環境及び対処すべき課題等 [テキストブロック]
	OverviewOfOperatingResultsEtcHeading = '' #経営成績等の概要 [目次項目]
	OverviewOfOperatingResultsEtcTextBlock = '' #経営成績等の概要 [テキストブロック]
	CriticalContractsForOperationHeading = '' #経営上の重要な契約等 [目次項目]
	CriticalContractsForOperationTextBlock = '' #経営上の重要な契約等 [テキストブロック]
	ResearchAndDevelopmentActivitiesHeading = '' #研究開発活動 [目次項目]
	ResearchAndDevelopmentActivitiesTextBlock = '' #研究開発活動 [テキストブロック]
	InformationAboutFacilitiesHeading = '' #設備の状況 [目次項目]
	MajorFacilitiesHeading = '' #主要な設備の状況 [目次項目]
	MajorFacilitiesTextBlock = '' #主要な設備の状況 [テキストブロック]
	PlannedAdditionsRetirementsEtcOfFacilitiesHeading = '' #設備の新設、除却等の計画 [目次項目]
	PlannedAdditionsRetirementsEtcOfFacilitiesTextBlock = '' #設備の新設、除却等の計画 [テキストブロック]
	FinancialInformationHeading = '' #経理の状況 [目次項目]
	FinancialInformationHeading = '' #経理の状況 [目次項目]
	RegulationsInAccordanceWithWhichConsolidatedFinancialStatementsHaveBeenPreparedFinancialInformation = '' #連結財務諸表が基づく規則、経理の状況
	RegulationsInAccordanceWithWhichFinancialStatementsHaveBeenPreparedFinancialInformation = '' #財務諸表が基づく規則、経理の状況
	DescriptionOfFactThatCompanyEngagesSpecifiedBusinessAndHasPreparedItsSemiAnnualConsolidatedFinancialStatementsFinancialInformation = '' #特定事業会社であり、中間連結財務諸表等を作成した場合の記載、経理の状況
	DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation = '' #連結財務諸表が別記事業の特別の法令若しくは準則に基づく場合の記載、経理の状況
	DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation = '' #財務諸表が別記事業の特別の法令若しくは準則に基づく場合の記載、経理の状況
	DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation = '' #指定国際会計基準により連結財務諸表を作成した場合の記載、経理の状況
	DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithJMISFinancialInformation = '' #修正国際基準により連結財務諸表を作成した場合の記載、経理の状況
	DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithUSGAAPFinancialInformation = '' #米国会計基準により連結財務諸表を作成した場合の記載、経理の状況
	DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedFinancialInformation = '' #連結財務諸表を作成していない場合の記載、経理の状況
	DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedAndFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation = '' #連結財務諸表を作成していない場合で指定国際会計基準により財務諸表を作成する場合の記載、経理の状況
	DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialProvisionFinancialInformation = '' #特例財務諸表を作成する場合の記載、経理の状況
	DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsStatementOfCashFlowsFinancialInformation = '' #第１四半期又は第３四半期に係る四半期報告書において四半期キャッシュ・フロー計算書を記載する場合の記載、経理の状況
	DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsConsolidatedStatementOfCashFlowsFinancialInformation = '' #第１四半期又は第３四半期に係る四半期報告書において四半期連結キャッシュ・フロー計算書を記載する場合の記載、経理の状況
	DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodStatementOfIncomeFinancialInformation = '' #四半期報告書において四半期会計期間に係る四半期損益計算書を記載する場合の記載、経理の状況
	DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodConsolidatedStatementOfComprehensiveIncomeFinancialInformation = '' #四半期報告書において四半期連結会計期間に係る四半期連結損益計算書及び四半期連結包括利益計算書又は四半期連結損益及び包括利益計算書を記載する場合の記載、経理の状況
	RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcFinancialInformation = '' #連結財務諸表等の適正性を確保するための特段の取組み、経理の状況
	RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithIFRSFinancialInformation = '' #指定国際会計基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
	RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcAndInternalSystemToPrepareConsolidatedFinancialStatementsEtcFairlyInAccordanceWithIFRSFinancialInformation = '' #連結財務諸表等の適正性を確保するための特段の取組み及び指定国際会計基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
	RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithJMISFinancialInformation = '' #修正国際基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
	NoteOnIndependentAuditFinancialInformation = '' #監査証明について、経理の状況
	NoteOnChangeOfIndependentAuditorsFinancialInformation = '' #監査人の交代、経理の状況
	NoteOnChangeInFiscalYearEndsFinancialInformation = '' #決算期変更について、経理の状況
	SemiAnnualFinancialStatementsHeading = '' #中間財務諸表 [目次項目]
	SemiAnnualBalanceSheetHeading = '' #中間貸借対照表 [目次項目]
	SemiAnnualBalanceSheetTextBlock = '' #中間貸借対照表 [テキストブロック]
	SemiAnnualStatementOfIncomeHeading = '' #中間損益計算書 [目次項目]
	SemiAnnualStatementOfIncomeTextBlock = '' #中間損益計算書 [テキストブロック]
	SemiAnnualStatementOfChangesInEquityHeading = '' #中間株主資本等変動計算書 [目次項目]
	SemiAnnualStatementOfChangesInEquityTextBlock = '' #中間株主資本等変動計算書 [テキストブロック]
	SemiAnnualStatementOfCashFlowsHeading = '' #中間キャッシュ・フロー計算書 [目次項目]
	SemiAnnualStatementOfCashFlowsTextBlock = '' #中間キャッシュ・フロー計算書 [テキストブロック]
	NotesSemiAnnualFinancialStatementsHeading = '' #注記事項、中間財務諸表 [目次項目]
	NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernSemiAnnualFinancialStatementsHeading = '' #継続企業の前提に関する事項、中間財務諸表 [目次項目]
	NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernSemiAnnualFinancialStatementsTextBlock = '' #継続企業の前提に関する事項、中間財務諸表 [テキストブロック]
	NotesSignificantAccountingPoliciesSemiAnnualFinancialStatementsHeading = '' #重要な会計方針、中間財務諸表 [目次項目]
	NotesSignificantAccountingPoliciesSemiAnnualFinancialStatementsTextBlock = '' #重要な会計方針、中間財務諸表 [テキストブロック]
	NotesChangesInAccountingPoliciesSemiAnnualFinancialStatementsHeading = '' #会計方針の変更、中間財務諸表 [目次項目]
	NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcSemiAnnualFinancialStatementsTextBlock = '' #会計基準等の改正等に伴う会計方針の変更、中間財務諸表 [テキストブロック]
	NotesVoluntaryChangesInAccountingPoliciesSemiAnnualFinancialStatementsTextBlock = '' #会計基準等の改正等以外の正当な理由による会計方針の変更、中間財務諸表 [テキストブロック]
	NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesSemiAnnualFinancialStatementsTextBlock = '' #会計上の見積りの変更と区別することが困難な会計方針の変更、中間財務諸表 [テキストブロック]
	NotesChangesInPresentationSemiAnnualFinancialStatementsHeading = '' #表示方法の変更、中間財務諸表 [目次項目]
	NotesChangesInPresentationSemiAnnualFinancialStatementsTextBlock = '' #表示方法の変更、中間財務諸表 [テキストブロック]
	NotesChangesInAccountingEstimatesSemiAnnualFinancialStatementsHeading = '' #会計上の見積りの変更、中間財務諸表 [目次項目]
	NotesChangesInAccountingEstimatesSemiAnnualFinancialStatementsTextBlock = '' #会計上の見積りの変更、中間財務諸表 [テキストブロック]
	NotesRestatementSemiAnnualFinancialStatementsHeading = '' #修正再表示、中間財務諸表 [目次項目]
	NotesRestatementSemiAnnualFinancialStatementsTextBlock = '' #修正再表示、中間財務諸表 [テキストブロック]
	NotesAdditionalInformationSemiAnnualFinancialStatementsHeading = '' #追加情報、中間財務諸表 [目次項目]
	NotesAdditionalInformationSemiAnnualFinancialStatementsTextBlock = '' #追加情報、中間財務諸表 [テキストブロック]
	NotesSemiAnnualBalanceSheetHeading = '' #中間貸借対照表関係 [目次項目]
	NotesSemiAnnualBalanceSheetHeading = '' #中間貸借対照表関係 [目次項目]
	NotesSemiAnnualBalanceSheetTable = '' #中間貸借対照表関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSemiAnnualBalanceSheetLineItems = '' #中間貸借対照表関係 [表示項目]
	NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock = '' #資産の金額から直接控除している引当金の注記 [テキストブロック]
	AllowanceForDoubtfulAccountsCA = '' #貸倒引当金、流動資産、一括控除
	AllowanceForDoubtfulAccountsIOAByGroup = '' #貸倒引当金、投資その他の資産、一括控除
	AllowanceForDoubtfulAccountsAccountsReceivableTrade = '' #貸倒引当金、売掛金
	AllowanceForDoubtfulAccountsLongTermLoansReceivable = '' #貸倒引当金、長期貸付金
	AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther = '' #貸倒引当金、破産更生債権等
	NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock = '' #有形固定資産の減価償却累計額の注記 [テキストブロック]
	AccumulatedDepreciationPPEByGroup = '' #減価償却累計額、有形固定資産、一括控除
	AccumulatedDepreciationBuildings = '' #減価償却累計額、建物
	AccumulatedDepreciationStructures = '' #減価償却累計額、構築物
	AccumulatedDepreciationMachineryAndEquipment = '' #減価償却累計額、機械及び装置
	NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock = '' #有形固定資産の圧縮記帳額の注記 [テキストブロック]
	NotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock = '' #減損損失累計額の表示に関する注記 [テキストブロック]
	NotesRegardingPledgedAssetsTextBlock = '' #担保に供している資産の注記 [テキストブロック]
	NotesRegardingReservesUnderSpecialLawsTextBlock = '' #特別法上の準備金等に関する注記 [テキストブロック]
	NotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock = '' #棚卸資産及び工事損失引当金の表示に関する注記 [テキストブロック]
	NotesRegardingProvisionIncurredFromBusinessCombinationTextBlock = '' #企業結合に係る特定勘定の注記 [テキストブロック]
	NotesRegardingGuaranteeObligationsTextBlock = '' #保証債務の注記 [テキストブロック]
	NotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock = '' #受取手形割引高及び（又は）受取手形裏書譲渡高 [テキストブロック]
	DiscountedTradeNotesReceivable = '' #受取手形割引高
	TradeNotesReceivableTransferredByEndorsement = '' #受取手形裏書譲渡高
	NotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock = '' #指定法人の純資産の記載に関する注記 [テキストブロック]
	NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock = '' #期末日満期手形の会計処理 [テキストブロック]
	OtherElementsForNotesBalanceSheetAbstract = '' #貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock = '' #消費貸借契約及び（又は）消費寄託契約により貸し付けている有価証券に関する注記 [テキストブロック]
	NotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock = '' #自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
	NotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock = '' #有価証券の消費貸借契約・消費寄託契約及び自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
	NotesRegardingLoanParticipationsTextBlock = '' #ローン・パーティシペーションに関する注記 [テキストブロック]
	CreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock = '' #当座貸越契約及び（又は）貸出コミットメントに関する貸手の注記 [テキストブロック]
	DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock = '' #当座貸越契約及び（又は）貸出コミットメントに関する借手の注記 [テキストブロック]
	NotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock = '' #関係会社の株式及び（又は）出資金の総額 [テキストブロック]
	NotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock = '' #非連結子会社及び関連会社の株式及び（又は）出資金の総額 [テキストブロック]
	NotesRegardingSubordinatedBorrowingsTextBlock = '' #劣後特約付借入金に関する注記 [テキストブロック]
	NotesRegardingSubordinatedBondsPayableTextBlock = '' #劣後特約付社債に関する注記 [テキストブロック]
	NotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock = '' #資産の部の社債に係る保証債務に関する注記 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfBankAbstract = '' #銀行業の貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock = '' #銀行法及び金融機能の再生のための緊急措置に関する法律に基づく債権に関する注記、銀行業 [テキストブロック]
	NotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock = '' #銀行業における手形割引に関する注記、銀行業 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract = '' #第一種金融商品取引業の貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock = '' #差し入れた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
	NotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock = '' #差し入れを受けた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
	BreakdownOfTradingAccountSecuritiesEtcSECTextBlock = '' #商品有価証券等の内訳、第一種金融商品取引業 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfInsuranceAbstract = '' #保険業の貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock = '' #保険業法に基づく債権に関する注記、保険業 [テキストブロック]
	NotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock = '' #保険業法第118条に規定する特別勘定の資産及び負債に関する注記、保険業 [テキストブロック]
	NotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock = '' #その他資産に含まれている保険業法第113条に規定する事業費の繰延額の注記 [テキストブロック]
	NotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock = '' #契約者配当準備金の増減異動及び契約者配当金の支払額に関する注記、保険業 [テキストブロック]
	NotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock = '' #保険業法第91条の規定による組織変更剰余金額の注記、保険業 [テキストブロック]
	NotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock = '' #保険業法施行規則第73条第3項において準用する同規則第71条第1項に規定する再保険を付した部分に相当する支払備金の金額の注記、保険業 [テキストブロック]
	NotesRegardingPolicyReservesReinsuredINSTextBlock = '' #保険業法施行規則第71条第1項に規定する再保険を付した部分に相当する責任準備金の金額の注記、保険業 [テキストブロック]
	NotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock = '' #保険業法第259条の規定に基づく生命保険契約者保護機構に対する今後の負担見積額、保険業 [テキストブロック]
	BreakdownOfOutstandingClaimsINSTextBlock = '' #支払備金の内訳、保険業 [テキストブロック]
	BreakdownOfPolicyReserveINSTextBlock = '' #責任準備金の内訳、保険業 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract = '' #特定金融業の貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingBadLoansSPFTextBlock = '' #不良債権に関する注記、特定金融業 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract = '' #商品先物取引業の貸借対照表関係のその他の要素 [タイトル項目]
	ExplanationOfFuturesTransactionMarginCustomerCMDTextBlock = '' #委託者先物取引差金の説明、商品先物取引業 [テキストブロック]
	NotesSemiAnnualStatementOfIncomeHeading = '' #中間損益計算書関係 [目次項目]
	NotesSemiAnnualStatementOfIncomeHeading = '' #中間損益計算書関係 [目次項目]
	NotesSemiAnnualStatementOfIncomeTable = '' #中間損益計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSemiAnnualStatementOfIncomeLineItems = '' #中間損益計算書関係 [表示項目]
	NotesRegardingSignificantComponentsOfNonOperatingIncomeTextBlock = '' #重要な営業外収益の注記 [テキストブロック]
	NotesRegardingSignificantComponentsOfNonOperatingExpensesTextBlock = '' #重要な営業外費用の注記 [テキストブロック]
	NotesRegardingSignificantComponentsOfExtraordinaryIncomeTextBlock = '' #重要な特別利益の注記 [テキストブロック]
	NotesRegardingSignificantComponentsOfExtraordinaryLossesTextBlock = '' #重要な特別損失の注記 [テキストブロック]
	NotesRegardingImpairmentLossTextBlock = '' #減損損失に関する注記 [テキストブロック]
	NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock = '' #企業結合に係る特定勘定の取崩益の注記 [テキストブロック]
	DescriptionOfFactThatSimplifiedMethodOfTaxEffectAccountingWasAppliedTextBlock = '' #簡便法による税効果会計を適用している場合の注記 [テキストブロック]
	NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock = '' #売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]
	NotesRegardingAmountOfDepreciationTextBlock = '' #減価償却額の注記 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeAbstract = '' #損益計算書関係のその他の要素 [タイトル項目]
	BreakdownOfBusinessCostTextBlock = '' #事業費の内訳 [テキストブロック]
	BreakdownOfPersonnelExpensesTextBlock = '' #人件費の内訳 [テキストブロック]
	BreakdownOfGainOnSalesOfSecuritiesTextBlock = '' #有価証券売却益の内訳 [テキストブロック]
	BreakdownOfLossOnSalesOfSecuritiesTextBlock = '' #有価証券売却損の内訳 [テキストブロック]
	BreakdownOfLossOnValuationOfSecuritiesTextBlock = '' #有価証券評価損の内訳 [テキストブロック]
	NotesRegardingTransactionsWithAffiliatedEntitiesTextBlock = '' #関係会社との取引に関する注記 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeOfBankAbstract = '' #銀行業の損益計算書関係のその他の要素 [タイトル項目]
	MajorComponentsOfOtherIncomeBNKTextBlock = '' #その他の経常収益の主要な内訳、銀行業 [テキストブロック]
	MajorComponentsOfOtherExpensesBNKTextBlock = '' #その他の経常費用の主要な内訳、銀行業 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract = '' #第一種金融商品取引業の損益計算書関係のその他の要素 [タイトル項目]
	BreakdownOfNetTradingIncomeSECTextBlock = '' #トレーディング損益の内訳、第一種金融商品取引業 [テキストブロック]
	BreakdownOfFinancialRevenueSECTextBlock = '' #金融収益の内訳、第一種金融商品取引業 [テキストブロック]
	BreakdownOfFinancialExpensesSECTextBlock = '' #金融費用の内訳、第一種金融商品取引業 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeOfInsuranceAbstract = '' #保険業の損益計算書関係のその他の要素 [タイトル項目]
	MajorComponentsOfBusinessCostTextBlock = '' #事業費の主な内訳 [テキストブロック]
	AgentFeeEtcINSNonlife = '' #代理店手数料等、損害保険業
	SalariesINSNonlife = '' #給与、損害保険業
	BreakdownOfNetPremiumsWrittenINSTextBlock = '' #正味収入保険料の内訳、保険業 [テキストブロック]
	BreakdownOfNetClaimsPaidINSTextBlock = '' #正味支払保険金の内訳、保険業 [テキストブロック]
	BreakdownOfCommissionsAndCollectionFeesINSTextBlock = '' #諸手数料及び集金費の内訳、保険業 [テキストブロック]
	BreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock = '' #支払備金繰入額又は支払備金戻入額の内訳、保険業 [テキストブロック]
	BreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock = '' #責任準備金繰入額又は責任準備金戻入額の内訳、保険業 [テキストブロック]
	NotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock = '' #支払備金繰入額又は支払備金戻入額の計算上、差し引かれた又は足し上げられた出再支払備金繰入額又は出再支払備金戻入額の注記、保険業 [テキストブロック]
	NotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock = '' #責任準備金繰入額又は責任準備金戻入額の計算上、差し引かれた又は足し上げられた出再責任準備金繰入額又は出再責任準備金戻入額の注記、保険業 [テキストブロック]
	BreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock = '' #利息及び配当金収入の資産源泉別内訳、保険業 [テキストブロック]
	InterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock = '' #商品有価証券及び売買目的有価証券に係るそれぞれの利息及び配当金収入、売却損益及び評価損益の金額、保険業 [テキストブロック]
	NotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock = '' #金銭の信託に係る評価損益の金額の注記、保険業 [テキストブロック]
	NotesRegardingUnrealizedGainLossForDerivativesINSTextBlock = '' #金融派生商品に係る評価損益の金額の注記、保険業 [テキストブロック]
	MajorComponentsOfOtherExtraordinaryIncomeINSTextBlock = '' #その他特別利益の主な内訳、保険業 [テキストブロック]
	MajorComponentsOfOtherExtraordinaryLossesINSTextBlock = '' #その他特別損失の主な内訳、保険業 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract = '' #商品先物取引業の損益計算書関係のその他の要素 [タイトル項目]
	BreakdownOfBrokerageIncomeCMDTextBlock = '' #受取手数料の内訳、商品先物取引業 [テキストブロック]
	BreakdownOfNetGainOnTradingCMDTextBlock = '' #売買損益の内訳、商品先物取引業 [テキストブロック]
	ExchangeRelatedExpensesCMDTextBlock = '' #取引所等関係費の内訳、商品先物取引業 [テキストブロック]
	NotesSemiAnnualStatementOfChangesInEquityHeading = '' #中間株主資本等変動計算書関係 [目次項目]
	NotesSemiAnnualStatementOfChangesInEquityHeading = '' #中間株主資本等変動計算書関係 [目次項目]
	NotesSemiAnnualStatementOfChangesInEquityTable = '' #中間株主資本等変動計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSemiAnnualStatementOfChangesInEquityLineItems = '' #中間株主資本等変動計算書関係 [表示項目]
	NotesRegardingIssuedSharesAndTreasurySharesTextBlock = '' #発行済株式及び自己株式に関する注記 [テキストブロック]
	NotesRegardingTreasurySharesTextBlock = '' #自己株式に関する注記 [テキストブロック]
	NotesRegardingNewShareSubscriptionRightsEtcTextBlock = '' #新株予約権等に関する注記 [テキストブロック]
	NotesRegardingDividendTextBlock = '' #配当に関する注記 [テキストブロック]
	NotesSemiAnnualStatementOfCashFlowsHeading = '' #中間キャッシュ・フロー計算書関係 [目次項目]
	NotesSemiAnnualStatementOfCashFlowsHeading = '' #中間キャッシュ・フロー計算書関係 [目次項目]
	NotesSemiAnnualStatementOfCashFlowsTable = '' #中間キャッシュ・フロー計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSemiAnnualStatementOfCashFlowsLineItems = '' #中間キャッシュ・フロー計算書関係 [表示項目]
	ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock = '' #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
	DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock = '' #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
	NotesLeasesSemiAnnualFinancialStatementsHeading = '' #リース取引関係、中間財務諸表 [目次項目]
	NotesLeasesSemiAnnualFinancialStatementsTextBlock = '' #リース取引関係、中間財務諸表 [テキストブロック]
	NotesFinancialInstrumentsSemiAnnualFinancialStatementsHeading = '' #金融商品関係、中間財務諸表 [目次項目]
	NotesFinancialInstrumentsSemiAnnualFinancialStatementsTextBlock = '' #金融商品関係、中間財務諸表 [テキストブロック]
	NotesSecuritiesSemiAnnualFinancialStatementsHeading = '' #有価証券関係、中間財務諸表 [目次項目]
	NotesSecuritiesSemiAnnualFinancialStatementsTextBlock = '' #有価証券関係、中間財務諸表 [テキストブロック]
	NotesMoneyHeldInTrustSemiAnnualFinancialStatementsHeading = '' #金銭の信託関係、中間財務諸表 [目次項目]
	NotesMoneyHeldInTrustSemiAnnualFinancialStatementsTextBlock = '' #金銭の信託関係、中間財務諸表 [テキストブロック]
	NotesValuationDifferenceOnAvailableForSaleSecuritiesSemiAnnualFinancialStatementsHeading = '' #その他有価証券評価差額金、中間財務諸表 [目次項目]
	NotesValuationDifferenceOnAvailableForSaleSecuritiesSemiAnnualFinancialStatementsTextBlock = '' #その他有価証券評価差額金、中間財務諸表 [テキストブロック]
	NotesDerivativesSemiAnnualFinancialStatementsHeading = '' #デリバティブ取引関係、中間財務諸表 [目次項目]
	NotesDerivativesSemiAnnualFinancialStatementsTextBlock = '' #デリバティブ取引関係、中間財務諸表 [テキストブロック]
	NotesShareOptionsEtcSemiAnnualFinancialStatementsHeading = '' #ストック・オプション等関係、中間財務諸表 [目次項目]
	NotesShareOptionsEtcSemiAnnualFinancialStatementsTextBlock = '' #ストック・オプション等関係、中間財務諸表 [テキストブロック]
	NotesBusinessCombinationsSemiAnnualFinancialStatementsHeading = '' #企業結合等関係、中間財務諸表 [目次項目]
	NotesBusinessCombinationsSemiAnnualFinancialStatementsTextBlock = '' #企業結合等関係、中間財務諸表 [テキストブロック]
	NotesAssetRetirementObligationsSemiAnnualFinancialStatementsHeading = '' #資産除去債務関係、中間財務諸表 [目次項目]
	NotesAssetRetirementObligationsSemiAnnualFinancialStatementsTextBlock = '' #資産除去債務関係、中間財務諸表 [テキストブロック]
	NotesRealEstateForLeaseEtcSemiAnnualFinancialStatementsHeading = '' #賃貸等不動産関係、中間財務諸表 [目次項目]
	NotesRealEstateForLeaseEtcSemiAnnualFinancialStatementsTextBlock = '' #賃貸等不動産関係、中間財務諸表 [テキストブロック]
	NotesRevenueRecognitionSemiAnnualFinancialStatementsHeading = '' #収益認識関係、中間財務諸表 [目次項目]
	NotesRevenueRecognitionSemiAnnualFinancialStatementsTextBlock = '' #収益認識関係、中間財務諸表 [テキストブロック]
	NotesInventoriesSemiAnnualFinancialStatementsHeading = '' #棚卸資産関係、中間財務諸表 [目次項目]
	NotesInventoriesSemiAnnualFinancialStatementsTextBlock = '' #棚卸資産関係、中間財務諸表 [テキストブロック]
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = '' #セグメント情報等、中間財務諸表 [目次項目]
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsTextBlock = '' #セグメント情報等、中間財務諸表 [テキストブロック]
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = '' #セグメント情報等、中間財務諸表 [目次項目]
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable = '' #セグメント情報等、中間財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems = '' #セグメント情報等、中間財務諸表 [表示項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	DescriptionOfReportableSegmentsTextBlock = '' #報告セグメントの概要 [テキストブロック]
	DisclosureOfChangesInReportableSegmentsTextBlock = '' #報告セグメントの変更に関する事項 [テキストブロック]
	DescriptionOfFactThatCompanysBusinessComprisesSingleSegment = '' #単一セグメントである旨
	ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock = '' #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = '' #セグメント情報等、中間財務諸表 [目次項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable = '' #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	TotalOfReportableSegmentsAndOthersMember = '' #報告セグメント及びその他の合計 [メンバー]
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	ReconcilingItemsMember = '' #調整項目 [メンバー]
	DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems = '' #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表示項目]
	SalesSegmentInformationAbstract = '' #売上高、セグメント情報 [タイトル項目]
	RevenuesFromExternalCustomers = '' #外部顧客への売上高
	TransactionsWithOtherSegments = '' #セグメント間の内部売上高又は振替高
	NetSales = '' #売上高
	OperatingRevenue1 = '' #営業収益
	OperatingRevenue2 = '' #営業収入
	GrossOperatingRevenue = '' #営業総収入
	OrdinaryIncomeBNK = '' #経常収益、銀行業
	OperatingIncomeINS = '' #経常収益、保険業
	SegmentProfitLossAbstract = '' #セグメント利益又は損失（△） [タイトル項目]
	OperatingIncome = '' #営業利益又は営業損失（△）
	OrdinaryIncome = '' #経常利益又は経常損失（△）
	IncomeBeforeIncomeTaxes = '' #税引前当期純利益又は税引前当期純損失（△）
	ProfitLoss = '' #当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）
	Assets = '' #資産
	Liabilities = '' #負債
	OtherItemsSegmentInformationAbstract = '' #その他の項目、セグメント情報 [タイトル項目]
	DepreciationSegmentInformation = '' #減価償却費、セグメント情報
	AmortizationOfGoodwillSGA = '' #のれん償却額、販売費及び一般管理費
	InterestIncomeNOI = '' #受取利息、営業外収益
	InterestExpensesNOE = '' #支払利息、営業外費用
	ExtraordinaryIncome = '' #特別利益
	GainOnNegativeGoodwillEI = '' #負ののれん発生益、特別利益
	ExtraordinaryLoss = '' #特別損失
	ImpairmentLossEL = '' #減損損失、特別損失
	IncomeTaxExpense = '' #税金費用
	IncreaseInPropertyPlantAndEquipmentAndIntangibleAssets = '' #有形固定資産及び無形固定資産の増加額
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = '' #セグメント情報等、中間財務諸表 [目次項目]
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable = '' #セグメント情報等、中間財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems = '' #セグメント情報等、中間財務諸表 [表示項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	FootnotesRegardingSegmentInformationTableTextBlock = '' #セグメント表の脚注 [テキストブロック]
	DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock = '' #報告セグメント合計額と財務諸表計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
	NotesInformationAssociatedWithReportableSegmentsAbstract = '' #関連情報 [タイトル項目]
	InformationForEachProductOrServiceTextBlock = '' #製品及びサービスごとの情報 [テキストブロック]
	InformationForEachRegionAbstract = '' #地域ごとの情報 [タイトル項目]
	RevenuesFromExternalCustomersInformationForEachRegionTextBlock = '' #売上高、地域ごとの情報 [テキストブロック]
	PropertyPlantAndEquipmentInformationForEachRegionTextBlock = '' #有形固定資産、地域ごとの情報 [テキストブロック]
	InformationForEachOfMainCustomersTextBlock = '' #主要な顧客ごとの情報 [テキストブロック]
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = '' #セグメント情報等、中間財務諸表 [目次項目]
	DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract = '' #報告セグメントごとの固定資産の減損損失に関する情報 [タイトル項目]
	DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable = '' #報告セグメントごとの固定資産の減損損失に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	UnallocatedAmountsAndEliminationMember = '' #全社・消去 [メンバー]
	DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems = '' #報告セグメントごとの固定資産の減損損失に関する情報 [表示項目]
	ImpairmentLossEL = '' #減損損失、特別損失
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = '' #セグメント情報等、中間財務諸表 [目次項目]
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable = '' #セグメント情報等、中間財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems = '' #セグメント情報等、中間財務諸表 [表示項目]
	DescriptionOfImpairmentLossNotAllocatedToReportableSegments = '' #報告セグメントに配分されていない減損損失の内容
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = '' #セグメント情報等、中間財務諸表 [目次項目]
	AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract = '' #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [タイトル項目]
	AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable = '' #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	UnallocatedAmountsAndEliminationMember = '' #全社・消去 [メンバー]
	AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems = '' #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表示項目]
	AmortizationOfGoodwillSGA = '' #のれん償却額、販売費及び一般管理費
	Goodwill = '' #のれん
	GoodwillBeforeOffsetting = '' #のれん（相殺前）
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = '' #セグメント情報等、中間財務諸表 [目次項目]
	AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract = '' #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [タイトル項目]
	AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable = '' #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	UnallocatedAmountsAndEliminationMember = '' #全社・消去 [メンバー]
	AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems = '' #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表示項目]
	AmortizationOfNegativeGoodwillNOI = '' #負ののれん償却額、営業外収益
	NegativeGoodwill = '' #負ののれん
	NegativeGoodwillBeforeOffsetting = '' #負ののれん（相殺前）
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = '' #セグメント情報等、中間財務諸表 [目次項目]
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable = '' #セグメント情報等、中間財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems = '' #セグメント情報等、中間財務諸表 [表示項目]
	DescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments = '' #報告セグメントに配分されていないのれんの償却額又は未償却残高の内容
	NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = '' #セグメント情報等、中間財務諸表 [目次項目]
	InformationAboutGainOnBargainPurchaseForEachReportableSegmentTable = '' #報告セグメントごとの負ののれん発生益に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	UnallocatedAmountsAndEliminationMember = '' #全社・消去 [メンバー]
	InformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems = '' #報告セグメントごとの負ののれん発生益に関する情報 [表示項目]
	DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock = '' #報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]
	NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSemiAnnualFinancialStatementsHeading = '' #持分法損益等、中間財務諸表 [目次項目]
	NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSemiAnnualFinancialStatementsTextBlock = '' #持分法損益等、中間財務諸表 [テキストブロック]
	NotesSpecialPurposeEntitiesSubjectToDisclosureSemiAnnualFinancialStatementsHeading = '' #開示対象特別目的会社関係、中間財務諸表 [目次項目]
	NotesSpecialPurposeEntitiesSubjectToDisclosureSemiAnnualFinancialStatementsTextBlock = '' #開示対象特別目的会社関係、中間財務諸表 [テキストブロック]
	NotesPerShareInformationSemiAnnualFinancialStatementsHeading = '' #１株当たり情報、中間財務諸表 [目次項目]
	NotesPerShareInformationSemiAnnualFinancialStatementsTextBlock = '' #１株当たり情報、中間財務諸表 [テキストブロック]
	NotesSignificantEventsAfterReportingPeriodSemiAnnualFinancialStatementsHeading = '' #重要な後発事象、中間財務諸表 [目次項目]
	NotesSignificantEventsAfterReportingPeriodSemiAnnualFinancialStatementsTextBlock = '' #重要な後発事象、中間財務諸表 [テキストブロック]
	OtherInformationFinancialStatementsEtcHeading = '' #その他、財務諸表等 [目次項目]
	OtherInformationFinancialStatementsEtcTextBlock = '' #その他、財務諸表等 [テキストブロック]
	ReferenceInformationOfReportingCompanyHeading = '' #提出会社の参考情報 [目次項目]
	ReferenceInformationOfReportingCompanyTextBlock = '' #提出会社の参考情報 [テキストブロック]
	InformationAboutAffiliatedEntitiesHeading = '' #関係会社の情報 [目次項目]
	InformationAboutAffiliatedEntitiesTextBlock = '' #関係会社の情報 [テキストブロック]
	InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyHeading = '' #提出会社の保証会社等の情報 [目次項目]
	InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyTextBlock = '' #提出会社の保証会社等の情報 [テキストブロック]
	InformationAboutGuaranteeCompanyHeading = '' #保証会社情報 [目次項目]
	InformationAboutGuaranteeCompanyTextBlock = '' #保証会社情報 [テキストブロック]
	CorporateBondsUnderGuaranteeHeading = '' #保証の対象となっている社債 [目次項目]
	CorporateBondsUnderGuaranteeTextBlock = '' #保証の対象となっている社債 [テキストブロック]
	InformationAboutGuaranteeCompanySubjectToOngoingDisclosureHeading = '' #継続開示会社たる保証会社に関する事項 [目次項目]
	InformationAboutGuaranteeCompanySubjectToOngoingDisclosureTextBlock = '' #継続開示会社たる保証会社に関する事項 [テキストブロック]
	DocumentsSubmittedByGuaranteeCompanyHeading = '' #保証会社が提出した書類 [目次項目]
	AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading = '' #有価証券報告書及びその添付書類又は四半期報告書若しくは半期報告書、保証会社が提出した書類 [目次項目]
	AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock = '' #有価証券報告書及びその添付書類又は四半期報告書若しくは半期報告書、保証会社が提出した書類 [テキストブロック]
	ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading = '' #臨時報告書、保証会社が提出した書類 [目次項目]
	ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock = '' #臨時報告書、保証会社が提出した書類 [テキストブロック]
	AmendmentReportDocumentsSubmittedByGuaranteeCompanyHeading = '' #訂正報告書、保証会社が提出した書類 [目次項目]
	AmendmentReportDocumentsSubmittedByGuaranteeCompanyTextBlock = '' #訂正報告書、保証会社が提出した書類 [テキストブロック]
	PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyHeading = '' #上記書類を縦覧に供している場所、保証会社が提出した書類 [目次項目]
	PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyTextBlock = '' #上記書類を縦覧に供している場所、保証会社が提出した書類 [テキストブロック]
	InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = '' #継続開示会社に該当しない保証会社に関する事項 [目次項目]
	InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = '' #継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
	CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterHeading = '' #会社名・代表者の役職氏名及び本店の所在の場所 [目次項目]
	CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterTextBlock = '' #会社名・代表者の役職氏名及び本店の所在の場所 [テキストブロック]
	OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = '' #企業の概況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
	OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = '' #企業の概況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
	OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = '' #事業の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
	OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = '' #事業の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
	InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = '' #設備の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
	InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = '' #設備の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
	GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = '' #保証会社の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
	GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = '' #保証会社の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
	FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = '' #経理の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
	FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = '' #経理の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
	InformationAboutCompaniesOtherThanGuaranteeCompanyHeading = '' #保証会社以外の会社の情報 [目次項目]
	InformationAboutCompaniesOtherThanGuaranteeCompanyTextBlock = '' #保証会社以外の会社の情報 [テキストブロック]
	ReasonForDisclosureOfInformationOfCompanyConcernedHeading = '' #当該会社の情報の開示を必要とする理由 [目次項目]
	ReasonForDisclosureOfInformationOfCompanyConcernedTextBlock = '' #当該会社の情報の開示を必要とする理由 [テキストブロック]
	InformationAboutCompanyConcernedSubjectToOngoingDisclosureHeading = '' #継続開示会社たる当該会社に関する事項 [目次項目]
	InformationAboutCompanyConcernedSubjectToOngoingDisclosureTextBlock = '' #継続開示会社たる当該会社に関する事項 [テキストブロック]
	InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureHeading = '' #継続開示会社に該当しない当該会社に関する事項 [目次項目]
	InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureTextBlock = '' #継続開示会社に該当しない当該会社に関する事項 [テキストブロック]
	InformationAboutIndexEtcHeading = '' #指数等の情報 [目次項目]
	InformationAboutIndexEtcTextBlock = '' #指数等の情報 [テキストブロック]
	ReasonForDisclosureOfSaidIndexEtcHeading = '' #当該指数等の情報の開示を必要とする理由 [目次項目]
	ReasonForDisclosureOfSaidIndexEtcTextBlock = '' #当該指数等の情報の開示を必要とする理由 [テキストブロック]
	HistoricalRecordsOfIndexEtcHeading = '' #当該指数等の推移 [目次項目]
	HistoricalRecordsOfIndexEtcTextBlock = '' #当該指数等の推移 [テキストブロック]
	IndependentAuditorsReportHeading = '' #独立監査人の報告書 [目次項目]
	IndependentAuditorsReportConsolidatedTextBlock = '' #独立監査人の報告書、連結 [テキストブロック]
	IndependentAuditorsReportNonConsolidatedTextBlock = '' #独立監査人の報告書、個別 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo52SemiannualSecuritiesReportHeading': #企業内容等の開示に関する内閣府令 第五号の二様式 半期報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo52SemiannualSecuritiesReportHeading = fact.value

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

			elif fact.concept.qname.localName == 'SemiAnnualAccountingPeriodCoverPage': #中間会計期間、表紙
				self.SemiAnnualAccountingPeriodCoverPage = fact.value

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

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'FootnotesCoverPageTextBlock': #脚注、表紙 [テキストブロック]
				self.FootnotesCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'CompanyInformationHeading': #企業情報 [目次項目]
				self.CompanyInformationHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCompanyHeading': #企業の概況 [目次項目]
				self.OverviewOfCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'SummaryOfBusinessResultsHeading': #主要な経営指標等の推移 [目次項目]
				self.SummaryOfBusinessResultsHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfReportingCompanyHeading': #提出会社の経営指標等 [目次項目]
				self.BusinessResultsOfReportingCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfReportingCompanyTextBlock': #提出会社の経営指標等 [テキストブロック]
				self.BusinessResultsOfReportingCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfReportingCompanyHeading': #提出会社の経営指標等 [目次項目]
				self.BusinessResultsOfReportingCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfReportingCompanyTable': #提出会社の経営指標等 [表]
				self.BusinessResultsOfReportingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfReportingCompanyLineItems': #提出会社の経営指標等 [表示項目]
				self.BusinessResultsOfReportingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NetSalesSummaryOfBusinessResults': #売上高、経営指標等
				self.NetSalesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RevenueKeyFinancialData': #売上収益、経営指標等
				self.RevenueKeyFinancialData = fact.value

			elif fact.concept.qname.localName == 'OperatingRevenue1SummaryOfBusinessResults': #営業収益、経営指標等
				self.OperatingRevenue1SummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'OperatingRevenue2SummaryOfBusinessResults': #営業収入、経営指標等
				self.OperatingRevenue2SummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'GrossOperatingRevenueSummaryOfBusinessResults': #営業総収入、経営指標等
				self.GrossOperatingRevenueSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'OrdinaryIncomeSummaryOfBusinessResults': #経常収益、経営指標等
				self.OrdinaryIncomeSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetPremiumsWrittenSummaryOfBusinessResultsINS': #正味収入保険料、経営指標等、保険業
				self.NetPremiumsWrittenSummaryOfBusinessResultsINS = fact.value

			elif fact.concept.qname.localName == 'OrdinaryIncomeLossSummaryOfBusinessResults': #経常利益又は経常損失（△）、経営指標等
				self.OrdinaryIncomeLossSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetIncomeLossSummaryOfBusinessResults': #当期純利益又は当期純損失（△）、経営指標等
				self.NetIncomeLossSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetLossRatioSummaryOfBusinessResultsINS': #正味損害率、経営指標等、保険業
				self.NetLossRatioSummaryOfBusinessResultsINS = fact.value

			elif fact.concept.qname.localName == 'NetOperatingExpenseRatioSummaryOfBusinessResultsINS': #正味事業費率、経営指標等、保険業
				self.NetOperatingExpenseRatioSummaryOfBusinessResultsINS = fact.value

			elif fact.concept.qname.localName == 'InterestAndDividendIncomeSummaryOfBusinessResultsINS': #利息及び配当金収入、経営指標等、保険業
				self.InterestAndDividendIncomeSummaryOfBusinessResultsINS = fact.value

			elif fact.concept.qname.localName == 'InvestmentAssetsYieldIncomeYieldSummaryOfBusinessResultsINS': #運用資産利回り（インカム利回り）、経営指標等、保険業
				self.InvestmentAssetsYieldIncomeYieldSummaryOfBusinessResultsINS = fact.value

			elif fact.concept.qname.localName == 'InvestmentYieldRealizedYieldSummaryOfBusinessResultsINS': #資産運用利回り（実現利回り）、経営指標等、保険業
				self.InvestmentYieldRealizedYieldSummaryOfBusinessResultsINS = fact.value

			elif fact.concept.qname.localName == 'EquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSummaryOfBusinessResults': #持分法を適用した場合の投資利益又は投資損失（△）、経営指標等
				self.EquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalStockSummaryOfBusinessResults': #資本金、経営指標等
				self.CapitalStockSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfIssuedSharesSummaryOfBusinessResults': #発行済株式総数（普通株式）、経営指標等
				self.TotalNumberOfIssuedSharesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetAssetsSummaryOfBusinessResults': #純資産額、経営指標等
				self.NetAssetsSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'TotalAssetsSummaryOfBusinessResults': #総資産額、経営指標等
				self.TotalAssetsSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'DepositsSummaryOfBusinessResults': #預金残高、経営指標等
				self.DepositsSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'LoansAndBillsDiscountedSummaryOfBusinessResults': #貸出金残高、経営指標等
				self.LoansAndBillsDiscountedSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'SecuritiesSummaryOfBusinessResults': #有価証券残高、経営指標等
				self.SecuritiesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetAssetsPerShareSummaryOfBusinessResults': #１株当たり純資産額、経営指標等
				self.NetAssetsPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'DividendPaidPerShareSummaryOfBusinessResults': #１株当たり配当額、経営指標等
				self.DividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'InterimDividendPaidPerShareSummaryOfBusinessResults': #１株当たり中間配当額、経営指標等
				self.InterimDividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'FirstQuarterDividendPaidPerShareSummaryOfBusinessResults': #１株当たり第１四半期配当額、経営指標等
				self.FirstQuarterDividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'SecondQuarterDividendPaidPerShareSummaryOfBusinessResults': #１株当たり第２四半期配当額、経営指標等
				self.SecondQuarterDividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ThirdQuarterDividendPaidPerShareSummaryOfBusinessResults': #１株当たり第３四半期配当額、経営指標等
				self.ThirdQuarterDividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'FourthQuarterDividendPaidPerShareSummaryOfBusinessResults': #１株当たり第４四半期配当額、経営指標等
				self.FourthQuarterDividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'FifthQuarterDividendPaidPerShareSummaryOfBusinessResults': #１株当たり第５四半期配当額、経営指標等
				self.FifthQuarterDividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'BasicEarningsLossPerShareSummaryOfBusinessResults': #１株当たり当期純利益又は当期純損失（△）、経営指標等
				self.BasicEarningsLossPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'DilutedEarningsPerShareSummaryOfBusinessResults': #潜在株式調整後１株当たり当期純利益、経営指標等
				self.DilutedEarningsPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityToAssetRatioSummaryOfBusinessResults': #自己資本比率、経営指標等
				self.EquityToAssetRatioSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults': #自己資本比率（国際統一基準）、経営指標等
				self.CapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults': #自己資本比率（国内基準）、経営指標等
				self.CapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalAdequacyRatioBISStandardSummaryOfBusinessResults': #自己資本比率（第一基準）、経営指標等
				self.CapitalAdequacyRatioBISStandardSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults': #自己資本比率（第二基準）、経営指標等
				self.CapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RateOfReturnOnEquitySummaryOfBusinessResults': #自己資本利益率、経営指標等
				self.RateOfReturnOnEquitySummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'PriceEarningsRatioSummaryOfBusinessResults': #株価収益率、経営指標等
				self.PriceEarningsRatioSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'PayoutRatioSummaryOfBusinessResults': #配当性向、経営指標等
				self.PayoutRatioSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults': #営業活動によるキャッシュ・フロー、経営指標等
				self.NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults': #投資活動によるキャッシュ・フロー、経営指標等
				self.NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults': #財務活動によるキャッシュ・フロー、経営指標等
				self.NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashAndCashEquivalentsSummaryOfBusinessResults': #現金及び現金同等物の残高、経営指標等
				self.CashAndCashEquivalentsSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NumberOfEmployees': #従業員数
				self.NumberOfEmployees = fact.value

			elif fact.concept.qname.localName == 'AverageNumberOfTemporaryWorkers': #平均臨時雇用人員
				self.AverageNumberOfTemporaryWorkers = fact.value

			elif fact.concept.qname.localName == 'TotalShareholderReturn': #株主総利回り
				self.TotalShareholderReturn = fact.value

			elif fact.concept.qname.localName == 'TotalReturnOnSharePriceIndex': #株価指数における総利回り
				self.TotalReturnOnSharePriceIndex = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBusinessHeading': #事業の内容 [目次項目]
				self.DescriptionOfBusinessHeading = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBusinessTextBlock': #事業の内容 [テキストブロック]
				self.DescriptionOfBusinessTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutSharesEtcHeading': #株式等の状況 [目次項目]
				self.InformationAboutSharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfSharesEtcHeading': #株式の総数等 [目次項目]
				self.TotalNumberOfSharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfSharesHeading': #株式の総数 [目次項目]
				self.TotalNumberOfSharesHeading = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfSharesTextBlock': #株式の総数 [テキストブロック]
				self.TotalNumberOfSharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesTotalNumberOfSharesEtcHeading': #発行済株式、株式の総数等 [目次項目]
				self.IssuedSharesTotalNumberOfSharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesTotalNumberOfSharesEtcTextBlock': #発行済株式、株式の総数等 [テキストブロック]
				self.IssuedSharesTotalNumberOfSharesEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'SubscriptionRightsToSharesEtcHeading': #新株予約権等の状況 [目次項目]
				self.SubscriptionRightsToSharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'DetailsOfEmployeeShareOptionProgramHeading': #ストックオプション制度の内容 [目次項目]
				self.DetailsOfEmployeeShareOptionProgramHeading = fact.value

			elif fact.concept.qname.localName == 'DetailsOfEmployeeShareOptionProgramTextBlock': #ストックオプション制度の内容 [テキストブロック]
				self.DetailsOfEmployeeShareOptionProgramTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationOnShareAcquisitionRightsHeading': #その他の新株予約権等の状況 [目次項目]
				self.OtherInformationOnShareAcquisitionRightsHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationOnShareAcquisitionRightsTextBlock': #その他の新株予約権等の状況 [テキストブロック]
				self.OtherInformationOnShareAcquisitionRightsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ExercisesEtcOfMovingStrikeConvertibleBondsEtcHeading': #行使価額修正条項付新株予約権付社債券等の行使状況等 [目次項目]
				self.ExercisesEtcOfMovingStrikeConvertibleBondsEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ExercisesEtcOfMovingStrikeConvertibleBondsEtcTextBlock': #行使価額修正条項付新株予約権付社債券等の行使状況等 [テキストブロック]
				self.ExercisesEtcOfMovingStrikeConvertibleBondsEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'ChangesInNumberOfIssuedSharesStatedCapitalEtcHeading': #発行済株式総数、資本金等の推移 [目次項目]
				self.ChangesInNumberOfIssuedSharesStatedCapitalEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ChangesInNumberOfIssuedSharesStatedCapitalEtcTextBlock': #発行済株式総数、資本金等の推移 [テキストブロック]
				self.ChangesInNumberOfIssuedSharesStatedCapitalEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersHeading': #大株主の状況 [目次項目]
				self.MajorShareholdersHeading = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersTextBlock': #大株主の状況 [テキストブロック]
				self.MajorShareholdersTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersHeading': #大株主の状況 [目次項目]
				self.MajorShareholdersHeading = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersTable': #大株主の状況 [表]
				self.MajorShareholdersTable = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersAxis': #大株主 [軸]
				self.MajorShareholdersAxis = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersMember': #大株主 [メンバー] ※ディメンションデフォルト
				self.MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No1MajorShareholdersMember': #第1位、大株主 [メンバー]
				self.No1MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No2MajorShareholdersMember': #第2位、大株主 [メンバー]
				self.No2MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No3MajorShareholdersMember': #第3位、大株主 [メンバー]
				self.No3MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No4MajorShareholdersMember': #第4位、大株主 [メンバー]
				self.No4MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No5MajorShareholdersMember': #第5位、大株主 [メンバー]
				self.No5MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No6MajorShareholdersMember': #第6位、大株主 [メンバー]
				self.No6MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No7MajorShareholdersMember': #第7位、大株主 [メンバー]
				self.No7MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No8MajorShareholdersMember': #第8位、大株主 [メンバー]
				self.No8MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No9MajorShareholdersMember': #第9位、大株主 [メンバー]
				self.No9MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No10MajorShareholdersMember': #第10位、大株主 [メンバー]
				self.No10MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No11MajorShareholdersMember': #第11位、大株主 [メンバー]
				self.No11MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No12MajorShareholdersMember': #第12位、大株主 [メンバー]
				self.No12MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No13MajorShareholdersMember': #第13位、大株主 [メンバー]
				self.No13MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No14MajorShareholdersMember': #第14位、大株主 [メンバー]
				self.No14MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No15MajorShareholdersMember': #第15位、大株主 [メンバー]
				self.No15MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersLineItems': #大株主の状況 [表示項目]
				self.MajorShareholdersLineItems = fact.value

			elif fact.concept.qname.localName == 'NameMajorShareholders': #氏名又は名称、大株主の状況
				self.NameMajorShareholders = fact.value

			elif fact.concept.qname.localName == 'AddressMajorShareholders': #住所、大株主の状況
				self.AddressMajorShareholders = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeld': #所有株式数
				self.NumberOfSharesHeld = fact.value

			elif fact.concept.qname.localName == 'ShareholdingRatio': #発行済株式（自己株式を除く。）の総数に対する所有株式数の割合
				self.ShareholdingRatio = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersHeading': #大株主の状況 [目次項目]
				self.MajorShareholdersHeading = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersVotingRightsTable': #所有株式に係る議決権上位者の状況 [表]
				self.MajorShareholdersVotingRightsTable = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersVotingRightsAxis': #議決権上位 [軸]
				self.MajorShareholdersVotingRightsAxis = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersVotingRightsMember': #議決権上位 [メンバー] ※ディメンションデフォルト
				self.MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No1MajorShareholdersVotingRightsMember': #第1位、議決権上位 [メンバー]
				self.No1MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No2MajorShareholdersVotingRightsMember': #第2位、議決権上位 [メンバー]
				self.No2MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No3MajorShareholdersVotingRightsMember': #第3位、議決権上位 [メンバー]
				self.No3MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No4MajorShareholdersVotingRightsMember': #第4位、議決権上位 [メンバー]
				self.No4MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No5MajorShareholdersVotingRightsMember': #第5位、議決権上位 [メンバー]
				self.No5MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No6MajorShareholdersVotingRightsMember': #第6位、議決権上位 [メンバー]
				self.No6MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No7MajorShareholdersVotingRightsMember': #第7位、議決権上位 [メンバー]
				self.No7MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No8MajorShareholdersVotingRightsMember': #第8位、議決権上位 [メンバー]
				self.No8MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No9MajorShareholdersVotingRightsMember': #第9位、議決権上位 [メンバー]
				self.No9MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No10MajorShareholdersVotingRightsMember': #第10位、議決権上位 [メンバー]
				self.No10MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No11MajorShareholdersVotingRightsMember': #第11位、議決権上位 [メンバー]
				self.No11MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No12MajorShareholdersVotingRightsMember': #第12位、議決権上位 [メンバー]
				self.No12MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No13MajorShareholdersVotingRightsMember': #第13位、議決権上位 [メンバー]
				self.No13MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No14MajorShareholdersVotingRightsMember': #第14位、議決権上位 [メンバー]
				self.No14MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No15MajorShareholdersVotingRightsMember': #第15位、議決権上位 [メンバー]
				self.No15MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersVotingRightsLineItems': #所有株式に係る議決権上位者の状況 [表示項目]
				self.MajorShareholdersVotingRightsLineItems = fact.value

			elif fact.concept.qname.localName == 'NameMajorShareholdersVotingRights': #氏名又は名称、所有株式に係る議決権上位者の状況
				self.NameMajorShareholdersVotingRights = fact.value

			elif fact.concept.qname.localName == 'AddressMajorShareholdersVotingRights': #住所、所有株式に係る議決権上位者の状況
				self.AddressMajorShareholdersVotingRights = fact.value

			elif fact.concept.qname.localName == 'NumberOfVotingRightsHeld': #所有議決権数（個）
				self.NumberOfVotingRightsHeld = fact.value

			elif fact.concept.qname.localName == 'RatioOfVotingRightsHeld': #総株主の議決権に対する所有議決権数の割合
				self.RatioOfVotingRightsHeld = fact.value

			elif fact.concept.qname.localName == 'VotingRightsHeading': #議決権の状況 [目次項目]
				self.VotingRightsHeading = fact.value

			elif fact.concept.qname.localName == 'VotingRightsTextBlock': #議決権の状況 [テキストブロック]
				self.VotingRightsTextBlock = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesVotingRightsHeading': #発行済株式、議決権の状況 [目次項目]
				self.IssuedSharesVotingRightsHeading = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesVotingRightsTextBlock': #発行済株式、議決権の状況 [テキストブロック]
				self.IssuedSharesVotingRightsTextBlock = fact.value

			elif fact.concept.qname.localName == 'TreasurySharesEtcHeading': #自己株式等 [目次項目]
				self.TreasurySharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'TreasurySharesEtcTextBlock': #自己株式等 [テキストブロック]
				self.TreasurySharesEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersTextBlock': #役員の状況 [テキストブロック]
				self.InformationAboutOfficersTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutEmployeesHeading': #従業員の状況 [目次項目]
				self.InformationAboutEmployeesHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutEmployeesTextBlock': #従業員の状況 [テキストブロック]
				self.InformationAboutEmployeesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfBusinessHeading': #事業の状況 [目次項目]
				self.OverviewOfBusinessHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessPolicyBusinessEnvironmentIssuesToAddressEtcHeading': #経営方針、経営環境及び対処すべき課題等 [目次項目]
				self.BusinessPolicyBusinessEnvironmentIssuesToAddressEtcHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock': #経営方針、経営環境及び対処すべき課題等 [テキストブロック]
				self.BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfOperatingResultsEtcHeading': #経営成績等の概要 [目次項目]
				self.OverviewOfOperatingResultsEtcHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfOperatingResultsEtcTextBlock': #経営成績等の概要 [テキストブロック]
				self.OverviewOfOperatingResultsEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'CriticalContractsForOperationHeading': #経営上の重要な契約等 [目次項目]
				self.CriticalContractsForOperationHeading = fact.value

			elif fact.concept.qname.localName == 'CriticalContractsForOperationTextBlock': #経営上の重要な契約等 [テキストブロック]
				self.CriticalContractsForOperationTextBlock = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentActivitiesHeading': #研究開発活動 [目次項目]
				self.ResearchAndDevelopmentActivitiesHeading = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentActivitiesTextBlock': #研究開発活動 [テキストブロック]
				self.ResearchAndDevelopmentActivitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutFacilitiesHeading': #設備の状況 [目次項目]
				self.InformationAboutFacilitiesHeading = fact.value

			elif fact.concept.qname.localName == 'MajorFacilitiesHeading': #主要な設備の状況 [目次項目]
				self.MajorFacilitiesHeading = fact.value

			elif fact.concept.qname.localName == 'MajorFacilitiesTextBlock': #主要な設備の状況 [テキストブロック]
				self.MajorFacilitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlannedAdditionsRetirementsEtcOfFacilitiesHeading': #設備の新設、除却等の計画 [目次項目]
				self.PlannedAdditionsRetirementsEtcOfFacilitiesHeading = fact.value

			elif fact.concept.qname.localName == 'PlannedAdditionsRetirementsEtcOfFacilitiesTextBlock': #設備の新設、除却等の計画 [テキストブロック]
				self.PlannedAdditionsRetirementsEtcOfFacilitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationHeading': #経理の状況 [目次項目]
				self.FinancialInformationHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationHeading': #経理の状況 [目次項目]
				self.FinancialInformationHeading = fact.value

			elif fact.concept.qname.localName == 'RegulationsInAccordanceWithWhichConsolidatedFinancialStatementsHaveBeenPreparedFinancialInformation': #連結財務諸表が基づく規則、経理の状況
				self.RegulationsInAccordanceWithWhichConsolidatedFinancialStatementsHaveBeenPreparedFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'RegulationsInAccordanceWithWhichFinancialStatementsHaveBeenPreparedFinancialInformation': #財務諸表が基づく規則、経理の状況
				self.RegulationsInAccordanceWithWhichFinancialStatementsHaveBeenPreparedFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatCompanyEngagesSpecifiedBusinessAndHasPreparedItsSemiAnnualConsolidatedFinancialStatementsFinancialInformation': #特定事業会社であり、中間連結財務諸表等を作成した場合の記載、経理の状況
				self.DescriptionOfFactThatCompanyEngagesSpecifiedBusinessAndHasPreparedItsSemiAnnualConsolidatedFinancialStatementsFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation': #連結財務諸表が別記事業の特別の法令若しくは準則に基づく場合の記載、経理の状況
				self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation': #財務諸表が別記事業の特別の法令若しくは準則に基づく場合の記載、経理の状況
				self.DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation': #指定国際会計基準により連結財務諸表を作成した場合の記載、経理の状況
				self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithJMISFinancialInformation': #修正国際基準により連結財務諸表を作成した場合の記載、経理の状況
				self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithJMISFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithUSGAAPFinancialInformation': #米国会計基準により連結財務諸表を作成した場合の記載、経理の状況
				self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithUSGAAPFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedFinancialInformation': #連結財務諸表を作成していない場合の記載、経理の状況
				self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedAndFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation': #連結財務諸表を作成していない場合で指定国際会計基準により財務諸表を作成する場合の記載、経理の状況
				self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedAndFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialProvisionFinancialInformation': #特例財務諸表を作成する場合の記載、経理の状況
				self.DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialProvisionFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsStatementOfCashFlowsFinancialInformation': #第１四半期又は第３四半期に係る四半期報告書において四半期キャッシュ・フロー計算書を記載する場合の記載、経理の状況
				self.DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsStatementOfCashFlowsFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsConsolidatedStatementOfCashFlowsFinancialInformation': #第１四半期又は第３四半期に係る四半期報告書において四半期連結キャッシュ・フロー計算書を記載する場合の記載、経理の状況
				self.DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsConsolidatedStatementOfCashFlowsFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodStatementOfIncomeFinancialInformation': #四半期報告書において四半期会計期間に係る四半期損益計算書を記載する場合の記載、経理の状況
				self.DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodStatementOfIncomeFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodConsolidatedStatementOfComprehensiveIncomeFinancialInformation': #四半期報告書において四半期連結会計期間に係る四半期連結損益計算書及び四半期連結包括利益計算書又は四半期連結損益及び包括利益計算書を記載する場合の記載、経理の状況
				self.DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodConsolidatedStatementOfComprehensiveIncomeFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcFinancialInformation': #連結財務諸表等の適正性を確保するための特段の取組み、経理の状況
				self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithIFRSFinancialInformation': #指定国際会計基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
				self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithIFRSFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcAndInternalSystemToPrepareConsolidatedFinancialStatementsEtcFairlyInAccordanceWithIFRSFinancialInformation': #連結財務諸表等の適正性を確保するための特段の取組み及び指定国際会計基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
				self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcAndInternalSystemToPrepareConsolidatedFinancialStatementsEtcFairlyInAccordanceWithIFRSFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithJMISFinancialInformation': #修正国際基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
				self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithJMISFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'NoteOnIndependentAuditFinancialInformation': #監査証明について、経理の状況
				self.NoteOnIndependentAuditFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'NoteOnChangeOfIndependentAuditorsFinancialInformation': #監査人の交代、経理の状況
				self.NoteOnChangeOfIndependentAuditorsFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'NoteOnChangeInFiscalYearEndsFinancialInformation': #決算期変更について、経理の状況
				self.NoteOnChangeInFiscalYearEndsFinancialInformation = fact.value

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

			elif fact.concept.qname.localName == 'NotesSemiAnnualFinancialStatementsHeading': #注記事項、中間財務諸表 [目次項目]
				self.NotesSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernSemiAnnualFinancialStatementsHeading': #継続企業の前提に関する事項、中間財務諸表 [目次項目]
				self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernSemiAnnualFinancialStatementsTextBlock': #継続企業の前提に関する事項、中間財務諸表 [テキストブロック]
				self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantAccountingPoliciesSemiAnnualFinancialStatementsHeading': #重要な会計方針、中間財務諸表 [目次項目]
				self.NotesSignificantAccountingPoliciesSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantAccountingPoliciesSemiAnnualFinancialStatementsTextBlock': #重要な会計方針、中間財務諸表 [テキストブロック]
				self.NotesSignificantAccountingPoliciesSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesSemiAnnualFinancialStatementsHeading': #会計方針の変更、中間財務諸表 [目次項目]
				self.NotesChangesInAccountingPoliciesSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcSemiAnnualFinancialStatementsTextBlock': #会計基準等の改正等に伴う会計方針の変更、中間財務諸表 [テキストブロック]
				self.NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesVoluntaryChangesInAccountingPoliciesSemiAnnualFinancialStatementsTextBlock': #会計基準等の改正等以外の正当な理由による会計方針の変更、中間財務諸表 [テキストブロック]
				self.NotesVoluntaryChangesInAccountingPoliciesSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesSemiAnnualFinancialStatementsTextBlock': #会計上の見積りの変更と区別することが困難な会計方針の変更、中間財務諸表 [テキストブロック]
				self.NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInPresentationSemiAnnualFinancialStatementsHeading': #表示方法の変更、中間財務諸表 [目次項目]
				self.NotesChangesInPresentationSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInPresentationSemiAnnualFinancialStatementsTextBlock': #表示方法の変更、中間財務諸表 [テキストブロック]
				self.NotesChangesInPresentationSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingEstimatesSemiAnnualFinancialStatementsHeading': #会計上の見積りの変更、中間財務諸表 [目次項目]
				self.NotesChangesInAccountingEstimatesSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingEstimatesSemiAnnualFinancialStatementsTextBlock': #会計上の見積りの変更、中間財務諸表 [テキストブロック]
				self.NotesChangesInAccountingEstimatesSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRestatementSemiAnnualFinancialStatementsHeading': #修正再表示、中間財務諸表 [目次項目]
				self.NotesRestatementSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRestatementSemiAnnualFinancialStatementsTextBlock': #修正再表示、中間財務諸表 [テキストブロック]
				self.NotesRestatementSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesAdditionalInformationSemiAnnualFinancialStatementsHeading': #追加情報、中間財務諸表 [目次項目]
				self.NotesAdditionalInformationSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesAdditionalInformationSemiAnnualFinancialStatementsTextBlock': #追加情報、中間財務諸表 [テキストブロック]
				self.NotesAdditionalInformationSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualBalanceSheetHeading': #中間貸借対照表関係 [目次項目]
				self.NotesSemiAnnualBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualBalanceSheetHeading': #中間貸借対照表関係 [目次項目]
				self.NotesSemiAnnualBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualBalanceSheetTable': #中間貸借対照表関係 [表]
				self.NotesSemiAnnualBalanceSheetTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualBalanceSheetLineItems': #中間貸借対照表関係 [表示項目]
				self.NotesSemiAnnualBalanceSheetLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock': #資産の金額から直接控除している引当金の注記 [テキストブロック]
				self.NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsCA': #貸倒引当金、流動資産、一括控除
				self.AllowanceForDoubtfulAccountsCA = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsIOAByGroup': #貸倒引当金、投資その他の資産、一括控除
				self.AllowanceForDoubtfulAccountsIOAByGroup = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsAccountsReceivableTrade': #貸倒引当金、売掛金
				self.AllowanceForDoubtfulAccountsAccountsReceivableTrade = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsLongTermLoansReceivable': #貸倒引当金、長期貸付金
				self.AllowanceForDoubtfulAccountsLongTermLoansReceivable = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther': #貸倒引当金、破産更生債権等
				self.AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock': #有形固定資産の減価償却累計額の注記 [テキストブロック]
				self.NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'AccumulatedDepreciationPPEByGroup': #減価償却累計額、有形固定資産、一括控除
				self.AccumulatedDepreciationPPEByGroup = fact.value

			elif fact.concept.qname.localName == 'AccumulatedDepreciationBuildings': #減価償却累計額、建物
				self.AccumulatedDepreciationBuildings = fact.value

			elif fact.concept.qname.localName == 'AccumulatedDepreciationStructures': #減価償却累計額、構築物
				self.AccumulatedDepreciationStructures = fact.value

			elif fact.concept.qname.localName == 'AccumulatedDepreciationMachineryAndEquipment': #減価償却累計額、機械及び装置
				self.AccumulatedDepreciationMachineryAndEquipment = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock': #有形固定資産の圧縮記帳額の注記 [テキストブロック]
				self.NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock': #減損損失累計額の表示に関する注記 [テキストブロック]
				self.NotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPledgedAssetsTextBlock': #担保に供している資産の注記 [テキストブロック]
				self.NotesRegardingPledgedAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReservesUnderSpecialLawsTextBlock': #特別法上の準備金等に関する注記 [テキストブロック]
				self.NotesRegardingReservesUnderSpecialLawsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock': #棚卸資産及び工事損失引当金の表示に関する注記 [テキストブロック]
				self.NotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingProvisionIncurredFromBusinessCombinationTextBlock': #企業結合に係る特定勘定の注記 [テキストブロック]
				self.NotesRegardingProvisionIncurredFromBusinessCombinationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingGuaranteeObligationsTextBlock': #保証債務の注記 [テキストブロック]
				self.NotesRegardingGuaranteeObligationsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock': #受取手形割引高及び（又は）受取手形裏書譲渡高 [テキストブロック]
				self.NotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock = fact.value

			elif fact.concept.qname.localName == 'DiscountedTradeNotesReceivable': #受取手形割引高
				self.DiscountedTradeNotesReceivable = fact.value

			elif fact.concept.qname.localName == 'TradeNotesReceivableTransferredByEndorsement': #受取手形裏書譲渡高
				self.TradeNotesReceivableTransferredByEndorsement = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock': #指定法人の純資産の記載に関する注記 [テキストブロック]
				self.NotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock': #期末日満期手形の会計処理 [テキストブロック]
				self.NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetAbstract': #貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock': #消費貸借契約及び（又は）消費寄託契約により貸し付けている有価証券に関する注記 [テキストブロック]
				self.NotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock': #自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
				self.NotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock': #有価証券の消費貸借契約・消費寄託契約及び自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
				self.NotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoanParticipationsTextBlock': #ローン・パーティシペーションに関する注記 [テキストブロック]
				self.NotesRegardingLoanParticipationsTextBlock = fact.value

			elif fact.concept.qname.localName == 'CreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock': #当座貸越契約及び（又は）貸出コミットメントに関する貸手の注記 [テキストブロック]
				self.CreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock': #当座貸越契約及び（又は）貸出コミットメントに関する借手の注記 [テキストブロック]
				self.DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock': #関係会社の株式及び（又は）出資金の総額 [テキストブロック]
				self.NotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock': #非連結子会社及び関連会社の株式及び（又は）出資金の総額 [テキストブロック]
				self.NotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSubordinatedBorrowingsTextBlock': #劣後特約付借入金に関する注記 [テキストブロック]
				self.NotesRegardingSubordinatedBorrowingsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSubordinatedBondsPayableTextBlock': #劣後特約付社債に関する注記 [テキストブロック]
				self.NotesRegardingSubordinatedBondsPayableTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock': #資産の部の社債に係る保証債務に関する注記 [テキストブロック]
				self.NotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfBankAbstract': #銀行業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfBankAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock': #銀行法及び金融機能の再生のための緊急措置に関する法律に基づく債権に関する注記、銀行業 [テキストブロック]
				self.NotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock': #銀行業における手形割引に関する注記、銀行業 [テキストブロック]
				self.NotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract': #第一種金融商品取引業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock': #差し入れた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
				self.NotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock': #差し入れを受けた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
				self.NotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfTradingAccountSecuritiesEtcSECTextBlock': #商品有価証券等の内訳、第一種金融商品取引業 [テキストブロック]
				self.BreakdownOfTradingAccountSecuritiesEtcSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfInsuranceAbstract': #保険業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfInsuranceAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock': #保険業法に基づく債権に関する注記、保険業 [テキストブロック]
				self.NotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock': #保険業法第118条に規定する特別勘定の資産及び負債に関する注記、保険業 [テキストブロック]
				self.NotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock': #その他資産に含まれている保険業法第113条に規定する事業費の繰延額の注記 [テキストブロック]
				self.NotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock': #契約者配当準備金の増減異動及び契約者配当金の支払額に関する注記、保険業 [テキストブロック]
				self.NotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock': #保険業法第91条の規定による組織変更剰余金額の注記、保険業 [テキストブロック]
				self.NotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock': #保険業法施行規則第73条第3項において準用する同規則第71条第1項に規定する再保険を付した部分に相当する支払備金の金額の注記、保険業 [テキストブロック]
				self.NotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPolicyReservesReinsuredINSTextBlock': #保険業法施行規則第71条第1項に規定する再保険を付した部分に相当する責任準備金の金額の注記、保険業 [テキストブロック]
				self.NotesRegardingPolicyReservesReinsuredINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock': #保険業法第259条の規定に基づく生命保険契約者保護機構に対する今後の負担見積額、保険業 [テキストブロック]
				self.NotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfOutstandingClaimsINSTextBlock': #支払備金の内訳、保険業 [テキストブロック]
				self.BreakdownOfOutstandingClaimsINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfPolicyReserveINSTextBlock': #責任準備金の内訳、保険業 [テキストブロック]
				self.BreakdownOfPolicyReserveINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract': #特定金融業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingBadLoansSPFTextBlock': #不良債権に関する注記、特定金融業 [テキストブロック]
				self.NotesRegardingBadLoansSPFTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract': #商品先物取引業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract = fact.value

			elif fact.concept.qname.localName == 'ExplanationOfFuturesTransactionMarginCustomerCMDTextBlock': #委託者先物取引差金の説明、商品先物取引業 [テキストブロック]
				self.ExplanationOfFuturesTransactionMarginCustomerCMDTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualStatementOfIncomeHeading': #中間損益計算書関係 [目次項目]
				self.NotesSemiAnnualStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualStatementOfIncomeHeading': #中間損益計算書関係 [目次項目]
				self.NotesSemiAnnualStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualStatementOfIncomeTable': #中間損益計算書関係 [表]
				self.NotesSemiAnnualStatementOfIncomeTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualStatementOfIncomeLineItems': #中間損益計算書関係 [表示項目]
				self.NotesSemiAnnualStatementOfIncomeLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSignificantComponentsOfNonOperatingIncomeTextBlock': #重要な営業外収益の注記 [テキストブロック]
				self.NotesRegardingSignificantComponentsOfNonOperatingIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSignificantComponentsOfNonOperatingExpensesTextBlock': #重要な営業外費用の注記 [テキストブロック]
				self.NotesRegardingSignificantComponentsOfNonOperatingExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSignificantComponentsOfExtraordinaryIncomeTextBlock': #重要な特別利益の注記 [テキストブロック]
				self.NotesRegardingSignificantComponentsOfExtraordinaryIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSignificantComponentsOfExtraordinaryLossesTextBlock': #重要な特別損失の注記 [テキストブロック]
				self.NotesRegardingSignificantComponentsOfExtraordinaryLossesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingImpairmentLossTextBlock': #減損損失に関する注記 [テキストブロック]
				self.NotesRegardingImpairmentLossTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock': #企業結合に係る特定勘定の取崩益の注記 [テキストブロック]
				self.NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatSimplifiedMethodOfTaxEffectAccountingWasAppliedTextBlock': #簡便法による税効果会計を適用している場合の注記 [テキストブロック]
				self.DescriptionOfFactThatSimplifiedMethodOfTaxEffectAccountingWasAppliedTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock': #売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]
				self.NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAmountOfDepreciationTextBlock': #減価償却額の注記 [テキストブロック]
				self.NotesRegardingAmountOfDepreciationTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeAbstract': #損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeAbstract = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfBusinessCostTextBlock': #事業費の内訳 [テキストブロック]
				self.BreakdownOfBusinessCostTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfPersonnelExpensesTextBlock': #人件費の内訳 [テキストブロック]
				self.BreakdownOfPersonnelExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfGainOnSalesOfSecuritiesTextBlock': #有価証券売却益の内訳 [テキストブロック]
				self.BreakdownOfGainOnSalesOfSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfLossOnSalesOfSecuritiesTextBlock': #有価証券売却損の内訳 [テキストブロック]
				self.BreakdownOfLossOnSalesOfSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfLossOnValuationOfSecuritiesTextBlock': #有価証券評価損の内訳 [テキストブロック]
				self.BreakdownOfLossOnValuationOfSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTransactionsWithAffiliatedEntitiesTextBlock': #関係会社との取引に関する注記 [テキストブロック]
				self.NotesRegardingTransactionsWithAffiliatedEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeOfBankAbstract': #銀行業の損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeOfBankAbstract = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherIncomeBNKTextBlock': #その他の経常収益の主要な内訳、銀行業 [テキストブロック]
				self.MajorComponentsOfOtherIncomeBNKTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherExpensesBNKTextBlock': #その他の経常費用の主要な内訳、銀行業 [テキストブロック]
				self.MajorComponentsOfOtherExpensesBNKTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract': #第一種金融商品取引業の損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfNetTradingIncomeSECTextBlock': #トレーディング損益の内訳、第一種金融商品取引業 [テキストブロック]
				self.BreakdownOfNetTradingIncomeSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfFinancialRevenueSECTextBlock': #金融収益の内訳、第一種金融商品取引業 [テキストブロック]
				self.BreakdownOfFinancialRevenueSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfFinancialExpensesSECTextBlock': #金融費用の内訳、第一種金融商品取引業 [テキストブロック]
				self.BreakdownOfFinancialExpensesSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeOfInsuranceAbstract': #保険業の損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeOfInsuranceAbstract = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfBusinessCostTextBlock': #事業費の主な内訳 [テキストブロック]
				self.MajorComponentsOfBusinessCostTextBlock = fact.value

			elif fact.concept.qname.localName == 'AgentFeeEtcINSNonlife': #代理店手数料等、損害保険業
				self.AgentFeeEtcINSNonlife = fact.value

			elif fact.concept.qname.localName == 'SalariesINSNonlife': #給与、損害保険業
				self.SalariesINSNonlife = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfNetPremiumsWrittenINSTextBlock': #正味収入保険料の内訳、保険業 [テキストブロック]
				self.BreakdownOfNetPremiumsWrittenINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfNetClaimsPaidINSTextBlock': #正味支払保険金の内訳、保険業 [テキストブロック]
				self.BreakdownOfNetClaimsPaidINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfCommissionsAndCollectionFeesINSTextBlock': #諸手数料及び集金費の内訳、保険業 [テキストブロック]
				self.BreakdownOfCommissionsAndCollectionFeesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock': #支払備金繰入額又は支払備金戻入額の内訳、保険業 [テキストブロック]
				self.BreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock': #責任準備金繰入額又は責任準備金戻入額の内訳、保険業 [テキストブロック]
				self.BreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock': #支払備金繰入額又は支払備金戻入額の計算上、差し引かれた又は足し上げられた出再支払備金繰入額又は出再支払備金戻入額の注記、保険業 [テキストブロック]
				self.NotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock': #責任準備金繰入額又は責任準備金戻入額の計算上、差し引かれた又は足し上げられた出再責任準備金繰入額又は出再責任準備金戻入額の注記、保険業 [テキストブロック]
				self.NotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock': #利息及び配当金収入の資産源泉別内訳、保険業 [テキストブロック]
				self.BreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'InterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock': #商品有価証券及び売買目的有価証券に係るそれぞれの利息及び配当金収入、売却損益及び評価損益の金額、保険業 [テキストブロック]
				self.InterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock': #金銭の信託に係る評価損益の金額の注記、保険業 [テキストブロック]
				self.NotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingUnrealizedGainLossForDerivativesINSTextBlock': #金融派生商品に係る評価損益の金額の注記、保険業 [テキストブロック]
				self.NotesRegardingUnrealizedGainLossForDerivativesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherExtraordinaryIncomeINSTextBlock': #その他特別利益の主な内訳、保険業 [テキストブロック]
				self.MajorComponentsOfOtherExtraordinaryIncomeINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherExtraordinaryLossesINSTextBlock': #その他特別損失の主な内訳、保険業 [テキストブロック]
				self.MajorComponentsOfOtherExtraordinaryLossesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract': #商品先物取引業の損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfBrokerageIncomeCMDTextBlock': #受取手数料の内訳、商品先物取引業 [テキストブロック]
				self.BreakdownOfBrokerageIncomeCMDTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfNetGainOnTradingCMDTextBlock': #売買損益の内訳、商品先物取引業 [テキストブロック]
				self.BreakdownOfNetGainOnTradingCMDTextBlock = fact.value

			elif fact.concept.qname.localName == 'ExchangeRelatedExpensesCMDTextBlock': #取引所等関係費の内訳、商品先物取引業 [テキストブロック]
				self.ExchangeRelatedExpensesCMDTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualStatementOfChangesInEquityHeading': #中間株主資本等変動計算書関係 [目次項目]
				self.NotesSemiAnnualStatementOfChangesInEquityHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualStatementOfChangesInEquityHeading': #中間株主資本等変動計算書関係 [目次項目]
				self.NotesSemiAnnualStatementOfChangesInEquityHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualStatementOfChangesInEquityTable': #中間株主資本等変動計算書関係 [表]
				self.NotesSemiAnnualStatementOfChangesInEquityTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualStatementOfChangesInEquityLineItems': #中間株主資本等変動計算書関係 [表示項目]
				self.NotesSemiAnnualStatementOfChangesInEquityLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingIssuedSharesAndTreasurySharesTextBlock': #発行済株式及び自己株式に関する注記 [テキストブロック]
				self.NotesRegardingIssuedSharesAndTreasurySharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTreasurySharesTextBlock': #自己株式に関する注記 [テキストブロック]
				self.NotesRegardingTreasurySharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingNewShareSubscriptionRightsEtcTextBlock': #新株予約権等に関する注記 [テキストブロック]
				self.NotesRegardingNewShareSubscriptionRightsEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingDividendTextBlock': #配当に関する注記 [テキストブロック]
				self.NotesRegardingDividendTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualStatementOfCashFlowsHeading': #中間キャッシュ・フロー計算書関係 [目次項目]
				self.NotesSemiAnnualStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualStatementOfCashFlowsHeading': #中間キャッシュ・フロー計算書関係 [目次項目]
				self.NotesSemiAnnualStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualStatementOfCashFlowsTable': #中間キャッシュ・フロー計算書関係 [表]
				self.NotesSemiAnnualStatementOfCashFlowsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSemiAnnualStatementOfCashFlowsLineItems': #中間キャッシュ・フロー計算書関係 [表示項目]
				self.NotesSemiAnnualStatementOfCashFlowsLineItems = fact.value

			elif fact.concept.qname.localName == 'ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock': #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
				self.ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock': #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
				self.DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesLeasesSemiAnnualFinancialStatementsHeading': #リース取引関係、中間財務諸表 [目次項目]
				self.NotesLeasesSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesLeasesSemiAnnualFinancialStatementsTextBlock': #リース取引関係、中間財務諸表 [テキストブロック]
				self.NotesLeasesSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesFinancialInstrumentsSemiAnnualFinancialStatementsHeading': #金融商品関係、中間財務諸表 [目次項目]
				self.NotesFinancialInstrumentsSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesFinancialInstrumentsSemiAnnualFinancialStatementsTextBlock': #金融商品関係、中間財務諸表 [テキストブロック]
				self.NotesFinancialInstrumentsSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSecuritiesSemiAnnualFinancialStatementsHeading': #有価証券関係、中間財務諸表 [目次項目]
				self.NotesSecuritiesSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSecuritiesSemiAnnualFinancialStatementsTextBlock': #有価証券関係、中間財務諸表 [テキストブロック]
				self.NotesSecuritiesSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesMoneyHeldInTrustSemiAnnualFinancialStatementsHeading': #金銭の信託関係、中間財務諸表 [目次項目]
				self.NotesMoneyHeldInTrustSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesMoneyHeldInTrustSemiAnnualFinancialStatementsTextBlock': #金銭の信託関係、中間財務諸表 [テキストブロック]
				self.NotesMoneyHeldInTrustSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesValuationDifferenceOnAvailableForSaleSecuritiesSemiAnnualFinancialStatementsHeading': #その他有価証券評価差額金、中間財務諸表 [目次項目]
				self.NotesValuationDifferenceOnAvailableForSaleSecuritiesSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesValuationDifferenceOnAvailableForSaleSecuritiesSemiAnnualFinancialStatementsTextBlock': #その他有価証券評価差額金、中間財務諸表 [テキストブロック]
				self.NotesValuationDifferenceOnAvailableForSaleSecuritiesSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesDerivativesSemiAnnualFinancialStatementsHeading': #デリバティブ取引関係、中間財務諸表 [目次項目]
				self.NotesDerivativesSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesDerivativesSemiAnnualFinancialStatementsTextBlock': #デリバティブ取引関係、中間財務諸表 [テキストブロック]
				self.NotesDerivativesSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesShareOptionsEtcSemiAnnualFinancialStatementsHeading': #ストック・オプション等関係、中間財務諸表 [目次項目]
				self.NotesShareOptionsEtcSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesShareOptionsEtcSemiAnnualFinancialStatementsTextBlock': #ストック・オプション等関係、中間財務諸表 [テキストブロック]
				self.NotesShareOptionsEtcSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesBusinessCombinationsSemiAnnualFinancialStatementsHeading': #企業結合等関係、中間財務諸表 [目次項目]
				self.NotesBusinessCombinationsSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesBusinessCombinationsSemiAnnualFinancialStatementsTextBlock': #企業結合等関係、中間財務諸表 [テキストブロック]
				self.NotesBusinessCombinationsSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesAssetRetirementObligationsSemiAnnualFinancialStatementsHeading': #資産除去債務関係、中間財務諸表 [目次項目]
				self.NotesAssetRetirementObligationsSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesAssetRetirementObligationsSemiAnnualFinancialStatementsTextBlock': #資産除去債務関係、中間財務諸表 [テキストブロック]
				self.NotesAssetRetirementObligationsSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRealEstateForLeaseEtcSemiAnnualFinancialStatementsHeading': #賃貸等不動産関係、中間財務諸表 [目次項目]
				self.NotesRealEstateForLeaseEtcSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRealEstateForLeaseEtcSemiAnnualFinancialStatementsTextBlock': #賃貸等不動産関係、中間財務諸表 [テキストブロック]
				self.NotesRealEstateForLeaseEtcSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRevenueRecognitionSemiAnnualFinancialStatementsHeading': #収益認識関係、中間財務諸表 [目次項目]
				self.NotesRevenueRecognitionSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRevenueRecognitionSemiAnnualFinancialStatementsTextBlock': #収益認識関係、中間財務諸表 [テキストブロック]
				self.NotesRevenueRecognitionSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesInventoriesSemiAnnualFinancialStatementsHeading': #棚卸資産関係、中間財務諸表 [目次項目]
				self.NotesInventoriesSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesInventoriesSemiAnnualFinancialStatementsTextBlock': #棚卸資産関係、中間財務諸表 [テキストブロック]
				self.NotesInventoriesSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading': #セグメント情報等、中間財務諸表 [目次項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsTextBlock': #セグメント情報等、中間財務諸表 [テキストブロック]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading': #セグメント情報等、中間財務諸表 [目次項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable': #セグメント情報等、中間財務諸表 [表]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems': #セグメント情報等、中間財務諸表 [表示項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfReportableSegmentsTextBlock': #報告セグメントの概要 [テキストブロック]
				self.DescriptionOfReportableSegmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfChangesInReportableSegmentsTextBlock': #報告セグメントの変更に関する事項 [テキストブロック]
				self.DisclosureOfChangesInReportableSegmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatCompanysBusinessComprisesSingleSegment': #単一セグメントである旨
				self.DescriptionOfFactThatCompanysBusinessComprisesSingleSegment = fact.value

			elif fact.concept.qname.localName == 'ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock': #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]
				self.ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading': #セグメント情報等、中間財務諸表 [目次項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable': #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表]
				self.DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'TotalOfReportableSegmentsAndOthersMember': #報告セグメント及びその他の合計 [メンバー]
				self.TotalOfReportableSegmentsAndOthersMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'ReconcilingItemsMember': #調整項目 [メンバー]
				self.ReconcilingItemsMember = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems': #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表示項目]
				self.DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'SalesSegmentInformationAbstract': #売上高、セグメント情報 [タイトル項目]
				self.SalesSegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'RevenuesFromExternalCustomers': #外部顧客への売上高
				self.RevenuesFromExternalCustomers = fact.value

			elif fact.concept.qname.localName == 'TransactionsWithOtherSegments': #セグメント間の内部売上高又は振替高
				self.TransactionsWithOtherSegments = fact.value

			elif fact.concept.qname.localName == 'NetSales': #売上高
				self.NetSales = fact.value

			elif fact.concept.qname.localName == 'OperatingRevenue1': #営業収益
				self.OperatingRevenue1 = fact.value

			elif fact.concept.qname.localName == 'OperatingRevenue2': #営業収入
				self.OperatingRevenue2 = fact.value

			elif fact.concept.qname.localName == 'GrossOperatingRevenue': #営業総収入
				self.GrossOperatingRevenue = fact.value

			elif fact.concept.qname.localName == 'OrdinaryIncomeBNK': #経常収益、銀行業
				self.OrdinaryIncomeBNK = fact.value

			elif fact.concept.qname.localName == 'OperatingIncomeINS': #経常収益、保険業
				self.OperatingIncomeINS = fact.value

			elif fact.concept.qname.localName == 'SegmentProfitLossAbstract': #セグメント利益又は損失（△） [タイトル項目]
				self.SegmentProfitLossAbstract = fact.value

			elif fact.concept.qname.localName == 'OperatingIncome': #営業利益又は営業損失（△）
				self.OperatingIncome = fact.value

			elif fact.concept.qname.localName == 'OrdinaryIncome': #経常利益又は経常損失（△）
				self.OrdinaryIncome = fact.value

			elif fact.concept.qname.localName == 'IncomeBeforeIncomeTaxes': #税引前当期純利益又は税引前当期純損失（△）
				self.IncomeBeforeIncomeTaxes = fact.value

			elif fact.concept.qname.localName == 'ProfitLoss': #当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）
				self.ProfitLoss = fact.value

			elif fact.concept.qname.localName == 'Assets': #資産
				self.Assets = fact.value

			elif fact.concept.qname.localName == 'Liabilities': #負債
				self.Liabilities = fact.value

			elif fact.concept.qname.localName == 'OtherItemsSegmentInformationAbstract': #その他の項目、セグメント情報 [タイトル項目]
				self.OtherItemsSegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'DepreciationSegmentInformation': #減価償却費、セグメント情報
				self.DepreciationSegmentInformation = fact.value

			elif fact.concept.qname.localName == 'AmortizationOfGoodwillSGA': #のれん償却額、販売費及び一般管理費
				self.AmortizationOfGoodwillSGA = fact.value

			elif fact.concept.qname.localName == 'InterestIncomeNOI': #受取利息、営業外収益
				self.InterestIncomeNOI = fact.value

			elif fact.concept.qname.localName == 'InterestExpensesNOE': #支払利息、営業外費用
				self.InterestExpensesNOE = fact.value

			elif fact.concept.qname.localName == 'ExtraordinaryIncome': #特別利益
				self.ExtraordinaryIncome = fact.value

			elif fact.concept.qname.localName == 'GainOnNegativeGoodwillEI': #負ののれん発生益、特別利益
				self.GainOnNegativeGoodwillEI = fact.value

			elif fact.concept.qname.localName == 'ExtraordinaryLoss': #特別損失
				self.ExtraordinaryLoss = fact.value

			elif fact.concept.qname.localName == 'ImpairmentLossEL': #減損損失、特別損失
				self.ImpairmentLossEL = fact.value

			elif fact.concept.qname.localName == 'IncomeTaxExpense': #税金費用
				self.IncomeTaxExpense = fact.value

			elif fact.concept.qname.localName == 'IncreaseInPropertyPlantAndEquipmentAndIntangibleAssets': #有形固定資産及び無形固定資産の増加額
				self.IncreaseInPropertyPlantAndEquipmentAndIntangibleAssets = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading': #セグメント情報等、中間財務諸表 [目次項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable': #セグメント情報等、中間財務諸表 [表]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems': #セグメント情報等、中間財務諸表 [表示項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'FootnotesRegardingSegmentInformationTableTextBlock': #セグメント表の脚注 [テキストブロック]
				self.FootnotesRegardingSegmentInformationTableTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock': #報告セグメント合計額と財務諸表計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
				self.DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesInformationAssociatedWithReportableSegmentsAbstract': #関連情報 [タイトル項目]
				self.NotesInformationAssociatedWithReportableSegmentsAbstract = fact.value

			elif fact.concept.qname.localName == 'InformationForEachProductOrServiceTextBlock': #製品及びサービスごとの情報 [テキストブロック]
				self.InformationForEachProductOrServiceTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationForEachRegionAbstract': #地域ごとの情報 [タイトル項目]
				self.InformationForEachRegionAbstract = fact.value

			elif fact.concept.qname.localName == 'RevenuesFromExternalCustomersInformationForEachRegionTextBlock': #売上高、地域ごとの情報 [テキストブロック]
				self.RevenuesFromExternalCustomersInformationForEachRegionTextBlock = fact.value

			elif fact.concept.qname.localName == 'PropertyPlantAndEquipmentInformationForEachRegionTextBlock': #有形固定資産、地域ごとの情報 [テキストブロック]
				self.PropertyPlantAndEquipmentInformationForEachRegionTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationForEachOfMainCustomersTextBlock': #主要な顧客ごとの情報 [テキストブロック]
				self.InformationForEachOfMainCustomersTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading': #セグメント情報等、中間財務諸表 [目次項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract': #報告セグメントごとの固定資産の減損損失に関する情報 [タイトル項目]
				self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable': #報告セグメントごとの固定資産の減損損失に関する情報 [表]
				self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'UnallocatedAmountsAndEliminationMember': #全社・消去 [メンバー]
				self.UnallocatedAmountsAndEliminationMember = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems': #報告セグメントごとの固定資産の減損損失に関する情報 [表示項目]
				self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'ImpairmentLossEL': #減損損失、特別損失
				self.ImpairmentLossEL = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading': #セグメント情報等、中間財務諸表 [目次項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable': #セグメント情報等、中間財務諸表 [表]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems': #セグメント情報等、中間財務諸表 [表示項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfImpairmentLossNotAllocatedToReportableSegments': #報告セグメントに配分されていない減損損失の内容
				self.DescriptionOfImpairmentLossNotAllocatedToReportableSegments = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading': #セグメント情報等、中間財務諸表 [目次項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract': #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [タイトル項目]
				self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable': #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表]
				self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'UnallocatedAmountsAndEliminationMember': #全社・消去 [メンバー]
				self.UnallocatedAmountsAndEliminationMember = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems': #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表示項目]
				self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'AmortizationOfGoodwillSGA': #のれん償却額、販売費及び一般管理費
				self.AmortizationOfGoodwillSGA = fact.value

			elif fact.concept.qname.localName == 'Goodwill': #のれん
				self.Goodwill = fact.value

			elif fact.concept.qname.localName == 'GoodwillBeforeOffsetting': #のれん（相殺前）
				self.GoodwillBeforeOffsetting = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading': #セグメント情報等、中間財務諸表 [目次項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract': #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [タイトル項目]
				self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable': #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表]
				self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'UnallocatedAmountsAndEliminationMember': #全社・消去 [メンバー]
				self.UnallocatedAmountsAndEliminationMember = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems': #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表示項目]
				self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'AmortizationOfNegativeGoodwillNOI': #負ののれん償却額、営業外収益
				self.AmortizationOfNegativeGoodwillNOI = fact.value

			elif fact.concept.qname.localName == 'NegativeGoodwill': #負ののれん
				self.NegativeGoodwill = fact.value

			elif fact.concept.qname.localName == 'NegativeGoodwillBeforeOffsetting': #負ののれん（相殺前）
				self.NegativeGoodwillBeforeOffsetting = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading': #セグメント情報等、中間財務諸表 [目次項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable': #セグメント情報等、中間財務諸表 [表]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems': #セグメント情報等、中間財務諸表 [表示項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments': #報告セグメントに配分されていないのれんの償却額又は未償却残高の内容
				self.DescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading': #セグメント情報等、中間財務諸表 [目次項目]
				self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGainOnBargainPurchaseForEachReportableSegmentTable': #報告セグメントごとの負ののれん発生益に関する情報 [表]
				self.InformationAboutGainOnBargainPurchaseForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'UnallocatedAmountsAndEliminationMember': #全社・消去 [メンバー]
				self.UnallocatedAmountsAndEliminationMember = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems': #報告セグメントごとの負ののれん発生益に関する情報 [表示項目]
				self.InformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock': #報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]
				self.DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSemiAnnualFinancialStatementsHeading': #持分法損益等、中間財務諸表 [目次項目]
				self.NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSemiAnnualFinancialStatementsTextBlock': #持分法損益等、中間財務諸表 [テキストブロック]
				self.NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSpecialPurposeEntitiesSubjectToDisclosureSemiAnnualFinancialStatementsHeading': #開示対象特別目的会社関係、中間財務諸表 [目次項目]
				self.NotesSpecialPurposeEntitiesSubjectToDisclosureSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSpecialPurposeEntitiesSubjectToDisclosureSemiAnnualFinancialStatementsTextBlock': #開示対象特別目的会社関係、中間財務諸表 [テキストブロック]
				self.NotesSpecialPurposeEntitiesSubjectToDisclosureSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesPerShareInformationSemiAnnualFinancialStatementsHeading': #１株当たり情報、中間財務諸表 [目次項目]
				self.NotesPerShareInformationSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesPerShareInformationSemiAnnualFinancialStatementsTextBlock': #１株当たり情報、中間財務諸表 [テキストブロック]
				self.NotesPerShareInformationSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantEventsAfterReportingPeriodSemiAnnualFinancialStatementsHeading': #重要な後発事象、中間財務諸表 [目次項目]
				self.NotesSignificantEventsAfterReportingPeriodSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantEventsAfterReportingPeriodSemiAnnualFinancialStatementsTextBlock': #重要な後発事象、中間財務諸表 [テキストブロック]
				self.NotesSignificantEventsAfterReportingPeriodSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationFinancialStatementsEtcHeading': #その他、財務諸表等 [目次項目]
				self.OtherInformationFinancialStatementsEtcHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationFinancialStatementsEtcTextBlock': #その他、財務諸表等 [テキストブロック]
				self.OtherInformationFinancialStatementsEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReferenceInformationOfReportingCompanyHeading': #提出会社の参考情報 [目次項目]
				self.ReferenceInformationOfReportingCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'ReferenceInformationOfReportingCompanyTextBlock': #提出会社の参考情報 [テキストブロック]
				self.ReferenceInformationOfReportingCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutAffiliatedEntitiesHeading': #関係会社の情報 [目次項目]
				self.InformationAboutAffiliatedEntitiesHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutAffiliatedEntitiesTextBlock': #関係会社の情報 [テキストブロック]
				self.InformationAboutAffiliatedEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyHeading': #提出会社の保証会社等の情報 [目次項目]
				self.InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyTextBlock': #提出会社の保証会社等の情報 [テキストブロック]
				self.InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGuaranteeCompanyHeading': #保証会社情報 [目次項目]
				self.InformationAboutGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGuaranteeCompanyTextBlock': #保証会社情報 [テキストブロック]
				self.InformationAboutGuaranteeCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'CorporateBondsUnderGuaranteeHeading': #保証の対象となっている社債 [目次項目]
				self.CorporateBondsUnderGuaranteeHeading = fact.value

			elif fact.concept.qname.localName == 'CorporateBondsUnderGuaranteeTextBlock': #保証の対象となっている社債 [テキストブロック]
				self.CorporateBondsUnderGuaranteeTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGuaranteeCompanySubjectToOngoingDisclosureHeading': #継続開示会社たる保証会社に関する事項 [目次項目]
				self.InformationAboutGuaranteeCompanySubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGuaranteeCompanySubjectToOngoingDisclosureTextBlock': #継続開示会社たる保証会社に関する事項 [テキストブロック]
				self.InformationAboutGuaranteeCompanySubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'DocumentsSubmittedByGuaranteeCompanyHeading': #保証会社が提出した書類 [目次項目]
				self.DocumentsSubmittedByGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading': #有価証券報告書及びその添付書類又は四半期報告書若しくは半期報告書、保証会社が提出した書類 [目次項目]
				self.AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock': #有価証券報告書及びその添付書類又は四半期報告書若しくは半期報告書、保証会社が提出した書類 [テキストブロック]
				self.AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading': #臨時報告書、保証会社が提出した書類 [目次項目]
				self.ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock': #臨時報告書、保証会社が提出した書類 [テキストブロック]
				self.ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'AmendmentReportDocumentsSubmittedByGuaranteeCompanyHeading': #訂正報告書、保証会社が提出した書類 [目次項目]
				self.AmendmentReportDocumentsSubmittedByGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'AmendmentReportDocumentsSubmittedByGuaranteeCompanyTextBlock': #訂正報告書、保証会社が提出した書類 [テキストブロック]
				self.AmendmentReportDocumentsSubmittedByGuaranteeCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyHeading': #上記書類を縦覧に供している場所、保証会社が提出した書類 [目次項目]
				self.PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyTextBlock': #上記書類を縦覧に供している場所、保証会社が提出した書類 [テキストブロック]
				self.PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading': #継続開示会社に該当しない保証会社に関する事項 [目次項目]
				self.InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock': #継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
				self.InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterHeading': #会社名・代表者の役職氏名及び本店の所在の場所 [目次項目]
				self.CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterHeading = fact.value

			elif fact.concept.qname.localName == 'CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterTextBlock': #会社名・代表者の役職氏名及び本店の所在の場所 [テキストブロック]
				self.CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading': #企業の概況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
				self.OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock': #企業の概況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
				self.OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading': #事業の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
				self.OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock': #事業の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
				self.OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading': #設備の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
				self.InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock': #設備の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
				self.InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading': #保証会社の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
				self.GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock': #保証会社の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
				self.GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading': #経理の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
				self.FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock': #経理の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
				self.FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompaniesOtherThanGuaranteeCompanyHeading': #保証会社以外の会社の情報 [目次項目]
				self.InformationAboutCompaniesOtherThanGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompaniesOtherThanGuaranteeCompanyTextBlock': #保証会社以外の会社の情報 [テキストブロック]
				self.InformationAboutCompaniesOtherThanGuaranteeCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReasonForDisclosureOfInformationOfCompanyConcernedHeading': #当該会社の情報の開示を必要とする理由 [目次項目]
				self.ReasonForDisclosureOfInformationOfCompanyConcernedHeading = fact.value

			elif fact.concept.qname.localName == 'ReasonForDisclosureOfInformationOfCompanyConcernedTextBlock': #当該会社の情報の開示を必要とする理由 [テキストブロック]
				self.ReasonForDisclosureOfInformationOfCompanyConcernedTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompanyConcernedSubjectToOngoingDisclosureHeading': #継続開示会社たる当該会社に関する事項 [目次項目]
				self.InformationAboutCompanyConcernedSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompanyConcernedSubjectToOngoingDisclosureTextBlock': #継続開示会社たる当該会社に関する事項 [テキストブロック]
				self.InformationAboutCompanyConcernedSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureHeading': #継続開示会社に該当しない当該会社に関する事項 [目次項目]
				self.InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureTextBlock': #継続開示会社に該当しない当該会社に関する事項 [テキストブロック]
				self.InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIndexEtcHeading': #指数等の情報 [目次項目]
				self.InformationAboutIndexEtcHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIndexEtcTextBlock': #指数等の情報 [テキストブロック]
				self.InformationAboutIndexEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReasonForDisclosureOfSaidIndexEtcHeading': #当該指数等の情報の開示を必要とする理由 [目次項目]
				self.ReasonForDisclosureOfSaidIndexEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ReasonForDisclosureOfSaidIndexEtcTextBlock': #当該指数等の情報の開示を必要とする理由 [テキストブロック]
				self.ReasonForDisclosureOfSaidIndexEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfIndexEtcHeading': #当該指数等の推移 [目次項目]
				self.HistoricalRecordsOfIndexEtcHeading = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfIndexEtcTextBlock': #当該指数等の推移 [テキストブロック]
				self.HistoricalRecordsOfIndexEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportHeading': #独立監査人の報告書 [目次項目]
				self.IndependentAuditorsReportHeading = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportConsolidatedTextBlock': #独立監査人の報告書、連結 [テキストブロック]
				self.IndependentAuditorsReportConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportNonConsolidatedTextBlock': #独立監査人の報告書、個別 [テキストブロック]
				self.IndependentAuditorsReportNonConsolidatedTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo52SemiannualSecuritiesReportHeading(self): #企業内容等の開示に関する内閣府令 第五号の二様式 半期報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo52SemiannualSecuritiesReportHeading

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

	def getSemiAnnualAccountingPeriodCoverPage(self): #中間会計期間、表紙
		return self.SemiAnnualAccountingPeriodCoverPage

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

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getFootnotesCoverPageTextBlock(self): #脚注、表紙 [テキストブロック]
		return self.FootnotesCoverPageTextBlock

	def getCompanyInformationHeading(self): #企業情報 [目次項目]
		return self.CompanyInformationHeading

	def getOverviewOfCompanyHeading(self): #企業の概況 [目次項目]
		return self.OverviewOfCompanyHeading

	def getSummaryOfBusinessResultsHeading(self): #主要な経営指標等の推移 [目次項目]
		return self.SummaryOfBusinessResultsHeading

	def getBusinessResultsOfReportingCompanyHeading(self): #提出会社の経営指標等 [目次項目]
		return self.BusinessResultsOfReportingCompanyHeading

	def getBusinessResultsOfReportingCompanyTextBlock(self): #提出会社の経営指標等 [テキストブロック]
		return self.BusinessResultsOfReportingCompanyTextBlock

	def getBusinessResultsOfReportingCompanyHeading(self): #提出会社の経営指標等 [目次項目]
		return self.BusinessResultsOfReportingCompanyHeading

	def getBusinessResultsOfReportingCompanyTable(self): #提出会社の経営指標等 [表]
		return self.BusinessResultsOfReportingCompanyTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getBusinessResultsOfReportingCompanyLineItems(self): #提出会社の経営指標等 [表示項目]
		return self.BusinessResultsOfReportingCompanyLineItems

	def getNetSalesSummaryOfBusinessResults(self): #売上高、経営指標等
		return self.NetSalesSummaryOfBusinessResults

	def getRevenueKeyFinancialData(self): #売上収益、経営指標等
		return self.RevenueKeyFinancialData

	def getOperatingRevenue1SummaryOfBusinessResults(self): #営業収益、経営指標等
		return self.OperatingRevenue1SummaryOfBusinessResults

	def getOperatingRevenue2SummaryOfBusinessResults(self): #営業収入、経営指標等
		return self.OperatingRevenue2SummaryOfBusinessResults

	def getGrossOperatingRevenueSummaryOfBusinessResults(self): #営業総収入、経営指標等
		return self.GrossOperatingRevenueSummaryOfBusinessResults

	def getOrdinaryIncomeSummaryOfBusinessResults(self): #経常収益、経営指標等
		return self.OrdinaryIncomeSummaryOfBusinessResults

	def getNetPremiumsWrittenSummaryOfBusinessResultsINS(self): #正味収入保険料、経営指標等、保険業
		return self.NetPremiumsWrittenSummaryOfBusinessResultsINS

	def getOrdinaryIncomeLossSummaryOfBusinessResults(self): #経常利益又は経常損失（△）、経営指標等
		return self.OrdinaryIncomeLossSummaryOfBusinessResults

	def getNetIncomeLossSummaryOfBusinessResults(self): #当期純利益又は当期純損失（△）、経営指標等
		return self.NetIncomeLossSummaryOfBusinessResults

	def getNetLossRatioSummaryOfBusinessResultsINS(self): #正味損害率、経営指標等、保険業
		return self.NetLossRatioSummaryOfBusinessResultsINS

	def getNetOperatingExpenseRatioSummaryOfBusinessResultsINS(self): #正味事業費率、経営指標等、保険業
		return self.NetOperatingExpenseRatioSummaryOfBusinessResultsINS

	def getInterestAndDividendIncomeSummaryOfBusinessResultsINS(self): #利息及び配当金収入、経営指標等、保険業
		return self.InterestAndDividendIncomeSummaryOfBusinessResultsINS

	def getInvestmentAssetsYieldIncomeYieldSummaryOfBusinessResultsINS(self): #運用資産利回り（インカム利回り）、経営指標等、保険業
		return self.InvestmentAssetsYieldIncomeYieldSummaryOfBusinessResultsINS

	def getInvestmentYieldRealizedYieldSummaryOfBusinessResultsINS(self): #資産運用利回り（実現利回り）、経営指標等、保険業
		return self.InvestmentYieldRealizedYieldSummaryOfBusinessResultsINS

	def getEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSummaryOfBusinessResults(self): #持分法を適用した場合の投資利益又は投資損失（△）、経営指標等
		return self.EquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSummaryOfBusinessResults

	def getCapitalStockSummaryOfBusinessResults(self): #資本金、経営指標等
		return self.CapitalStockSummaryOfBusinessResults

	def getTotalNumberOfIssuedSharesSummaryOfBusinessResults(self): #発行済株式総数（普通株式）、経営指標等
		return self.TotalNumberOfIssuedSharesSummaryOfBusinessResults

	def getNetAssetsSummaryOfBusinessResults(self): #純資産額、経営指標等
		return self.NetAssetsSummaryOfBusinessResults

	def getTotalAssetsSummaryOfBusinessResults(self): #総資産額、経営指標等
		return self.TotalAssetsSummaryOfBusinessResults

	def getDepositsSummaryOfBusinessResults(self): #預金残高、経営指標等
		return self.DepositsSummaryOfBusinessResults

	def getLoansAndBillsDiscountedSummaryOfBusinessResults(self): #貸出金残高、経営指標等
		return self.LoansAndBillsDiscountedSummaryOfBusinessResults

	def getSecuritiesSummaryOfBusinessResults(self): #有価証券残高、経営指標等
		return self.SecuritiesSummaryOfBusinessResults

	def getNetAssetsPerShareSummaryOfBusinessResults(self): #１株当たり純資産額、経営指標等
		return self.NetAssetsPerShareSummaryOfBusinessResults

	def getDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり配当額、経営指標等
		return self.DividendPaidPerShareSummaryOfBusinessResults

	def getInterimDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり中間配当額、経営指標等
		return self.InterimDividendPaidPerShareSummaryOfBusinessResults

	def getFirstQuarterDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり第１四半期配当額、経営指標等
		return self.FirstQuarterDividendPaidPerShareSummaryOfBusinessResults

	def getSecondQuarterDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり第２四半期配当額、経営指標等
		return self.SecondQuarterDividendPaidPerShareSummaryOfBusinessResults

	def getThirdQuarterDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり第３四半期配当額、経営指標等
		return self.ThirdQuarterDividendPaidPerShareSummaryOfBusinessResults

	def getFourthQuarterDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり第４四半期配当額、経営指標等
		return self.FourthQuarterDividendPaidPerShareSummaryOfBusinessResults

	def getFifthQuarterDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり第５四半期配当額、経営指標等
		return self.FifthQuarterDividendPaidPerShareSummaryOfBusinessResults

	def getBasicEarningsLossPerShareSummaryOfBusinessResults(self): #１株当たり当期純利益又は当期純損失（△）、経営指標等
		return self.BasicEarningsLossPerShareSummaryOfBusinessResults

	def getDilutedEarningsPerShareSummaryOfBusinessResults(self): #潜在株式調整後１株当たり当期純利益、経営指標等
		return self.DilutedEarningsPerShareSummaryOfBusinessResults

	def getEquityToAssetRatioSummaryOfBusinessResults(self): #自己資本比率、経営指標等
		return self.EquityToAssetRatioSummaryOfBusinessResults

	def getCapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults(self): #自己資本比率（国際統一基準）、経営指標等
		return self.CapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults

	def getCapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults(self): #自己資本比率（国内基準）、経営指標等
		return self.CapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults

	def getCapitalAdequacyRatioBISStandardSummaryOfBusinessResults(self): #自己資本比率（第一基準）、経営指標等
		return self.CapitalAdequacyRatioBISStandardSummaryOfBusinessResults

	def getCapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults(self): #自己資本比率（第二基準）、経営指標等
		return self.CapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults

	def getRateOfReturnOnEquitySummaryOfBusinessResults(self): #自己資本利益率、経営指標等
		return self.RateOfReturnOnEquitySummaryOfBusinessResults

	def getPriceEarningsRatioSummaryOfBusinessResults(self): #株価収益率、経営指標等
		return self.PriceEarningsRatioSummaryOfBusinessResults

	def getPayoutRatioSummaryOfBusinessResults(self): #配当性向、経営指標等
		return self.PayoutRatioSummaryOfBusinessResults

	def getNetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults(self): #営業活動によるキャッシュ・フロー、経営指標等
		return self.NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults

	def getNetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults(self): #投資活動によるキャッシュ・フロー、経営指標等
		return self.NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults

	def getNetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults(self): #財務活動によるキャッシュ・フロー、経営指標等
		return self.NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults

	def getCashAndCashEquivalentsSummaryOfBusinessResults(self): #現金及び現金同等物の残高、経営指標等
		return self.CashAndCashEquivalentsSummaryOfBusinessResults

	def getNumberOfEmployees(self): #従業員数
		return self.NumberOfEmployees

	def getAverageNumberOfTemporaryWorkers(self): #平均臨時雇用人員
		return self.AverageNumberOfTemporaryWorkers

	def getTotalShareholderReturn(self): #株主総利回り
		return self.TotalShareholderReturn

	def getTotalReturnOnSharePriceIndex(self): #株価指数における総利回り
		return self.TotalReturnOnSharePriceIndex

	def getDescriptionOfBusinessHeading(self): #事業の内容 [目次項目]
		return self.DescriptionOfBusinessHeading

	def getDescriptionOfBusinessTextBlock(self): #事業の内容 [テキストブロック]
		return self.DescriptionOfBusinessTextBlock

	def getInformationAboutSharesEtcHeading(self): #株式等の状況 [目次項目]
		return self.InformationAboutSharesEtcHeading

	def getTotalNumberOfSharesEtcHeading(self): #株式の総数等 [目次項目]
		return self.TotalNumberOfSharesEtcHeading

	def getTotalNumberOfSharesHeading(self): #株式の総数 [目次項目]
		return self.TotalNumberOfSharesHeading

	def getTotalNumberOfSharesTextBlock(self): #株式の総数 [テキストブロック]
		return self.TotalNumberOfSharesTextBlock

	def getIssuedSharesTotalNumberOfSharesEtcHeading(self): #発行済株式、株式の総数等 [目次項目]
		return self.IssuedSharesTotalNumberOfSharesEtcHeading

	def getIssuedSharesTotalNumberOfSharesEtcTextBlock(self): #発行済株式、株式の総数等 [テキストブロック]
		return self.IssuedSharesTotalNumberOfSharesEtcTextBlock

	def getSubscriptionRightsToSharesEtcHeading(self): #新株予約権等の状況 [目次項目]
		return self.SubscriptionRightsToSharesEtcHeading

	def getDetailsOfEmployeeShareOptionProgramHeading(self): #ストックオプション制度の内容 [目次項目]
		return self.DetailsOfEmployeeShareOptionProgramHeading

	def getDetailsOfEmployeeShareOptionProgramTextBlock(self): #ストックオプション制度の内容 [テキストブロック]
		return self.DetailsOfEmployeeShareOptionProgramTextBlock

	def getOtherInformationOnShareAcquisitionRightsHeading(self): #その他の新株予約権等の状況 [目次項目]
		return self.OtherInformationOnShareAcquisitionRightsHeading

	def getOtherInformationOnShareAcquisitionRightsTextBlock(self): #その他の新株予約権等の状況 [テキストブロック]
		return self.OtherInformationOnShareAcquisitionRightsTextBlock

	def getExercisesEtcOfMovingStrikeConvertibleBondsEtcHeading(self): #行使価額修正条項付新株予約権付社債券等の行使状況等 [目次項目]
		return self.ExercisesEtcOfMovingStrikeConvertibleBondsEtcHeading

	def getExercisesEtcOfMovingStrikeConvertibleBondsEtcTextBlock(self): #行使価額修正条項付新株予約権付社債券等の行使状況等 [テキストブロック]
		return self.ExercisesEtcOfMovingStrikeConvertibleBondsEtcTextBlock

	def getChangesInNumberOfIssuedSharesStatedCapitalEtcHeading(self): #発行済株式総数、資本金等の推移 [目次項目]
		return self.ChangesInNumberOfIssuedSharesStatedCapitalEtcHeading

	def getChangesInNumberOfIssuedSharesStatedCapitalEtcTextBlock(self): #発行済株式総数、資本金等の推移 [テキストブロック]
		return self.ChangesInNumberOfIssuedSharesStatedCapitalEtcTextBlock

	def getMajorShareholdersHeading(self): #大株主の状況 [目次項目]
		return self.MajorShareholdersHeading

	def getMajorShareholdersTextBlock(self): #大株主の状況 [テキストブロック]
		return self.MajorShareholdersTextBlock

	def getMajorShareholdersHeading(self): #大株主の状況 [目次項目]
		return self.MajorShareholdersHeading

	def getMajorShareholdersTable(self): #大株主の状況 [表]
		return self.MajorShareholdersTable

	def getMajorShareholdersAxis(self): #大株主 [軸]
		return self.MajorShareholdersAxis

	def getMajorShareholdersMember(self): #大株主 [メンバー] ※ディメンションデフォルト
		return self.MajorShareholdersMember

	def getNo1MajorShareholdersMember(self): #第1位、大株主 [メンバー]
		return self.No1MajorShareholdersMember

	def getNo2MajorShareholdersMember(self): #第2位、大株主 [メンバー]
		return self.No2MajorShareholdersMember

	def getNo3MajorShareholdersMember(self): #第3位、大株主 [メンバー]
		return self.No3MajorShareholdersMember

	def getNo4MajorShareholdersMember(self): #第4位、大株主 [メンバー]
		return self.No4MajorShareholdersMember

	def getNo5MajorShareholdersMember(self): #第5位、大株主 [メンバー]
		return self.No5MajorShareholdersMember

	def getNo6MajorShareholdersMember(self): #第6位、大株主 [メンバー]
		return self.No6MajorShareholdersMember

	def getNo7MajorShareholdersMember(self): #第7位、大株主 [メンバー]
		return self.No7MajorShareholdersMember

	def getNo8MajorShareholdersMember(self): #第8位、大株主 [メンバー]
		return self.No8MajorShareholdersMember

	def getNo9MajorShareholdersMember(self): #第9位、大株主 [メンバー]
		return self.No9MajorShareholdersMember

	def getNo10MajorShareholdersMember(self): #第10位、大株主 [メンバー]
		return self.No10MajorShareholdersMember

	def getNo11MajorShareholdersMember(self): #第11位、大株主 [メンバー]
		return self.No11MajorShareholdersMember

	def getNo12MajorShareholdersMember(self): #第12位、大株主 [メンバー]
		return self.No12MajorShareholdersMember

	def getNo13MajorShareholdersMember(self): #第13位、大株主 [メンバー]
		return self.No13MajorShareholdersMember

	def getNo14MajorShareholdersMember(self): #第14位、大株主 [メンバー]
		return self.No14MajorShareholdersMember

	def getNo15MajorShareholdersMember(self): #第15位、大株主 [メンバー]
		return self.No15MajorShareholdersMember

	def getMajorShareholdersLineItems(self): #大株主の状況 [表示項目]
		return self.MajorShareholdersLineItems

	def getNameMajorShareholders(self): #氏名又は名称、大株主の状況
		return self.NameMajorShareholders

	def getAddressMajorShareholders(self): #住所、大株主の状況
		return self.AddressMajorShareholders

	def getNumberOfSharesHeld(self): #所有株式数
		return self.NumberOfSharesHeld

	def getShareholdingRatio(self): #発行済株式（自己株式を除く。）の総数に対する所有株式数の割合
		return self.ShareholdingRatio

	def getMajorShareholdersHeading(self): #大株主の状況 [目次項目]
		return self.MajorShareholdersHeading

	def getMajorShareholdersVotingRightsTable(self): #所有株式に係る議決権上位者の状況 [表]
		return self.MajorShareholdersVotingRightsTable

	def getMajorShareholdersVotingRightsAxis(self): #議決権上位 [軸]
		return self.MajorShareholdersVotingRightsAxis

	def getMajorShareholdersVotingRightsMember(self): #議決権上位 [メンバー] ※ディメンションデフォルト
		return self.MajorShareholdersVotingRightsMember

	def getNo1MajorShareholdersVotingRightsMember(self): #第1位、議決権上位 [メンバー]
		return self.No1MajorShareholdersVotingRightsMember

	def getNo2MajorShareholdersVotingRightsMember(self): #第2位、議決権上位 [メンバー]
		return self.No2MajorShareholdersVotingRightsMember

	def getNo3MajorShareholdersVotingRightsMember(self): #第3位、議決権上位 [メンバー]
		return self.No3MajorShareholdersVotingRightsMember

	def getNo4MajorShareholdersVotingRightsMember(self): #第4位、議決権上位 [メンバー]
		return self.No4MajorShareholdersVotingRightsMember

	def getNo5MajorShareholdersVotingRightsMember(self): #第5位、議決権上位 [メンバー]
		return self.No5MajorShareholdersVotingRightsMember

	def getNo6MajorShareholdersVotingRightsMember(self): #第6位、議決権上位 [メンバー]
		return self.No6MajorShareholdersVotingRightsMember

	def getNo7MajorShareholdersVotingRightsMember(self): #第7位、議決権上位 [メンバー]
		return self.No7MajorShareholdersVotingRightsMember

	def getNo8MajorShareholdersVotingRightsMember(self): #第8位、議決権上位 [メンバー]
		return self.No8MajorShareholdersVotingRightsMember

	def getNo9MajorShareholdersVotingRightsMember(self): #第9位、議決権上位 [メンバー]
		return self.No9MajorShareholdersVotingRightsMember

	def getNo10MajorShareholdersVotingRightsMember(self): #第10位、議決権上位 [メンバー]
		return self.No10MajorShareholdersVotingRightsMember

	def getNo11MajorShareholdersVotingRightsMember(self): #第11位、議決権上位 [メンバー]
		return self.No11MajorShareholdersVotingRightsMember

	def getNo12MajorShareholdersVotingRightsMember(self): #第12位、議決権上位 [メンバー]
		return self.No12MajorShareholdersVotingRightsMember

	def getNo13MajorShareholdersVotingRightsMember(self): #第13位、議決権上位 [メンバー]
		return self.No13MajorShareholdersVotingRightsMember

	def getNo14MajorShareholdersVotingRightsMember(self): #第14位、議決権上位 [メンバー]
		return self.No14MajorShareholdersVotingRightsMember

	def getNo15MajorShareholdersVotingRightsMember(self): #第15位、議決権上位 [メンバー]
		return self.No15MajorShareholdersVotingRightsMember

	def getMajorShareholdersVotingRightsLineItems(self): #所有株式に係る議決権上位者の状況 [表示項目]
		return self.MajorShareholdersVotingRightsLineItems

	def getNameMajorShareholdersVotingRights(self): #氏名又は名称、所有株式に係る議決権上位者の状況
		return self.NameMajorShareholdersVotingRights

	def getAddressMajorShareholdersVotingRights(self): #住所、所有株式に係る議決権上位者の状況
		return self.AddressMajorShareholdersVotingRights

	def getNumberOfVotingRightsHeld(self): #所有議決権数（個）
		return self.NumberOfVotingRightsHeld

	def getRatioOfVotingRightsHeld(self): #総株主の議決権に対する所有議決権数の割合
		return self.RatioOfVotingRightsHeld

	def getVotingRightsHeading(self): #議決権の状況 [目次項目]
		return self.VotingRightsHeading

	def getVotingRightsTextBlock(self): #議決権の状況 [テキストブロック]
		return self.VotingRightsTextBlock

	def getIssuedSharesVotingRightsHeading(self): #発行済株式、議決権の状況 [目次項目]
		return self.IssuedSharesVotingRightsHeading

	def getIssuedSharesVotingRightsTextBlock(self): #発行済株式、議決権の状況 [テキストブロック]
		return self.IssuedSharesVotingRightsTextBlock

	def getTreasurySharesEtcHeading(self): #自己株式等 [目次項目]
		return self.TreasurySharesEtcHeading

	def getTreasurySharesEtcTextBlock(self): #自己株式等 [テキストブロック]
		return self.TreasurySharesEtcTextBlock

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getInformationAboutOfficersTextBlock(self): #役員の状況 [テキストブロック]
		return self.InformationAboutOfficersTextBlock

	def getInformationAboutEmployeesHeading(self): #従業員の状況 [目次項目]
		return self.InformationAboutEmployeesHeading

	def getInformationAboutEmployeesTextBlock(self): #従業員の状況 [テキストブロック]
		return self.InformationAboutEmployeesTextBlock

	def getOverviewOfBusinessHeading(self): #事業の状況 [目次項目]
		return self.OverviewOfBusinessHeading

	def getBusinessPolicyBusinessEnvironmentIssuesToAddressEtcHeading(self): #経営方針、経営環境及び対処すべき課題等 [目次項目]
		return self.BusinessPolicyBusinessEnvironmentIssuesToAddressEtcHeading

	def getBusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock(self): #経営方針、経営環境及び対処すべき課題等 [テキストブロック]
		return self.BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock

	def getOverviewOfOperatingResultsEtcHeading(self): #経営成績等の概要 [目次項目]
		return self.OverviewOfOperatingResultsEtcHeading

	def getOverviewOfOperatingResultsEtcTextBlock(self): #経営成績等の概要 [テキストブロック]
		return self.OverviewOfOperatingResultsEtcTextBlock

	def getCriticalContractsForOperationHeading(self): #経営上の重要な契約等 [目次項目]
		return self.CriticalContractsForOperationHeading

	def getCriticalContractsForOperationTextBlock(self): #経営上の重要な契約等 [テキストブロック]
		return self.CriticalContractsForOperationTextBlock

	def getResearchAndDevelopmentActivitiesHeading(self): #研究開発活動 [目次項目]
		return self.ResearchAndDevelopmentActivitiesHeading

	def getResearchAndDevelopmentActivitiesTextBlock(self): #研究開発活動 [テキストブロック]
		return self.ResearchAndDevelopmentActivitiesTextBlock

	def getInformationAboutFacilitiesHeading(self): #設備の状況 [目次項目]
		return self.InformationAboutFacilitiesHeading

	def getMajorFacilitiesHeading(self): #主要な設備の状況 [目次項目]
		return self.MajorFacilitiesHeading

	def getMajorFacilitiesTextBlock(self): #主要な設備の状況 [テキストブロック]
		return self.MajorFacilitiesTextBlock

	def getPlannedAdditionsRetirementsEtcOfFacilitiesHeading(self): #設備の新設、除却等の計画 [目次項目]
		return self.PlannedAdditionsRetirementsEtcOfFacilitiesHeading

	def getPlannedAdditionsRetirementsEtcOfFacilitiesTextBlock(self): #設備の新設、除却等の計画 [テキストブロック]
		return self.PlannedAdditionsRetirementsEtcOfFacilitiesTextBlock

	def getFinancialInformationHeading(self): #経理の状況 [目次項目]
		return self.FinancialInformationHeading

	def getFinancialInformationHeading(self): #経理の状況 [目次項目]
		return self.FinancialInformationHeading

	def getRegulationsInAccordanceWithWhichConsolidatedFinancialStatementsHaveBeenPreparedFinancialInformation(self): #連結財務諸表が基づく規則、経理の状況
		return self.RegulationsInAccordanceWithWhichConsolidatedFinancialStatementsHaveBeenPreparedFinancialInformation

	def getRegulationsInAccordanceWithWhichFinancialStatementsHaveBeenPreparedFinancialInformation(self): #財務諸表が基づく規則、経理の状況
		return self.RegulationsInAccordanceWithWhichFinancialStatementsHaveBeenPreparedFinancialInformation

	def getDescriptionOfFactThatCompanyEngagesSpecifiedBusinessAndHasPreparedItsSemiAnnualConsolidatedFinancialStatementsFinancialInformation(self): #特定事業会社であり、中間連結財務諸表等を作成した場合の記載、経理の状況
		return self.DescriptionOfFactThatCompanyEngagesSpecifiedBusinessAndHasPreparedItsSemiAnnualConsolidatedFinancialStatementsFinancialInformation

	def getDescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation(self): #連結財務諸表が別記事業の特別の法令若しくは準則に基づく場合の記載、経理の状況
		return self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation

	def getDescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation(self): #財務諸表が別記事業の特別の法令若しくは準則に基づく場合の記載、経理の状況
		return self.DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation

	def getDescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation(self): #指定国際会計基準により連結財務諸表を作成した場合の記載、経理の状況
		return self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation

	def getDescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithJMISFinancialInformation(self): #修正国際基準により連結財務諸表を作成した場合の記載、経理の状況
		return self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithJMISFinancialInformation

	def getDescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithUSGAAPFinancialInformation(self): #米国会計基準により連結財務諸表を作成した場合の記載、経理の状況
		return self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithUSGAAPFinancialInformation

	def getDescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedFinancialInformation(self): #連結財務諸表を作成していない場合の記載、経理の状況
		return self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedFinancialInformation

	def getDescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedAndFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation(self): #連結財務諸表を作成していない場合で指定国際会計基準により財務諸表を作成する場合の記載、経理の状況
		return self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedAndFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation

	def getDescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialProvisionFinancialInformation(self): #特例財務諸表を作成する場合の記載、経理の状況
		return self.DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialProvisionFinancialInformation

	def getDescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsStatementOfCashFlowsFinancialInformation(self): #第１四半期又は第３四半期に係る四半期報告書において四半期キャッシュ・フロー計算書を記載する場合の記載、経理の状況
		return self.DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsStatementOfCashFlowsFinancialInformation

	def getDescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsConsolidatedStatementOfCashFlowsFinancialInformation(self): #第１四半期又は第３四半期に係る四半期報告書において四半期連結キャッシュ・フロー計算書を記載する場合の記載、経理の状況
		return self.DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsConsolidatedStatementOfCashFlowsFinancialInformation

	def getDescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodStatementOfIncomeFinancialInformation(self): #四半期報告書において四半期会計期間に係る四半期損益計算書を記載する場合の記載、経理の状況
		return self.DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodStatementOfIncomeFinancialInformation

	def getDescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodConsolidatedStatementOfComprehensiveIncomeFinancialInformation(self): #四半期報告書において四半期連結会計期間に係る四半期連結損益計算書及び四半期連結包括利益計算書又は四半期連結損益及び包括利益計算書を記載する場合の記載、経理の状況
		return self.DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodConsolidatedStatementOfComprehensiveIncomeFinancialInformation

	def getRemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcFinancialInformation(self): #連結財務諸表等の適正性を確保するための特段の取組み、経理の状況
		return self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcFinancialInformation

	def getRemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithIFRSFinancialInformation(self): #指定国際会計基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
		return self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithIFRSFinancialInformation

	def getRemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcAndInternalSystemToPrepareConsolidatedFinancialStatementsEtcFairlyInAccordanceWithIFRSFinancialInformation(self): #連結財務諸表等の適正性を確保するための特段の取組み及び指定国際会計基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
		return self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcAndInternalSystemToPrepareConsolidatedFinancialStatementsEtcFairlyInAccordanceWithIFRSFinancialInformation

	def getRemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithJMISFinancialInformation(self): #修正国際基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
		return self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithJMISFinancialInformation

	def getNoteOnIndependentAuditFinancialInformation(self): #監査証明について、経理の状況
		return self.NoteOnIndependentAuditFinancialInformation

	def getNoteOnChangeOfIndependentAuditorsFinancialInformation(self): #監査人の交代、経理の状況
		return self.NoteOnChangeOfIndependentAuditorsFinancialInformation

	def getNoteOnChangeInFiscalYearEndsFinancialInformation(self): #決算期変更について、経理の状況
		return self.NoteOnChangeInFiscalYearEndsFinancialInformation

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

	def getNotesSemiAnnualFinancialStatementsHeading(self): #注記事項、中間財務諸表 [目次項目]
		return self.NotesSemiAnnualFinancialStatementsHeading

	def getNotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernSemiAnnualFinancialStatementsHeading(self): #継続企業の前提に関する事項、中間財務諸表 [目次項目]
		return self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernSemiAnnualFinancialStatementsHeading

	def getNotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernSemiAnnualFinancialStatementsTextBlock(self): #継続企業の前提に関する事項、中間財務諸表 [テキストブロック]
		return self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernSemiAnnualFinancialStatementsTextBlock

	def getNotesSignificantAccountingPoliciesSemiAnnualFinancialStatementsHeading(self): #重要な会計方針、中間財務諸表 [目次項目]
		return self.NotesSignificantAccountingPoliciesSemiAnnualFinancialStatementsHeading

	def getNotesSignificantAccountingPoliciesSemiAnnualFinancialStatementsTextBlock(self): #重要な会計方針、中間財務諸表 [テキストブロック]
		return self.NotesSignificantAccountingPoliciesSemiAnnualFinancialStatementsTextBlock

	def getNotesChangesInAccountingPoliciesSemiAnnualFinancialStatementsHeading(self): #会計方針の変更、中間財務諸表 [目次項目]
		return self.NotesChangesInAccountingPoliciesSemiAnnualFinancialStatementsHeading

	def getNotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcSemiAnnualFinancialStatementsTextBlock(self): #会計基準等の改正等に伴う会計方針の変更、中間財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcSemiAnnualFinancialStatementsTextBlock

	def getNotesVoluntaryChangesInAccountingPoliciesSemiAnnualFinancialStatementsTextBlock(self): #会計基準等の改正等以外の正当な理由による会計方針の変更、中間財務諸表 [テキストブロック]
		return self.NotesVoluntaryChangesInAccountingPoliciesSemiAnnualFinancialStatementsTextBlock

	def getNotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesSemiAnnualFinancialStatementsTextBlock(self): #会計上の見積りの変更と区別することが困難な会計方針の変更、中間財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesSemiAnnualFinancialStatementsTextBlock

	def getNotesChangesInPresentationSemiAnnualFinancialStatementsHeading(self): #表示方法の変更、中間財務諸表 [目次項目]
		return self.NotesChangesInPresentationSemiAnnualFinancialStatementsHeading

	def getNotesChangesInPresentationSemiAnnualFinancialStatementsTextBlock(self): #表示方法の変更、中間財務諸表 [テキストブロック]
		return self.NotesChangesInPresentationSemiAnnualFinancialStatementsTextBlock

	def getNotesChangesInAccountingEstimatesSemiAnnualFinancialStatementsHeading(self): #会計上の見積りの変更、中間財務諸表 [目次項目]
		return self.NotesChangesInAccountingEstimatesSemiAnnualFinancialStatementsHeading

	def getNotesChangesInAccountingEstimatesSemiAnnualFinancialStatementsTextBlock(self): #会計上の見積りの変更、中間財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingEstimatesSemiAnnualFinancialStatementsTextBlock

	def getNotesRestatementSemiAnnualFinancialStatementsHeading(self): #修正再表示、中間財務諸表 [目次項目]
		return self.NotesRestatementSemiAnnualFinancialStatementsHeading

	def getNotesRestatementSemiAnnualFinancialStatementsTextBlock(self): #修正再表示、中間財務諸表 [テキストブロック]
		return self.NotesRestatementSemiAnnualFinancialStatementsTextBlock

	def getNotesAdditionalInformationSemiAnnualFinancialStatementsHeading(self): #追加情報、中間財務諸表 [目次項目]
		return self.NotesAdditionalInformationSemiAnnualFinancialStatementsHeading

	def getNotesAdditionalInformationSemiAnnualFinancialStatementsTextBlock(self): #追加情報、中間財務諸表 [テキストブロック]
		return self.NotesAdditionalInformationSemiAnnualFinancialStatementsTextBlock

	def getNotesSemiAnnualBalanceSheetHeading(self): #中間貸借対照表関係 [目次項目]
		return self.NotesSemiAnnualBalanceSheetHeading

	def getNotesSemiAnnualBalanceSheetHeading(self): #中間貸借対照表関係 [目次項目]
		return self.NotesSemiAnnualBalanceSheetHeading

	def getNotesSemiAnnualBalanceSheetTable(self): #中間貸借対照表関係 [表]
		return self.NotesSemiAnnualBalanceSheetTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSemiAnnualBalanceSheetLineItems(self): #中間貸借対照表関係 [表示項目]
		return self.NotesSemiAnnualBalanceSheetLineItems

	def getNotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock(self): #資産の金額から直接控除している引当金の注記 [テキストブロック]
		return self.NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock

	def getAllowanceForDoubtfulAccountsCA(self): #貸倒引当金、流動資産、一括控除
		return self.AllowanceForDoubtfulAccountsCA

	def getAllowanceForDoubtfulAccountsIOAByGroup(self): #貸倒引当金、投資その他の資産、一括控除
		return self.AllowanceForDoubtfulAccountsIOAByGroup

	def getAllowanceForDoubtfulAccountsAccountsReceivableTrade(self): #貸倒引当金、売掛金
		return self.AllowanceForDoubtfulAccountsAccountsReceivableTrade

	def getAllowanceForDoubtfulAccountsLongTermLoansReceivable(self): #貸倒引当金、長期貸付金
		return self.AllowanceForDoubtfulAccountsLongTermLoansReceivable

	def getAllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther(self): #貸倒引当金、破産更生債権等
		return self.AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther

	def getNotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock(self): #有形固定資産の減価償却累計額の注記 [テキストブロック]
		return self.NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock

	def getAccumulatedDepreciationPPEByGroup(self): #減価償却累計額、有形固定資産、一括控除
		return self.AccumulatedDepreciationPPEByGroup

	def getAccumulatedDepreciationBuildings(self): #減価償却累計額、建物
		return self.AccumulatedDepreciationBuildings

	def getAccumulatedDepreciationStructures(self): #減価償却累計額、構築物
		return self.AccumulatedDepreciationStructures

	def getAccumulatedDepreciationMachineryAndEquipment(self): #減価償却累計額、機械及び装置
		return self.AccumulatedDepreciationMachineryAndEquipment

	def getNotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock(self): #有形固定資産の圧縮記帳額の注記 [テキストブロック]
		return self.NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock

	def getNotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock(self): #減損損失累計額の表示に関する注記 [テキストブロック]
		return self.NotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock

	def getNotesRegardingPledgedAssetsTextBlock(self): #担保に供している資産の注記 [テキストブロック]
		return self.NotesRegardingPledgedAssetsTextBlock

	def getNotesRegardingReservesUnderSpecialLawsTextBlock(self): #特別法上の準備金等に関する注記 [テキストブロック]
		return self.NotesRegardingReservesUnderSpecialLawsTextBlock

	def getNotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock(self): #棚卸資産及び工事損失引当金の表示に関する注記 [テキストブロック]
		return self.NotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock

	def getNotesRegardingProvisionIncurredFromBusinessCombinationTextBlock(self): #企業結合に係る特定勘定の注記 [テキストブロック]
		return self.NotesRegardingProvisionIncurredFromBusinessCombinationTextBlock

	def getNotesRegardingGuaranteeObligationsTextBlock(self): #保証債務の注記 [テキストブロック]
		return self.NotesRegardingGuaranteeObligationsTextBlock

	def getNotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock(self): #受取手形割引高及び（又は）受取手形裏書譲渡高 [テキストブロック]
		return self.NotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock

	def getDiscountedTradeNotesReceivable(self): #受取手形割引高
		return self.DiscountedTradeNotesReceivable

	def getTradeNotesReceivableTransferredByEndorsement(self): #受取手形裏書譲渡高
		return self.TradeNotesReceivableTransferredByEndorsement

	def getNotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock(self): #指定法人の純資産の記載に関する注記 [テキストブロック]
		return self.NotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock

	def getNotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock(self): #期末日満期手形の会計処理 [テキストブロック]
		return self.NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock

	def getOtherElementsForNotesBalanceSheetAbstract(self): #貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetAbstract

	def getNotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock(self): #消費貸借契約及び（又は）消費寄託契約により貸し付けている有価証券に関する注記 [テキストブロック]
		return self.NotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock

	def getNotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock(self): #自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
		return self.NotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock

	def getNotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock(self): #有価証券の消費貸借契約・消費寄託契約及び自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
		return self.NotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock

	def getNotesRegardingLoanParticipationsTextBlock(self): #ローン・パーティシペーションに関する注記 [テキストブロック]
		return self.NotesRegardingLoanParticipationsTextBlock

	def getCreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock(self): #当座貸越契約及び（又は）貸出コミットメントに関する貸手の注記 [テキストブロック]
		return self.CreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock

	def getDebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock(self): #当座貸越契約及び（又は）貸出コミットメントに関する借手の注記 [テキストブロック]
		return self.DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock

	def getNotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock(self): #関係会社の株式及び（又は）出資金の総額 [テキストブロック]
		return self.NotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock

	def getNotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock(self): #非連結子会社及び関連会社の株式及び（又は）出資金の総額 [テキストブロック]
		return self.NotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock

	def getNotesRegardingSubordinatedBorrowingsTextBlock(self): #劣後特約付借入金に関する注記 [テキストブロック]
		return self.NotesRegardingSubordinatedBorrowingsTextBlock

	def getNotesRegardingSubordinatedBondsPayableTextBlock(self): #劣後特約付社債に関する注記 [テキストブロック]
		return self.NotesRegardingSubordinatedBondsPayableTextBlock

	def getNotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock(self): #資産の部の社債に係る保証債務に関する注記 [テキストブロック]
		return self.NotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock

	def getOtherElementsForNotesBalanceSheetOfBankAbstract(self): #銀行業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfBankAbstract

	def getNotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock(self): #銀行法及び金融機能の再生のための緊急措置に関する法律に基づく債権に関する注記、銀行業 [テキストブロック]
		return self.NotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock

	def getNotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock(self): #銀行業における手形割引に関する注記、銀行業 [テキストブロック]
		return self.NotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock

	def getOtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract(self): #第一種金融商品取引業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract

	def getNotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock(self): #差し入れた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
		return self.NotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock

	def getNotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock(self): #差し入れを受けた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
		return self.NotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock

	def getBreakdownOfTradingAccountSecuritiesEtcSECTextBlock(self): #商品有価証券等の内訳、第一種金融商品取引業 [テキストブロック]
		return self.BreakdownOfTradingAccountSecuritiesEtcSECTextBlock

	def getOtherElementsForNotesBalanceSheetOfInsuranceAbstract(self): #保険業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfInsuranceAbstract

	def getNotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock(self): #保険業法に基づく債権に関する注記、保険業 [テキストブロック]
		return self.NotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock

	def getNotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock(self): #保険業法第118条に規定する特別勘定の資産及び負債に関する注記、保険業 [テキストブロック]
		return self.NotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock

	def getNotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock(self): #その他資産に含まれている保険業法第113条に規定する事業費の繰延額の注記 [テキストブロック]
		return self.NotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock

	def getNotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock(self): #契約者配当準備金の増減異動及び契約者配当金の支払額に関する注記、保険業 [テキストブロック]
		return self.NotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock

	def getNotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock(self): #保険業法第91条の規定による組織変更剰余金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock

	def getNotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock(self): #保険業法施行規則第73条第3項において準用する同規則第71条第1項に規定する再保険を付した部分に相当する支払備金の金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock

	def getNotesRegardingPolicyReservesReinsuredINSTextBlock(self): #保険業法施行規則第71条第1項に規定する再保険を付した部分に相当する責任準備金の金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingPolicyReservesReinsuredINSTextBlock

	def getNotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock(self): #保険業法第259条の規定に基づく生命保険契約者保護機構に対する今後の負担見積額、保険業 [テキストブロック]
		return self.NotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock

	def getBreakdownOfOutstandingClaimsINSTextBlock(self): #支払備金の内訳、保険業 [テキストブロック]
		return self.BreakdownOfOutstandingClaimsINSTextBlock

	def getBreakdownOfPolicyReserveINSTextBlock(self): #責任準備金の内訳、保険業 [テキストブロック]
		return self.BreakdownOfPolicyReserveINSTextBlock

	def getOtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract(self): #特定金融業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract

	def getNotesRegardingBadLoansSPFTextBlock(self): #不良債権に関する注記、特定金融業 [テキストブロック]
		return self.NotesRegardingBadLoansSPFTextBlock

	def getOtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract(self): #商品先物取引業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract

	def getExplanationOfFuturesTransactionMarginCustomerCMDTextBlock(self): #委託者先物取引差金の説明、商品先物取引業 [テキストブロック]
		return self.ExplanationOfFuturesTransactionMarginCustomerCMDTextBlock

	def getNotesSemiAnnualStatementOfIncomeHeading(self): #中間損益計算書関係 [目次項目]
		return self.NotesSemiAnnualStatementOfIncomeHeading

	def getNotesSemiAnnualStatementOfIncomeHeading(self): #中間損益計算書関係 [目次項目]
		return self.NotesSemiAnnualStatementOfIncomeHeading

	def getNotesSemiAnnualStatementOfIncomeTable(self): #中間損益計算書関係 [表]
		return self.NotesSemiAnnualStatementOfIncomeTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSemiAnnualStatementOfIncomeLineItems(self): #中間損益計算書関係 [表示項目]
		return self.NotesSemiAnnualStatementOfIncomeLineItems

	def getNotesRegardingSignificantComponentsOfNonOperatingIncomeTextBlock(self): #重要な営業外収益の注記 [テキストブロック]
		return self.NotesRegardingSignificantComponentsOfNonOperatingIncomeTextBlock

	def getNotesRegardingSignificantComponentsOfNonOperatingExpensesTextBlock(self): #重要な営業外費用の注記 [テキストブロック]
		return self.NotesRegardingSignificantComponentsOfNonOperatingExpensesTextBlock

	def getNotesRegardingSignificantComponentsOfExtraordinaryIncomeTextBlock(self): #重要な特別利益の注記 [テキストブロック]
		return self.NotesRegardingSignificantComponentsOfExtraordinaryIncomeTextBlock

	def getNotesRegardingSignificantComponentsOfExtraordinaryLossesTextBlock(self): #重要な特別損失の注記 [テキストブロック]
		return self.NotesRegardingSignificantComponentsOfExtraordinaryLossesTextBlock

	def getNotesRegardingImpairmentLossTextBlock(self): #減損損失に関する注記 [テキストブロック]
		return self.NotesRegardingImpairmentLossTextBlock

	def getNotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock(self): #企業結合に係る特定勘定の取崩益の注記 [テキストブロック]
		return self.NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock

	def getDescriptionOfFactThatSimplifiedMethodOfTaxEffectAccountingWasAppliedTextBlock(self): #簡便法による税効果会計を適用している場合の注記 [テキストブロック]
		return self.DescriptionOfFactThatSimplifiedMethodOfTaxEffectAccountingWasAppliedTextBlock

	def getNotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock(self): #売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]
		return self.NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock

	def getNotesRegardingAmountOfDepreciationTextBlock(self): #減価償却額の注記 [テキストブロック]
		return self.NotesRegardingAmountOfDepreciationTextBlock

	def getOtherElementsForNotesStatementOfIncomeAbstract(self): #損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeAbstract

	def getBreakdownOfBusinessCostTextBlock(self): #事業費の内訳 [テキストブロック]
		return self.BreakdownOfBusinessCostTextBlock

	def getBreakdownOfPersonnelExpensesTextBlock(self): #人件費の内訳 [テキストブロック]
		return self.BreakdownOfPersonnelExpensesTextBlock

	def getBreakdownOfGainOnSalesOfSecuritiesTextBlock(self): #有価証券売却益の内訳 [テキストブロック]
		return self.BreakdownOfGainOnSalesOfSecuritiesTextBlock

	def getBreakdownOfLossOnSalesOfSecuritiesTextBlock(self): #有価証券売却損の内訳 [テキストブロック]
		return self.BreakdownOfLossOnSalesOfSecuritiesTextBlock

	def getBreakdownOfLossOnValuationOfSecuritiesTextBlock(self): #有価証券評価損の内訳 [テキストブロック]
		return self.BreakdownOfLossOnValuationOfSecuritiesTextBlock

	def getNotesRegardingTransactionsWithAffiliatedEntitiesTextBlock(self): #関係会社との取引に関する注記 [テキストブロック]
		return self.NotesRegardingTransactionsWithAffiliatedEntitiesTextBlock

	def getOtherElementsForNotesStatementOfIncomeOfBankAbstract(self): #銀行業の損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeOfBankAbstract

	def getMajorComponentsOfOtherIncomeBNKTextBlock(self): #その他の経常収益の主要な内訳、銀行業 [テキストブロック]
		return self.MajorComponentsOfOtherIncomeBNKTextBlock

	def getMajorComponentsOfOtherExpensesBNKTextBlock(self): #その他の経常費用の主要な内訳、銀行業 [テキストブロック]
		return self.MajorComponentsOfOtherExpensesBNKTextBlock

	def getOtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract(self): #第一種金融商品取引業の損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract

	def getBreakdownOfNetTradingIncomeSECTextBlock(self): #トレーディング損益の内訳、第一種金融商品取引業 [テキストブロック]
		return self.BreakdownOfNetTradingIncomeSECTextBlock

	def getBreakdownOfFinancialRevenueSECTextBlock(self): #金融収益の内訳、第一種金融商品取引業 [テキストブロック]
		return self.BreakdownOfFinancialRevenueSECTextBlock

	def getBreakdownOfFinancialExpensesSECTextBlock(self): #金融費用の内訳、第一種金融商品取引業 [テキストブロック]
		return self.BreakdownOfFinancialExpensesSECTextBlock

	def getOtherElementsForNotesStatementOfIncomeOfInsuranceAbstract(self): #保険業の損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeOfInsuranceAbstract

	def getMajorComponentsOfBusinessCostTextBlock(self): #事業費の主な内訳 [テキストブロック]
		return self.MajorComponentsOfBusinessCostTextBlock

	def getAgentFeeEtcINSNonlife(self): #代理店手数料等、損害保険業
		return self.AgentFeeEtcINSNonlife

	def getSalariesINSNonlife(self): #給与、損害保険業
		return self.SalariesINSNonlife

	def getBreakdownOfNetPremiumsWrittenINSTextBlock(self): #正味収入保険料の内訳、保険業 [テキストブロック]
		return self.BreakdownOfNetPremiumsWrittenINSTextBlock

	def getBreakdownOfNetClaimsPaidINSTextBlock(self): #正味支払保険金の内訳、保険業 [テキストブロック]
		return self.BreakdownOfNetClaimsPaidINSTextBlock

	def getBreakdownOfCommissionsAndCollectionFeesINSTextBlock(self): #諸手数料及び集金費の内訳、保険業 [テキストブロック]
		return self.BreakdownOfCommissionsAndCollectionFeesINSTextBlock

	def getBreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock(self): #支払備金繰入額又は支払備金戻入額の内訳、保険業 [テキストブロック]
		return self.BreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock

	def getBreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock(self): #責任準備金繰入額又は責任準備金戻入額の内訳、保険業 [テキストブロック]
		return self.BreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock

	def getNotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock(self): #支払備金繰入額又は支払備金戻入額の計算上、差し引かれた又は足し上げられた出再支払備金繰入額又は出再支払備金戻入額の注記、保険業 [テキストブロック]
		return self.NotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock

	def getNotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock(self): #責任準備金繰入額又は責任準備金戻入額の計算上、差し引かれた又は足し上げられた出再責任準備金繰入額又は出再責任準備金戻入額の注記、保険業 [テキストブロック]
		return self.NotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock

	def getBreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock(self): #利息及び配当金収入の資産源泉別内訳、保険業 [テキストブロック]
		return self.BreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock

	def getInterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock(self): #商品有価証券及び売買目的有価証券に係るそれぞれの利息及び配当金収入、売却損益及び評価損益の金額、保険業 [テキストブロック]
		return self.InterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock

	def getNotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock(self): #金銭の信託に係る評価損益の金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock

	def getNotesRegardingUnrealizedGainLossForDerivativesINSTextBlock(self): #金融派生商品に係る評価損益の金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingUnrealizedGainLossForDerivativesINSTextBlock

	def getMajorComponentsOfOtherExtraordinaryIncomeINSTextBlock(self): #その他特別利益の主な内訳、保険業 [テキストブロック]
		return self.MajorComponentsOfOtherExtraordinaryIncomeINSTextBlock

	def getMajorComponentsOfOtherExtraordinaryLossesINSTextBlock(self): #その他特別損失の主な内訳、保険業 [テキストブロック]
		return self.MajorComponentsOfOtherExtraordinaryLossesINSTextBlock

	def getOtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract(self): #商品先物取引業の損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract

	def getBreakdownOfBrokerageIncomeCMDTextBlock(self): #受取手数料の内訳、商品先物取引業 [テキストブロック]
		return self.BreakdownOfBrokerageIncomeCMDTextBlock

	def getBreakdownOfNetGainOnTradingCMDTextBlock(self): #売買損益の内訳、商品先物取引業 [テキストブロック]
		return self.BreakdownOfNetGainOnTradingCMDTextBlock

	def getExchangeRelatedExpensesCMDTextBlock(self): #取引所等関係費の内訳、商品先物取引業 [テキストブロック]
		return self.ExchangeRelatedExpensesCMDTextBlock

	def getNotesSemiAnnualStatementOfChangesInEquityHeading(self): #中間株主資本等変動計算書関係 [目次項目]
		return self.NotesSemiAnnualStatementOfChangesInEquityHeading

	def getNotesSemiAnnualStatementOfChangesInEquityHeading(self): #中間株主資本等変動計算書関係 [目次項目]
		return self.NotesSemiAnnualStatementOfChangesInEquityHeading

	def getNotesSemiAnnualStatementOfChangesInEquityTable(self): #中間株主資本等変動計算書関係 [表]
		return self.NotesSemiAnnualStatementOfChangesInEquityTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSemiAnnualStatementOfChangesInEquityLineItems(self): #中間株主資本等変動計算書関係 [表示項目]
		return self.NotesSemiAnnualStatementOfChangesInEquityLineItems

	def getNotesRegardingIssuedSharesAndTreasurySharesTextBlock(self): #発行済株式及び自己株式に関する注記 [テキストブロック]
		return self.NotesRegardingIssuedSharesAndTreasurySharesTextBlock

	def getNotesRegardingTreasurySharesTextBlock(self): #自己株式に関する注記 [テキストブロック]
		return self.NotesRegardingTreasurySharesTextBlock

	def getNotesRegardingNewShareSubscriptionRightsEtcTextBlock(self): #新株予約権等に関する注記 [テキストブロック]
		return self.NotesRegardingNewShareSubscriptionRightsEtcTextBlock

	def getNotesRegardingDividendTextBlock(self): #配当に関する注記 [テキストブロック]
		return self.NotesRegardingDividendTextBlock

	def getNotesSemiAnnualStatementOfCashFlowsHeading(self): #中間キャッシュ・フロー計算書関係 [目次項目]
		return self.NotesSemiAnnualStatementOfCashFlowsHeading

	def getNotesSemiAnnualStatementOfCashFlowsHeading(self): #中間キャッシュ・フロー計算書関係 [目次項目]
		return self.NotesSemiAnnualStatementOfCashFlowsHeading

	def getNotesSemiAnnualStatementOfCashFlowsTable(self): #中間キャッシュ・フロー計算書関係 [表]
		return self.NotesSemiAnnualStatementOfCashFlowsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSemiAnnualStatementOfCashFlowsLineItems(self): #中間キャッシュ・フロー計算書関係 [表示項目]
		return self.NotesSemiAnnualStatementOfCashFlowsLineItems

	def getReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock(self): #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
		return self.ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock

	def getDescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock(self): #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
		return self.DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock

	def getNotesLeasesSemiAnnualFinancialStatementsHeading(self): #リース取引関係、中間財務諸表 [目次項目]
		return self.NotesLeasesSemiAnnualFinancialStatementsHeading

	def getNotesLeasesSemiAnnualFinancialStatementsTextBlock(self): #リース取引関係、中間財務諸表 [テキストブロック]
		return self.NotesLeasesSemiAnnualFinancialStatementsTextBlock

	def getNotesFinancialInstrumentsSemiAnnualFinancialStatementsHeading(self): #金融商品関係、中間財務諸表 [目次項目]
		return self.NotesFinancialInstrumentsSemiAnnualFinancialStatementsHeading

	def getNotesFinancialInstrumentsSemiAnnualFinancialStatementsTextBlock(self): #金融商品関係、中間財務諸表 [テキストブロック]
		return self.NotesFinancialInstrumentsSemiAnnualFinancialStatementsTextBlock

	def getNotesSecuritiesSemiAnnualFinancialStatementsHeading(self): #有価証券関係、中間財務諸表 [目次項目]
		return self.NotesSecuritiesSemiAnnualFinancialStatementsHeading

	def getNotesSecuritiesSemiAnnualFinancialStatementsTextBlock(self): #有価証券関係、中間財務諸表 [テキストブロック]
		return self.NotesSecuritiesSemiAnnualFinancialStatementsTextBlock

	def getNotesMoneyHeldInTrustSemiAnnualFinancialStatementsHeading(self): #金銭の信託関係、中間財務諸表 [目次項目]
		return self.NotesMoneyHeldInTrustSemiAnnualFinancialStatementsHeading

	def getNotesMoneyHeldInTrustSemiAnnualFinancialStatementsTextBlock(self): #金銭の信託関係、中間財務諸表 [テキストブロック]
		return self.NotesMoneyHeldInTrustSemiAnnualFinancialStatementsTextBlock

	def getNotesValuationDifferenceOnAvailableForSaleSecuritiesSemiAnnualFinancialStatementsHeading(self): #その他有価証券評価差額金、中間財務諸表 [目次項目]
		return self.NotesValuationDifferenceOnAvailableForSaleSecuritiesSemiAnnualFinancialStatementsHeading

	def getNotesValuationDifferenceOnAvailableForSaleSecuritiesSemiAnnualFinancialStatementsTextBlock(self): #その他有価証券評価差額金、中間財務諸表 [テキストブロック]
		return self.NotesValuationDifferenceOnAvailableForSaleSecuritiesSemiAnnualFinancialStatementsTextBlock

	def getNotesDerivativesSemiAnnualFinancialStatementsHeading(self): #デリバティブ取引関係、中間財務諸表 [目次項目]
		return self.NotesDerivativesSemiAnnualFinancialStatementsHeading

	def getNotesDerivativesSemiAnnualFinancialStatementsTextBlock(self): #デリバティブ取引関係、中間財務諸表 [テキストブロック]
		return self.NotesDerivativesSemiAnnualFinancialStatementsTextBlock

	def getNotesShareOptionsEtcSemiAnnualFinancialStatementsHeading(self): #ストック・オプション等関係、中間財務諸表 [目次項目]
		return self.NotesShareOptionsEtcSemiAnnualFinancialStatementsHeading

	def getNotesShareOptionsEtcSemiAnnualFinancialStatementsTextBlock(self): #ストック・オプション等関係、中間財務諸表 [テキストブロック]
		return self.NotesShareOptionsEtcSemiAnnualFinancialStatementsTextBlock

	def getNotesBusinessCombinationsSemiAnnualFinancialStatementsHeading(self): #企業結合等関係、中間財務諸表 [目次項目]
		return self.NotesBusinessCombinationsSemiAnnualFinancialStatementsHeading

	def getNotesBusinessCombinationsSemiAnnualFinancialStatementsTextBlock(self): #企業結合等関係、中間財務諸表 [テキストブロック]
		return self.NotesBusinessCombinationsSemiAnnualFinancialStatementsTextBlock

	def getNotesAssetRetirementObligationsSemiAnnualFinancialStatementsHeading(self): #資産除去債務関係、中間財務諸表 [目次項目]
		return self.NotesAssetRetirementObligationsSemiAnnualFinancialStatementsHeading

	def getNotesAssetRetirementObligationsSemiAnnualFinancialStatementsTextBlock(self): #資産除去債務関係、中間財務諸表 [テキストブロック]
		return self.NotesAssetRetirementObligationsSemiAnnualFinancialStatementsTextBlock

	def getNotesRealEstateForLeaseEtcSemiAnnualFinancialStatementsHeading(self): #賃貸等不動産関係、中間財務諸表 [目次項目]
		return self.NotesRealEstateForLeaseEtcSemiAnnualFinancialStatementsHeading

	def getNotesRealEstateForLeaseEtcSemiAnnualFinancialStatementsTextBlock(self): #賃貸等不動産関係、中間財務諸表 [テキストブロック]
		return self.NotesRealEstateForLeaseEtcSemiAnnualFinancialStatementsTextBlock

	def getNotesRevenueRecognitionSemiAnnualFinancialStatementsHeading(self): #収益認識関係、中間財務諸表 [目次項目]
		return self.NotesRevenueRecognitionSemiAnnualFinancialStatementsHeading

	def getNotesRevenueRecognitionSemiAnnualFinancialStatementsTextBlock(self): #収益認識関係、中間財務諸表 [テキストブロック]
		return self.NotesRevenueRecognitionSemiAnnualFinancialStatementsTextBlock

	def getNotesInventoriesSemiAnnualFinancialStatementsHeading(self): #棚卸資産関係、中間財務諸表 [目次項目]
		return self.NotesInventoriesSemiAnnualFinancialStatementsHeading

	def getNotesInventoriesSemiAnnualFinancialStatementsTextBlock(self): #棚卸資産関係、中間財務諸表 [テキストブロック]
		return self.NotesInventoriesSemiAnnualFinancialStatementsTextBlock

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading(self): #セグメント情報等、中間財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsTextBlock(self): #セグメント情報等、中間財務諸表 [テキストブロック]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsTextBlock

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading(self): #セグメント情報等、中間財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsTable(self): #セグメント情報等、中間財務諸表 [表]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems(self): #セグメント情報等、中間財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getDescriptionOfReportableSegmentsTextBlock(self): #報告セグメントの概要 [テキストブロック]
		return self.DescriptionOfReportableSegmentsTextBlock

	def getDisclosureOfChangesInReportableSegmentsTextBlock(self): #報告セグメントの変更に関する事項 [テキストブロック]
		return self.DisclosureOfChangesInReportableSegmentsTextBlock

	def getDescriptionOfFactThatCompanysBusinessComprisesSingleSegment(self): #単一セグメントである旨
		return self.DescriptionOfFactThatCompanysBusinessComprisesSingleSegment

	def getExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock(self): #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]
		return self.ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading(self): #セグメント情報等、中間財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getDisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable(self): #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表]
		return self.DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getTotalOfReportableSegmentsAndOthersMember(self): #報告セグメント及びその他の合計 [メンバー]
		return self.TotalOfReportableSegmentsAndOthersMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getReconcilingItemsMember(self): #調整項目 [メンバー]
		return self.ReconcilingItemsMember

	def getDisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems(self): #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表示項目]
		return self.DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems

	def getSalesSegmentInformationAbstract(self): #売上高、セグメント情報 [タイトル項目]
		return self.SalesSegmentInformationAbstract

	def getRevenuesFromExternalCustomers(self): #外部顧客への売上高
		return self.RevenuesFromExternalCustomers

	def getTransactionsWithOtherSegments(self): #セグメント間の内部売上高又は振替高
		return self.TransactionsWithOtherSegments

	def getNetSales(self): #売上高
		return self.NetSales

	def getOperatingRevenue1(self): #営業収益
		return self.OperatingRevenue1

	def getOperatingRevenue2(self): #営業収入
		return self.OperatingRevenue2

	def getGrossOperatingRevenue(self): #営業総収入
		return self.GrossOperatingRevenue

	def getOrdinaryIncomeBNK(self): #経常収益、銀行業
		return self.OrdinaryIncomeBNK

	def getOperatingIncomeINS(self): #経常収益、保険業
		return self.OperatingIncomeINS

	def getSegmentProfitLossAbstract(self): #セグメント利益又は損失（△） [タイトル項目]
		return self.SegmentProfitLossAbstract

	def getOperatingIncome(self): #営業利益又は営業損失（△）
		return self.OperatingIncome

	def getOrdinaryIncome(self): #経常利益又は経常損失（△）
		return self.OrdinaryIncome

	def getIncomeBeforeIncomeTaxes(self): #税引前当期純利益又は税引前当期純損失（△）
		return self.IncomeBeforeIncomeTaxes

	def getProfitLoss(self): #当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）
		return self.ProfitLoss

	def getAssets(self): #資産
		return self.Assets

	def getLiabilities(self): #負債
		return self.Liabilities

	def getOtherItemsSegmentInformationAbstract(self): #その他の項目、セグメント情報 [タイトル項目]
		return self.OtherItemsSegmentInformationAbstract

	def getDepreciationSegmentInformation(self): #減価償却費、セグメント情報
		return self.DepreciationSegmentInformation

	def getAmortizationOfGoodwillSGA(self): #のれん償却額、販売費及び一般管理費
		return self.AmortizationOfGoodwillSGA

	def getInterestIncomeNOI(self): #受取利息、営業外収益
		return self.InterestIncomeNOI

	def getInterestExpensesNOE(self): #支払利息、営業外費用
		return self.InterestExpensesNOE

	def getExtraordinaryIncome(self): #特別利益
		return self.ExtraordinaryIncome

	def getGainOnNegativeGoodwillEI(self): #負ののれん発生益、特別利益
		return self.GainOnNegativeGoodwillEI

	def getExtraordinaryLoss(self): #特別損失
		return self.ExtraordinaryLoss

	def getImpairmentLossEL(self): #減損損失、特別損失
		return self.ImpairmentLossEL

	def getIncomeTaxExpense(self): #税金費用
		return self.IncomeTaxExpense

	def getIncreaseInPropertyPlantAndEquipmentAndIntangibleAssets(self): #有形固定資産及び無形固定資産の増加額
		return self.IncreaseInPropertyPlantAndEquipmentAndIntangibleAssets

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading(self): #セグメント情報等、中間財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsTable(self): #セグメント情報等、中間財務諸表 [表]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems(self): #セグメント情報等、中間財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getFootnotesRegardingSegmentInformationTableTextBlock(self): #セグメント表の脚注 [テキストブロック]
		return self.FootnotesRegardingSegmentInformationTableTextBlock

	def getDescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock(self): #報告セグメント合計額と財務諸表計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
		return self.DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock

	def getNotesInformationAssociatedWithReportableSegmentsAbstract(self): #関連情報 [タイトル項目]
		return self.NotesInformationAssociatedWithReportableSegmentsAbstract

	def getInformationForEachProductOrServiceTextBlock(self): #製品及びサービスごとの情報 [テキストブロック]
		return self.InformationForEachProductOrServiceTextBlock

	def getInformationForEachRegionAbstract(self): #地域ごとの情報 [タイトル項目]
		return self.InformationForEachRegionAbstract

	def getRevenuesFromExternalCustomersInformationForEachRegionTextBlock(self): #売上高、地域ごとの情報 [テキストブロック]
		return self.RevenuesFromExternalCustomersInformationForEachRegionTextBlock

	def getPropertyPlantAndEquipmentInformationForEachRegionTextBlock(self): #有形固定資産、地域ごとの情報 [テキストブロック]
		return self.PropertyPlantAndEquipmentInformationForEachRegionTextBlock

	def getInformationForEachOfMainCustomersTextBlock(self): #主要な顧客ごとの情報 [テキストブロック]
		return self.InformationForEachOfMainCustomersTextBlock

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading(self): #セグメント情報等、中間財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading

	def getDisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract(self): #報告セグメントごとの固定資産の減損損失に関する情報 [タイトル項目]
		return self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract

	def getDisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable(self): #報告セグメントごとの固定資産の減損損失に関する情報 [表]
		return self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getUnallocatedAmountsAndEliminationMember(self): #全社・消去 [メンバー]
		return self.UnallocatedAmountsAndEliminationMember

	def getDisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems(self): #報告セグメントごとの固定資産の減損損失に関する情報 [表示項目]
		return self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems

	def getImpairmentLossEL(self): #減損損失、特別損失
		return self.ImpairmentLossEL

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading(self): #セグメント情報等、中間財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsTable(self): #セグメント情報等、中間財務諸表 [表]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems(self): #セグメント情報等、中間財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems

	def getDescriptionOfImpairmentLossNotAllocatedToReportableSegments(self): #報告セグメントに配分されていない減損損失の内容
		return self.DescriptionOfImpairmentLossNotAllocatedToReportableSegments

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading(self): #セグメント情報等、中間財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading

	def getAmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract(self): #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [タイトル項目]
		return self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract

	def getAmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable(self): #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表]
		return self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getUnallocatedAmountsAndEliminationMember(self): #全社・消去 [メンバー]
		return self.UnallocatedAmountsAndEliminationMember

	def getAmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems(self): #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表示項目]
		return self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems

	def getAmortizationOfGoodwillSGA(self): #のれん償却額、販売費及び一般管理費
		return self.AmortizationOfGoodwillSGA

	def getGoodwill(self): #のれん
		return self.Goodwill

	def getGoodwillBeforeOffsetting(self): #のれん（相殺前）
		return self.GoodwillBeforeOffsetting

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading(self): #セグメント情報等、中間財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading

	def getAmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract(self): #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [タイトル項目]
		return self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract

	def getAmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable(self): #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表]
		return self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getUnallocatedAmountsAndEliminationMember(self): #全社・消去 [メンバー]
		return self.UnallocatedAmountsAndEliminationMember

	def getAmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems(self): #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表示項目]
		return self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems

	def getAmortizationOfNegativeGoodwillNOI(self): #負ののれん償却額、営業外収益
		return self.AmortizationOfNegativeGoodwillNOI

	def getNegativeGoodwill(self): #負ののれん
		return self.NegativeGoodwill

	def getNegativeGoodwillBeforeOffsetting(self): #負ののれん（相殺前）
		return self.NegativeGoodwillBeforeOffsetting

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading(self): #セグメント情報等、中間財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsTable(self): #セグメント情報等、中間財務諸表 [表]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems(self): #セグメント情報等、中間財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsLineItems

	def getDescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments(self): #報告セグメントに配分されていないのれんの償却額又は未償却残高の内容
		return self.DescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments

	def getNotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading(self): #セグメント情報等、中間財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcSemiAnnualFinancialStatementsHeading

	def getInformationAboutGainOnBargainPurchaseForEachReportableSegmentTable(self): #報告セグメントごとの負ののれん発生益に関する情報 [表]
		return self.InformationAboutGainOnBargainPurchaseForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getUnallocatedAmountsAndEliminationMember(self): #全社・消去 [メンバー]
		return self.UnallocatedAmountsAndEliminationMember

	def getInformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems(self): #報告セグメントごとの負ののれん発生益に関する情報 [表示項目]
		return self.InformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems

	def getDescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock(self): #報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]
		return self.DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock

	def getNotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSemiAnnualFinancialStatementsHeading(self): #持分法損益等、中間財務諸表 [目次項目]
		return self.NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSemiAnnualFinancialStatementsHeading

	def getNotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSemiAnnualFinancialStatementsTextBlock(self): #持分法損益等、中間財務諸表 [テキストブロック]
		return self.NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSemiAnnualFinancialStatementsTextBlock

	def getNotesSpecialPurposeEntitiesSubjectToDisclosureSemiAnnualFinancialStatementsHeading(self): #開示対象特別目的会社関係、中間財務諸表 [目次項目]
		return self.NotesSpecialPurposeEntitiesSubjectToDisclosureSemiAnnualFinancialStatementsHeading

	def getNotesSpecialPurposeEntitiesSubjectToDisclosureSemiAnnualFinancialStatementsTextBlock(self): #開示対象特別目的会社関係、中間財務諸表 [テキストブロック]
		return self.NotesSpecialPurposeEntitiesSubjectToDisclosureSemiAnnualFinancialStatementsTextBlock

	def getNotesPerShareInformationSemiAnnualFinancialStatementsHeading(self): #１株当たり情報、中間財務諸表 [目次項目]
		return self.NotesPerShareInformationSemiAnnualFinancialStatementsHeading

	def getNotesPerShareInformationSemiAnnualFinancialStatementsTextBlock(self): #１株当たり情報、中間財務諸表 [テキストブロック]
		return self.NotesPerShareInformationSemiAnnualFinancialStatementsTextBlock

	def getNotesSignificantEventsAfterReportingPeriodSemiAnnualFinancialStatementsHeading(self): #重要な後発事象、中間財務諸表 [目次項目]
		return self.NotesSignificantEventsAfterReportingPeriodSemiAnnualFinancialStatementsHeading

	def getNotesSignificantEventsAfterReportingPeriodSemiAnnualFinancialStatementsTextBlock(self): #重要な後発事象、中間財務諸表 [テキストブロック]
		return self.NotesSignificantEventsAfterReportingPeriodSemiAnnualFinancialStatementsTextBlock

	def getOtherInformationFinancialStatementsEtcHeading(self): #その他、財務諸表等 [目次項目]
		return self.OtherInformationFinancialStatementsEtcHeading

	def getOtherInformationFinancialStatementsEtcTextBlock(self): #その他、財務諸表等 [テキストブロック]
		return self.OtherInformationFinancialStatementsEtcTextBlock

	def getReferenceInformationOfReportingCompanyHeading(self): #提出会社の参考情報 [目次項目]
		return self.ReferenceInformationOfReportingCompanyHeading

	def getReferenceInformationOfReportingCompanyTextBlock(self): #提出会社の参考情報 [テキストブロック]
		return self.ReferenceInformationOfReportingCompanyTextBlock

	def getInformationAboutAffiliatedEntitiesHeading(self): #関係会社の情報 [目次項目]
		return self.InformationAboutAffiliatedEntitiesHeading

	def getInformationAboutAffiliatedEntitiesTextBlock(self): #関係会社の情報 [テキストブロック]
		return self.InformationAboutAffiliatedEntitiesTextBlock

	def getInformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyHeading(self): #提出会社の保証会社等の情報 [目次項目]
		return self.InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyHeading

	def getInformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyTextBlock(self): #提出会社の保証会社等の情報 [テキストブロック]
		return self.InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyTextBlock

	def getInformationAboutGuaranteeCompanyHeading(self): #保証会社情報 [目次項目]
		return self.InformationAboutGuaranteeCompanyHeading

	def getInformationAboutGuaranteeCompanyTextBlock(self): #保証会社情報 [テキストブロック]
		return self.InformationAboutGuaranteeCompanyTextBlock

	def getCorporateBondsUnderGuaranteeHeading(self): #保証の対象となっている社債 [目次項目]
		return self.CorporateBondsUnderGuaranteeHeading

	def getCorporateBondsUnderGuaranteeTextBlock(self): #保証の対象となっている社債 [テキストブロック]
		return self.CorporateBondsUnderGuaranteeTextBlock

	def getInformationAboutGuaranteeCompanySubjectToOngoingDisclosureHeading(self): #継続開示会社たる保証会社に関する事項 [目次項目]
		return self.InformationAboutGuaranteeCompanySubjectToOngoingDisclosureHeading

	def getInformationAboutGuaranteeCompanySubjectToOngoingDisclosureTextBlock(self): #継続開示会社たる保証会社に関する事項 [テキストブロック]
		return self.InformationAboutGuaranteeCompanySubjectToOngoingDisclosureTextBlock

	def getDocumentsSubmittedByGuaranteeCompanyHeading(self): #保証会社が提出した書類 [目次項目]
		return self.DocumentsSubmittedByGuaranteeCompanyHeading

	def getAnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading(self): #有価証券報告書及びその添付書類又は四半期報告書若しくは半期報告書、保証会社が提出した書類 [目次項目]
		return self.AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading

	def getAnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock(self): #有価証券報告書及びその添付書類又は四半期報告書若しくは半期報告書、保証会社が提出した書類 [テキストブロック]
		return self.AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock

	def getExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading(self): #臨時報告書、保証会社が提出した書類 [目次項目]
		return self.ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading

	def getExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock(self): #臨時報告書、保証会社が提出した書類 [テキストブロック]
		return self.ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock

	def getAmendmentReportDocumentsSubmittedByGuaranteeCompanyHeading(self): #訂正報告書、保証会社が提出した書類 [目次項目]
		return self.AmendmentReportDocumentsSubmittedByGuaranteeCompanyHeading

	def getAmendmentReportDocumentsSubmittedByGuaranteeCompanyTextBlock(self): #訂正報告書、保証会社が提出した書類 [テキストブロック]
		return self.AmendmentReportDocumentsSubmittedByGuaranteeCompanyTextBlock

	def getPlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyHeading(self): #上記書類を縦覧に供している場所、保証会社が提出した書類 [目次項目]
		return self.PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyHeading

	def getPlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyTextBlock(self): #上記書類を縦覧に供している場所、保証会社が提出した書類 [テキストブロック]
		return self.PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyTextBlock

	def getInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading(self): #継続開示会社に該当しない保証会社に関する事項 [目次項目]
		return self.InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading

	def getInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock(self): #継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
		return self.InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock

	def getCompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterHeading(self): #会社名・代表者の役職氏名及び本店の所在の場所 [目次項目]
		return self.CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterHeading

	def getCompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterTextBlock(self): #会社名・代表者の役職氏名及び本店の所在の場所 [テキストブロック]
		return self.CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterTextBlock

	def getOverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading(self): #企業の概況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
		return self.OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading

	def getOverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock(self): #企業の概況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
		return self.OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock

	def getOverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading(self): #事業の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
		return self.OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading

	def getOverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock(self): #事業の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
		return self.OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock

	def getInformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading(self): #設備の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
		return self.InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading

	def getInformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock(self): #設備の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
		return self.InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock

	def getGuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading(self): #保証会社の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
		return self.GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading

	def getGuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock(self): #保証会社の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
		return self.GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock

	def getFinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading(self): #経理の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
		return self.FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading

	def getFinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock(self): #経理の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
		return self.FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock

	def getInformationAboutCompaniesOtherThanGuaranteeCompanyHeading(self): #保証会社以外の会社の情報 [目次項目]
		return self.InformationAboutCompaniesOtherThanGuaranteeCompanyHeading

	def getInformationAboutCompaniesOtherThanGuaranteeCompanyTextBlock(self): #保証会社以外の会社の情報 [テキストブロック]
		return self.InformationAboutCompaniesOtherThanGuaranteeCompanyTextBlock

	def getReasonForDisclosureOfInformationOfCompanyConcernedHeading(self): #当該会社の情報の開示を必要とする理由 [目次項目]
		return self.ReasonForDisclosureOfInformationOfCompanyConcernedHeading

	def getReasonForDisclosureOfInformationOfCompanyConcernedTextBlock(self): #当該会社の情報の開示を必要とする理由 [テキストブロック]
		return self.ReasonForDisclosureOfInformationOfCompanyConcernedTextBlock

	def getInformationAboutCompanyConcernedSubjectToOngoingDisclosureHeading(self): #継続開示会社たる当該会社に関する事項 [目次項目]
		return self.InformationAboutCompanyConcernedSubjectToOngoingDisclosureHeading

	def getInformationAboutCompanyConcernedSubjectToOngoingDisclosureTextBlock(self): #継続開示会社たる当該会社に関する事項 [テキストブロック]
		return self.InformationAboutCompanyConcernedSubjectToOngoingDisclosureTextBlock

	def getInformationAboutCompanyConcernedNotSubjectToOngoingDisclosureHeading(self): #継続開示会社に該当しない当該会社に関する事項 [目次項目]
		return self.InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureHeading

	def getInformationAboutCompanyConcernedNotSubjectToOngoingDisclosureTextBlock(self): #継続開示会社に該当しない当該会社に関する事項 [テキストブロック]
		return self.InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureTextBlock

	def getInformationAboutIndexEtcHeading(self): #指数等の情報 [目次項目]
		return self.InformationAboutIndexEtcHeading

	def getInformationAboutIndexEtcTextBlock(self): #指数等の情報 [テキストブロック]
		return self.InformationAboutIndexEtcTextBlock

	def getReasonForDisclosureOfSaidIndexEtcHeading(self): #当該指数等の情報の開示を必要とする理由 [目次項目]
		return self.ReasonForDisclosureOfSaidIndexEtcHeading

	def getReasonForDisclosureOfSaidIndexEtcTextBlock(self): #当該指数等の情報の開示を必要とする理由 [テキストブロック]
		return self.ReasonForDisclosureOfSaidIndexEtcTextBlock

	def getHistoricalRecordsOfIndexEtcHeading(self): #当該指数等の推移 [目次項目]
		return self.HistoricalRecordsOfIndexEtcHeading

	def getHistoricalRecordsOfIndexEtcTextBlock(self): #当該指数等の推移 [テキストブロック]
		return self.HistoricalRecordsOfIndexEtcTextBlock

	def getIndependentAuditorsReportHeading(self): #独立監査人の報告書 [目次項目]
		return self.IndependentAuditorsReportHeading

	def getIndependentAuditorsReportConsolidatedTextBlock(self): #独立監査人の報告書、連結 [テキストブロック]
		return self.IndependentAuditorsReportConsolidatedTextBlock

	def getIndependentAuditorsReportNonConsolidatedTextBlock(self): #独立監査人の報告書、個別 [テキストブロック]
		return self.IndependentAuditorsReportNonConsolidatedTextBlock
