# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_240`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_240/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 480: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [15-132] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-171] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-51] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-27] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [44-52] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [61-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [103-163] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-72] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-75] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-95] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-132] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-180] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [18-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '11' starts at frame 74, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [74-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-92] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-73] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-180] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [15-88] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-57] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-91] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-94] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-152] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-164] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-98] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-172] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-174] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-160] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-179] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '29' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.