# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_48`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_48/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 30 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 76: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [65-105] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-204] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-101] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-137] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-148] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [72-193] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [72-201] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-133] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [72-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [93-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BootAway' range [126-129] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-56] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [68-80] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 84, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [84-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-135] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-200] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-236] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-234] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-224] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-234] for track '29' has 1 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.