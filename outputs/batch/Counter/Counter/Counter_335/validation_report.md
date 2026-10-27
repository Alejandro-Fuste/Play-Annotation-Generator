# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_335`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_335/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '3' (LT) duration 95 frames exceeds threshold 90 frames [start=31, end=125].
> - Validation warning: Action 'Action_PullBlock' for track '21' (C) duration 97 frames exceeds threshold 90 frames [start=31, end=127].
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [28–41], lower_priority='Action_PullBlock' annotated_start=31, effective_Action_PullBlock_start=42.
> - Action 'Action_None' range [28-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [31-63] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [66-67] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [83-103] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [105-125] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [28-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-137] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [31-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [89-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-137] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-148] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-166] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-156] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [158-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [31-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [112-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-180] for track '16' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [28-53] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-59] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-68] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-45] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [31-57] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [42-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-176] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-150] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-176] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-166] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '30' has 1 frames without a visible bounding box.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.