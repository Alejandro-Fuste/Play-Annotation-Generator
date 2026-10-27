# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_380`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_380/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 762: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 762: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-38] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-78] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [47-122] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-152] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-73] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-103] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-159] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [136-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [50-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [76-86] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-165] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-127] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-144] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [50-86] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [89-95] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [98-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [124-132] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-169] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-81] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-206] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-66] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-82] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [50-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [78-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-82] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-54] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-63] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-124] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-87] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-149] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-161] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-144] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-146] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-154] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-163] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '30' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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