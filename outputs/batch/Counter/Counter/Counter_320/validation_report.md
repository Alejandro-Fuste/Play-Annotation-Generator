# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_320`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_320/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '7' (LG) duration 108 frames exceeds threshold 90 frames [start=81, end=188].
> - Validation warning: Action 'Action_DownBlock' for track '8' (LT) duration 108 frames exceeds threshold 90 frames [start=81, end=188].
> - Validation warning: Action 'Action_PullBlock' for track '9' (RG) duration 108 frames exceeds threshold 90 frames [start=81, end=188].
> - Validation warning: Action 'Action_DownBlock' for track '12' (C) duration 108 frames exceeds threshold 90 frames [start=81, end=188].
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [78–93], lower_priority='Action_DownBlock' annotated_start=81, effective_Action_DownBlock_start=94.
> - Action 'Action_PreSnap' range [0-97] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [137-138] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [140-148] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [152-156] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [159-299] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [78-188] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-199] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-220] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [81-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-88] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [81-112] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [114-119] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [152-174] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-206] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [81-138] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-252] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [94-125] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [78-153] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [78-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-218] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-299] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-208] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-99] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-146] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-224] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-256] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-171] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-251] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-262] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-282] for track '24' has 2 frames without a visible bounding box.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.