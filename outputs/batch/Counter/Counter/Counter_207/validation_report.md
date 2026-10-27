# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_207`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_207/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [17–29], lower_priority='Action_DownBlock' annotated_start=21, effective_Action_DownBlock_start=30.
> - Validation warning: Action 'Action_DownBlock' for track '12' (TE1) duration 97 frames exceeds threshold 90 frames [start=21, end=117].
> - Validation warning: Action 'Action_DownBlock' for track '17' (RG) duration 97 frames exceeds threshold 90 frames [start=21, end=117].
> - Validation warning: Action 'Action_PullBlock' for track '20' (LG) duration 97 frames exceeds threshold 90 frames [start=21, end=117].
> - Action 'Action_None' range [17-94] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-180] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-135] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-169] for track '4' has 8 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-43] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-55] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-76] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [30-72] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [21-34] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [58-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [21-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [21-102] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-50] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-82] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-97] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-161] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-151] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-180] for track '28' has 1 frames without a visible bounding box.
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