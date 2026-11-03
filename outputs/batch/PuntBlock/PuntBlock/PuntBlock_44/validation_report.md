# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_44`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 90: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [5-151] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-119] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-110] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-161] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [57-62] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [67-108] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [110-141] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [156-167] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [170-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-126] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-62] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-73] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-105] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-46] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-163] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-10] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-95] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-137] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-13] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-23] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-95] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-46] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-153] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-144] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-162] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [68-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-210] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-135] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-119] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-206] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-126] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-133] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-153] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-131] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-184] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-189] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '36' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.