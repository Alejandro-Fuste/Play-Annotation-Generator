# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_225`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_225/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 121 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '3' (LT) duration 92 frames exceeds threshold 90 frames [start=74, end=165].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [72–87], lower_priority='Action_DownBlock' annotated_start=74, effective_Action_DownBlock_start=88.
> - Validation warning: Action 'Action_DownBlock' for track '18' (LG) duration 92 frames exceeds threshold 90 frames [start=74, end=165].
> - Validation warning: Action 'Action_PullBlock' for track '21' (RG) duration 92 frames exceeds threshold 90 frames [start=74, end=165].
> - Action 'Action_None' range [72-317] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-300] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [74-104] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [112-114] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [116-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-315] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [74-152] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-185] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-204] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [126-272] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [275-302] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [304-305] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-329] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [72-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-256] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [258-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [88-92] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [95-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [101-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [104-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [108-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-112] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-139] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-93] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [74-91] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [96-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [104-145] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [152-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-329] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-141] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-329] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [74-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [129-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [137-165] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-124] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-188] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-329] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-252] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-277] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [288-299] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-315] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-294] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-274] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-284] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-274] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-284] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-274] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-306] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [288-292] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-326] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.