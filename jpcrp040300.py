from arelle import ModelManager
from arelle import Cntlr

class jpcrp040300:#企業内容等の開示に関する内閣府令 第四号の三様式 四半期報告書
	CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo43QuarterlySecuritiesReportHeading = '' #企業内容等の開示に関する内閣府令 第四号の三様式 四半期報告書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	ClauseOfStipulationCoverPage = '' #根拠条文、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	QuarterlyAccountingPeriodCoverPage = '' #四半期会計期間、表紙
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
	BusinessResultsOfGroupHeading = '' #連結経営指標等 [目次項目]
	BusinessResultsOfGroupTextBlock = '' #連結経営指標等 [テキストブロック]
	BusinessResultsOfGroupHeading = '' #連結経営指標等 [目次項目]
	BusinessResultsOfGroupTable = '' #連結経営指標等 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	BusinessResultsOfGroupLineItems = '' #連結経営指標等 [表示項目]
	NetSalesSummaryOfBusinessResults = '' #売上高、経営指標等
	RevenueKeyFinancialData = '' #売上収益、経営指標等
	OperatingRevenue1SummaryOfBusinessResults = '' #営業収益、経営指標等
	OperatingRevenue2SummaryOfBusinessResults = '' #営業収入、経営指標等
	GrossOperatingRevenueSummaryOfBusinessResults = '' #営業総収入、経営指標等
	OrdinaryIncomeSummaryOfBusinessResults = '' #経常収益、経営指標等
	NetPremiumsWrittenSummaryOfBusinessResultsINS = '' #正味収入保険料、経営指標等、保険業
	OrdinaryIncomeLossSummaryOfBusinessResults = '' #経常利益又は経常損失（△）、経営指標等
	ProfitLossAttributableToOwnersOfParentSummaryOfBusinessResults = '' #親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）、経営指標等
	ComprehensiveIncomeSummaryOfBusinessResults = '' #包括利益、経営指標等
	NetAssetsSummaryOfBusinessResults = '' #純資産額、経営指標等
	TotalAssetsSummaryOfBusinessResults = '' #総資産額、経営指標等
	NetAssetsPerShareSummaryOfBusinessResults = '' #１株当たり純資産額、経営指標等
	BasicEarningsLossPerShareSummaryOfBusinessResults = '' #１株当たり当期純利益又は当期純損失（△）、経営指標等
	DilutedEarningsPerShareSummaryOfBusinessResults = '' #潜在株式調整後１株当たり当期純利益、経営指標等
	EquityToAssetRatioSummaryOfBusinessResults = '' #自己資本比率、経営指標等
	CapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults = '' #自己資本比率（国際統一基準）、経営指標等
	CapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults = '' #自己資本比率（国内基準）、経営指標等
	CapitalAdequacyRatioBISStandardSummaryOfBusinessResults = '' #自己資本比率（第一基準）、経営指標等
	CapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults = '' #自己資本比率（第二基準）、経営指標等
	RateOfReturnOnEquitySummaryOfBusinessResults = '' #自己資本利益率、経営指標等
	PriceEarningsRatioSummaryOfBusinessResults = '' #株価収益率、経営指標等
	NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults = '' #営業活動によるキャッシュ・フロー、経営指標等
	NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults = '' #投資活動によるキャッシュ・フロー、経営指標等
	NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults = '' #財務活動によるキャッシュ・フロー、経営指標等
	CashAndCashEquivalentsSummaryOfBusinessResults = '' #現金及び現金同等物の残高、経営指標等
	NumberOfEmployees = '' #従業員数
	AverageNumberOfTemporaryWorkers = '' #平均臨時雇用人員
	RevenueIFRSSummaryOfBusinessResults = '' #売上収益（IFRS）、経営指標等
	ProfitLossBeforeTaxIFRSSummaryOfBusinessResults = '' #税引前利益又は税引前損失（△）（IFRS）、経営指標等
	ProfitLossFromContinuingOperationsIFRSSummaryOfBusinessResults = '' #継続事業からの当期利益又は当期損失（△）（IFRS）、経営指標等
	ProfitLossIFRSSummaryOfBusinessResults = '' #当期利益又は当期損失（△）（IFRS）、経営指標等
	ProfitLossAttributableToOwnersOfParentIFRSSummaryOfBusinessResults = '' #当期利益又は当期損失（△）：親会社の所有者に帰属（IFRS）、経営指標等
	ComprehensiveIncomeIFRSSummaryOfBusinessResults = '' #当期包括利益（IFRS）、経営指標等
	ComprehensiveIncomeAttributableToOwnersOfParentIFRSSummaryOfBusinessResults = '' #当期包括利益：親会社の所有者に帰属（IFRS）、経営指標等
	EquityAttributableToOwnersOfParentIFRSSummaryOfBusinessResults = '' #親会社の所有者に帰属する持分（IFRS）、経営指標等
	TotalAssetsIFRSSummaryOfBusinessResults = '' #総資産額（IFRS）、経営指標等
	EquityToAssetRatioIFRSSummaryOfBusinessResults = '' #１株当たり親会社所有者帰属持分（IFRS）、経営指標等
	BasicEarningsLossPerShareIFRSSummaryOfBusinessResults = '' #基本的１株当たり利益又は損失（△）（IFRS）、経営指標等
	DilutedEarningsLossPerShareIFRSSummaryOfBusinessResults = '' #希薄化後１株当たり利益又は損失（△）（IFRS）、経営指標等
	RatioOfOwnersEquityToGrossAssetsIFRSSummaryOfBusinessResults = '' #親会社所有者帰属持分比率（IFRS）、経営指標等
	RateOfReturnOnEquityIFRSSummaryOfBusinessResults = '' #親会社所有者帰属持分利益率（IFRS）、経営指標等
	PriceEarningsRatioIFRSSummaryOfBusinessResults = '' #株価収益率（IFRS）、経営指標等
	CashFlowsFromUsedInOperatingActivitiesIFRSSummaryOfBusinessResults = '' #営業活動によるキャッシュ・フロー（IFRS）、経営指標等
	CashFlowsFromUsedInInvestingActivitiesIFRSSummaryOfBusinessResults = '' #投資活動によるキャッシュ・フロー（IFRS）、経営指標等
	CashFlowsFromUsedInFinancingActivitiesIFRSSummaryOfBusinessResults = '' #財務活動によるキャッシュ・フロー（IFRS）、経営指標等
	CashAndCashEquivalentsIFRSSummaryOfBusinessResults = '' #現金及び現金同等物（IFRS）、経営指標等
	RevenueJMISSummaryOfBusinessResults = '' #売上収益（JMIS）、経営指標等
	ProfitLossBeforeTaxJMISSummaryOfBusinessResults = '' #税引前利益又は税引前損失（△）（JMIS）、経営指標等
	ProfitLossFromContinuingOperationsJMISSummaryOfBusinessResults = '' #継続事業からの当期利益又は当期損失（△）（JMIS）、経営指標等
	ProfitLossJMISSummaryOfBusinessResults = '' #当期利益又は当期損失（△）（JMIS）、経営指標等
	ProfitLossAttributableToOwnersOfParentJMISSummaryOfBusinessResults = '' #当期利益又は当期損失（△）：親会社の所有者に帰属（JMIS）、経営指標等
	ComprehensiveIncomeJMISSummaryOfBusinessResults = '' #当期包括利益（JMIS）、経営指標等
	ComprehensiveIncomeAttributableToOwnersOfParentJMISSummaryOfBusinessResults = '' #当期包括利益：親会社の所有者に帰属（JMIS）、経営指標等
	EquityAttributableToOwnersOfParentJMISSummaryOfBusinessResults = '' #親会社の所有者に帰属する持分（JMIS）、経営指標等
	TotalAssetsJMISSummaryOfBusinessResults = '' #総資産額（JMIS）、経営指標等
	EquityToAssetRatioJMISSummaryOfBusinessResults = '' #１株当たり親会社所有者帰属持分（JMIS）、経営指標等
	BasicEarningsLossPerShareJMISSummaryOfBusinessResults = '' #基本的１株当たり利益又は損失（△）（JMIS）、経営指標等
	DilutedEarningsLossPerShareJMISSummaryOfBusinessResults = '' #希薄化後１株当たり利益又は損失（△）（JMIS）、経営指標等
	RatioOfOwnersEquityToGrossAssetsJMISSummaryOfBusinessResults = '' #親会社所有者帰属持分比率（JMIS）、経営指標等
	RateOfReturnOnEquityJMISSummaryOfBusinessResults = '' #親会社所有者帰属持分利益率（JMIS）、経営指標等
	PriceEarningsRatioJMISSummaryOfBusinessResults = '' #株価収益率（JMIS）、経営指標等
	CashFlowsFromUsedInOperatingActivitiesJMISSummaryOfBusinessResults = '' #営業活動によるキャッシュ・フロー（JMIS）、経営指標等
	CashFlowsFromUsedInInvestingActivitiesJMISSummaryOfBusinessResults = '' #投資活動によるキャッシュ・フロー（JMIS）、経営指標等
	CashFlowsFromUsedInFinancingActivitiesJMISSummaryOfBusinessResults = '' #財務活動によるキャッシュ・フロー（JMIS）、経営指標等
	CashAndCashEquivalentsJMISSummaryOfBusinessResults = '' #現金及び現金同等物（JMIS）、経営指標等
	RevenuesUSGAAPSummaryOfBusinessResults = '' #売上高（US GAAP）、経営指標等
	OperatingIncomeLossUSGAAPSummaryOfBusinessResults = '' #営業利益又は営業損失（△）（US GAAP）、経営指標等
	ProfitLossBeforeTaxUSGAAPSummaryOfBusinessResults = '' #税引前利益又は税引前損失（△）（US GAAP）、経営指標等
	NetIncomeLossAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults = '' #当社株主に帰属する純利益又は純損失（△）（US GAAP）、経営指標等
	ComprehensiveIncomeUSGAAPSummaryOfBusinessResults = '' #包括利益（US GAAP）、経営指標等
	ComprehensiveIncomeAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults = '' #当社株主に帰属する包括利益（US GAAP）、経営指標等
	EquityAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults = '' #株主資本（US GAAP）、経営指標等
	EquityIncludingPortionAttributableToNonControllingInterestUSGAAPSummaryOfBusinessResults = '' #純資産額（US GAAP）、経営指標等
	TotalAssetsUSGAAPSummaryOfBusinessResults = '' #総資産額（US GAAP）、経営指標等
	EquityAttributableToOwnersOfParentPerShareUSGAAPSummaryOfBusinessResults = '' #１株当たり株主資本（US GAAP）、経営指標等
	BasicEarningsLossPerShareUSGAAPSummaryOfBusinessResults = '' #基本的１株当たり当社株主に帰属する利益又は損失（△）（US GAAP）、経営指標等
	DilutedEarningsLossPerShareUSGAAPSummaryOfBusinessResults = '' #希薄化後１株当たり当社株主に帰属する利益又は損失（△）（US GAAP）、経営指標等
	EquityToAssetRatioUSGAAPSummaryOfBusinessResults = '' #自己資本比率（US GAAP）、経営指標等
	PriceEarningsRatioUSGAAPSummaryOfBusinessResults = '' #株価収益率（US GAAP）、経営指標等
	RateOfReturnOnEquityUSGAAPSummaryOfBusinessResults = '' #株主資本利益率（US GAAP）、経営指標等
	CashFlowsFromUsedInOperatingActivitiesUSGAAPSummaryOfBusinessResults = '' #営業活動によるキャッシュ・フロー（US GAAP）、経営指標等
	CashFlowsFromUsedInInvestingActivitiesUSGAAPSummaryOfBusinessResults = '' #投資活動によるキャッシュ・フロー（US GAAP）、経営指標等
	CashFlowsFromUsedInFinancingActivitiesUSGAAPSummaryOfBusinessResults = '' #財務活動によるキャッシュ・フロー（US GAAP）、経営指標等
	CashAndCashEquivalentsUSGAAPSummaryOfBusinessResults = '' #現金及び現金同等物（US GAAP）、経営指標等
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
	OverviewOfBusinessHeading = '' #事業の状況 [目次項目]
	BusinessRisksHeading = '' #事業等のリスク [目次項目]
	BusinessRisksTextBlock = '' #事業等のリスク [テキストブロック]
	MaterialMattersRelatingToGoingConcernEtcBusinessRisksTextBlock = '' #重要事象等の内容、分析及び対応策、事業等のリスク [テキストブロック]
	ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsHeading = '' #経営者による財政状態、経営成績及びキャッシュ・フローの状況の分析 [目次項目]
	ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsTextBlock = '' #経営者による財政状態、経営成績及びキャッシュ・フローの状況の分析 [テキストブロック]
	BasicPolicyRegardingControlOfCompanyTextBlock = '' #会社の支配に関する基本方針 [テキストブロック]
	CriticalContractsForOperationHeading = '' #経営上の重要な契約等 [目次項目]
	CriticalContractsForOperationTextBlock = '' #経営上の重要な契約等 [テキストブロック]
	InformationAboutReportingCompanyHeading = '' #提出会社の状況 [目次項目]
	InformationAboutSharesEtcHeading = '' #株式等の状況 [目次項目]
	TotalNumberOfSharesEtcHeading = '' #株式の総数等 [目次項目]
	TotalNumberOfSharesHeading = '' #株式の総数 [目次項目]
	TotalNumberOfSharesTextBlock = '' #株式の総数 [テキストブロック]
	IssuedSharesTotalNumberOfSharesEtcHeading = '' #発行済株式、株式の総数等 [目次項目]
	IssuedSharesTotalNumberOfSharesEtcTextBlock = '' #発行済株式、株式の総数等 [テキストブロック]
	IssuedSharesTotalNumberOfSharesEtcHeading = '' #発行済株式、株式の総数等 [目次項目]
	IssuedSharesTotalNumberOfSharesEtcTable = '' #発行済株式、株式の総数等 [表]
	ClassesOfSharesAxis = '' #株式種類 [軸]
	TotalClassesOfSharesMember = '' #合計、株式種類 [メンバー] ※ディメンションデフォルト
	OrdinaryShareMember = '' #普通株式 [メンバー]
	ClassAPreferredSharesMember = '' #Ａ種優先株式 [メンバー]
	ClassBPreferredSharesMember = '' #Ｂ種優先株式 [メンバー]
	ClassOnePreferredSharesMember = '' #第一種優先株式 [メンバー]
	ClassTwoPreferredSharesMember = '' #第二種優先株式 [メンバー]
	ClassASharesMember = '' #Ａ種種類株式 [メンバー]
	IssuedSharesTotalNumberOfSharesEtcLineItems = '' #発行済株式、株式の総数等 [表示項目]
	ClassIssuedSharesTotalNumberOfSharesEtc = '' #種類、発行済株式、株式の総数等
	NumberOfIssuedSharesIssuedSharesTotalNumberOfSharesEtc = '' #発行数（株）、発行済株式、株式の総数等
	NumberOfIssuedSharesAsOfFiscalYearEndIssuedSharesTotalNumberOfSharesEtc = '' #事業年度末現在発行数（株）、発行済株式、株式の総数等
	NumberOfIssuedSharesAsOfFilingDateIssuedSharesTotalNumberOfSharesEtc = '' #提出日現在発行数（株）、発行済株式、株式の総数等
	NameOfFinancialInstrumentsExchangeOnWhichSecuritiesAreListedOrAuthorizedFinancialInstrumentsBusinessAssociationToWhichSecuritiesAreRegistered = '' #上場金融商品取引所名又は登録認可金融商品取引業協会名
	DescriptionIssuedSharesTotalNumberOfSharesEtc = '' #内容、発行済株式、株式の総数等
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
	IssuedSharesVotingRightsHeading = '' #発行済株式、議決権の状況 [目次項目]
	IssuedSharesVotingRightsTable = '' #発行済株式、議決権の状況 [表]
	CategoriesIssuedSharesAxis = '' #区分、発行済株式 [軸]
	TotalNumberOfIssuedSharesNumberOfVotingRightsHeldByAllShareholdersMember = '' #発行済株式総数／総株主の議決権 [メンバー] ※ディメンションデフォルト
	SharesWithNoVotingRightsMember = '' #無議決権株式 [メンバー]
	SharesWithRestrictedVotingRightsTreasurySharesEtcMember = '' #議決権制限株式（自己株式等） [メンバー]
	SharesWithRestrictedVotingRightsOtherMember = '' #議決権制限株式（その他） [メンバー]
	SharesWithFullVotingRightsTreasurySharesEtcMember = '' #完全議決権株式（自己株式等） [メンバー]
	OrdinarySharesSharesWithFullVotingRightsTreasurySharesEtcMember = '' #普通株式、完全議決権株式（自己株式等） [メンバー]
	OrdinarySharesTreasurySharesSharesWithFullVotingRightsTreasurySharesEtcMember = '' #（自己保有株式）普通株式、完全議決権株式（自己株式等） [メンバー]
	OrdinarySharesReciprocalHoldingSharesWithFullVotingRightsTreasurySharesEtcMember = '' #（相互保有株式）普通株式、完全議決権株式（自己株式等） [メンバー]
	SharesWithFullVotingRightsOtherMember = '' #完全議決権株式（その他） [メンバー]
	OrdinarySharesSharesWithFullVotingRightsOtherMember = '' #普通株式、完全議決権株式（その他） [メンバー]
	SharesLessThanOneUnitMember = '' #単元未満株式 [メンバー]
	OrdinarySharesSharesLessThanOneUnitMember = '' #普通株式、単元未満株式 [メンバー]
	IssuedSharesVotingRightsLineItems = '' #発行済株式、議決権の状況 [表示項目]
	NumberOfSharesIssuedSharesVotingRights = '' #株式数（株）、発行済株式、議決権の状況
	NumberOfVotingRightsIssuedSharesVotingRights = '' #議決権の数（個）、発行済株式、議決権の状況
	DescriptionIssuedSharesVotingRights = '' #内容、発行済株式、議決権の状況
	TreasurySharesEtcHeading = '' #自己株式等 [目次項目]
	TreasurySharesEtcTextBlock = '' #自己株式等 [テキストブロック]
	TreasurySharesEtcHeading = '' #自己株式等 [目次項目]
	TreasurySharesEtcTable = '' #自己株式等 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	TotalSequentialNumbersMember = '' #合計、連番 [メンバー] ※ディメンションデフォルト
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	Row4Member = '' #4件目 [メンバー]
	TreasurySharesEtcLineItems = '' #自己株式等 [表示項目]
	NameOfShareholderTreasurySharesEtc = '' #所有者の氏名又は名称、自己株式等
	AddressOfShareholderTreasurySharesEtc = '' #所有者の住所、自己株式等
	NumberOfSharesHeldInOwnNameTreasurySharesEtc = '' #自己名義所有株式数（株）、自己株式等
	NumberOfSharesHeldInOthersNamesTreasurySharesEtc = '' #他人名義所有株式数（株）、自己株式等
	TotalNumberOfSharesHeldTreasurySharesEtc = '' #所有株式数の合計（株）、自己株式等
	ShareholdingRatioTreasurySharesEtc = '' #発行済株式総数に対する所有株式数の割合（％）、自己株式等
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	InformationAboutOfficersTextBlock = '' #役員の状況 [テキストブロック]
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	NumberOfMaleDirectorsAndOtherOfficers = '' #役員のうち男性の人数
	NumberOfFemaleDirectorsAndOtherOfficers = '' #役員のうち女性の人数
	RatioOfFemaleDirectorsAndOtherOfficers = '' #役員のうち女性の比率
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
	QuarterlyConsolidatedFinancialStatementsHeading = '' #四半期連結財務諸表 [目次項目]
	QuarterlyConsolidatedBalanceSheetHeading = '' #四半期連結貸借対照表 [目次項目]
	QuarterlyConsolidatedBalanceSheetTextBlock = '' #四半期連結貸借対照表 [テキストブロック]
	CondensedQuarterlyConsolidatedStatementOfFinancialPositionJMISTextBlock = '' #要約四半期連結財政状態計算書（JMIS） [テキストブロック]
	QuarterlyConsolidatedBalanceSheetUSGAAPTextBlock = '' #四半期連結貸借対照表（US GAAP） [テキストブロック]
	QuarterlyConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading = '' #四半期連結損益計算書及び四半期連結包括利益計算書 [目次項目]
	QuarterlyConsolidatedStatementOfIncomeHeading = '' #四半期連結損益計算書 [目次項目]
	YearToQuarterEndConsolidatedStatementOfIncomeHeading = '' #四半期連結累計期間、四半期連結損益計算書 [目次項目]
	YearToQuarterEndConsolidatedStatementOfIncomeTextBlock = '' #四半期連結累計期間、四半期連結損益計算書 [テキストブロック]
	CondensedYearToQuarterEndConsolidatedStatementOfIncomeJMISTextBlock = '' #四半期連結累計期間、要約四半期連結損益計算書（JMIS） [テキストブロック]
	YearToQuarterEndConsolidatedStatementOfIncomeUSGAAPTextBlock = '' #四半期連結累計期間、四半期連結損益計算書（US GAAP） [テキストブロック]
	QuarterPeriodConsolidatedStatementOfIncomeHeading = '' #四半期連結会計期間、四半期連結損益計算書 [目次項目]
	QuarterPeriodConsolidatedStatementOfIncomeTextBlock = '' #四半期連結会計期間、四半期連結損益計算書 [テキストブロック]
	CondensedQuarterPeriodConsolidatedStatementOfIncomeJMISTextBlock = '' #四半期連結会計期間、要約四半期連結損益計算書（JMIS） [テキストブロック]
	QuarterPeriodConsolidatedStatementOfIncomeUSGAAPTextBlock = '' #四半期連結会計期間、四半期連結損益計算書（US GAAP） [テキストブロック]
	QuarterlyConsolidatedStatementOfComprehensiveIncomeHeading = '' #四半期連結包括利益計算書 [目次項目]
	YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeHeading = '' #四半期連結累計期間、四半期連結包括利益計算書 [目次項目]
	YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock = '' #四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック]
	CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeJMISTextBlock = '' #四半期連結累計期間、要約四半期連結包括利益計算書（JMIS） [テキストブロック]
	YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock = '' #四半期連結累計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]
	QuarterPeriodConsolidatedStatementOfComprehensiveIncomeHeading = '' #四半期連結会計期間、四半期連結包括利益計算書 [目次項目]
	QuarterPeriodConsolidatedStatementOfComprehensiveIncomeTextBlock = '' #四半期連結会計期間、四半期連結包括利益計算書 [テキストブロック]
	CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeJMISTextBlock = '' #四半期連結会計期間、要約四半期連結包括利益計算書（JMIS） [テキストブロック]
	QuarterPeriodConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock = '' #四半期連結会計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]
	QuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = '' #四半期連結損益及び包括利益計算書 [目次項目]
	YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = '' #四半期連結累計期間、四半期連結損益及び包括利益計算書 [目次項目]
	YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = '' #四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック]
	CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock = '' #四半期連結累計期間、要約四半期連結包括利益計算書（１計算書）（JMIS） [テキストブロック]
	YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock = '' #四半期連結累計期間、四半期連結損益及び包括利益計算書（US GAAP） [テキストブロック]
	QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = '' #四半期連結会計期間、四半期連結損益及び包括利益計算書 [目次項目]
	QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = '' #四半期連結会計期間、四半期連結損益及び包括利益計算書 [テキストブロック]
	CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock = '' #四半期連結会計期間、要約四半期連結包括利益計算書（１計算書）（JMIS） [テキストブロック]
	QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock = '' #四半期連結会計期間、四半期連結損益及び包括利益計算書（US GAAP） [テキストブロック]
	CondensedQuarterlyConsolidatedStatementOfChangesInEquityJMISHeading = '' #要約四半期連結持分変動計算書（JMIS） [目次項目]
	CondensedQuarterlyConsolidatedStatementOfChangesInEquityJMISTextBlock = '' #要約四半期連結持分変動計算書（JMIS） [テキストブロック]
	ConsolidatedQuarterlyStatementOfEquityUSGAAPHeading = '' #四半期連結資本勘定計算書（US GAAP） [目次項目]
	ConsolidatedQuarterlyStatementOfEquityUSGAAPTextBlock = '' #四半期連結資本勘定計算書（US GAAP） [テキストブロック]
	QuarterlyConsolidatedStatementOfCashFlowsHeading = '' #四半期連結キャッシュ・フロー計算書 [目次項目]
	QuarterlyConsolidatedStatementOfCashFlowsTextBlock = '' #四半期連結キャッシュ・フロー計算書 [テキストブロック]
	CondensedQuarterlyConsolidatedStatementOfCashFlowsJMISTextBlock = '' #要約四半期連結キャッシュ・フロー計算書（JMIS） [テキストブロック]
	QuarterlyConsolidatedStatementOfCashFlowsUSGAAPTextBlock = '' #四半期連結キャッシュ・フロー計算書（US GAAP） [テキストブロック]
	NotesQuarterlyConsolidatedFinancialStatementsHeading = '' #注記事項、四半期連結財務諸表 [目次項目]
	NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyConsolidatedFinancialStatementsHeading = '' #継続企業の前提に関する事項、四半期連結財務諸表 [目次項目]
	NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyConsolidatedFinancialStatementsTextBlock = '' #継続企業の前提に関する事項、四半期連結財務諸表 [テキストブロック]
	NotesChangesInScopeOfConsolidationOrEquityMethodHeading = '' #連結の範囲又は持分法適用の範囲の変更に関する注記 [目次項目]
	NotesChangesInScopeOfConsolidationOrEquityMethodTextBlock = '' #連結の範囲又は持分法適用の範囲の変更に関する注記 [テキストブロック]
	NotesChangesInAccountingPoliciesQuarterlyConsolidatedFinancialStatementsHeading = '' #会計方針の変更、四半期連結財務諸表 [目次項目]
	NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcQuarterlyConsolidatedFinancialStatementsTextBlock = '' #会計基準等の改正等に伴う会計方針の変更、四半期連結財務諸表 [テキストブロック]
	NotesVoluntaryChangesInAccountingPoliciesQuarterlyConsolidatedFinancialStatementsTextBlock = '' #会計基準等の改正等以外の正当な理由による会計方針の変更、四半期連結財務諸表 [テキストブロック]
	NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsTextBlock = '' #会計上の見積りの変更と区別することが困難な会計方針の変更、四半期連結財務諸表 [テキストブロック]
	NotesChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsHeading = '' #会計上の見積りの変更、四半期連結財務諸表 [目次項目]
	NotesChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsTextBlock = '' #会計上の見積りの変更、四半期連結財務諸表 [テキストブロック]
	NotesRestatementQuarterlyConsolidatedFinancialStatementsHeading = '' #修正再表示、四半期連結財務諸表 [目次項目]
	NotesRestatementQuarterlyConsolidatedFinancialStatementsTextBlock = '' #修正再表示、四半期連結財務諸表 [テキストブロック]
	NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyConsolidatedFinancialStatementsHeading = '' #四半期特有の会計処理、四半期連結財務諸表 [目次項目]
	NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyConsolidatedFinancialStatementsTextBlock = '' #四半期特有の会計処理、四半期連結財務諸表 [テキストブロック]
	NotesAdditionalInformationQuarterlyConsolidatedFinancialStatementsHeading = '' #追加情報、四半期連結財務諸表 [目次項目]
	NotesAdditionalInformationQuarterlyConsolidatedFinancialStatementsTextBlock = '' #追加情報、四半期連結財務諸表 [テキストブロック]
	NotesQuarterlyConsolidatedBalanceSheetHeading = '' #四半期連結貸借対照表関係 [目次項目]
	NotesQuarterlyConsolidatedBalanceSheetHeading = '' #四半期連結貸借対照表関係 [目次項目]
	NotesQuarterlyConsolidatedBalanceSheetTable = '' #四半期連結貸借対照表関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesQuarterlyConsolidatedBalanceSheetLineItems = '' #四半期連結貸借対照表関係 [表示項目]
	NotesRegardingInventoriesTextBlock = '' #棚卸資産の内訳の注記 [テキストブロック]
	MerchandiseAndFinishedGoods = '' #商品及び製品
	WorkInProcess = '' #仕掛品
	RawMaterialsAndSupplies = '' #原材料及び貯蔵品
	Inventories = '' #棚卸資産
	NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock = '' #資産の金額から直接控除している引当金の注記 [テキストブロック]
	AllowanceForDoubtfulAccountsCA = '' #貸倒引当金、流動資産、一括控除
	AllowanceForDoubtfulAccountsIOAByGroup = '' #貸倒引当金、投資その他の資産、一括控除
	AllowanceForDoubtfulAccountsAccountsReceivableTrade = '' #貸倒引当金、売掛金
	AllowanceForDoubtfulAccountsLongTermLoansReceivable = '' #貸倒引当金、長期貸付金
	AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther = '' #貸倒引当金、破産更生債権等
	NotesRegardingPresentationOfGoodwillAndNegativeGoodwillTextBlock = '' #のれん及び負ののれんの表示に関する注記 [テキストブロック]
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
	NotesQuarterlyConsolidatedStatementOfIncomeHeading = '' #四半期連結損益計算書関係 [目次項目]
	NotesQuarterlyConsolidatedStatementOfIncomeHeading = '' #四半期連結損益計算書関係 [目次項目]
	NotesQuarterlyConsolidatedStatementOfIncomeTable = '' #四半期連結損益計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesQuarterlyConsolidatedStatementOfIncomeLineItems = '' #四半期連結損益計算書関係 [表示項目]
	MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock = '' #主要な販売費及び一般管理費 [テキストブロック]
	DepreciationSGA = '' #減価償却費、販売費及び一般管理費
	ProvisionOfAllowanceForDoubtfulAccountsSGA = '' #貸倒引当金繰入額、販売費及び一般管理費
	NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock = '' #売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]
	NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = '' #四半期連結損益及び包括利益計算書関係 [目次項目]
	NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = '' #四半期連結損益及び包括利益計算書関係 [目次項目]
	NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementTable = '' #四半期連結損益及び包括利益計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementLineItems = '' #四半期連結損益及び包括利益計算書関係 [表示項目]
	MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock = '' #主要な販売費及び一般管理費 [テキストブロック]
	DepreciationSGA = '' #減価償却費、販売費及び一般管理費
	ProvisionOfAllowanceForDoubtfulAccountsSGA = '' #貸倒引当金繰入額、販売費及び一般管理費
	NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock = '' #売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]
	NotesQuarterlyConsolidatedStatementOfCashFlowsHeading = '' #四半期連結キャッシュ・フロー計算書関係 [目次項目]
	NotesQuarterlyConsolidatedStatementOfCashFlowsHeading = '' #四半期連結キャッシュ・フロー計算書関係 [目次項目]
	NotesQuarterlyConsolidatedStatementOfCashFlowsTable = '' #四半期連結キャッシュ・フロー計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesQuarterlyConsolidatedStatementOfCashFlowsLineItems = '' #四半期連結キャッシュ・フロー計算書関係 [表示項目]
	DescriptionOfFactThatQuarterlyStatementOfCashFlowsHasNotBeenPreparedTextBlock = '' #四半期キャッシュ・フロー計算書を作成しない場合の注記 [テキストブロック]
	ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock = '' #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
	DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock = '' #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
	NotesEquityQuarterlyConsolidatedFinancialStatementsHeading = '' #株主資本等に関する注記、四半期連結財務諸表 [目次項目]
	NotesEquityQuarterlyConsolidatedFinancialStatementsHeading = '' #株主資本等に関する注記、四半期連結財務諸表 [目次項目]
	NotesEquityQuarterlyConsolidatedFinancialStatementsTable = '' #株主資本等に関する注記、四半期連結財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesEquityQuarterlyConsolidatedFinancialStatementsLineItems = '' #株主資本等に関する注記、四半期連結財務諸表 [表示項目]
	NotesRegardingDividendTextBlock = '' #配当に関する注記 [テキストブロック]
	NotesWhenThereIsSignificantChangesInAmountsOfEquityTextBlock = '' #株主資本の金額に著しい変動があった場合の注記 [テキストブロック]
	NotesFinancialInstrumentsQuarterlyConsolidatedFinancialStatementsHeading = '' #金融商品関係、四半期連結財務諸表 [目次項目]
	NotesFinancialInstrumentsQuarterlyConsolidatedFinancialStatementsTextBlock = '' #金融商品関係、四半期連結財務諸表 [テキストブロック]
	NotesSecuritiesQuarterlyConsolidatedFinancialStatementsHeading = '' #有価証券関係、四半期連結財務諸表 [目次項目]
	NotesSecuritiesQuarterlyConsolidatedFinancialStatementsTextBlock = '' #有価証券関係、四半期連結財務諸表 [テキストブロック]
	NotesMoneyHeldInTrustQuarterlyConsolidatedFinancialStatementsHeading = '' #金銭の信託関係、四半期連結財務諸表 [目次項目]
	NotesMoneyHeldInTrustQuarterlyConsolidatedFinancialStatementsTextBlock = '' #金銭の信託関係、四半期連結財務諸表 [テキストブロック]
	NotesDerivativesQuarterlyConsolidatedFinancialStatementsHeading = '' #デリバティブ取引関係、四半期連結財務諸表 [目次項目]
	NotesDerivativesQuarterlyConsolidatedFinancialStatementsTextBlock = '' #デリバティブ取引関係、四半期連結財務諸表 [テキストブロック]
	NotesBusinessCombinationsQuarterlyConsolidatedFinancialStatementsHeading = '' #企業結合等関係、四半期連結財務諸表 [目次項目]
	NotesBusinessCombinationsQuarterlyConsolidatedFinancialStatementsTextBlock = '' #企業結合等関係、四半期連結財務諸表 [テキストブロック]
	NotesRevenueRecognitionQuarterlyConsolidatedFinancialStatementsHeading = '' #収益認識関係、四半期連結財務諸表 [目次項目]
	NotesRevenueRecognitionQuarterlyConsolidatedFinancialStatementsTextBlock = '' #収益認識関係、四半期連結財務諸表 [テキストブロック]
	NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading = '' #セグメント情報等、四半期連結財務諸表 [目次項目]
	NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock = '' #セグメント情報等、四半期連結財務諸表 [テキストブロック]
	NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading = '' #セグメント情報等、四半期連結財務諸表 [目次項目]
	NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTable = '' #セグメント情報等、四半期連結財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsLineItems = '' #セグメント情報等、四半期連結財務諸表 [表示項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	DescriptionOfFactThatCompanysBusinessComprisesSingleSegment = '' #単一セグメントである旨
	NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading = '' #セグメント情報等、四半期連結財務諸表 [目次項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	DisclosureOfSalesAndProfitLossForEachReportableSegmentTable = '' #報告セグメントごとの売上高及び利益又は損失の金額に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	TotalOfReportableSegmentsAndOthersMember = '' #報告セグメント及びその他の合計 [メンバー]
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	ReconcilingItemsMember = '' #調整項目 [メンバー]
	DisclosureOfSalesAndProfitLossForEachReportableSegmentLineItems = '' #報告セグメントごとの売上高及び利益又は損失の金額に関する情報 [表示項目]
	SalesSegmentInformationAbstract = '' #売上高、セグメント情報 [タイトル項目]
	RevenuesFromExternalCustomers = '' #外部顧客への売上高
	TransactionsWithOtherSegments = '' #セグメント間の内部売上高又は振替高
	NetSales = '' #売上高
	Revenue = '' #売上収益
	OperatingRevenue1 = '' #営業収益
	OperatingRevenue2 = '' #営業収入
	GrossOperatingRevenue = '' #営業総収入
	OrdinaryIncomeBNK = '' #経常収益、銀行業
	OperatingIncomeINS = '' #経常収益、保険業
	SegmentProfitLossAbstract = '' #セグメント利益又は損失（△） [タイトル項目]
	OperatingIncome = '' #営業利益又は営業損失（△）
	OrdinaryIncome = '' #経常利益又は経常損失（△）
	IncomeBeforeIncomeTaxes = '' #税引前当期純利益又は税引前当期純損失（△）
	ProfitLossAttributableToOwnersOfParent = '' #親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）
	ProfitLoss = '' #当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）
	NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading = '' #セグメント情報等、四半期連結財務諸表 [目次項目]
	NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTable = '' #セグメント情報等、四半期連結財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsLineItems = '' #セグメント情報等、四半期連結財務諸表 [表示項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	FootnotesRegardingSegmentInformationTableTextBlock = '' #セグメント表の脚注 [テキストブロック]
	InformationAboutAssetsForEachReportableSegmentTextBlock = '' #報告セグメントごとの資産に関する情報 [テキストブロック]
	DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock = '' #報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
	DisclosureOfChangesEtcInReportableSegmentsTextBlock = '' #報告セグメントの変更等に関する事項 [テキストブロック]
	InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock = '' #報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]
	NotesPerShareInformationQuarterlyConsolidatedFinancialStatementsHeading = '' #１株当たり情報、四半期連結財務諸表 [目次項目]
	NotesPerShareInformationQuarterlyConsolidatedFinancialStatementsTextBlock = '' #１株当たり情報、四半期連結財務諸表 [テキストブロック]
	NotesSignificantEventsAfterReportingPeriodQuarterlyConsolidatedFinancialStatementsHeading = '' #重要な後発事象、四半期連結財務諸表 [目次項目]
	NotesSignificantEventsAfterReportingPeriodQuarterlyConsolidatedFinancialStatementsTextBlock = '' #重要な後発事象、四半期連結財務諸表 [テキストブロック]
	NotesToQuarterlyConsolidatedFinancialStatementsJMISHeading = '' #四半期連結財務諸表注記事項（JMIS） [目次項目]
	NotesToQuarterlyConsolidatedFinancialStatementsJMISTextBlock = '' #四半期連結財務諸表注記事項（JMIS） [テキストブロック]
	NotesToQuarterlyConsolidatedFinancialStatementsUSGAAPHeading = '' #四半期連結財務諸表注記事項（US GAAP） [目次項目]
	NotesToQuarterlyConsolidatedFinancialStatementsUSGAAPTextBlock = '' #四半期連結財務諸表注記事項（US GAAP） [テキストブロック]
	OtherInformationConsolidatedFinancialStatementsEtcHeading = '' #その他、連結財務諸表等 [目次項目]
	OtherInformationConsolidatedFinancialStatementsEtcTextBlock = '' #その他、連結財務諸表等 [テキストブロック]
	PriorYearConsolidatedFinancialStatementsPreapredInAccordanceWithJMISHeading = '' #修正国際基準による前連結会計年度に係る連結財務諸表 [目次項目]
	PriorYearConsolidatedFinancialStatementsPreapredInAccordanceWithJMISTextBlock = '' #修正国際基準による前連結会計年度に係る連結財務諸表 [テキストブロック]
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
	NotesQuarterlyFinancialStatementsHeading = '' #注記事項、四半期財務諸表 [目次項目]
	NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyFinancialStatementsHeading = '' #継続企業の前提に関する事項、四半期財務諸表 [目次項目]
	NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyFinancialStatementsTextBlock = '' #継続企業の前提に関する事項、四半期財務諸表 [テキストブロック]
	NotesChangesInAccountingPoliciesQuarterlyFinancialStatementsHeading = '' #会計方針の変更、四半期財務諸表 [目次項目]
	NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcQuarterlyFinancialStatementsTextBlock = '' #会計基準等の改正等に伴う会計方針の変更、四半期財務諸表 [テキストブロック]
	NotesVoluntaryChangesInAccountingPoliciesQuarterlyFinancialStatementsTextBlock = '' #会計基準等の改正等以外の正当な理由による会計方針の変更、四半期財務諸表 [テキストブロック]
	NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesQuarterlyFinancialStatementsTextBlock = '' #会計上の見積りの変更と区別することが困難な会計方針の変更、四半期財務諸表 [テキストブロック]
	NotesChangesInAccountingEstimatesQuarterlyFinancialStatementsHeading = '' #会計上の見積りの変更、四半期財務諸表 [目次項目]
	NotesChangesInAccountingEstimatesQuarterlyFinancialStatementsTextBlock = '' #会計上の見積りの変更、四半期財務諸表 [テキストブロック]
	NotesRestatementQuarterlyFinancialStatementsHeading = '' #修正再表示、四半期財務諸表 [目次項目]
	NotesRestatementQuarterlyFinancialStatementsTextBlock = '' #修正再表示、四半期財務諸表 [テキストブロック]
	NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyFinancialStatementsHeading = '' #四半期特有の会計処理、四半期財務諸表 [目次項目]
	NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyFinancialStatementsTextBlock = '' #四半期特有の会計処理、四半期財務諸表 [テキストブロック]
	NotesAdditionalInformationQuarterlyFinancialStatementsHeading = '' #追加情報、四半期財務諸表 [目次項目]
	NotesAdditionalInformationQuarterlyFinancialStatementsTextBlock = '' #追加情報、四半期財務諸表 [テキストブロック]
	NotesQuarterlyBalanceSheetHeading = '' #四半期貸借対照表関係 [目次項目]
	NotesQuarterlyBalanceSheetHeading = '' #四半期貸借対照表関係 [目次項目]
	NotesQuarterlyBalanceSheetTable = '' #四半期貸借対照表関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesQuarterlyBalanceSheetLineItems = '' #四半期貸借対照表関係 [表示項目]
	NotesRegardingInventoriesTextBlock = '' #棚卸資産の内訳の注記 [テキストブロック]
	MerchandiseAndFinishedGoods = '' #商品及び製品
	WorkInProcess = '' #仕掛品
	RawMaterialsAndSupplies = '' #原材料及び貯蔵品
	Inventories = '' #棚卸資産
	NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock = '' #資産の金額から直接控除している引当金の注記 [テキストブロック]
	AllowanceForDoubtfulAccountsCA = '' #貸倒引当金、流動資産、一括控除
	AllowanceForDoubtfulAccountsIOAByGroup = '' #貸倒引当金、投資その他の資産、一括控除
	AllowanceForDoubtfulAccountsAccountsReceivableTrade = '' #貸倒引当金、売掛金
	AllowanceForDoubtfulAccountsLongTermLoansReceivable = '' #貸倒引当金、長期貸付金
	AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther = '' #貸倒引当金、破産更生債権等
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
	NotesQuarterlyStatementOfIncomeHeading = '' #四半期損益計算書関係 [目次項目]
	NotesQuarterlyStatementOfIncomeHeading = '' #四半期損益計算書関係 [目次項目]
	NotesQuarterlyStatementOfIncomeTable = '' #四半期損益計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesQuarterlyStatementOfIncomeLineItems = '' #四半期損益計算書関係 [表示項目]
	MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock = '' #主要な販売費及び一般管理費 [テキストブロック]
	DepreciationSGA = '' #減価償却費、販売費及び一般管理費
	ProvisionOfAllowanceForDoubtfulAccountsSGA = '' #貸倒引当金繰入額、販売費及び一般管理費
	NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock = '' #売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]
	NotesQuarterlyStatementOfCashFlowsHeading = '' #四半期キャッシュ・フロー計算書関係 [目次項目]
	NotesQuarterlyStatementOfCashFlowsHeading = '' #四半期キャッシュ・フロー計算書関係 [目次項目]
	NotesQuarterlyStatementOfCashFlowsTable = '' #四半期キャッシュ・フロー計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesQuarterlyStatementOfCashFlowsLineItems = '' #四半期キャッシュ・フロー計算書関係 [表示項目]
	DescriptionOfFactThatQuarterlyStatementOfCashFlowsHasNotBeenPreparedTextBlock = '' #四半期キャッシュ・フロー計算書を作成しない場合の注記 [テキストブロック]
	ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock = '' #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
	DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock = '' #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
	NotesEquityQuarterlyFinancialStatementsHeading = '' #株主資本等に関する注記、四半期財務諸表 [目次項目]
	NotesEquityQuarterlyFinancialStatementsHeading = '' #株主資本等に関する注記、四半期財務諸表 [目次項目]
	NotesEquityQuarterlyFinancialStatementsTable = '' #株主資本等に関する注記、四半期財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesEquityQuarterlyFinancialStatementsLineItems = '' #株主資本等に関する注記、四半期財務諸表 [表示項目]
	NotesRegardingDividendTextBlock = '' #配当に関する注記 [テキストブロック]
	NotesWhenThereIsSignificantChangesInAmountsOfEquityTextBlock = '' #株主資本の金額に著しい変動があった場合の注記 [テキストブロック]
	NotesFinancialInstrumentsQuarterlyFinancialStatementsHeading = '' #金融商品関係、四半期財務諸表 [目次項目]
	NotesFinancialInstrumentsQuarterlyFinancialStatementsTextBlock = '' #金融商品関係、四半期財務諸表 [テキストブロック]
	NotesSecuritiesQuarterlyFinancialStatementsHeading = '' #有価証券関係、四半期財務諸表 [目次項目]
	NotesSecuritiesQuarterlyFinancialStatementsTextBlock = '' #有価証券関係、四半期財務諸表 [テキストブロック]
	NotesMoneyHeldInTrustQuarterlyFinancialStatementsHeading = '' #金銭の信託関係、四半期財務諸表 [目次項目]
	NotesMoneyHeldInTrustQuarterlyFinancialStatementsTextBlock = '' #金銭の信託関係、四半期財務諸表 [テキストブロック]
	NotesDerivativesQuarterlyFinancialStatementsHeading = '' #デリバティブ取引関係、四半期財務諸表 [目次項目]
	NotesDerivativesQuarterlyFinancialStatementsTextBlock = '' #デリバティブ取引関係、四半期財務諸表 [テキストブロック]
	NotesBusinessCombinationsQuarterlyFinancialStatementsHeading = '' #企業結合等関係、四半期財務諸表 [目次項目]
	NotesBusinessCombinationsQuarterlyFinancialStatementsTextBlock = '' #企業結合等関係、四半期財務諸表 [テキストブロック]
	NotesRevenueRecognitionQuarterlyFinancialStatementsHeading = '' #収益認識関係、四半期財務諸表 [目次項目]
	NotesRevenueRecognitionQuarterlyFinancialStatementsTextBlock = '' #収益認識関係、四半期財務諸表 [テキストブロック]
	NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading = '' #セグメント情報等、四半期財務諸表 [目次項目]
	NotesSegmentInformationEtcQuarterlyFinancialStatementsTextBlock = '' #セグメント情報等、四半期財務諸表 [テキストブロック]
	NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading = '' #セグメント情報等、四半期財務諸表 [目次項目]
	NotesSegmentInformationEtcQuarterlyFinancialStatementsTable = '' #セグメント情報等、四半期財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSegmentInformationEtcQuarterlyFinancialStatementsLineItems = '' #セグメント情報等、四半期財務諸表 [表示項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	DescriptionOfFactThatCompanysBusinessComprisesSingleSegment = '' #単一セグメントである旨
	NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading = '' #セグメント情報等、四半期財務諸表 [目次項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	DisclosureOfSalesAndProfitLossForEachReportableSegmentTable = '' #報告セグメントごとの売上高及び利益又は損失の金額に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	TotalOfReportableSegmentsAndOthersMember = '' #報告セグメント及びその他の合計 [メンバー]
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	ReconcilingItemsMember = '' #調整項目 [メンバー]
	DisclosureOfSalesAndProfitLossForEachReportableSegmentLineItems = '' #報告セグメントごとの売上高及び利益又は損失の金額に関する情報 [表示項目]
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
	NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading = '' #セグメント情報等、四半期財務諸表 [目次項目]
	NotesSegmentInformationEtcQuarterlyFinancialStatementsTable = '' #セグメント情報等、四半期財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSegmentInformationEtcQuarterlyFinancialStatementsLineItems = '' #セグメント情報等、四半期財務諸表 [表示項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	FootnotesRegardingSegmentInformationTableTextBlock = '' #セグメント表の脚注 [テキストブロック]
	InformationAboutAssetsForEachReportableSegmentTextBlock = '' #報告セグメントごとの資産に関する情報 [テキストブロック]
	DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock = '' #報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
	DisclosureOfChangesEtcInReportableSegmentsTextBlock = '' #報告セグメントの変更等に関する事項 [テキストブロック]
	InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock = '' #報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]
	NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedQuarterlyFinancialStatementsHeading = '' #持分法損益等、四半期財務諸表 [目次項目]
	NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedQuarterlyFinancialStatementsTextBlock = '' #持分法損益等、四半期財務諸表 [テキストブロック]
	NotesPerShareInformationQuarterlyFinancialStatementsHeading = '' #１株当たり情報、四半期財務諸表 [目次項目]
	NotesPerShareInformationQuarterlyFinancialStatementsTextBlock = '' #１株当たり情報、四半期財務諸表 [テキストブロック]
	NotesSignificantEventsAfterReportingPeriodQuarterlyFinancialStatementsHeading = '' #重要な後発事象、四半期財務諸表 [目次項目]
	NotesSignificantEventsAfterReportingPeriodQuarterlyFinancialStatementsTextBlock = '' #重要な後発事象、四半期財務諸表 [テキストブロック]
	OtherInformationFinancialStatementsEtcHeading = '' #その他、財務諸表等 [目次項目]
	OtherInformationFinancialStatementsEtcTextBlock = '' #その他、財務諸表等 [テキストブロック]
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
	IndependentAuditorsReportHeading = '' #独立監査人の報告書 [目次項目]
	IndependentAuditorsReportConsolidatedTextBlock = '' #独立監査人の報告書、連結 [テキストブロック]
	AuditFirm1Consolidated = '' #監査法人１、連結
	CPA1AuditFirm1Consolidated = '' #公認会計士１、監査法人１、連結
	CPA2AuditFirm1Consolidated = '' #公認会計士２、監査法人１、連結
	CPA3AuditFirm1Consolidated = '' #公認会計士３、監査法人１、連結
	CPA4AuditFirm1Consolidated = '' #公認会計士４、監査法人１、連結
	CPA5AuditFirm1Consolidated = '' #公認会計士５、監査法人１、連結
	AuditFirm2Consolidated = '' #監査法人２、連結
	CPA1AuditFirm2Consolidated = '' #公認会計士１、監査法人２、連結
	CPA2AuditFirm2Consolidated = '' #公認会計士２、監査法人２、連結
	KeyAuditMattersConsolidatedTextBlock = '' #監査上の主要な検討事項、連結 [テキストブロック]
	OverviewKAMConsolidatedTextBlock = '' #全体概要、監査上の主要な検討事項、連結 [テキストブロック]
	IndependentAuditorsReportNonConsolidatedTextBlock = '' #独立監査人の報告書、個別 [テキストブロック]
	AuditFirm1NonConsolidated = '' #監査法人１、個別
	CPA1AuditFirm1NonConsolidated = '' #公認会計士１、監査法人１、個別
	CPA2AuditFirm1NonConsolidated = '' #公認会計士２、監査法人１、個別
	CPA3AuditFirm1NonConsolidated = '' #公認会計士３、監査法人１、個別
	CPA4AuditFirm1NonConsolidated = '' #公認会計士４、監査法人１、個別
	CPA5AuditFirm1NonConsolidated = '' #公認会計士５、監査法人１、個別
	AuditFirm2NonConsolidated = '' #監査法人２、個別
	CPA1AuditFirm2NonConsolidated = '' #公認会計士１、監査法人２、個別
	CPA2AuditFirm2NonConsolidated = '' #公認会計士２、監査法人２、個別
	KeyAuditMattersNonConsolidatedTextBlock = '' #監査上の主要な検討事項、個別 [テキストブロック]
	OverviewKAMNonConsolidatedTextBlock = '' #全体概要、監査上の主要な検討事項、個別 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo43QuarterlySecuritiesReportHeading': #企業内容等の開示に関する内閣府令 第四号の三様式 四半期報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo43QuarterlySecuritiesReportHeading = fact.value

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

			elif fact.concept.qname.localName == 'QuarterlyAccountingPeriodCoverPage': #四半期会計期間、表紙
				self.QuarterlyAccountingPeriodCoverPage = fact.value

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

			elif fact.concept.qname.localName == 'BusinessResultsOfGroupHeading': #連結経営指標等 [目次項目]
				self.BusinessResultsOfGroupHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfGroupTextBlock': #連結経営指標等 [テキストブロック]
				self.BusinessResultsOfGroupTextBlock = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfGroupHeading': #連結経営指標等 [目次項目]
				self.BusinessResultsOfGroupHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfGroupTable': #連結経営指標等 [表]
				self.BusinessResultsOfGroupTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfGroupLineItems': #連結経営指標等 [表示項目]
				self.BusinessResultsOfGroupLineItems = fact.value

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

			elif fact.concept.qname.localName == 'ProfitLossAttributableToOwnersOfParentSummaryOfBusinessResults': #親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）、経営指標等
				self.ProfitLossAttributableToOwnersOfParentSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeSummaryOfBusinessResults': #包括利益、経営指標等
				self.ComprehensiveIncomeSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetAssetsSummaryOfBusinessResults': #純資産額、経営指標等
				self.NetAssetsSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'TotalAssetsSummaryOfBusinessResults': #総資産額、経営指標等
				self.TotalAssetsSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetAssetsPerShareSummaryOfBusinessResults': #１株当たり純資産額、経営指標等
				self.NetAssetsPerShareSummaryOfBusinessResults = fact.value

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

			elif fact.concept.qname.localName == 'RevenueIFRSSummaryOfBusinessResults': #売上収益（IFRS）、経営指標等
				self.RevenueIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossBeforeTaxIFRSSummaryOfBusinessResults': #税引前利益又は税引前損失（△）（IFRS）、経営指標等
				self.ProfitLossBeforeTaxIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossFromContinuingOperationsIFRSSummaryOfBusinessResults': #継続事業からの当期利益又は当期損失（△）（IFRS）、経営指標等
				self.ProfitLossFromContinuingOperationsIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossIFRSSummaryOfBusinessResults': #当期利益又は当期損失（△）（IFRS）、経営指標等
				self.ProfitLossIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossAttributableToOwnersOfParentIFRSSummaryOfBusinessResults': #当期利益又は当期損失（△）：親会社の所有者に帰属（IFRS）、経営指標等
				self.ProfitLossAttributableToOwnersOfParentIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeIFRSSummaryOfBusinessResults': #当期包括利益（IFRS）、経営指標等
				self.ComprehensiveIncomeIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeAttributableToOwnersOfParentIFRSSummaryOfBusinessResults': #当期包括利益：親会社の所有者に帰属（IFRS）、経営指標等
				self.ComprehensiveIncomeAttributableToOwnersOfParentIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityAttributableToOwnersOfParentIFRSSummaryOfBusinessResults': #親会社の所有者に帰属する持分（IFRS）、経営指標等
				self.EquityAttributableToOwnersOfParentIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'TotalAssetsIFRSSummaryOfBusinessResults': #総資産額（IFRS）、経営指標等
				self.TotalAssetsIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityToAssetRatioIFRSSummaryOfBusinessResults': #１株当たり親会社所有者帰属持分（IFRS）、経営指標等
				self.EquityToAssetRatioIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'BasicEarningsLossPerShareIFRSSummaryOfBusinessResults': #基本的１株当たり利益又は損失（△）（IFRS）、経営指標等
				self.BasicEarningsLossPerShareIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'DilutedEarningsLossPerShareIFRSSummaryOfBusinessResults': #希薄化後１株当たり利益又は損失（△）（IFRS）、経営指標等
				self.DilutedEarningsLossPerShareIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RatioOfOwnersEquityToGrossAssetsIFRSSummaryOfBusinessResults': #親会社所有者帰属持分比率（IFRS）、経営指標等
				self.RatioOfOwnersEquityToGrossAssetsIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RateOfReturnOnEquityIFRSSummaryOfBusinessResults': #親会社所有者帰属持分利益率（IFRS）、経営指標等
				self.RateOfReturnOnEquityIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'PriceEarningsRatioIFRSSummaryOfBusinessResults': #株価収益率（IFRS）、経営指標等
				self.PriceEarningsRatioIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInOperatingActivitiesIFRSSummaryOfBusinessResults': #営業活動によるキャッシュ・フロー（IFRS）、経営指標等
				self.CashFlowsFromUsedInOperatingActivitiesIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInInvestingActivitiesIFRSSummaryOfBusinessResults': #投資活動によるキャッシュ・フロー（IFRS）、経営指標等
				self.CashFlowsFromUsedInInvestingActivitiesIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInFinancingActivitiesIFRSSummaryOfBusinessResults': #財務活動によるキャッシュ・フロー（IFRS）、経営指標等
				self.CashFlowsFromUsedInFinancingActivitiesIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashAndCashEquivalentsIFRSSummaryOfBusinessResults': #現金及び現金同等物（IFRS）、経営指標等
				self.CashAndCashEquivalentsIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RevenueJMISSummaryOfBusinessResults': #売上収益（JMIS）、経営指標等
				self.RevenueJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossBeforeTaxJMISSummaryOfBusinessResults': #税引前利益又は税引前損失（△）（JMIS）、経営指標等
				self.ProfitLossBeforeTaxJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossFromContinuingOperationsJMISSummaryOfBusinessResults': #継続事業からの当期利益又は当期損失（△）（JMIS）、経営指標等
				self.ProfitLossFromContinuingOperationsJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossJMISSummaryOfBusinessResults': #当期利益又は当期損失（△）（JMIS）、経営指標等
				self.ProfitLossJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossAttributableToOwnersOfParentJMISSummaryOfBusinessResults': #当期利益又は当期損失（△）：親会社の所有者に帰属（JMIS）、経営指標等
				self.ProfitLossAttributableToOwnersOfParentJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeJMISSummaryOfBusinessResults': #当期包括利益（JMIS）、経営指標等
				self.ComprehensiveIncomeJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeAttributableToOwnersOfParentJMISSummaryOfBusinessResults': #当期包括利益：親会社の所有者に帰属（JMIS）、経営指標等
				self.ComprehensiveIncomeAttributableToOwnersOfParentJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityAttributableToOwnersOfParentJMISSummaryOfBusinessResults': #親会社の所有者に帰属する持分（JMIS）、経営指標等
				self.EquityAttributableToOwnersOfParentJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'TotalAssetsJMISSummaryOfBusinessResults': #総資産額（JMIS）、経営指標等
				self.TotalAssetsJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityToAssetRatioJMISSummaryOfBusinessResults': #１株当たり親会社所有者帰属持分（JMIS）、経営指標等
				self.EquityToAssetRatioJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'BasicEarningsLossPerShareJMISSummaryOfBusinessResults': #基本的１株当たり利益又は損失（△）（JMIS）、経営指標等
				self.BasicEarningsLossPerShareJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'DilutedEarningsLossPerShareJMISSummaryOfBusinessResults': #希薄化後１株当たり利益又は損失（△）（JMIS）、経営指標等
				self.DilutedEarningsLossPerShareJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RatioOfOwnersEquityToGrossAssetsJMISSummaryOfBusinessResults': #親会社所有者帰属持分比率（JMIS）、経営指標等
				self.RatioOfOwnersEquityToGrossAssetsJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RateOfReturnOnEquityJMISSummaryOfBusinessResults': #親会社所有者帰属持分利益率（JMIS）、経営指標等
				self.RateOfReturnOnEquityJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'PriceEarningsRatioJMISSummaryOfBusinessResults': #株価収益率（JMIS）、経営指標等
				self.PriceEarningsRatioJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInOperatingActivitiesJMISSummaryOfBusinessResults': #営業活動によるキャッシュ・フロー（JMIS）、経営指標等
				self.CashFlowsFromUsedInOperatingActivitiesJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInInvestingActivitiesJMISSummaryOfBusinessResults': #投資活動によるキャッシュ・フロー（JMIS）、経営指標等
				self.CashFlowsFromUsedInInvestingActivitiesJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInFinancingActivitiesJMISSummaryOfBusinessResults': #財務活動によるキャッシュ・フロー（JMIS）、経営指標等
				self.CashFlowsFromUsedInFinancingActivitiesJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashAndCashEquivalentsJMISSummaryOfBusinessResults': #現金及び現金同等物（JMIS）、経営指標等
				self.CashAndCashEquivalentsJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RevenuesUSGAAPSummaryOfBusinessResults': #売上高（US GAAP）、経営指標等
				self.RevenuesUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'OperatingIncomeLossUSGAAPSummaryOfBusinessResults': #営業利益又は営業損失（△）（US GAAP）、経営指標等
				self.OperatingIncomeLossUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossBeforeTaxUSGAAPSummaryOfBusinessResults': #税引前利益又は税引前損失（△）（US GAAP）、経営指標等
				self.ProfitLossBeforeTaxUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetIncomeLossAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults': #当社株主に帰属する純利益又は純損失（△）（US GAAP）、経営指標等
				self.NetIncomeLossAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeUSGAAPSummaryOfBusinessResults': #包括利益（US GAAP）、経営指標等
				self.ComprehensiveIncomeUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults': #当社株主に帰属する包括利益（US GAAP）、経営指標等
				self.ComprehensiveIncomeAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults': #株主資本（US GAAP）、経営指標等
				self.EquityAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityIncludingPortionAttributableToNonControllingInterestUSGAAPSummaryOfBusinessResults': #純資産額（US GAAP）、経営指標等
				self.EquityIncludingPortionAttributableToNonControllingInterestUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'TotalAssetsUSGAAPSummaryOfBusinessResults': #総資産額（US GAAP）、経営指標等
				self.TotalAssetsUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityAttributableToOwnersOfParentPerShareUSGAAPSummaryOfBusinessResults': #１株当たり株主資本（US GAAP）、経営指標等
				self.EquityAttributableToOwnersOfParentPerShareUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'BasicEarningsLossPerShareUSGAAPSummaryOfBusinessResults': #基本的１株当たり当社株主に帰属する利益又は損失（△）（US GAAP）、経営指標等
				self.BasicEarningsLossPerShareUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'DilutedEarningsLossPerShareUSGAAPSummaryOfBusinessResults': #希薄化後１株当たり当社株主に帰属する利益又は損失（△）（US GAAP）、経営指標等
				self.DilutedEarningsLossPerShareUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityToAssetRatioUSGAAPSummaryOfBusinessResults': #自己資本比率（US GAAP）、経営指標等
				self.EquityToAssetRatioUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'PriceEarningsRatioUSGAAPSummaryOfBusinessResults': #株価収益率（US GAAP）、経営指標等
				self.PriceEarningsRatioUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RateOfReturnOnEquityUSGAAPSummaryOfBusinessResults': #株主資本利益率（US GAAP）、経営指標等
				self.RateOfReturnOnEquityUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInOperatingActivitiesUSGAAPSummaryOfBusinessResults': #営業活動によるキャッシュ・フロー（US GAAP）、経営指標等
				self.CashFlowsFromUsedInOperatingActivitiesUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInInvestingActivitiesUSGAAPSummaryOfBusinessResults': #投資活動によるキャッシュ・フロー（US GAAP）、経営指標等
				self.CashFlowsFromUsedInInvestingActivitiesUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInFinancingActivitiesUSGAAPSummaryOfBusinessResults': #財務活動によるキャッシュ・フロー（US GAAP）、経営指標等
				self.CashFlowsFromUsedInFinancingActivitiesUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashAndCashEquivalentsUSGAAPSummaryOfBusinessResults': #現金及び現金同等物（US GAAP）、経営指標等
				self.CashAndCashEquivalentsUSGAAPSummaryOfBusinessResults = fact.value

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

			elif fact.concept.qname.localName == 'OverviewOfBusinessHeading': #事業の状況 [目次項目]
				self.OverviewOfBusinessHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessRisksHeading': #事業等のリスク [目次項目]
				self.BusinessRisksHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessRisksTextBlock': #事業等のリスク [テキストブロック]
				self.BusinessRisksTextBlock = fact.value

			elif fact.concept.qname.localName == 'MaterialMattersRelatingToGoingConcernEtcBusinessRisksTextBlock': #重要事象等の内容、分析及び対応策、事業等のリスク [テキストブロック]
				self.MaterialMattersRelatingToGoingConcernEtcBusinessRisksTextBlock = fact.value

			elif fact.concept.qname.localName == 'ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsHeading': #経営者による財政状態、経営成績及びキャッシュ・フローの状況の分析 [目次項目]
				self.ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsTextBlock': #経営者による財政状態、経営成績及びキャッシュ・フローの状況の分析 [テキストブロック]
				self.ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsTextBlock = fact.value

			elif fact.concept.qname.localName == 'BasicPolicyRegardingControlOfCompanyTextBlock': #会社の支配に関する基本方針 [テキストブロック]
				self.BasicPolicyRegardingControlOfCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'CriticalContractsForOperationHeading': #経営上の重要な契約等 [目次項目]
				self.CriticalContractsForOperationHeading = fact.value

			elif fact.concept.qname.localName == 'CriticalContractsForOperationTextBlock': #経営上の重要な契約等 [テキストブロック]
				self.CriticalContractsForOperationTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutReportingCompanyHeading': #提出会社の状況 [目次項目]
				self.InformationAboutReportingCompanyHeading = fact.value

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

			elif fact.concept.qname.localName == 'IssuedSharesTotalNumberOfSharesEtcHeading': #発行済株式、株式の総数等 [目次項目]
				self.IssuedSharesTotalNumberOfSharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesTotalNumberOfSharesEtcTable': #発行済株式、株式の総数等 [表]
				self.IssuedSharesTotalNumberOfSharesEtcTable = fact.value

			elif fact.concept.qname.localName == 'ClassesOfSharesAxis': #株式種類 [軸]
				self.ClassesOfSharesAxis = fact.value

			elif fact.concept.qname.localName == 'TotalClassesOfSharesMember': #合計、株式種類 [メンバー] ※ディメンションデフォルト
				self.TotalClassesOfSharesMember = fact.value

			elif fact.concept.qname.localName == 'OrdinaryShareMember': #普通株式 [メンバー]
				self.OrdinaryShareMember = fact.value

			elif fact.concept.qname.localName == 'ClassAPreferredSharesMember': #Ａ種優先株式 [メンバー]
				self.ClassAPreferredSharesMember = fact.value

			elif fact.concept.qname.localName == 'ClassBPreferredSharesMember': #Ｂ種優先株式 [メンバー]
				self.ClassBPreferredSharesMember = fact.value

			elif fact.concept.qname.localName == 'ClassOnePreferredSharesMember': #第一種優先株式 [メンバー]
				self.ClassOnePreferredSharesMember = fact.value

			elif fact.concept.qname.localName == 'ClassTwoPreferredSharesMember': #第二種優先株式 [メンバー]
				self.ClassTwoPreferredSharesMember = fact.value

			elif fact.concept.qname.localName == 'ClassASharesMember': #Ａ種種類株式 [メンバー]
				self.ClassASharesMember = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesTotalNumberOfSharesEtcLineItems': #発行済株式、株式の総数等 [表示項目]
				self.IssuedSharesTotalNumberOfSharesEtcLineItems = fact.value

			elif fact.concept.qname.localName == 'ClassIssuedSharesTotalNumberOfSharesEtc': #種類、発行済株式、株式の総数等
				self.ClassIssuedSharesTotalNumberOfSharesEtc = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuedSharesIssuedSharesTotalNumberOfSharesEtc': #発行数（株）、発行済株式、株式の総数等
				self.NumberOfIssuedSharesIssuedSharesTotalNumberOfSharesEtc = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuedSharesAsOfFiscalYearEndIssuedSharesTotalNumberOfSharesEtc': #事業年度末現在発行数（株）、発行済株式、株式の総数等
				self.NumberOfIssuedSharesAsOfFiscalYearEndIssuedSharesTotalNumberOfSharesEtc = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuedSharesAsOfFilingDateIssuedSharesTotalNumberOfSharesEtc': #提出日現在発行数（株）、発行済株式、株式の総数等
				self.NumberOfIssuedSharesAsOfFilingDateIssuedSharesTotalNumberOfSharesEtc = fact.value

			elif fact.concept.qname.localName == 'NameOfFinancialInstrumentsExchangeOnWhichSecuritiesAreListedOrAuthorizedFinancialInstrumentsBusinessAssociationToWhichSecuritiesAreRegistered': #上場金融商品取引所名又は登録認可金融商品取引業協会名
				self.NameOfFinancialInstrumentsExchangeOnWhichSecuritiesAreListedOrAuthorizedFinancialInstrumentsBusinessAssociationToWhichSecuritiesAreRegistered = fact.value

			elif fact.concept.qname.localName == 'DescriptionIssuedSharesTotalNumberOfSharesEtc': #内容、発行済株式、株式の総数等
				self.DescriptionIssuedSharesTotalNumberOfSharesEtc = fact.value

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

			elif fact.concept.qname.localName == 'IssuedSharesVotingRightsHeading': #発行済株式、議決権の状況 [目次項目]
				self.IssuedSharesVotingRightsHeading = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesVotingRightsTable': #発行済株式、議決権の状況 [表]
				self.IssuedSharesVotingRightsTable = fact.value

			elif fact.concept.qname.localName == 'CategoriesIssuedSharesAxis': #区分、発行済株式 [軸]
				self.CategoriesIssuedSharesAxis = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfIssuedSharesNumberOfVotingRightsHeldByAllShareholdersMember': #発行済株式総数／総株主の議決権 [メンバー] ※ディメンションデフォルト
				self.TotalNumberOfIssuedSharesNumberOfVotingRightsHeldByAllShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'SharesWithNoVotingRightsMember': #無議決権株式 [メンバー]
				self.SharesWithNoVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'SharesWithRestrictedVotingRightsTreasurySharesEtcMember': #議決権制限株式（自己株式等） [メンバー]
				self.SharesWithRestrictedVotingRightsTreasurySharesEtcMember = fact.value

			elif fact.concept.qname.localName == 'SharesWithRestrictedVotingRightsOtherMember': #議決権制限株式（その他） [メンバー]
				self.SharesWithRestrictedVotingRightsOtherMember = fact.value

			elif fact.concept.qname.localName == 'SharesWithFullVotingRightsTreasurySharesEtcMember': #完全議決権株式（自己株式等） [メンバー]
				self.SharesWithFullVotingRightsTreasurySharesEtcMember = fact.value

			elif fact.concept.qname.localName == 'OrdinarySharesSharesWithFullVotingRightsTreasurySharesEtcMember': #普通株式、完全議決権株式（自己株式等） [メンバー]
				self.OrdinarySharesSharesWithFullVotingRightsTreasurySharesEtcMember = fact.value

			elif fact.concept.qname.localName == 'OrdinarySharesTreasurySharesSharesWithFullVotingRightsTreasurySharesEtcMember': #（自己保有株式）普通株式、完全議決権株式（自己株式等） [メンバー]
				self.OrdinarySharesTreasurySharesSharesWithFullVotingRightsTreasurySharesEtcMember = fact.value

			elif fact.concept.qname.localName == 'OrdinarySharesReciprocalHoldingSharesWithFullVotingRightsTreasurySharesEtcMember': #（相互保有株式）普通株式、完全議決権株式（自己株式等） [メンバー]
				self.OrdinarySharesReciprocalHoldingSharesWithFullVotingRightsTreasurySharesEtcMember = fact.value

			elif fact.concept.qname.localName == 'SharesWithFullVotingRightsOtherMember': #完全議決権株式（その他） [メンバー]
				self.SharesWithFullVotingRightsOtherMember = fact.value

			elif fact.concept.qname.localName == 'OrdinarySharesSharesWithFullVotingRightsOtherMember': #普通株式、完全議決権株式（その他） [メンバー]
				self.OrdinarySharesSharesWithFullVotingRightsOtherMember = fact.value

			elif fact.concept.qname.localName == 'SharesLessThanOneUnitMember': #単元未満株式 [メンバー]
				self.SharesLessThanOneUnitMember = fact.value

			elif fact.concept.qname.localName == 'OrdinarySharesSharesLessThanOneUnitMember': #普通株式、単元未満株式 [メンバー]
				self.OrdinarySharesSharesLessThanOneUnitMember = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesVotingRightsLineItems': #発行済株式、議決権の状況 [表示項目]
				self.IssuedSharesVotingRightsLineItems = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesIssuedSharesVotingRights': #株式数（株）、発行済株式、議決権の状況
				self.NumberOfSharesIssuedSharesVotingRights = fact.value

			elif fact.concept.qname.localName == 'NumberOfVotingRightsIssuedSharesVotingRights': #議決権の数（個）、発行済株式、議決権の状況
				self.NumberOfVotingRightsIssuedSharesVotingRights = fact.value

			elif fact.concept.qname.localName == 'DescriptionIssuedSharesVotingRights': #内容、発行済株式、議決権の状況
				self.DescriptionIssuedSharesVotingRights = fact.value

			elif fact.concept.qname.localName == 'TreasurySharesEtcHeading': #自己株式等 [目次項目]
				self.TreasurySharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'TreasurySharesEtcTextBlock': #自己株式等 [テキストブロック]
				self.TreasurySharesEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'TreasurySharesEtcHeading': #自己株式等 [目次項目]
				self.TreasurySharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'TreasurySharesEtcTable': #自己株式等 [表]
				self.TreasurySharesEtcTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'TotalSequentialNumbersMember': #合計、連番 [メンバー] ※ディメンションデフォルト
				self.TotalSequentialNumbersMember = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'Row4Member': #4件目 [メンバー]
				self.Row4Member = fact.value

			elif fact.concept.qname.localName == 'TreasurySharesEtcLineItems': #自己株式等 [表示項目]
				self.TreasurySharesEtcLineItems = fact.value

			elif fact.concept.qname.localName == 'NameOfShareholderTreasurySharesEtc': #所有者の氏名又は名称、自己株式等
				self.NameOfShareholderTreasurySharesEtc = fact.value

			elif fact.concept.qname.localName == 'AddressOfShareholderTreasurySharesEtc': #所有者の住所、自己株式等
				self.AddressOfShareholderTreasurySharesEtc = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldInOwnNameTreasurySharesEtc': #自己名義所有株式数（株）、自己株式等
				self.NumberOfSharesHeldInOwnNameTreasurySharesEtc = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldInOthersNamesTreasurySharesEtc': #他人名義所有株式数（株）、自己株式等
				self.NumberOfSharesHeldInOthersNamesTreasurySharesEtc = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfSharesHeldTreasurySharesEtc': #所有株式数の合計（株）、自己株式等
				self.TotalNumberOfSharesHeldTreasurySharesEtc = fact.value

			elif fact.concept.qname.localName == 'ShareholdingRatioTreasurySharesEtc': #発行済株式総数に対する所有株式数の割合（％）、自己株式等
				self.ShareholdingRatioTreasurySharesEtc = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersTextBlock': #役員の状況 [テキストブロック]
				self.InformationAboutOfficersTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfMaleDirectorsAndOtherOfficers': #役員のうち男性の人数
				self.NumberOfMaleDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'NumberOfFemaleDirectorsAndOtherOfficers': #役員のうち女性の人数
				self.NumberOfFemaleDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'RatioOfFemaleDirectorsAndOtherOfficers': #役員のうち女性の比率
				self.RatioOfFemaleDirectorsAndOtherOfficers = fact.value

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

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedFinancialStatementsHeading': #四半期連結財務諸表 [目次項目]
				self.QuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedBalanceSheetHeading': #四半期連結貸借対照表 [目次項目]
				self.QuarterlyConsolidatedBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedBalanceSheetTextBlock': #四半期連結貸借対照表 [テキストブロック]
				self.QuarterlyConsolidatedBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'CondensedQuarterlyConsolidatedStatementOfFinancialPositionJMISTextBlock': #要約四半期連結財政状態計算書（JMIS） [テキストブロック]
				self.CondensedQuarterlyConsolidatedStatementOfFinancialPositionJMISTextBlock = fact.value

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

			elif fact.concept.qname.localName == 'CondensedYearToQuarterEndConsolidatedStatementOfIncomeJMISTextBlock': #四半期連結累計期間、要約四半期連結損益計算書（JMIS） [テキストブロック]
				self.CondensedYearToQuarterEndConsolidatedStatementOfIncomeJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfIncomeUSGAAPTextBlock': #四半期連結累計期間、四半期連結損益計算書（US GAAP） [テキストブロック]
				self.YearToQuarterEndConsolidatedStatementOfIncomeUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfIncomeHeading': #四半期連結会計期間、四半期連結損益計算書 [目次項目]
				self.QuarterPeriodConsolidatedStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfIncomeTextBlock': #四半期連結会計期間、四半期連結損益計算書 [テキストブロック]
				self.QuarterPeriodConsolidatedStatementOfIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'CondensedQuarterPeriodConsolidatedStatementOfIncomeJMISTextBlock': #四半期連結会計期間、要約四半期連結損益計算書（JMIS） [テキストブロック]
				self.CondensedQuarterPeriodConsolidatedStatementOfIncomeJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfIncomeUSGAAPTextBlock': #四半期連結会計期間、四半期連結損益計算書（US GAAP） [テキストブロック]
				self.QuarterPeriodConsolidatedStatementOfIncomeUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedStatementOfComprehensiveIncomeHeading': #四半期連結包括利益計算書 [目次項目]
				self.QuarterlyConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeHeading': #四半期連結累計期間、四半期連結包括利益計算書 [目次項目]
				self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock': #四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック]
				self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeJMISTextBlock': #四半期連結累計期間、要約四半期連結包括利益計算書（JMIS） [テキストブロック]
				self.CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock': #四半期連結累計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]
				self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfComprehensiveIncomeHeading': #四半期連結会計期間、四半期連結包括利益計算書 [目次項目]
				self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfComprehensiveIncomeTextBlock': #四半期連結会計期間、四半期連結包括利益計算書 [テキストブロック]
				self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeJMISTextBlock': #四半期連結会計期間、要約四半期連結包括利益計算書（JMIS） [テキストブロック]
				self.CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock': #四半期連結会計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]
				self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading': #四半期連結損益及び包括利益計算書 [目次項目]
				self.QuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading': #四半期連結累計期間、四半期連結損益及び包括利益計算書 [目次項目]
				self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock': #四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック]
				self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = fact.value

			elif fact.concept.qname.localName == 'CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock': #四半期連結累計期間、要約四半期連結包括利益計算書（１計算書）（JMIS） [テキストブロック]
				self.CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock': #四半期連結累計期間、四半期連結損益及び包括利益計算書（US GAAP） [テキストブロック]
				self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading': #四半期連結会計期間、四半期連結損益及び包括利益計算書 [目次項目]
				self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock': #四半期連結会計期間、四半期連結損益及び包括利益計算書 [テキストブロック]
				self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = fact.value

			elif fact.concept.qname.localName == 'CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock': #四半期連結会計期間、要約四半期連結包括利益計算書（１計算書）（JMIS） [テキストブロック]
				self.CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock': #四半期連結会計期間、四半期連結損益及び包括利益計算書（US GAAP） [テキストブロック]
				self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'CondensedQuarterlyConsolidatedStatementOfChangesInEquityJMISHeading': #要約四半期連結持分変動計算書（JMIS） [目次項目]
				self.CondensedQuarterlyConsolidatedStatementOfChangesInEquityJMISHeading = fact.value

			elif fact.concept.qname.localName == 'CondensedQuarterlyConsolidatedStatementOfChangesInEquityJMISTextBlock': #要約四半期連結持分変動計算書（JMIS） [テキストブロック]
				self.CondensedQuarterlyConsolidatedStatementOfChangesInEquityJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedQuarterlyStatementOfEquityUSGAAPHeading': #四半期連結資本勘定計算書（US GAAP） [目次項目]
				self.ConsolidatedQuarterlyStatementOfEquityUSGAAPHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedQuarterlyStatementOfEquityUSGAAPTextBlock': #四半期連結資本勘定計算書（US GAAP） [テキストブロック]
				self.ConsolidatedQuarterlyStatementOfEquityUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedStatementOfCashFlowsHeading': #四半期連結キャッシュ・フロー計算書 [目次項目]
				self.QuarterlyConsolidatedStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedStatementOfCashFlowsTextBlock': #四半期連結キャッシュ・フロー計算書 [テキストブロック]
				self.QuarterlyConsolidatedStatementOfCashFlowsTextBlock = fact.value

			elif fact.concept.qname.localName == 'CondensedQuarterlyConsolidatedStatementOfCashFlowsJMISTextBlock': #要約四半期連結キャッシュ・フロー計算書（JMIS） [テキストブロック]
				self.CondensedQuarterlyConsolidatedStatementOfCashFlowsJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'QuarterlyConsolidatedStatementOfCashFlowsUSGAAPTextBlock': #四半期連結キャッシュ・フロー計算書（US GAAP） [テキストブロック]
				self.QuarterlyConsolidatedStatementOfCashFlowsUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedFinancialStatementsHeading': #注記事項、四半期連結財務諸表 [目次項目]
				self.NotesQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyConsolidatedFinancialStatementsHeading': #継続企業の前提に関する事項、四半期連結財務諸表 [目次項目]
				self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyConsolidatedFinancialStatementsTextBlock': #継続企業の前提に関する事項、四半期連結財務諸表 [テキストブロック]
				self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInScopeOfConsolidationOrEquityMethodHeading': #連結の範囲又は持分法適用の範囲の変更に関する注記 [目次項目]
				self.NotesChangesInScopeOfConsolidationOrEquityMethodHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInScopeOfConsolidationOrEquityMethodTextBlock': #連結の範囲又は持分法適用の範囲の変更に関する注記 [テキストブロック]
				self.NotesChangesInScopeOfConsolidationOrEquityMethodTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesQuarterlyConsolidatedFinancialStatementsHeading': #会計方針の変更、四半期連結財務諸表 [目次項目]
				self.NotesChangesInAccountingPoliciesQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcQuarterlyConsolidatedFinancialStatementsTextBlock': #会計基準等の改正等に伴う会計方針の変更、四半期連結財務諸表 [テキストブロック]
				self.NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesVoluntaryChangesInAccountingPoliciesQuarterlyConsolidatedFinancialStatementsTextBlock': #会計基準等の改正等以外の正当な理由による会計方針の変更、四半期連結財務諸表 [テキストブロック]
				self.NotesVoluntaryChangesInAccountingPoliciesQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsTextBlock': #会計上の見積りの変更と区別することが困難な会計方針の変更、四半期連結財務諸表 [テキストブロック]
				self.NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsHeading': #会計上の見積りの変更、四半期連結財務諸表 [目次項目]
				self.NotesChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsTextBlock': #会計上の見積りの変更、四半期連結財務諸表 [テキストブロック]
				self.NotesChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRestatementQuarterlyConsolidatedFinancialStatementsHeading': #修正再表示、四半期連結財務諸表 [目次項目]
				self.NotesRestatementQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRestatementQuarterlyConsolidatedFinancialStatementsTextBlock': #修正再表示、四半期連結財務諸表 [テキストブロック]
				self.NotesRestatementQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyConsolidatedFinancialStatementsHeading': #四半期特有の会計処理、四半期連結財務諸表 [目次項目]
				self.NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyConsolidatedFinancialStatementsTextBlock': #四半期特有の会計処理、四半期連結財務諸表 [テキストブロック]
				self.NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesAdditionalInformationQuarterlyConsolidatedFinancialStatementsHeading': #追加情報、四半期連結財務諸表 [目次項目]
				self.NotesAdditionalInformationQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesAdditionalInformationQuarterlyConsolidatedFinancialStatementsTextBlock': #追加情報、四半期連結財務諸表 [テキストブロック]
				self.NotesAdditionalInformationQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedBalanceSheetHeading': #四半期連結貸借対照表関係 [目次項目]
				self.NotesQuarterlyConsolidatedBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedBalanceSheetHeading': #四半期連結貸借対照表関係 [目次項目]
				self.NotesQuarterlyConsolidatedBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedBalanceSheetTable': #四半期連結貸借対照表関係 [表]
				self.NotesQuarterlyConsolidatedBalanceSheetTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedBalanceSheetLineItems': #四半期連結貸借対照表関係 [表示項目]
				self.NotesQuarterlyConsolidatedBalanceSheetLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingInventoriesTextBlock': #棚卸資産の内訳の注記 [テキストブロック]
				self.NotesRegardingInventoriesTextBlock = fact.value

			elif fact.concept.qname.localName == 'MerchandiseAndFinishedGoods': #商品及び製品
				self.MerchandiseAndFinishedGoods = fact.value

			elif fact.concept.qname.localName == 'WorkInProcess': #仕掛品
				self.WorkInProcess = fact.value

			elif fact.concept.qname.localName == 'RawMaterialsAndSupplies': #原材料及び貯蔵品
				self.RawMaterialsAndSupplies = fact.value

			elif fact.concept.qname.localName == 'Inventories': #棚卸資産
				self.Inventories = fact.value

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

			elif fact.concept.qname.localName == 'NotesRegardingPresentationOfGoodwillAndNegativeGoodwillTextBlock': #のれん及び負ののれんの表示に関する注記 [テキストブロック]
				self.NotesRegardingPresentationOfGoodwillAndNegativeGoodwillTextBlock = fact.value

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

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedStatementOfIncomeHeading': #四半期連結損益計算書関係 [目次項目]
				self.NotesQuarterlyConsolidatedStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedStatementOfIncomeHeading': #四半期連結損益計算書関係 [目次項目]
				self.NotesQuarterlyConsolidatedStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedStatementOfIncomeTable': #四半期連結損益計算書関係 [表]
				self.NotesQuarterlyConsolidatedStatementOfIncomeTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedStatementOfIncomeLineItems': #四半期連結損益計算書関係 [表示項目]
				self.NotesQuarterlyConsolidatedStatementOfIncomeLineItems = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock': #主要な販売費及び一般管理費 [テキストブロック]
				self.MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DepreciationSGA': #減価償却費、販売費及び一般管理費
				self.DepreciationSGA = fact.value

			elif fact.concept.qname.localName == 'ProvisionOfAllowanceForDoubtfulAccountsSGA': #貸倒引当金繰入額、販売費及び一般管理費
				self.ProvisionOfAllowanceForDoubtfulAccountsSGA = fact.value

			elif fact.concept.qname.localName == 'NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock': #売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]
				self.NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading': #四半期連結損益及び包括利益計算書関係 [目次項目]
				self.NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading': #四半期連結損益及び包括利益計算書関係 [目次項目]
				self.NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementTable': #四半期連結損益及び包括利益計算書関係 [表]
				self.NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementLineItems': #四半期連結損益及び包括利益計算書関係 [表示項目]
				self.NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementLineItems = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock': #主要な販売費及び一般管理費 [テキストブロック]
				self.MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DepreciationSGA': #減価償却費、販売費及び一般管理費
				self.DepreciationSGA = fact.value

			elif fact.concept.qname.localName == 'ProvisionOfAllowanceForDoubtfulAccountsSGA': #貸倒引当金繰入額、販売費及び一般管理費
				self.ProvisionOfAllowanceForDoubtfulAccountsSGA = fact.value

			elif fact.concept.qname.localName == 'NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock': #売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]
				self.NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedStatementOfCashFlowsHeading': #四半期連結キャッシュ・フロー計算書関係 [目次項目]
				self.NotesQuarterlyConsolidatedStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedStatementOfCashFlowsHeading': #四半期連結キャッシュ・フロー計算書関係 [目次項目]
				self.NotesQuarterlyConsolidatedStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedStatementOfCashFlowsTable': #四半期連結キャッシュ・フロー計算書関係 [表]
				self.NotesQuarterlyConsolidatedStatementOfCashFlowsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyConsolidatedStatementOfCashFlowsLineItems': #四半期連結キャッシュ・フロー計算書関係 [表示項目]
				self.NotesQuarterlyConsolidatedStatementOfCashFlowsLineItems = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatQuarterlyStatementOfCashFlowsHasNotBeenPreparedTextBlock': #四半期キャッシュ・フロー計算書を作成しない場合の注記 [テキストブロック]
				self.DescriptionOfFactThatQuarterlyStatementOfCashFlowsHasNotBeenPreparedTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock': #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
				self.ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock': #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
				self.DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesEquityQuarterlyConsolidatedFinancialStatementsHeading': #株主資本等に関する注記、四半期連結財務諸表 [目次項目]
				self.NotesEquityQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesEquityQuarterlyConsolidatedFinancialStatementsHeading': #株主資本等に関する注記、四半期連結財務諸表 [目次項目]
				self.NotesEquityQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesEquityQuarterlyConsolidatedFinancialStatementsTable': #株主資本等に関する注記、四半期連結財務諸表 [表]
				self.NotesEquityQuarterlyConsolidatedFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesEquityQuarterlyConsolidatedFinancialStatementsLineItems': #株主資本等に関する注記、四半期連結財務諸表 [表示項目]
				self.NotesEquityQuarterlyConsolidatedFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingDividendTextBlock': #配当に関する注記 [テキストブロック]
				self.NotesRegardingDividendTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesWhenThereIsSignificantChangesInAmountsOfEquityTextBlock': #株主資本の金額に著しい変動があった場合の注記 [テキストブロック]
				self.NotesWhenThereIsSignificantChangesInAmountsOfEquityTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesFinancialInstrumentsQuarterlyConsolidatedFinancialStatementsHeading': #金融商品関係、四半期連結財務諸表 [目次項目]
				self.NotesFinancialInstrumentsQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesFinancialInstrumentsQuarterlyConsolidatedFinancialStatementsTextBlock': #金融商品関係、四半期連結財務諸表 [テキストブロック]
				self.NotesFinancialInstrumentsQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSecuritiesQuarterlyConsolidatedFinancialStatementsHeading': #有価証券関係、四半期連結財務諸表 [目次項目]
				self.NotesSecuritiesQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSecuritiesQuarterlyConsolidatedFinancialStatementsTextBlock': #有価証券関係、四半期連結財務諸表 [テキストブロック]
				self.NotesSecuritiesQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesMoneyHeldInTrustQuarterlyConsolidatedFinancialStatementsHeading': #金銭の信託関係、四半期連結財務諸表 [目次項目]
				self.NotesMoneyHeldInTrustQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesMoneyHeldInTrustQuarterlyConsolidatedFinancialStatementsTextBlock': #金銭の信託関係、四半期連結財務諸表 [テキストブロック]
				self.NotesMoneyHeldInTrustQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesDerivativesQuarterlyConsolidatedFinancialStatementsHeading': #デリバティブ取引関係、四半期連結財務諸表 [目次項目]
				self.NotesDerivativesQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesDerivativesQuarterlyConsolidatedFinancialStatementsTextBlock': #デリバティブ取引関係、四半期連結財務諸表 [テキストブロック]
				self.NotesDerivativesQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesBusinessCombinationsQuarterlyConsolidatedFinancialStatementsHeading': #企業結合等関係、四半期連結財務諸表 [目次項目]
				self.NotesBusinessCombinationsQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesBusinessCombinationsQuarterlyConsolidatedFinancialStatementsTextBlock': #企業結合等関係、四半期連結財務諸表 [テキストブロック]
				self.NotesBusinessCombinationsQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRevenueRecognitionQuarterlyConsolidatedFinancialStatementsHeading': #収益認識関係、四半期連結財務諸表 [目次項目]
				self.NotesRevenueRecognitionQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRevenueRecognitionQuarterlyConsolidatedFinancialStatementsTextBlock': #収益認識関係、四半期連結財務諸表 [テキストブロック]
				self.NotesRevenueRecognitionQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading': #セグメント情報等、四半期連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock': #セグメント情報等、四半期連結財務諸表 [テキストブロック]
				self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading': #セグメント情報等、四半期連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTable': #セグメント情報等、四半期連結財務諸表 [表]
				self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsLineItems': #セグメント情報等、四半期連結財務諸表 [表示項目]
				self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatCompanysBusinessComprisesSingleSegment': #単一セグメントである旨
				self.DescriptionOfFactThatCompanysBusinessComprisesSingleSegment = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading': #セグメント情報等、四半期連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfSalesAndProfitLossForEachReportableSegmentTable': #報告セグメントごとの売上高及び利益又は損失の金額に関する情報 [表]
				self.DisclosureOfSalesAndProfitLossForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

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

			elif fact.concept.qname.localName == 'DisclosureOfSalesAndProfitLossForEachReportableSegmentLineItems': #報告セグメントごとの売上高及び利益又は損失の金額に関する情報 [表示項目]
				self.DisclosureOfSalesAndProfitLossForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'SalesSegmentInformationAbstract': #売上高、セグメント情報 [タイトル項目]
				self.SalesSegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'RevenuesFromExternalCustomers': #外部顧客への売上高
				self.RevenuesFromExternalCustomers = fact.value

			elif fact.concept.qname.localName == 'TransactionsWithOtherSegments': #セグメント間の内部売上高又は振替高
				self.TransactionsWithOtherSegments = fact.value

			elif fact.concept.qname.localName == 'NetSales': #売上高
				self.NetSales = fact.value

			elif fact.concept.qname.localName == 'Revenue': #売上収益
				self.Revenue = fact.value

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

			elif fact.concept.qname.localName == 'ProfitLossAttributableToOwnersOfParent': #親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）
				self.ProfitLossAttributableToOwnersOfParent = fact.value

			elif fact.concept.qname.localName == 'ProfitLoss': #当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）
				self.ProfitLoss = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading': #セグメント情報等、四半期連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTable': #セグメント情報等、四半期連結財務諸表 [表]
				self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsLineItems': #セグメント情報等、四半期連結財務諸表 [表示項目]
				self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'FootnotesRegardingSegmentInformationTableTextBlock': #セグメント表の脚注 [テキストブロック]
				self.FootnotesRegardingSegmentInformationTableTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutAssetsForEachReportableSegmentTextBlock': #報告セグメントごとの資産に関する情報 [テキストブロック]
				self.InformationAboutAssetsForEachReportableSegmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock': #報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
				self.DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfChangesEtcInReportableSegmentsTextBlock': #報告セグメントの変更等に関する事項 [テキストブロック]
				self.DisclosureOfChangesEtcInReportableSegmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock': #報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]
				self.InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesPerShareInformationQuarterlyConsolidatedFinancialStatementsHeading': #１株当たり情報、四半期連結財務諸表 [目次項目]
				self.NotesPerShareInformationQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesPerShareInformationQuarterlyConsolidatedFinancialStatementsTextBlock': #１株当たり情報、四半期連結財務諸表 [テキストブロック]
				self.NotesPerShareInformationQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantEventsAfterReportingPeriodQuarterlyConsolidatedFinancialStatementsHeading': #重要な後発事象、四半期連結財務諸表 [目次項目]
				self.NotesSignificantEventsAfterReportingPeriodQuarterlyConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantEventsAfterReportingPeriodQuarterlyConsolidatedFinancialStatementsTextBlock': #重要な後発事象、四半期連結財務諸表 [テキストブロック]
				self.NotesSignificantEventsAfterReportingPeriodQuarterlyConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesToQuarterlyConsolidatedFinancialStatementsJMISHeading': #四半期連結財務諸表注記事項（JMIS） [目次項目]
				self.NotesToQuarterlyConsolidatedFinancialStatementsJMISHeading = fact.value

			elif fact.concept.qname.localName == 'NotesToQuarterlyConsolidatedFinancialStatementsJMISTextBlock': #四半期連結財務諸表注記事項（JMIS） [テキストブロック]
				self.NotesToQuarterlyConsolidatedFinancialStatementsJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesToQuarterlyConsolidatedFinancialStatementsUSGAAPHeading': #四半期連結財務諸表注記事項（US GAAP） [目次項目]
				self.NotesToQuarterlyConsolidatedFinancialStatementsUSGAAPHeading = fact.value

			elif fact.concept.qname.localName == 'NotesToQuarterlyConsolidatedFinancialStatementsUSGAAPTextBlock': #四半期連結財務諸表注記事項（US GAAP） [テキストブロック]
				self.NotesToQuarterlyConsolidatedFinancialStatementsUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationConsolidatedFinancialStatementsEtcHeading': #その他、連結財務諸表等 [目次項目]
				self.OtherInformationConsolidatedFinancialStatementsEtcHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationConsolidatedFinancialStatementsEtcTextBlock': #その他、連結財務諸表等 [テキストブロック]
				self.OtherInformationConsolidatedFinancialStatementsEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'PriorYearConsolidatedFinancialStatementsPreapredInAccordanceWithJMISHeading': #修正国際基準による前連結会計年度に係る連結財務諸表 [目次項目]
				self.PriorYearConsolidatedFinancialStatementsPreapredInAccordanceWithJMISHeading = fact.value

			elif fact.concept.qname.localName == 'PriorYearConsolidatedFinancialStatementsPreapredInAccordanceWithJMISTextBlock': #修正国際基準による前連結会計年度に係る連結財務諸表 [テキストブロック]
				self.PriorYearConsolidatedFinancialStatementsPreapredInAccordanceWithJMISTextBlock = fact.value

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

			elif fact.concept.qname.localName == 'NotesQuarterlyFinancialStatementsHeading': #注記事項、四半期財務諸表 [目次項目]
				self.NotesQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyFinancialStatementsHeading': #継続企業の前提に関する事項、四半期財務諸表 [目次項目]
				self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyFinancialStatementsTextBlock': #継続企業の前提に関する事項、四半期財務諸表 [テキストブロック]
				self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesQuarterlyFinancialStatementsHeading': #会計方針の変更、四半期財務諸表 [目次項目]
				self.NotesChangesInAccountingPoliciesQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcQuarterlyFinancialStatementsTextBlock': #会計基準等の改正等に伴う会計方針の変更、四半期財務諸表 [テキストブロック]
				self.NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesVoluntaryChangesInAccountingPoliciesQuarterlyFinancialStatementsTextBlock': #会計基準等の改正等以外の正当な理由による会計方針の変更、四半期財務諸表 [テキストブロック]
				self.NotesVoluntaryChangesInAccountingPoliciesQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesQuarterlyFinancialStatementsTextBlock': #会計上の見積りの変更と区別することが困難な会計方針の変更、四半期財務諸表 [テキストブロック]
				self.NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingEstimatesQuarterlyFinancialStatementsHeading': #会計上の見積りの変更、四半期財務諸表 [目次項目]
				self.NotesChangesInAccountingEstimatesQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingEstimatesQuarterlyFinancialStatementsTextBlock': #会計上の見積りの変更、四半期財務諸表 [テキストブロック]
				self.NotesChangesInAccountingEstimatesQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRestatementQuarterlyFinancialStatementsHeading': #修正再表示、四半期財務諸表 [目次項目]
				self.NotesRestatementQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRestatementQuarterlyFinancialStatementsTextBlock': #修正再表示、四半期財務諸表 [テキストブロック]
				self.NotesRestatementQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyFinancialStatementsHeading': #四半期特有の会計処理、四半期財務諸表 [目次項目]
				self.NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyFinancialStatementsTextBlock': #四半期特有の会計処理、四半期財務諸表 [テキストブロック]
				self.NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesAdditionalInformationQuarterlyFinancialStatementsHeading': #追加情報、四半期財務諸表 [目次項目]
				self.NotesAdditionalInformationQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesAdditionalInformationQuarterlyFinancialStatementsTextBlock': #追加情報、四半期財務諸表 [テキストブロック]
				self.NotesAdditionalInformationQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyBalanceSheetHeading': #四半期貸借対照表関係 [目次項目]
				self.NotesQuarterlyBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyBalanceSheetHeading': #四半期貸借対照表関係 [目次項目]
				self.NotesQuarterlyBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyBalanceSheetTable': #四半期貸借対照表関係 [表]
				self.NotesQuarterlyBalanceSheetTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyBalanceSheetLineItems': #四半期貸借対照表関係 [表示項目]
				self.NotesQuarterlyBalanceSheetLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingInventoriesTextBlock': #棚卸資産の内訳の注記 [テキストブロック]
				self.NotesRegardingInventoriesTextBlock = fact.value

			elif fact.concept.qname.localName == 'MerchandiseAndFinishedGoods': #商品及び製品
				self.MerchandiseAndFinishedGoods = fact.value

			elif fact.concept.qname.localName == 'WorkInProcess': #仕掛品
				self.WorkInProcess = fact.value

			elif fact.concept.qname.localName == 'RawMaterialsAndSupplies': #原材料及び貯蔵品
				self.RawMaterialsAndSupplies = fact.value

			elif fact.concept.qname.localName == 'Inventories': #棚卸資産
				self.Inventories = fact.value

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

			elif fact.concept.qname.localName == 'NotesQuarterlyStatementOfIncomeHeading': #四半期損益計算書関係 [目次項目]
				self.NotesQuarterlyStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyStatementOfIncomeHeading': #四半期損益計算書関係 [目次項目]
				self.NotesQuarterlyStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyStatementOfIncomeTable': #四半期損益計算書関係 [表]
				self.NotesQuarterlyStatementOfIncomeTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyStatementOfIncomeLineItems': #四半期損益計算書関係 [表示項目]
				self.NotesQuarterlyStatementOfIncomeLineItems = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock': #主要な販売費及び一般管理費 [テキストブロック]
				self.MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DepreciationSGA': #減価償却費、販売費及び一般管理費
				self.DepreciationSGA = fact.value

			elif fact.concept.qname.localName == 'ProvisionOfAllowanceForDoubtfulAccountsSGA': #貸倒引当金繰入額、販売費及び一般管理費
				self.ProvisionOfAllowanceForDoubtfulAccountsSGA = fact.value

			elif fact.concept.qname.localName == 'NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock': #売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]
				self.NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyStatementOfCashFlowsHeading': #四半期キャッシュ・フロー計算書関係 [目次項目]
				self.NotesQuarterlyStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyStatementOfCashFlowsHeading': #四半期キャッシュ・フロー計算書関係 [目次項目]
				self.NotesQuarterlyStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyStatementOfCashFlowsTable': #四半期キャッシュ・フロー計算書関係 [表]
				self.NotesQuarterlyStatementOfCashFlowsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesQuarterlyStatementOfCashFlowsLineItems': #四半期キャッシュ・フロー計算書関係 [表示項目]
				self.NotesQuarterlyStatementOfCashFlowsLineItems = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatQuarterlyStatementOfCashFlowsHasNotBeenPreparedTextBlock': #四半期キャッシュ・フロー計算書を作成しない場合の注記 [テキストブロック]
				self.DescriptionOfFactThatQuarterlyStatementOfCashFlowsHasNotBeenPreparedTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock': #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
				self.ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock': #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
				self.DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesEquityQuarterlyFinancialStatementsHeading': #株主資本等に関する注記、四半期財務諸表 [目次項目]
				self.NotesEquityQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesEquityQuarterlyFinancialStatementsHeading': #株主資本等に関する注記、四半期財務諸表 [目次項目]
				self.NotesEquityQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesEquityQuarterlyFinancialStatementsTable': #株主資本等に関する注記、四半期財務諸表 [表]
				self.NotesEquityQuarterlyFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesEquityQuarterlyFinancialStatementsLineItems': #株主資本等に関する注記、四半期財務諸表 [表示項目]
				self.NotesEquityQuarterlyFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingDividendTextBlock': #配当に関する注記 [テキストブロック]
				self.NotesRegardingDividendTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesWhenThereIsSignificantChangesInAmountsOfEquityTextBlock': #株主資本の金額に著しい変動があった場合の注記 [テキストブロック]
				self.NotesWhenThereIsSignificantChangesInAmountsOfEquityTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesFinancialInstrumentsQuarterlyFinancialStatementsHeading': #金融商品関係、四半期財務諸表 [目次項目]
				self.NotesFinancialInstrumentsQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesFinancialInstrumentsQuarterlyFinancialStatementsTextBlock': #金融商品関係、四半期財務諸表 [テキストブロック]
				self.NotesFinancialInstrumentsQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSecuritiesQuarterlyFinancialStatementsHeading': #有価証券関係、四半期財務諸表 [目次項目]
				self.NotesSecuritiesQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSecuritiesQuarterlyFinancialStatementsTextBlock': #有価証券関係、四半期財務諸表 [テキストブロック]
				self.NotesSecuritiesQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesMoneyHeldInTrustQuarterlyFinancialStatementsHeading': #金銭の信託関係、四半期財務諸表 [目次項目]
				self.NotesMoneyHeldInTrustQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesMoneyHeldInTrustQuarterlyFinancialStatementsTextBlock': #金銭の信託関係、四半期財務諸表 [テキストブロック]
				self.NotesMoneyHeldInTrustQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesDerivativesQuarterlyFinancialStatementsHeading': #デリバティブ取引関係、四半期財務諸表 [目次項目]
				self.NotesDerivativesQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesDerivativesQuarterlyFinancialStatementsTextBlock': #デリバティブ取引関係、四半期財務諸表 [テキストブロック]
				self.NotesDerivativesQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesBusinessCombinationsQuarterlyFinancialStatementsHeading': #企業結合等関係、四半期財務諸表 [目次項目]
				self.NotesBusinessCombinationsQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesBusinessCombinationsQuarterlyFinancialStatementsTextBlock': #企業結合等関係、四半期財務諸表 [テキストブロック]
				self.NotesBusinessCombinationsQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRevenueRecognitionQuarterlyFinancialStatementsHeading': #収益認識関係、四半期財務諸表 [目次項目]
				self.NotesRevenueRecognitionQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRevenueRecognitionQuarterlyFinancialStatementsTextBlock': #収益認識関係、四半期財務諸表 [テキストブロック]
				self.NotesRevenueRecognitionQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading': #セグメント情報等、四半期財務諸表 [目次項目]
				self.NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyFinancialStatementsTextBlock': #セグメント情報等、四半期財務諸表 [テキストブロック]
				self.NotesSegmentInformationEtcQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading': #セグメント情報等、四半期財務諸表 [目次項目]
				self.NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyFinancialStatementsTable': #セグメント情報等、四半期財務諸表 [表]
				self.NotesSegmentInformationEtcQuarterlyFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyFinancialStatementsLineItems': #セグメント情報等、四半期財務諸表 [表示項目]
				self.NotesSegmentInformationEtcQuarterlyFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatCompanysBusinessComprisesSingleSegment': #単一セグメントである旨
				self.DescriptionOfFactThatCompanysBusinessComprisesSingleSegment = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading': #セグメント情報等、四半期財務諸表 [目次項目]
				self.NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfSalesAndProfitLossForEachReportableSegmentTable': #報告セグメントごとの売上高及び利益又は損失の金額に関する情報 [表]
				self.DisclosureOfSalesAndProfitLossForEachReportableSegmentTable = fact.value

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

			elif fact.concept.qname.localName == 'DisclosureOfSalesAndProfitLossForEachReportableSegmentLineItems': #報告セグメントごとの売上高及び利益又は損失の金額に関する情報 [表示項目]
				self.DisclosureOfSalesAndProfitLossForEachReportableSegmentLineItems = fact.value

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

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading': #セグメント情報等、四半期財務諸表 [目次項目]
				self.NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyFinancialStatementsTable': #セグメント情報等、四半期財務諸表 [表]
				self.NotesSegmentInformationEtcQuarterlyFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcQuarterlyFinancialStatementsLineItems': #セグメント情報等、四半期財務諸表 [表示項目]
				self.NotesSegmentInformationEtcQuarterlyFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'FootnotesRegardingSegmentInformationTableTextBlock': #セグメント表の脚注 [テキストブロック]
				self.FootnotesRegardingSegmentInformationTableTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutAssetsForEachReportableSegmentTextBlock': #報告セグメントごとの資産に関する情報 [テキストブロック]
				self.InformationAboutAssetsForEachReportableSegmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock': #報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
				self.DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfChangesEtcInReportableSegmentsTextBlock': #報告セグメントの変更等に関する事項 [テキストブロック]
				self.DisclosureOfChangesEtcInReportableSegmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock': #報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]
				self.InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedQuarterlyFinancialStatementsHeading': #持分法損益等、四半期財務諸表 [目次項目]
				self.NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedQuarterlyFinancialStatementsTextBlock': #持分法損益等、四半期財務諸表 [テキストブロック]
				self.NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesPerShareInformationQuarterlyFinancialStatementsHeading': #１株当たり情報、四半期財務諸表 [目次項目]
				self.NotesPerShareInformationQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesPerShareInformationQuarterlyFinancialStatementsTextBlock': #１株当たり情報、四半期財務諸表 [テキストブロック]
				self.NotesPerShareInformationQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantEventsAfterReportingPeriodQuarterlyFinancialStatementsHeading': #重要な後発事象、四半期財務諸表 [目次項目]
				self.NotesSignificantEventsAfterReportingPeriodQuarterlyFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantEventsAfterReportingPeriodQuarterlyFinancialStatementsTextBlock': #重要な後発事象、四半期財務諸表 [テキストブロック]
				self.NotesSignificantEventsAfterReportingPeriodQuarterlyFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationFinancialStatementsEtcHeading': #その他、財務諸表等 [目次項目]
				self.OtherInformationFinancialStatementsEtcHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationFinancialStatementsEtcTextBlock': #その他、財務諸表等 [テキストブロック]
				self.OtherInformationFinancialStatementsEtcTextBlock = fact.value

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

			elif fact.concept.qname.localName == 'IndependentAuditorsReportHeading': #独立監査人の報告書 [目次項目]
				self.IndependentAuditorsReportHeading = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportConsolidatedTextBlock': #独立監査人の報告書、連結 [テキストブロック]
				self.IndependentAuditorsReportConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'AuditFirm1Consolidated': #監査法人１、連結
				self.AuditFirm1Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA1AuditFirm1Consolidated': #公認会計士１、監査法人１、連結
				self.CPA1AuditFirm1Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA2AuditFirm1Consolidated': #公認会計士２、監査法人１、連結
				self.CPA2AuditFirm1Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA3AuditFirm1Consolidated': #公認会計士３、監査法人１、連結
				self.CPA3AuditFirm1Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA4AuditFirm1Consolidated': #公認会計士４、監査法人１、連結
				self.CPA4AuditFirm1Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA5AuditFirm1Consolidated': #公認会計士５、監査法人１、連結
				self.CPA5AuditFirm1Consolidated = fact.value

			elif fact.concept.qname.localName == 'AuditFirm2Consolidated': #監査法人２、連結
				self.AuditFirm2Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA1AuditFirm2Consolidated': #公認会計士１、監査法人２、連結
				self.CPA1AuditFirm2Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA2AuditFirm2Consolidated': #公認会計士２、監査法人２、連結
				self.CPA2AuditFirm2Consolidated = fact.value

			elif fact.concept.qname.localName == 'KeyAuditMattersConsolidatedTextBlock': #監査上の主要な検討事項、連結 [テキストブロック]
				self.KeyAuditMattersConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewKAMConsolidatedTextBlock': #全体概要、監査上の主要な検討事項、連結 [テキストブロック]
				self.OverviewKAMConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportNonConsolidatedTextBlock': #独立監査人の報告書、個別 [テキストブロック]
				self.IndependentAuditorsReportNonConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'AuditFirm1NonConsolidated': #監査法人１、個別
				self.AuditFirm1NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA1AuditFirm1NonConsolidated': #公認会計士１、監査法人１、個別
				self.CPA1AuditFirm1NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA2AuditFirm1NonConsolidated': #公認会計士２、監査法人１、個別
				self.CPA2AuditFirm1NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA3AuditFirm1NonConsolidated': #公認会計士３、監査法人１、個別
				self.CPA3AuditFirm1NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA4AuditFirm1NonConsolidated': #公認会計士４、監査法人１、個別
				self.CPA4AuditFirm1NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA5AuditFirm1NonConsolidated': #公認会計士５、監査法人１、個別
				self.CPA5AuditFirm1NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'AuditFirm2NonConsolidated': #監査法人２、個別
				self.AuditFirm2NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA1AuditFirm2NonConsolidated': #公認会計士１、監査法人２、個別
				self.CPA1AuditFirm2NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA2AuditFirm2NonConsolidated': #公認会計士２、監査法人２、個別
				self.CPA2AuditFirm2NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'KeyAuditMattersNonConsolidatedTextBlock': #監査上の主要な検討事項、個別 [テキストブロック]
				self.KeyAuditMattersNonConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewKAMNonConsolidatedTextBlock': #全体概要、監査上の主要な検討事項、個別 [テキストブロック]
				self.OverviewKAMNonConsolidatedTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo43QuarterlySecuritiesReportHeading(self): #企業内容等の開示に関する内閣府令 第四号の三様式 四半期報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo43QuarterlySecuritiesReportHeading

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

	def getQuarterlyAccountingPeriodCoverPage(self): #四半期会計期間、表紙
		return self.QuarterlyAccountingPeriodCoverPage

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

	def getBusinessResultsOfGroupHeading(self): #連結経営指標等 [目次項目]
		return self.BusinessResultsOfGroupHeading

	def getBusinessResultsOfGroupTextBlock(self): #連結経営指標等 [テキストブロック]
		return self.BusinessResultsOfGroupTextBlock

	def getBusinessResultsOfGroupHeading(self): #連結経営指標等 [目次項目]
		return self.BusinessResultsOfGroupHeading

	def getBusinessResultsOfGroupTable(self): #連結経営指標等 [表]
		return self.BusinessResultsOfGroupTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getBusinessResultsOfGroupLineItems(self): #連結経営指標等 [表示項目]
		return self.BusinessResultsOfGroupLineItems

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

	def getProfitLossAttributableToOwnersOfParentSummaryOfBusinessResults(self): #親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）、経営指標等
		return self.ProfitLossAttributableToOwnersOfParentSummaryOfBusinessResults

	def getComprehensiveIncomeSummaryOfBusinessResults(self): #包括利益、経営指標等
		return self.ComprehensiveIncomeSummaryOfBusinessResults

	def getNetAssetsSummaryOfBusinessResults(self): #純資産額、経営指標等
		return self.NetAssetsSummaryOfBusinessResults

	def getTotalAssetsSummaryOfBusinessResults(self): #総資産額、経営指標等
		return self.TotalAssetsSummaryOfBusinessResults

	def getNetAssetsPerShareSummaryOfBusinessResults(self): #１株当たり純資産額、経営指標等
		return self.NetAssetsPerShareSummaryOfBusinessResults

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

	def getRevenueIFRSSummaryOfBusinessResults(self): #売上収益（IFRS）、経営指標等
		return self.RevenueIFRSSummaryOfBusinessResults

	def getProfitLossBeforeTaxIFRSSummaryOfBusinessResults(self): #税引前利益又は税引前損失（△）（IFRS）、経営指標等
		return self.ProfitLossBeforeTaxIFRSSummaryOfBusinessResults

	def getProfitLossFromContinuingOperationsIFRSSummaryOfBusinessResults(self): #継続事業からの当期利益又は当期損失（△）（IFRS）、経営指標等
		return self.ProfitLossFromContinuingOperationsIFRSSummaryOfBusinessResults

	def getProfitLossIFRSSummaryOfBusinessResults(self): #当期利益又は当期損失（△）（IFRS）、経営指標等
		return self.ProfitLossIFRSSummaryOfBusinessResults

	def getProfitLossAttributableToOwnersOfParentIFRSSummaryOfBusinessResults(self): #当期利益又は当期損失（△）：親会社の所有者に帰属（IFRS）、経営指標等
		return self.ProfitLossAttributableToOwnersOfParentIFRSSummaryOfBusinessResults

	def getComprehensiveIncomeIFRSSummaryOfBusinessResults(self): #当期包括利益（IFRS）、経営指標等
		return self.ComprehensiveIncomeIFRSSummaryOfBusinessResults

	def getComprehensiveIncomeAttributableToOwnersOfParentIFRSSummaryOfBusinessResults(self): #当期包括利益：親会社の所有者に帰属（IFRS）、経営指標等
		return self.ComprehensiveIncomeAttributableToOwnersOfParentIFRSSummaryOfBusinessResults

	def getEquityAttributableToOwnersOfParentIFRSSummaryOfBusinessResults(self): #親会社の所有者に帰属する持分（IFRS）、経営指標等
		return self.EquityAttributableToOwnersOfParentIFRSSummaryOfBusinessResults

	def getTotalAssetsIFRSSummaryOfBusinessResults(self): #総資産額（IFRS）、経営指標等
		return self.TotalAssetsIFRSSummaryOfBusinessResults

	def getEquityToAssetRatioIFRSSummaryOfBusinessResults(self): #１株当たり親会社所有者帰属持分（IFRS）、経営指標等
		return self.EquityToAssetRatioIFRSSummaryOfBusinessResults

	def getBasicEarningsLossPerShareIFRSSummaryOfBusinessResults(self): #基本的１株当たり利益又は損失（△）（IFRS）、経営指標等
		return self.BasicEarningsLossPerShareIFRSSummaryOfBusinessResults

	def getDilutedEarningsLossPerShareIFRSSummaryOfBusinessResults(self): #希薄化後１株当たり利益又は損失（△）（IFRS）、経営指標等
		return self.DilutedEarningsLossPerShareIFRSSummaryOfBusinessResults

	def getRatioOfOwnersEquityToGrossAssetsIFRSSummaryOfBusinessResults(self): #親会社所有者帰属持分比率（IFRS）、経営指標等
		return self.RatioOfOwnersEquityToGrossAssetsIFRSSummaryOfBusinessResults

	def getRateOfReturnOnEquityIFRSSummaryOfBusinessResults(self): #親会社所有者帰属持分利益率（IFRS）、経営指標等
		return self.RateOfReturnOnEquityIFRSSummaryOfBusinessResults

	def getPriceEarningsRatioIFRSSummaryOfBusinessResults(self): #株価収益率（IFRS）、経営指標等
		return self.PriceEarningsRatioIFRSSummaryOfBusinessResults

	def getCashFlowsFromUsedInOperatingActivitiesIFRSSummaryOfBusinessResults(self): #営業活動によるキャッシュ・フロー（IFRS）、経営指標等
		return self.CashFlowsFromUsedInOperatingActivitiesIFRSSummaryOfBusinessResults

	def getCashFlowsFromUsedInInvestingActivitiesIFRSSummaryOfBusinessResults(self): #投資活動によるキャッシュ・フロー（IFRS）、経営指標等
		return self.CashFlowsFromUsedInInvestingActivitiesIFRSSummaryOfBusinessResults

	def getCashFlowsFromUsedInFinancingActivitiesIFRSSummaryOfBusinessResults(self): #財務活動によるキャッシュ・フロー（IFRS）、経営指標等
		return self.CashFlowsFromUsedInFinancingActivitiesIFRSSummaryOfBusinessResults

	def getCashAndCashEquivalentsIFRSSummaryOfBusinessResults(self): #現金及び現金同等物（IFRS）、経営指標等
		return self.CashAndCashEquivalentsIFRSSummaryOfBusinessResults

	def getRevenueJMISSummaryOfBusinessResults(self): #売上収益（JMIS）、経営指標等
		return self.RevenueJMISSummaryOfBusinessResults

	def getProfitLossBeforeTaxJMISSummaryOfBusinessResults(self): #税引前利益又は税引前損失（△）（JMIS）、経営指標等
		return self.ProfitLossBeforeTaxJMISSummaryOfBusinessResults

	def getProfitLossFromContinuingOperationsJMISSummaryOfBusinessResults(self): #継続事業からの当期利益又は当期損失（△）（JMIS）、経営指標等
		return self.ProfitLossFromContinuingOperationsJMISSummaryOfBusinessResults

	def getProfitLossJMISSummaryOfBusinessResults(self): #当期利益又は当期損失（△）（JMIS）、経営指標等
		return self.ProfitLossJMISSummaryOfBusinessResults

	def getProfitLossAttributableToOwnersOfParentJMISSummaryOfBusinessResults(self): #当期利益又は当期損失（△）：親会社の所有者に帰属（JMIS）、経営指標等
		return self.ProfitLossAttributableToOwnersOfParentJMISSummaryOfBusinessResults

	def getComprehensiveIncomeJMISSummaryOfBusinessResults(self): #当期包括利益（JMIS）、経営指標等
		return self.ComprehensiveIncomeJMISSummaryOfBusinessResults

	def getComprehensiveIncomeAttributableToOwnersOfParentJMISSummaryOfBusinessResults(self): #当期包括利益：親会社の所有者に帰属（JMIS）、経営指標等
		return self.ComprehensiveIncomeAttributableToOwnersOfParentJMISSummaryOfBusinessResults

	def getEquityAttributableToOwnersOfParentJMISSummaryOfBusinessResults(self): #親会社の所有者に帰属する持分（JMIS）、経営指標等
		return self.EquityAttributableToOwnersOfParentJMISSummaryOfBusinessResults

	def getTotalAssetsJMISSummaryOfBusinessResults(self): #総資産額（JMIS）、経営指標等
		return self.TotalAssetsJMISSummaryOfBusinessResults

	def getEquityToAssetRatioJMISSummaryOfBusinessResults(self): #１株当たり親会社所有者帰属持分（JMIS）、経営指標等
		return self.EquityToAssetRatioJMISSummaryOfBusinessResults

	def getBasicEarningsLossPerShareJMISSummaryOfBusinessResults(self): #基本的１株当たり利益又は損失（△）（JMIS）、経営指標等
		return self.BasicEarningsLossPerShareJMISSummaryOfBusinessResults

	def getDilutedEarningsLossPerShareJMISSummaryOfBusinessResults(self): #希薄化後１株当たり利益又は損失（△）（JMIS）、経営指標等
		return self.DilutedEarningsLossPerShareJMISSummaryOfBusinessResults

	def getRatioOfOwnersEquityToGrossAssetsJMISSummaryOfBusinessResults(self): #親会社所有者帰属持分比率（JMIS）、経営指標等
		return self.RatioOfOwnersEquityToGrossAssetsJMISSummaryOfBusinessResults

	def getRateOfReturnOnEquityJMISSummaryOfBusinessResults(self): #親会社所有者帰属持分利益率（JMIS）、経営指標等
		return self.RateOfReturnOnEquityJMISSummaryOfBusinessResults

	def getPriceEarningsRatioJMISSummaryOfBusinessResults(self): #株価収益率（JMIS）、経営指標等
		return self.PriceEarningsRatioJMISSummaryOfBusinessResults

	def getCashFlowsFromUsedInOperatingActivitiesJMISSummaryOfBusinessResults(self): #営業活動によるキャッシュ・フロー（JMIS）、経営指標等
		return self.CashFlowsFromUsedInOperatingActivitiesJMISSummaryOfBusinessResults

	def getCashFlowsFromUsedInInvestingActivitiesJMISSummaryOfBusinessResults(self): #投資活動によるキャッシュ・フロー（JMIS）、経営指標等
		return self.CashFlowsFromUsedInInvestingActivitiesJMISSummaryOfBusinessResults

	def getCashFlowsFromUsedInFinancingActivitiesJMISSummaryOfBusinessResults(self): #財務活動によるキャッシュ・フロー（JMIS）、経営指標等
		return self.CashFlowsFromUsedInFinancingActivitiesJMISSummaryOfBusinessResults

	def getCashAndCashEquivalentsJMISSummaryOfBusinessResults(self): #現金及び現金同等物（JMIS）、経営指標等
		return self.CashAndCashEquivalentsJMISSummaryOfBusinessResults

	def getRevenuesUSGAAPSummaryOfBusinessResults(self): #売上高（US GAAP）、経営指標等
		return self.RevenuesUSGAAPSummaryOfBusinessResults

	def getOperatingIncomeLossUSGAAPSummaryOfBusinessResults(self): #営業利益又は営業損失（△）（US GAAP）、経営指標等
		return self.OperatingIncomeLossUSGAAPSummaryOfBusinessResults

	def getProfitLossBeforeTaxUSGAAPSummaryOfBusinessResults(self): #税引前利益又は税引前損失（△）（US GAAP）、経営指標等
		return self.ProfitLossBeforeTaxUSGAAPSummaryOfBusinessResults

	def getNetIncomeLossAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults(self): #当社株主に帰属する純利益又は純損失（△）（US GAAP）、経営指標等
		return self.NetIncomeLossAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults

	def getComprehensiveIncomeUSGAAPSummaryOfBusinessResults(self): #包括利益（US GAAP）、経営指標等
		return self.ComprehensiveIncomeUSGAAPSummaryOfBusinessResults

	def getComprehensiveIncomeAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults(self): #当社株主に帰属する包括利益（US GAAP）、経営指標等
		return self.ComprehensiveIncomeAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults

	def getEquityAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults(self): #株主資本（US GAAP）、経営指標等
		return self.EquityAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults

	def getEquityIncludingPortionAttributableToNonControllingInterestUSGAAPSummaryOfBusinessResults(self): #純資産額（US GAAP）、経営指標等
		return self.EquityIncludingPortionAttributableToNonControllingInterestUSGAAPSummaryOfBusinessResults

	def getTotalAssetsUSGAAPSummaryOfBusinessResults(self): #総資産額（US GAAP）、経営指標等
		return self.TotalAssetsUSGAAPSummaryOfBusinessResults

	def getEquityAttributableToOwnersOfParentPerShareUSGAAPSummaryOfBusinessResults(self): #１株当たり株主資本（US GAAP）、経営指標等
		return self.EquityAttributableToOwnersOfParentPerShareUSGAAPSummaryOfBusinessResults

	def getBasicEarningsLossPerShareUSGAAPSummaryOfBusinessResults(self): #基本的１株当たり当社株主に帰属する利益又は損失（△）（US GAAP）、経営指標等
		return self.BasicEarningsLossPerShareUSGAAPSummaryOfBusinessResults

	def getDilutedEarningsLossPerShareUSGAAPSummaryOfBusinessResults(self): #希薄化後１株当たり当社株主に帰属する利益又は損失（△）（US GAAP）、経営指標等
		return self.DilutedEarningsLossPerShareUSGAAPSummaryOfBusinessResults

	def getEquityToAssetRatioUSGAAPSummaryOfBusinessResults(self): #自己資本比率（US GAAP）、経営指標等
		return self.EquityToAssetRatioUSGAAPSummaryOfBusinessResults

	def getPriceEarningsRatioUSGAAPSummaryOfBusinessResults(self): #株価収益率（US GAAP）、経営指標等
		return self.PriceEarningsRatioUSGAAPSummaryOfBusinessResults

	def getRateOfReturnOnEquityUSGAAPSummaryOfBusinessResults(self): #株主資本利益率（US GAAP）、経営指標等
		return self.RateOfReturnOnEquityUSGAAPSummaryOfBusinessResults

	def getCashFlowsFromUsedInOperatingActivitiesUSGAAPSummaryOfBusinessResults(self): #営業活動によるキャッシュ・フロー（US GAAP）、経営指標等
		return self.CashFlowsFromUsedInOperatingActivitiesUSGAAPSummaryOfBusinessResults

	def getCashFlowsFromUsedInInvestingActivitiesUSGAAPSummaryOfBusinessResults(self): #投資活動によるキャッシュ・フロー（US GAAP）、経営指標等
		return self.CashFlowsFromUsedInInvestingActivitiesUSGAAPSummaryOfBusinessResults

	def getCashFlowsFromUsedInFinancingActivitiesUSGAAPSummaryOfBusinessResults(self): #財務活動によるキャッシュ・フロー（US GAAP）、経営指標等
		return self.CashFlowsFromUsedInFinancingActivitiesUSGAAPSummaryOfBusinessResults

	def getCashAndCashEquivalentsUSGAAPSummaryOfBusinessResults(self): #現金及び現金同等物（US GAAP）、経営指標等
		return self.CashAndCashEquivalentsUSGAAPSummaryOfBusinessResults

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

	def getOverviewOfBusinessHeading(self): #事業の状況 [目次項目]
		return self.OverviewOfBusinessHeading

	def getBusinessRisksHeading(self): #事業等のリスク [目次項目]
		return self.BusinessRisksHeading

	def getBusinessRisksTextBlock(self): #事業等のリスク [テキストブロック]
		return self.BusinessRisksTextBlock

	def getMaterialMattersRelatingToGoingConcernEtcBusinessRisksTextBlock(self): #重要事象等の内容、分析及び対応策、事業等のリスク [テキストブロック]
		return self.MaterialMattersRelatingToGoingConcernEtcBusinessRisksTextBlock

	def getManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsHeading(self): #経営者による財政状態、経営成績及びキャッシュ・フローの状況の分析 [目次項目]
		return self.ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsHeading

	def getManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsTextBlock(self): #経営者による財政状態、経営成績及びキャッシュ・フローの状況の分析 [テキストブロック]
		return self.ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsTextBlock

	def getBasicPolicyRegardingControlOfCompanyTextBlock(self): #会社の支配に関する基本方針 [テキストブロック]
		return self.BasicPolicyRegardingControlOfCompanyTextBlock

	def getCriticalContractsForOperationHeading(self): #経営上の重要な契約等 [目次項目]
		return self.CriticalContractsForOperationHeading

	def getCriticalContractsForOperationTextBlock(self): #経営上の重要な契約等 [テキストブロック]
		return self.CriticalContractsForOperationTextBlock

	def getInformationAboutReportingCompanyHeading(self): #提出会社の状況 [目次項目]
		return self.InformationAboutReportingCompanyHeading

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

	def getIssuedSharesTotalNumberOfSharesEtcHeading(self): #発行済株式、株式の総数等 [目次項目]
		return self.IssuedSharesTotalNumberOfSharesEtcHeading

	def getIssuedSharesTotalNumberOfSharesEtcTable(self): #発行済株式、株式の総数等 [表]
		return self.IssuedSharesTotalNumberOfSharesEtcTable

	def getClassesOfSharesAxis(self): #株式種類 [軸]
		return self.ClassesOfSharesAxis

	def getTotalClassesOfSharesMember(self): #合計、株式種類 [メンバー] ※ディメンションデフォルト
		return self.TotalClassesOfSharesMember

	def getOrdinaryShareMember(self): #普通株式 [メンバー]
		return self.OrdinaryShareMember

	def getClassAPreferredSharesMember(self): #Ａ種優先株式 [メンバー]
		return self.ClassAPreferredSharesMember

	def getClassBPreferredSharesMember(self): #Ｂ種優先株式 [メンバー]
		return self.ClassBPreferredSharesMember

	def getClassOnePreferredSharesMember(self): #第一種優先株式 [メンバー]
		return self.ClassOnePreferredSharesMember

	def getClassTwoPreferredSharesMember(self): #第二種優先株式 [メンバー]
		return self.ClassTwoPreferredSharesMember

	def getClassASharesMember(self): #Ａ種種類株式 [メンバー]
		return self.ClassASharesMember

	def getIssuedSharesTotalNumberOfSharesEtcLineItems(self): #発行済株式、株式の総数等 [表示項目]
		return self.IssuedSharesTotalNumberOfSharesEtcLineItems

	def getClassIssuedSharesTotalNumberOfSharesEtc(self): #種類、発行済株式、株式の総数等
		return self.ClassIssuedSharesTotalNumberOfSharesEtc

	def getNumberOfIssuedSharesIssuedSharesTotalNumberOfSharesEtc(self): #発行数（株）、発行済株式、株式の総数等
		return self.NumberOfIssuedSharesIssuedSharesTotalNumberOfSharesEtc

	def getNumberOfIssuedSharesAsOfFiscalYearEndIssuedSharesTotalNumberOfSharesEtc(self): #事業年度末現在発行数（株）、発行済株式、株式の総数等
		return self.NumberOfIssuedSharesAsOfFiscalYearEndIssuedSharesTotalNumberOfSharesEtc

	def getNumberOfIssuedSharesAsOfFilingDateIssuedSharesTotalNumberOfSharesEtc(self): #提出日現在発行数（株）、発行済株式、株式の総数等
		return self.NumberOfIssuedSharesAsOfFilingDateIssuedSharesTotalNumberOfSharesEtc

	def getNameOfFinancialInstrumentsExchangeOnWhichSecuritiesAreListedOrAuthorizedFinancialInstrumentsBusinessAssociationToWhichSecuritiesAreRegistered(self): #上場金融商品取引所名又は登録認可金融商品取引業協会名
		return self.NameOfFinancialInstrumentsExchangeOnWhichSecuritiesAreListedOrAuthorizedFinancialInstrumentsBusinessAssociationToWhichSecuritiesAreRegistered

	def getDescriptionIssuedSharesTotalNumberOfSharesEtc(self): #内容、発行済株式、株式の総数等
		return self.DescriptionIssuedSharesTotalNumberOfSharesEtc

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

	def getIssuedSharesVotingRightsHeading(self): #発行済株式、議決権の状況 [目次項目]
		return self.IssuedSharesVotingRightsHeading

	def getIssuedSharesVotingRightsTable(self): #発行済株式、議決権の状況 [表]
		return self.IssuedSharesVotingRightsTable

	def getCategoriesIssuedSharesAxis(self): #区分、発行済株式 [軸]
		return self.CategoriesIssuedSharesAxis

	def getTotalNumberOfIssuedSharesNumberOfVotingRightsHeldByAllShareholdersMember(self): #発行済株式総数／総株主の議決権 [メンバー] ※ディメンションデフォルト
		return self.TotalNumberOfIssuedSharesNumberOfVotingRightsHeldByAllShareholdersMember

	def getSharesWithNoVotingRightsMember(self): #無議決権株式 [メンバー]
		return self.SharesWithNoVotingRightsMember

	def getSharesWithRestrictedVotingRightsTreasurySharesEtcMember(self): #議決権制限株式（自己株式等） [メンバー]
		return self.SharesWithRestrictedVotingRightsTreasurySharesEtcMember

	def getSharesWithRestrictedVotingRightsOtherMember(self): #議決権制限株式（その他） [メンバー]
		return self.SharesWithRestrictedVotingRightsOtherMember

	def getSharesWithFullVotingRightsTreasurySharesEtcMember(self): #完全議決権株式（自己株式等） [メンバー]
		return self.SharesWithFullVotingRightsTreasurySharesEtcMember

	def getOrdinarySharesSharesWithFullVotingRightsTreasurySharesEtcMember(self): #普通株式、完全議決権株式（自己株式等） [メンバー]
		return self.OrdinarySharesSharesWithFullVotingRightsTreasurySharesEtcMember

	def getOrdinarySharesTreasurySharesSharesWithFullVotingRightsTreasurySharesEtcMember(self): #（自己保有株式）普通株式、完全議決権株式（自己株式等） [メンバー]
		return self.OrdinarySharesTreasurySharesSharesWithFullVotingRightsTreasurySharesEtcMember

	def getOrdinarySharesReciprocalHoldingSharesWithFullVotingRightsTreasurySharesEtcMember(self): #（相互保有株式）普通株式、完全議決権株式（自己株式等） [メンバー]
		return self.OrdinarySharesReciprocalHoldingSharesWithFullVotingRightsTreasurySharesEtcMember

	def getSharesWithFullVotingRightsOtherMember(self): #完全議決権株式（その他） [メンバー]
		return self.SharesWithFullVotingRightsOtherMember

	def getOrdinarySharesSharesWithFullVotingRightsOtherMember(self): #普通株式、完全議決権株式（その他） [メンバー]
		return self.OrdinarySharesSharesWithFullVotingRightsOtherMember

	def getSharesLessThanOneUnitMember(self): #単元未満株式 [メンバー]
		return self.SharesLessThanOneUnitMember

	def getOrdinarySharesSharesLessThanOneUnitMember(self): #普通株式、単元未満株式 [メンバー]
		return self.OrdinarySharesSharesLessThanOneUnitMember

	def getIssuedSharesVotingRightsLineItems(self): #発行済株式、議決権の状況 [表示項目]
		return self.IssuedSharesVotingRightsLineItems

	def getNumberOfSharesIssuedSharesVotingRights(self): #株式数（株）、発行済株式、議決権の状況
		return self.NumberOfSharesIssuedSharesVotingRights

	def getNumberOfVotingRightsIssuedSharesVotingRights(self): #議決権の数（個）、発行済株式、議決権の状況
		return self.NumberOfVotingRightsIssuedSharesVotingRights

	def getDescriptionIssuedSharesVotingRights(self): #内容、発行済株式、議決権の状況
		return self.DescriptionIssuedSharesVotingRights

	def getTreasurySharesEtcHeading(self): #自己株式等 [目次項目]
		return self.TreasurySharesEtcHeading

	def getTreasurySharesEtcTextBlock(self): #自己株式等 [テキストブロック]
		return self.TreasurySharesEtcTextBlock

	def getTreasurySharesEtcHeading(self): #自己株式等 [目次項目]
		return self.TreasurySharesEtcHeading

	def getTreasurySharesEtcTable(self): #自己株式等 [表]
		return self.TreasurySharesEtcTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getTotalSequentialNumbersMember(self): #合計、連番 [メンバー] ※ディメンションデフォルト
		return self.TotalSequentialNumbersMember

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getRow4Member(self): #4件目 [メンバー]
		return self.Row4Member

	def getTreasurySharesEtcLineItems(self): #自己株式等 [表示項目]
		return self.TreasurySharesEtcLineItems

	def getNameOfShareholderTreasurySharesEtc(self): #所有者の氏名又は名称、自己株式等
		return self.NameOfShareholderTreasurySharesEtc

	def getAddressOfShareholderTreasurySharesEtc(self): #所有者の住所、自己株式等
		return self.AddressOfShareholderTreasurySharesEtc

	def getNumberOfSharesHeldInOwnNameTreasurySharesEtc(self): #自己名義所有株式数（株）、自己株式等
		return self.NumberOfSharesHeldInOwnNameTreasurySharesEtc

	def getNumberOfSharesHeldInOthersNamesTreasurySharesEtc(self): #他人名義所有株式数（株）、自己株式等
		return self.NumberOfSharesHeldInOthersNamesTreasurySharesEtc

	def getTotalNumberOfSharesHeldTreasurySharesEtc(self): #所有株式数の合計（株）、自己株式等
		return self.TotalNumberOfSharesHeldTreasurySharesEtc

	def getShareholdingRatioTreasurySharesEtc(self): #発行済株式総数に対する所有株式数の割合（％）、自己株式等
		return self.ShareholdingRatioTreasurySharesEtc

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getInformationAboutOfficersTextBlock(self): #役員の状況 [テキストブロック]
		return self.InformationAboutOfficersTextBlock

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getNumberOfMaleDirectorsAndOtherOfficers(self): #役員のうち男性の人数
		return self.NumberOfMaleDirectorsAndOtherOfficers

	def getNumberOfFemaleDirectorsAndOtherOfficers(self): #役員のうち女性の人数
		return self.NumberOfFemaleDirectorsAndOtherOfficers

	def getRatioOfFemaleDirectorsAndOtherOfficers(self): #役員のうち女性の比率
		return self.RatioOfFemaleDirectorsAndOtherOfficers

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

	def getQuarterlyConsolidatedFinancialStatementsHeading(self): #四半期連結財務諸表 [目次項目]
		return self.QuarterlyConsolidatedFinancialStatementsHeading

	def getQuarterlyConsolidatedBalanceSheetHeading(self): #四半期連結貸借対照表 [目次項目]
		return self.QuarterlyConsolidatedBalanceSheetHeading

	def getQuarterlyConsolidatedBalanceSheetTextBlock(self): #四半期連結貸借対照表 [テキストブロック]
		return self.QuarterlyConsolidatedBalanceSheetTextBlock

	def getCondensedQuarterlyConsolidatedStatementOfFinancialPositionJMISTextBlock(self): #要約四半期連結財政状態計算書（JMIS） [テキストブロック]
		return self.CondensedQuarterlyConsolidatedStatementOfFinancialPositionJMISTextBlock

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

	def getCondensedYearToQuarterEndConsolidatedStatementOfIncomeJMISTextBlock(self): #四半期連結累計期間、要約四半期連結損益計算書（JMIS） [テキストブロック]
		return self.CondensedYearToQuarterEndConsolidatedStatementOfIncomeJMISTextBlock

	def getYearToQuarterEndConsolidatedStatementOfIncomeUSGAAPTextBlock(self): #四半期連結累計期間、四半期連結損益計算書（US GAAP） [テキストブロック]
		return self.YearToQuarterEndConsolidatedStatementOfIncomeUSGAAPTextBlock

	def getQuarterPeriodConsolidatedStatementOfIncomeHeading(self): #四半期連結会計期間、四半期連結損益計算書 [目次項目]
		return self.QuarterPeriodConsolidatedStatementOfIncomeHeading

	def getQuarterPeriodConsolidatedStatementOfIncomeTextBlock(self): #四半期連結会計期間、四半期連結損益計算書 [テキストブロック]
		return self.QuarterPeriodConsolidatedStatementOfIncomeTextBlock

	def getCondensedQuarterPeriodConsolidatedStatementOfIncomeJMISTextBlock(self): #四半期連結会計期間、要約四半期連結損益計算書（JMIS） [テキストブロック]
		return self.CondensedQuarterPeriodConsolidatedStatementOfIncomeJMISTextBlock

	def getQuarterPeriodConsolidatedStatementOfIncomeUSGAAPTextBlock(self): #四半期連結会計期間、四半期連結損益計算書（US GAAP） [テキストブロック]
		return self.QuarterPeriodConsolidatedStatementOfIncomeUSGAAPTextBlock

	def getQuarterlyConsolidatedStatementOfComprehensiveIncomeHeading(self): #四半期連結包括利益計算書 [目次項目]
		return self.QuarterlyConsolidatedStatementOfComprehensiveIncomeHeading

	def getYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeHeading(self): #四半期連結累計期間、四半期連結包括利益計算書 [目次項目]
		return self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeHeading

	def getYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock(self): #四半期連結累計期間、四半期連結包括利益計算書 [テキストブロック]
		return self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeTextBlock

	def getCondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeJMISTextBlock(self): #四半期連結累計期間、要約四半期連結包括利益計算書（JMIS） [テキストブロック]
		return self.CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeJMISTextBlock

	def getYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock(self): #四半期連結累計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]
		return self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock

	def getQuarterPeriodConsolidatedStatementOfComprehensiveIncomeHeading(self): #四半期連結会計期間、四半期連結包括利益計算書 [目次項目]
		return self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeHeading

	def getQuarterPeriodConsolidatedStatementOfComprehensiveIncomeTextBlock(self): #四半期連結会計期間、四半期連結包括利益計算書 [テキストブロック]
		return self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeTextBlock

	def getCondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeJMISTextBlock(self): #四半期連結会計期間、要約四半期連結包括利益計算書（JMIS） [テキストブロック]
		return self.CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeJMISTextBlock

	def getQuarterPeriodConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock(self): #四半期連結会計期間、四半期連結包括利益計算書（US GAAP） [テキストブロック]
		return self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock

	def getQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading(self): #四半期連結損益及び包括利益計算書 [目次項目]
		return self.QuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading

	def getYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading(self): #四半期連結累計期間、四半期連結損益及び包括利益計算書 [目次項目]
		return self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading

	def getYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock(self): #四半期連結累計期間、四半期連結損益及び包括利益計算書 [テキストブロック]
		return self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock

	def getCondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock(self): #四半期連結累計期間、要約四半期連結包括利益計算書（１計算書）（JMIS） [テキストブロック]
		return self.CondensedYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock

	def getYearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock(self): #四半期連結累計期間、四半期連結損益及び包括利益計算書（US GAAP） [テキストブロック]
		return self.YearToQuarterEndConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock

	def getQuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading(self): #四半期連結会計期間、四半期連結損益及び包括利益計算書 [目次項目]
		return self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading

	def getQuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock(self): #四半期連結会計期間、四半期連結損益及び包括利益計算書 [テキストブロック]
		return self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock

	def getCondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock(self): #四半期連結会計期間、要約四半期連結包括利益計算書（１計算書）（JMIS） [テキストブロック]
		return self.CondensedQuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock

	def getQuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock(self): #四半期連結会計期間、四半期連結損益及び包括利益計算書（US GAAP） [テキストブロック]
		return self.QuarterPeriodConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock

	def getCondensedQuarterlyConsolidatedStatementOfChangesInEquityJMISHeading(self): #要約四半期連結持分変動計算書（JMIS） [目次項目]
		return self.CondensedQuarterlyConsolidatedStatementOfChangesInEquityJMISHeading

	def getCondensedQuarterlyConsolidatedStatementOfChangesInEquityJMISTextBlock(self): #要約四半期連結持分変動計算書（JMIS） [テキストブロック]
		return self.CondensedQuarterlyConsolidatedStatementOfChangesInEquityJMISTextBlock

	def getConsolidatedQuarterlyStatementOfEquityUSGAAPHeading(self): #四半期連結資本勘定計算書（US GAAP） [目次項目]
		return self.ConsolidatedQuarterlyStatementOfEquityUSGAAPHeading

	def getConsolidatedQuarterlyStatementOfEquityUSGAAPTextBlock(self): #四半期連結資本勘定計算書（US GAAP） [テキストブロック]
		return self.ConsolidatedQuarterlyStatementOfEquityUSGAAPTextBlock

	def getQuarterlyConsolidatedStatementOfCashFlowsHeading(self): #四半期連結キャッシュ・フロー計算書 [目次項目]
		return self.QuarterlyConsolidatedStatementOfCashFlowsHeading

	def getQuarterlyConsolidatedStatementOfCashFlowsTextBlock(self): #四半期連結キャッシュ・フロー計算書 [テキストブロック]
		return self.QuarterlyConsolidatedStatementOfCashFlowsTextBlock

	def getCondensedQuarterlyConsolidatedStatementOfCashFlowsJMISTextBlock(self): #要約四半期連結キャッシュ・フロー計算書（JMIS） [テキストブロック]
		return self.CondensedQuarterlyConsolidatedStatementOfCashFlowsJMISTextBlock

	def getQuarterlyConsolidatedStatementOfCashFlowsUSGAAPTextBlock(self): #四半期連結キャッシュ・フロー計算書（US GAAP） [テキストブロック]
		return self.QuarterlyConsolidatedStatementOfCashFlowsUSGAAPTextBlock

	def getNotesQuarterlyConsolidatedFinancialStatementsHeading(self): #注記事項、四半期連結財務諸表 [目次項目]
		return self.NotesQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyConsolidatedFinancialStatementsHeading(self): #継続企業の前提に関する事項、四半期連結財務諸表 [目次項目]
		return self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyConsolidatedFinancialStatementsTextBlock(self): #継続企業の前提に関する事項、四半期連結財務諸表 [テキストブロック]
		return self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesChangesInScopeOfConsolidationOrEquityMethodHeading(self): #連結の範囲又は持分法適用の範囲の変更に関する注記 [目次項目]
		return self.NotesChangesInScopeOfConsolidationOrEquityMethodHeading

	def getNotesChangesInScopeOfConsolidationOrEquityMethodTextBlock(self): #連結の範囲又は持分法適用の範囲の変更に関する注記 [テキストブロック]
		return self.NotesChangesInScopeOfConsolidationOrEquityMethodTextBlock

	def getNotesChangesInAccountingPoliciesQuarterlyConsolidatedFinancialStatementsHeading(self): #会計方針の変更、四半期連結財務諸表 [目次項目]
		return self.NotesChangesInAccountingPoliciesQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcQuarterlyConsolidatedFinancialStatementsTextBlock(self): #会計基準等の改正等に伴う会計方針の変更、四半期連結財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesVoluntaryChangesInAccountingPoliciesQuarterlyConsolidatedFinancialStatementsTextBlock(self): #会計基準等の改正等以外の正当な理由による会計方針の変更、四半期連結財務諸表 [テキストブロック]
		return self.NotesVoluntaryChangesInAccountingPoliciesQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsTextBlock(self): #会計上の見積りの変更と区別することが困難な会計方針の変更、四半期連結財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsHeading(self): #会計上の見積りの変更、四半期連結財務諸表 [目次項目]
		return self.NotesChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsTextBlock(self): #会計上の見積りの変更、四半期連結財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingEstimatesQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesRestatementQuarterlyConsolidatedFinancialStatementsHeading(self): #修正再表示、四半期連結財務諸表 [目次項目]
		return self.NotesRestatementQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesRestatementQuarterlyConsolidatedFinancialStatementsTextBlock(self): #修正再表示、四半期連結財務諸表 [テキストブロック]
		return self.NotesRestatementQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyConsolidatedFinancialStatementsHeading(self): #四半期特有の会計処理、四半期連結財務諸表 [目次項目]
		return self.NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyConsolidatedFinancialStatementsTextBlock(self): #四半期特有の会計処理、四半期連結財務諸表 [テキストブロック]
		return self.NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesAdditionalInformationQuarterlyConsolidatedFinancialStatementsHeading(self): #追加情報、四半期連結財務諸表 [目次項目]
		return self.NotesAdditionalInformationQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesAdditionalInformationQuarterlyConsolidatedFinancialStatementsTextBlock(self): #追加情報、四半期連結財務諸表 [テキストブロック]
		return self.NotesAdditionalInformationQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesQuarterlyConsolidatedBalanceSheetHeading(self): #四半期連結貸借対照表関係 [目次項目]
		return self.NotesQuarterlyConsolidatedBalanceSheetHeading

	def getNotesQuarterlyConsolidatedBalanceSheetHeading(self): #四半期連結貸借対照表関係 [目次項目]
		return self.NotesQuarterlyConsolidatedBalanceSheetHeading

	def getNotesQuarterlyConsolidatedBalanceSheetTable(self): #四半期連結貸借対照表関係 [表]
		return self.NotesQuarterlyConsolidatedBalanceSheetTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesQuarterlyConsolidatedBalanceSheetLineItems(self): #四半期連結貸借対照表関係 [表示項目]
		return self.NotesQuarterlyConsolidatedBalanceSheetLineItems

	def getNotesRegardingInventoriesTextBlock(self): #棚卸資産の内訳の注記 [テキストブロック]
		return self.NotesRegardingInventoriesTextBlock

	def getMerchandiseAndFinishedGoods(self): #商品及び製品
		return self.MerchandiseAndFinishedGoods

	def getWorkInProcess(self): #仕掛品
		return self.WorkInProcess

	def getRawMaterialsAndSupplies(self): #原材料及び貯蔵品
		return self.RawMaterialsAndSupplies

	def getInventories(self): #棚卸資産
		return self.Inventories

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

	def getNotesRegardingPresentationOfGoodwillAndNegativeGoodwillTextBlock(self): #のれん及び負ののれんの表示に関する注記 [テキストブロック]
		return self.NotesRegardingPresentationOfGoodwillAndNegativeGoodwillTextBlock

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

	def getNotesQuarterlyConsolidatedStatementOfIncomeHeading(self): #四半期連結損益計算書関係 [目次項目]
		return self.NotesQuarterlyConsolidatedStatementOfIncomeHeading

	def getNotesQuarterlyConsolidatedStatementOfIncomeHeading(self): #四半期連結損益計算書関係 [目次項目]
		return self.NotesQuarterlyConsolidatedStatementOfIncomeHeading

	def getNotesQuarterlyConsolidatedStatementOfIncomeTable(self): #四半期連結損益計算書関係 [表]
		return self.NotesQuarterlyConsolidatedStatementOfIncomeTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesQuarterlyConsolidatedStatementOfIncomeLineItems(self): #四半期連結損益計算書関係 [表示項目]
		return self.NotesQuarterlyConsolidatedStatementOfIncomeLineItems

	def getMajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock(self): #主要な販売費及び一般管理費 [テキストブロック]
		return self.MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock

	def getDepreciationSGA(self): #減価償却費、販売費及び一般管理費
		return self.DepreciationSGA

	def getProvisionOfAllowanceForDoubtfulAccountsSGA(self): #貸倒引当金繰入額、販売費及び一般管理費
		return self.ProvisionOfAllowanceForDoubtfulAccountsSGA

	def getNotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock(self): #売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]
		return self.NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock

	def getNotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading(self): #四半期連結損益及び包括利益計算書関係 [目次項目]
		return self.NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading

	def getNotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading(self): #四半期連結損益及び包括利益計算書関係 [目次項目]
		return self.NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading

	def getNotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementTable(self): #四半期連結損益及び包括利益計算書関係 [表]
		return self.NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementLineItems(self): #四半期連結損益及び包括利益計算書関係 [表示項目]
		return self.NotesQuarterlyConsolidatedStatementOfComprehensiveIncomeSingleStatementLineItems

	def getMajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock(self): #主要な販売費及び一般管理費 [テキストブロック]
		return self.MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock

	def getDepreciationSGA(self): #減価償却費、販売費及び一般管理費
		return self.DepreciationSGA

	def getProvisionOfAllowanceForDoubtfulAccountsSGA(self): #貸倒引当金繰入額、販売費及び一般管理費
		return self.ProvisionOfAllowanceForDoubtfulAccountsSGA

	def getNotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock(self): #売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]
		return self.NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock

	def getNotesQuarterlyConsolidatedStatementOfCashFlowsHeading(self): #四半期連結キャッシュ・フロー計算書関係 [目次項目]
		return self.NotesQuarterlyConsolidatedStatementOfCashFlowsHeading

	def getNotesQuarterlyConsolidatedStatementOfCashFlowsHeading(self): #四半期連結キャッシュ・フロー計算書関係 [目次項目]
		return self.NotesQuarterlyConsolidatedStatementOfCashFlowsHeading

	def getNotesQuarterlyConsolidatedStatementOfCashFlowsTable(self): #四半期連結キャッシュ・フロー計算書関係 [表]
		return self.NotesQuarterlyConsolidatedStatementOfCashFlowsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesQuarterlyConsolidatedStatementOfCashFlowsLineItems(self): #四半期連結キャッシュ・フロー計算書関係 [表示項目]
		return self.NotesQuarterlyConsolidatedStatementOfCashFlowsLineItems

	def getDescriptionOfFactThatQuarterlyStatementOfCashFlowsHasNotBeenPreparedTextBlock(self): #四半期キャッシュ・フロー計算書を作成しない場合の注記 [テキストブロック]
		return self.DescriptionOfFactThatQuarterlyStatementOfCashFlowsHasNotBeenPreparedTextBlock

	def getReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock(self): #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
		return self.ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock

	def getDescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock(self): #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
		return self.DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock

	def getNotesEquityQuarterlyConsolidatedFinancialStatementsHeading(self): #株主資本等に関する注記、四半期連結財務諸表 [目次項目]
		return self.NotesEquityQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesEquityQuarterlyConsolidatedFinancialStatementsHeading(self): #株主資本等に関する注記、四半期連結財務諸表 [目次項目]
		return self.NotesEquityQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesEquityQuarterlyConsolidatedFinancialStatementsTable(self): #株主資本等に関する注記、四半期連結財務諸表 [表]
		return self.NotesEquityQuarterlyConsolidatedFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesEquityQuarterlyConsolidatedFinancialStatementsLineItems(self): #株主資本等に関する注記、四半期連結財務諸表 [表示項目]
		return self.NotesEquityQuarterlyConsolidatedFinancialStatementsLineItems

	def getNotesRegardingDividendTextBlock(self): #配当に関する注記 [テキストブロック]
		return self.NotesRegardingDividendTextBlock

	def getNotesWhenThereIsSignificantChangesInAmountsOfEquityTextBlock(self): #株主資本の金額に著しい変動があった場合の注記 [テキストブロック]
		return self.NotesWhenThereIsSignificantChangesInAmountsOfEquityTextBlock

	def getNotesFinancialInstrumentsQuarterlyConsolidatedFinancialStatementsHeading(self): #金融商品関係、四半期連結財務諸表 [目次項目]
		return self.NotesFinancialInstrumentsQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesFinancialInstrumentsQuarterlyConsolidatedFinancialStatementsTextBlock(self): #金融商品関係、四半期連結財務諸表 [テキストブロック]
		return self.NotesFinancialInstrumentsQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesSecuritiesQuarterlyConsolidatedFinancialStatementsHeading(self): #有価証券関係、四半期連結財務諸表 [目次項目]
		return self.NotesSecuritiesQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesSecuritiesQuarterlyConsolidatedFinancialStatementsTextBlock(self): #有価証券関係、四半期連結財務諸表 [テキストブロック]
		return self.NotesSecuritiesQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesMoneyHeldInTrustQuarterlyConsolidatedFinancialStatementsHeading(self): #金銭の信託関係、四半期連結財務諸表 [目次項目]
		return self.NotesMoneyHeldInTrustQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesMoneyHeldInTrustQuarterlyConsolidatedFinancialStatementsTextBlock(self): #金銭の信託関係、四半期連結財務諸表 [テキストブロック]
		return self.NotesMoneyHeldInTrustQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesDerivativesQuarterlyConsolidatedFinancialStatementsHeading(self): #デリバティブ取引関係、四半期連結財務諸表 [目次項目]
		return self.NotesDerivativesQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesDerivativesQuarterlyConsolidatedFinancialStatementsTextBlock(self): #デリバティブ取引関係、四半期連結財務諸表 [テキストブロック]
		return self.NotesDerivativesQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesBusinessCombinationsQuarterlyConsolidatedFinancialStatementsHeading(self): #企業結合等関係、四半期連結財務諸表 [目次項目]
		return self.NotesBusinessCombinationsQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesBusinessCombinationsQuarterlyConsolidatedFinancialStatementsTextBlock(self): #企業結合等関係、四半期連結財務諸表 [テキストブロック]
		return self.NotesBusinessCombinationsQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesRevenueRecognitionQuarterlyConsolidatedFinancialStatementsHeading(self): #収益認識関係、四半期連結財務諸表 [目次項目]
		return self.NotesRevenueRecognitionQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesRevenueRecognitionQuarterlyConsolidatedFinancialStatementsTextBlock(self): #収益認識関係、四半期連結財務諸表 [テキストブロック]
		return self.NotesRevenueRecognitionQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading(self): #セグメント情報等、四半期連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock(self): #セグメント情報等、四半期連結財務諸表 [テキストブロック]
		return self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading(self): #セグメント情報等、四半期連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTable(self): #セグメント情報等、四半期連結財務諸表 [表]
		return self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsLineItems(self): #セグメント情報等、四半期連結財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsLineItems

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getDescriptionOfFactThatCompanysBusinessComprisesSingleSegment(self): #単一セグメントである旨
		return self.DescriptionOfFactThatCompanysBusinessComprisesSingleSegment

	def getNotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading(self): #セグメント情報等、四半期連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getDisclosureOfSalesAndProfitLossForEachReportableSegmentTable(self): #報告セグメントごとの売上高及び利益又は損失の金額に関する情報 [表]
		return self.DisclosureOfSalesAndProfitLossForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

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

	def getDisclosureOfSalesAndProfitLossForEachReportableSegmentLineItems(self): #報告セグメントごとの売上高及び利益又は損失の金額に関する情報 [表示項目]
		return self.DisclosureOfSalesAndProfitLossForEachReportableSegmentLineItems

	def getSalesSegmentInformationAbstract(self): #売上高、セグメント情報 [タイトル項目]
		return self.SalesSegmentInformationAbstract

	def getRevenuesFromExternalCustomers(self): #外部顧客への売上高
		return self.RevenuesFromExternalCustomers

	def getTransactionsWithOtherSegments(self): #セグメント間の内部売上高又は振替高
		return self.TransactionsWithOtherSegments

	def getNetSales(self): #売上高
		return self.NetSales

	def getRevenue(self): #売上収益
		return self.Revenue

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

	def getProfitLossAttributableToOwnersOfParent(self): #親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）
		return self.ProfitLossAttributableToOwnersOfParent

	def getProfitLoss(self): #当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）
		return self.ProfitLoss

	def getNotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading(self): #セグメント情報等、四半期連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTable(self): #セグメント情報等、四半期連結財務諸表 [表]
		return self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsLineItems(self): #セグメント情報等、四半期連結財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcQuarterlyConsolidatedFinancialStatementsLineItems

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getFootnotesRegardingSegmentInformationTableTextBlock(self): #セグメント表の脚注 [テキストブロック]
		return self.FootnotesRegardingSegmentInformationTableTextBlock

	def getInformationAboutAssetsForEachReportableSegmentTextBlock(self): #報告セグメントごとの資産に関する情報 [テキストブロック]
		return self.InformationAboutAssetsForEachReportableSegmentTextBlock

	def getDescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock(self): #報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
		return self.DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock

	def getDisclosureOfChangesEtcInReportableSegmentsTextBlock(self): #報告セグメントの変更等に関する事項 [テキストブロック]
		return self.DisclosureOfChangesEtcInReportableSegmentsTextBlock

	def getInformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock(self): #報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]
		return self.InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock

	def getNotesPerShareInformationQuarterlyConsolidatedFinancialStatementsHeading(self): #１株当たり情報、四半期連結財務諸表 [目次項目]
		return self.NotesPerShareInformationQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesPerShareInformationQuarterlyConsolidatedFinancialStatementsTextBlock(self): #１株当たり情報、四半期連結財務諸表 [テキストブロック]
		return self.NotesPerShareInformationQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesSignificantEventsAfterReportingPeriodQuarterlyConsolidatedFinancialStatementsHeading(self): #重要な後発事象、四半期連結財務諸表 [目次項目]
		return self.NotesSignificantEventsAfterReportingPeriodQuarterlyConsolidatedFinancialStatementsHeading

	def getNotesSignificantEventsAfterReportingPeriodQuarterlyConsolidatedFinancialStatementsTextBlock(self): #重要な後発事象、四半期連結財務諸表 [テキストブロック]
		return self.NotesSignificantEventsAfterReportingPeriodQuarterlyConsolidatedFinancialStatementsTextBlock

	def getNotesToQuarterlyConsolidatedFinancialStatementsJMISHeading(self): #四半期連結財務諸表注記事項（JMIS） [目次項目]
		return self.NotesToQuarterlyConsolidatedFinancialStatementsJMISHeading

	def getNotesToQuarterlyConsolidatedFinancialStatementsJMISTextBlock(self): #四半期連結財務諸表注記事項（JMIS） [テキストブロック]
		return self.NotesToQuarterlyConsolidatedFinancialStatementsJMISTextBlock

	def getNotesToQuarterlyConsolidatedFinancialStatementsUSGAAPHeading(self): #四半期連結財務諸表注記事項（US GAAP） [目次項目]
		return self.NotesToQuarterlyConsolidatedFinancialStatementsUSGAAPHeading

	def getNotesToQuarterlyConsolidatedFinancialStatementsUSGAAPTextBlock(self): #四半期連結財務諸表注記事項（US GAAP） [テキストブロック]
		return self.NotesToQuarterlyConsolidatedFinancialStatementsUSGAAPTextBlock

	def getOtherInformationConsolidatedFinancialStatementsEtcHeading(self): #その他、連結財務諸表等 [目次項目]
		return self.OtherInformationConsolidatedFinancialStatementsEtcHeading

	def getOtherInformationConsolidatedFinancialStatementsEtcTextBlock(self): #その他、連結財務諸表等 [テキストブロック]
		return self.OtherInformationConsolidatedFinancialStatementsEtcTextBlock

	def getPriorYearConsolidatedFinancialStatementsPreapredInAccordanceWithJMISHeading(self): #修正国際基準による前連結会計年度に係る連結財務諸表 [目次項目]
		return self.PriorYearConsolidatedFinancialStatementsPreapredInAccordanceWithJMISHeading

	def getPriorYearConsolidatedFinancialStatementsPreapredInAccordanceWithJMISTextBlock(self): #修正国際基準による前連結会計年度に係る連結財務諸表 [テキストブロック]
		return self.PriorYearConsolidatedFinancialStatementsPreapredInAccordanceWithJMISTextBlock

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

	def getNotesQuarterlyFinancialStatementsHeading(self): #注記事項、四半期財務諸表 [目次項目]
		return self.NotesQuarterlyFinancialStatementsHeading

	def getNotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyFinancialStatementsHeading(self): #継続企業の前提に関する事項、四半期財務諸表 [目次項目]
		return self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyFinancialStatementsHeading

	def getNotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyFinancialStatementsTextBlock(self): #継続企業の前提に関する事項、四半期財務諸表 [テキストブロック]
		return self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernQuarterlyFinancialStatementsTextBlock

	def getNotesChangesInAccountingPoliciesQuarterlyFinancialStatementsHeading(self): #会計方針の変更、四半期財務諸表 [目次項目]
		return self.NotesChangesInAccountingPoliciesQuarterlyFinancialStatementsHeading

	def getNotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcQuarterlyFinancialStatementsTextBlock(self): #会計基準等の改正等に伴う会計方針の変更、四半期財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcQuarterlyFinancialStatementsTextBlock

	def getNotesVoluntaryChangesInAccountingPoliciesQuarterlyFinancialStatementsTextBlock(self): #会計基準等の改正等以外の正当な理由による会計方針の変更、四半期財務諸表 [テキストブロック]
		return self.NotesVoluntaryChangesInAccountingPoliciesQuarterlyFinancialStatementsTextBlock

	def getNotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesQuarterlyFinancialStatementsTextBlock(self): #会計上の見積りの変更と区別することが困難な会計方針の変更、四半期財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesQuarterlyFinancialStatementsTextBlock

	def getNotesChangesInAccountingEstimatesQuarterlyFinancialStatementsHeading(self): #会計上の見積りの変更、四半期財務諸表 [目次項目]
		return self.NotesChangesInAccountingEstimatesQuarterlyFinancialStatementsHeading

	def getNotesChangesInAccountingEstimatesQuarterlyFinancialStatementsTextBlock(self): #会計上の見積りの変更、四半期財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingEstimatesQuarterlyFinancialStatementsTextBlock

	def getNotesRestatementQuarterlyFinancialStatementsHeading(self): #修正再表示、四半期財務諸表 [目次項目]
		return self.NotesRestatementQuarterlyFinancialStatementsHeading

	def getNotesRestatementQuarterlyFinancialStatementsTextBlock(self): #修正再表示、四半期財務諸表 [テキストブロック]
		return self.NotesRestatementQuarterlyFinancialStatementsTextBlock

	def getNotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyFinancialStatementsHeading(self): #四半期特有の会計処理、四半期財務諸表 [目次項目]
		return self.NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyFinancialStatementsHeading

	def getNotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyFinancialStatementsTextBlock(self): #四半期特有の会計処理、四半期財務諸表 [テキストブロック]
		return self.NotesAccountingTreatmentsSpecificToQuarterlyFinancialStatementsQuarterlyFinancialStatementsTextBlock

	def getNotesAdditionalInformationQuarterlyFinancialStatementsHeading(self): #追加情報、四半期財務諸表 [目次項目]
		return self.NotesAdditionalInformationQuarterlyFinancialStatementsHeading

	def getNotesAdditionalInformationQuarterlyFinancialStatementsTextBlock(self): #追加情報、四半期財務諸表 [テキストブロック]
		return self.NotesAdditionalInformationQuarterlyFinancialStatementsTextBlock

	def getNotesQuarterlyBalanceSheetHeading(self): #四半期貸借対照表関係 [目次項目]
		return self.NotesQuarterlyBalanceSheetHeading

	def getNotesQuarterlyBalanceSheetHeading(self): #四半期貸借対照表関係 [目次項目]
		return self.NotesQuarterlyBalanceSheetHeading

	def getNotesQuarterlyBalanceSheetTable(self): #四半期貸借対照表関係 [表]
		return self.NotesQuarterlyBalanceSheetTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesQuarterlyBalanceSheetLineItems(self): #四半期貸借対照表関係 [表示項目]
		return self.NotesQuarterlyBalanceSheetLineItems

	def getNotesRegardingInventoriesTextBlock(self): #棚卸資産の内訳の注記 [テキストブロック]
		return self.NotesRegardingInventoriesTextBlock

	def getMerchandiseAndFinishedGoods(self): #商品及び製品
		return self.MerchandiseAndFinishedGoods

	def getWorkInProcess(self): #仕掛品
		return self.WorkInProcess

	def getRawMaterialsAndSupplies(self): #原材料及び貯蔵品
		return self.RawMaterialsAndSupplies

	def getInventories(self): #棚卸資産
		return self.Inventories

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

	def getNotesQuarterlyStatementOfIncomeHeading(self): #四半期損益計算書関係 [目次項目]
		return self.NotesQuarterlyStatementOfIncomeHeading

	def getNotesQuarterlyStatementOfIncomeHeading(self): #四半期損益計算書関係 [目次項目]
		return self.NotesQuarterlyStatementOfIncomeHeading

	def getNotesQuarterlyStatementOfIncomeTable(self): #四半期損益計算書関係 [表]
		return self.NotesQuarterlyStatementOfIncomeTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesQuarterlyStatementOfIncomeLineItems(self): #四半期損益計算書関係 [表示項目]
		return self.NotesQuarterlyStatementOfIncomeLineItems

	def getMajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock(self): #主要な販売費及び一般管理費 [テキストブロック]
		return self.MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock

	def getDepreciationSGA(self): #減価償却費、販売費及び一般管理費
		return self.DepreciationSGA

	def getProvisionOfAllowanceForDoubtfulAccountsSGA(self): #貸倒引当金繰入額、販売費及び一般管理費
		return self.ProvisionOfAllowanceForDoubtfulAccountsSGA

	def getNotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock(self): #売上高又は営業費用に著しい季節的変動がある場合の注記 [テキストブロック]
		return self.NotesWhenThereIsSignificantSeasonalFluctuationInSalesOrOperatingExpensesTextBlock

	def getNotesQuarterlyStatementOfCashFlowsHeading(self): #四半期キャッシュ・フロー計算書関係 [目次項目]
		return self.NotesQuarterlyStatementOfCashFlowsHeading

	def getNotesQuarterlyStatementOfCashFlowsHeading(self): #四半期キャッシュ・フロー計算書関係 [目次項目]
		return self.NotesQuarterlyStatementOfCashFlowsHeading

	def getNotesQuarterlyStatementOfCashFlowsTable(self): #四半期キャッシュ・フロー計算書関係 [表]
		return self.NotesQuarterlyStatementOfCashFlowsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesQuarterlyStatementOfCashFlowsLineItems(self): #四半期キャッシュ・フロー計算書関係 [表示項目]
		return self.NotesQuarterlyStatementOfCashFlowsLineItems

	def getDescriptionOfFactThatQuarterlyStatementOfCashFlowsHasNotBeenPreparedTextBlock(self): #四半期キャッシュ・フロー計算書を作成しない場合の注記 [テキストブロック]
		return self.DescriptionOfFactThatQuarterlyStatementOfCashFlowsHasNotBeenPreparedTextBlock

	def getReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock(self): #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
		return self.ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock

	def getDescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock(self): #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
		return self.DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock

	def getNotesEquityQuarterlyFinancialStatementsHeading(self): #株主資本等に関する注記、四半期財務諸表 [目次項目]
		return self.NotesEquityQuarterlyFinancialStatementsHeading

	def getNotesEquityQuarterlyFinancialStatementsHeading(self): #株主資本等に関する注記、四半期財務諸表 [目次項目]
		return self.NotesEquityQuarterlyFinancialStatementsHeading

	def getNotesEquityQuarterlyFinancialStatementsTable(self): #株主資本等に関する注記、四半期財務諸表 [表]
		return self.NotesEquityQuarterlyFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesEquityQuarterlyFinancialStatementsLineItems(self): #株主資本等に関する注記、四半期財務諸表 [表示項目]
		return self.NotesEquityQuarterlyFinancialStatementsLineItems

	def getNotesRegardingDividendTextBlock(self): #配当に関する注記 [テキストブロック]
		return self.NotesRegardingDividendTextBlock

	def getNotesWhenThereIsSignificantChangesInAmountsOfEquityTextBlock(self): #株主資本の金額に著しい変動があった場合の注記 [テキストブロック]
		return self.NotesWhenThereIsSignificantChangesInAmountsOfEquityTextBlock

	def getNotesFinancialInstrumentsQuarterlyFinancialStatementsHeading(self): #金融商品関係、四半期財務諸表 [目次項目]
		return self.NotesFinancialInstrumentsQuarterlyFinancialStatementsHeading

	def getNotesFinancialInstrumentsQuarterlyFinancialStatementsTextBlock(self): #金融商品関係、四半期財務諸表 [テキストブロック]
		return self.NotesFinancialInstrumentsQuarterlyFinancialStatementsTextBlock

	def getNotesSecuritiesQuarterlyFinancialStatementsHeading(self): #有価証券関係、四半期財務諸表 [目次項目]
		return self.NotesSecuritiesQuarterlyFinancialStatementsHeading

	def getNotesSecuritiesQuarterlyFinancialStatementsTextBlock(self): #有価証券関係、四半期財務諸表 [テキストブロック]
		return self.NotesSecuritiesQuarterlyFinancialStatementsTextBlock

	def getNotesMoneyHeldInTrustQuarterlyFinancialStatementsHeading(self): #金銭の信託関係、四半期財務諸表 [目次項目]
		return self.NotesMoneyHeldInTrustQuarterlyFinancialStatementsHeading

	def getNotesMoneyHeldInTrustQuarterlyFinancialStatementsTextBlock(self): #金銭の信託関係、四半期財務諸表 [テキストブロック]
		return self.NotesMoneyHeldInTrustQuarterlyFinancialStatementsTextBlock

	def getNotesDerivativesQuarterlyFinancialStatementsHeading(self): #デリバティブ取引関係、四半期財務諸表 [目次項目]
		return self.NotesDerivativesQuarterlyFinancialStatementsHeading

	def getNotesDerivativesQuarterlyFinancialStatementsTextBlock(self): #デリバティブ取引関係、四半期財務諸表 [テキストブロック]
		return self.NotesDerivativesQuarterlyFinancialStatementsTextBlock

	def getNotesBusinessCombinationsQuarterlyFinancialStatementsHeading(self): #企業結合等関係、四半期財務諸表 [目次項目]
		return self.NotesBusinessCombinationsQuarterlyFinancialStatementsHeading

	def getNotesBusinessCombinationsQuarterlyFinancialStatementsTextBlock(self): #企業結合等関係、四半期財務諸表 [テキストブロック]
		return self.NotesBusinessCombinationsQuarterlyFinancialStatementsTextBlock

	def getNotesRevenueRecognitionQuarterlyFinancialStatementsHeading(self): #収益認識関係、四半期財務諸表 [目次項目]
		return self.NotesRevenueRecognitionQuarterlyFinancialStatementsHeading

	def getNotesRevenueRecognitionQuarterlyFinancialStatementsTextBlock(self): #収益認識関係、四半期財務諸表 [テキストブロック]
		return self.NotesRevenueRecognitionQuarterlyFinancialStatementsTextBlock

	def getNotesSegmentInformationEtcQuarterlyFinancialStatementsHeading(self): #セグメント情報等、四半期財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading

	def getNotesSegmentInformationEtcQuarterlyFinancialStatementsTextBlock(self): #セグメント情報等、四半期財務諸表 [テキストブロック]
		return self.NotesSegmentInformationEtcQuarterlyFinancialStatementsTextBlock

	def getNotesSegmentInformationEtcQuarterlyFinancialStatementsHeading(self): #セグメント情報等、四半期財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading

	def getNotesSegmentInformationEtcQuarterlyFinancialStatementsTable(self): #セグメント情報等、四半期財務諸表 [表]
		return self.NotesSegmentInformationEtcQuarterlyFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSegmentInformationEtcQuarterlyFinancialStatementsLineItems(self): #セグメント情報等、四半期財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcQuarterlyFinancialStatementsLineItems

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getDescriptionOfFactThatCompanysBusinessComprisesSingleSegment(self): #単一セグメントである旨
		return self.DescriptionOfFactThatCompanysBusinessComprisesSingleSegment

	def getNotesSegmentInformationEtcQuarterlyFinancialStatementsHeading(self): #セグメント情報等、四半期財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getDisclosureOfSalesAndProfitLossForEachReportableSegmentTable(self): #報告セグメントごとの売上高及び利益又は損失の金額に関する情報 [表]
		return self.DisclosureOfSalesAndProfitLossForEachReportableSegmentTable

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

	def getDisclosureOfSalesAndProfitLossForEachReportableSegmentLineItems(self): #報告セグメントごとの売上高及び利益又は損失の金額に関する情報 [表示項目]
		return self.DisclosureOfSalesAndProfitLossForEachReportableSegmentLineItems

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

	def getNotesSegmentInformationEtcQuarterlyFinancialStatementsHeading(self): #セグメント情報等、四半期財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcQuarterlyFinancialStatementsHeading

	def getNotesSegmentInformationEtcQuarterlyFinancialStatementsTable(self): #セグメント情報等、四半期財務諸表 [表]
		return self.NotesSegmentInformationEtcQuarterlyFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSegmentInformationEtcQuarterlyFinancialStatementsLineItems(self): #セグメント情報等、四半期財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcQuarterlyFinancialStatementsLineItems

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getFootnotesRegardingSegmentInformationTableTextBlock(self): #セグメント表の脚注 [テキストブロック]
		return self.FootnotesRegardingSegmentInformationTableTextBlock

	def getInformationAboutAssetsForEachReportableSegmentTextBlock(self): #報告セグメントごとの資産に関する情報 [テキストブロック]
		return self.InformationAboutAssetsForEachReportableSegmentTextBlock

	def getDescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock(self): #報告セグメントごとの利益又は損失の金額の合計額と四半期損益計算書計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
		return self.DescriptionOfNatureOfDifferencesBetweenProfitLossOfReportableSegmentsTotalAndQuarterlyFinancialStatementsTextBlock

	def getDisclosureOfChangesEtcInReportableSegmentsTextBlock(self): #報告セグメントの変更等に関する事項 [テキストブロック]
		return self.DisclosureOfChangesEtcInReportableSegmentsTextBlock

	def getInformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock(self): #報告セグメントごとの固定資産の減損損失又はのれん等に関する情報 [テキストブロック]
		return self.InformationAboutImpairmentLossOfNonCurrentAssetsOrGoodwillEtcForEachReportableSegmentTextBlock

	def getNotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedQuarterlyFinancialStatementsHeading(self): #持分法損益等、四半期財務諸表 [目次項目]
		return self.NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedQuarterlyFinancialStatementsHeading

	def getNotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedQuarterlyFinancialStatementsTextBlock(self): #持分法損益等、四半期財務諸表 [テキストブロック]
		return self.NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedQuarterlyFinancialStatementsTextBlock

	def getNotesPerShareInformationQuarterlyFinancialStatementsHeading(self): #１株当たり情報、四半期財務諸表 [目次項目]
		return self.NotesPerShareInformationQuarterlyFinancialStatementsHeading

	def getNotesPerShareInformationQuarterlyFinancialStatementsTextBlock(self): #１株当たり情報、四半期財務諸表 [テキストブロック]
		return self.NotesPerShareInformationQuarterlyFinancialStatementsTextBlock

	def getNotesSignificantEventsAfterReportingPeriodQuarterlyFinancialStatementsHeading(self): #重要な後発事象、四半期財務諸表 [目次項目]
		return self.NotesSignificantEventsAfterReportingPeriodQuarterlyFinancialStatementsHeading

	def getNotesSignificantEventsAfterReportingPeriodQuarterlyFinancialStatementsTextBlock(self): #重要な後発事象、四半期財務諸表 [テキストブロック]
		return self.NotesSignificantEventsAfterReportingPeriodQuarterlyFinancialStatementsTextBlock

	def getOtherInformationFinancialStatementsEtcHeading(self): #その他、財務諸表等 [目次項目]
		return self.OtherInformationFinancialStatementsEtcHeading

	def getOtherInformationFinancialStatementsEtcTextBlock(self): #その他、財務諸表等 [テキストブロック]
		return self.OtherInformationFinancialStatementsEtcTextBlock

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

	def getIndependentAuditorsReportHeading(self): #独立監査人の報告書 [目次項目]
		return self.IndependentAuditorsReportHeading

	def getIndependentAuditorsReportConsolidatedTextBlock(self): #独立監査人の報告書、連結 [テキストブロック]
		return self.IndependentAuditorsReportConsolidatedTextBlock

	def getAuditFirm1Consolidated(self): #監査法人１、連結
		return self.AuditFirm1Consolidated

	def getCPA1AuditFirm1Consolidated(self): #公認会計士１、監査法人１、連結
		return self.CPA1AuditFirm1Consolidated

	def getCPA2AuditFirm1Consolidated(self): #公認会計士２、監査法人１、連結
		return self.CPA2AuditFirm1Consolidated

	def getCPA3AuditFirm1Consolidated(self): #公認会計士３、監査法人１、連結
		return self.CPA3AuditFirm1Consolidated

	def getCPA4AuditFirm1Consolidated(self): #公認会計士４、監査法人１、連結
		return self.CPA4AuditFirm1Consolidated

	def getCPA5AuditFirm1Consolidated(self): #公認会計士５、監査法人１、連結
		return self.CPA5AuditFirm1Consolidated

	def getAuditFirm2Consolidated(self): #監査法人２、連結
		return self.AuditFirm2Consolidated

	def getCPA1AuditFirm2Consolidated(self): #公認会計士１、監査法人２、連結
		return self.CPA1AuditFirm2Consolidated

	def getCPA2AuditFirm2Consolidated(self): #公認会計士２、監査法人２、連結
		return self.CPA2AuditFirm2Consolidated

	def getKeyAuditMattersConsolidatedTextBlock(self): #監査上の主要な検討事項、連結 [テキストブロック]
		return self.KeyAuditMattersConsolidatedTextBlock

	def getOverviewKAMConsolidatedTextBlock(self): #全体概要、監査上の主要な検討事項、連結 [テキストブロック]
		return self.OverviewKAMConsolidatedTextBlock

	def getIndependentAuditorsReportNonConsolidatedTextBlock(self): #独立監査人の報告書、個別 [テキストブロック]
		return self.IndependentAuditorsReportNonConsolidatedTextBlock

	def getAuditFirm1NonConsolidated(self): #監査法人１、個別
		return self.AuditFirm1NonConsolidated

	def getCPA1AuditFirm1NonConsolidated(self): #公認会計士１、監査法人１、個別
		return self.CPA1AuditFirm1NonConsolidated

	def getCPA2AuditFirm1NonConsolidated(self): #公認会計士２、監査法人１、個別
		return self.CPA2AuditFirm1NonConsolidated

	def getCPA3AuditFirm1NonConsolidated(self): #公認会計士３、監査法人１、個別
		return self.CPA3AuditFirm1NonConsolidated

	def getCPA4AuditFirm1NonConsolidated(self): #公認会計士４、監査法人１、個別
		return self.CPA4AuditFirm1NonConsolidated

	def getCPA5AuditFirm1NonConsolidated(self): #公認会計士５、監査法人１、個別
		return self.CPA5AuditFirm1NonConsolidated

	def getAuditFirm2NonConsolidated(self): #監査法人２、個別
		return self.AuditFirm2NonConsolidated

	def getCPA1AuditFirm2NonConsolidated(self): #公認会計士１、監査法人２、個別
		return self.CPA1AuditFirm2NonConsolidated

	def getCPA2AuditFirm2NonConsolidated(self): #公認会計士２、監査法人２、個別
		return self.CPA2AuditFirm2NonConsolidated

	def getKeyAuditMattersNonConsolidatedTextBlock(self): #監査上の主要な検討事項、個別 [テキストブロック]
		return self.KeyAuditMattersNonConsolidatedTextBlock

	def getOverviewKAMNonConsolidatedTextBlock(self): #全体概要、監査上の主要な検討事項、個別 [テキストブロック]
		return self.OverviewKAMNonConsolidatedTextBlock
