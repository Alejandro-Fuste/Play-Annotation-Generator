# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_30`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_30/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [10-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-93] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-98] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-128] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-132] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-144] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [96-98] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [109-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-55] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-79] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-58] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-95] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-126] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [40-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-48] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-36] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-41] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-81] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-130] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-79] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-90] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [56-66] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-68] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-75] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-92] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-109] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-86] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-75] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-128] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-148] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-132] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-150] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-150] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-138] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-143] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '37' has 1 frames without a visible bounding box.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.