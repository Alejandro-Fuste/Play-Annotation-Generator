# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_278`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_278/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '2' (C) duration 91 frames exceeds threshold 90 frames [start=52, end=142].
> - Validation warning: Action 'Action_DownBlock' for track '12' (LG) duration 91 frames exceeds threshold 90 frames [start=52, end=142].
> - Validation warning: Action 'Action_DownBlock' for track '13' (RG) duration 91 frames exceeds threshold 90 frames [start=52, end=142].
> - Action 'Action_None' range [49-103] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [52-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-127] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-90] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-221] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-173] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-115] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-93] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-217] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [52-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [91-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [134-138] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [52-119] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [129-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-216] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-138] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-154] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-170] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-224] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-82] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-239] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-219] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-238] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-197] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '28' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.