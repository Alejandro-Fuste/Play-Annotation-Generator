# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_66`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_66/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 47 |
| Player Tracks | 47 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 74: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureCatch' for track '1' has invalid range: start=98, end=68. Clamping end to start.
> - Segment 'Action_BallCarry' for track '1' has invalid range: start=108, end=68. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '21' has invalid range: start=69, end=35. Clamping end to start.
> - Action 'Action_PreSnap' range [0-68] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-98] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-65] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-72] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-70] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-74] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [35-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [72-79] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-72] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [35-65] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-61] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-68] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-72] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [69-72] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-71] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-72] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-70] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-70] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-87] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-86] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-87] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-105] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-188] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-181] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-127] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-131] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-128] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-177] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-190] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-200] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-210] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-206] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-144] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-166] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-172] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-190] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-184] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-191] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-193] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-201] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-208] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '46' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.