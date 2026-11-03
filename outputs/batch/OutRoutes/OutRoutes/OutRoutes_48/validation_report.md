# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_48`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_48/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 56 |
| Player Tracks | 56 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 117 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 56: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 56: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureCatch' for track '2' has invalid range: start=150, end=122. Clamping end to start.
> - Segment 'Action_BallCarry' for track '2' has invalid range: start=161, end=122. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '18' has invalid range: start=117, end=91. Clamping end to start.
> - Action 'Action_PreSnap' range [0-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [74-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-71] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-75] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-77] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-88] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-222] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-26] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-63] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-71] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-91] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-63] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-75] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-67] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-87] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-66] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-136] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-202] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-222] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-103] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-186] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-86] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-163] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-215] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-84] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-93] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-158] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-90] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-98] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-91] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-179] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-126] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-139] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-169] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-136] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-163] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-171] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-177] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-197] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-208] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-213] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-161] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-169] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-226] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-222] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-186] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-219] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-188] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-196] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-230] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-236] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-174] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-175] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-171] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-190] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-201] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-188] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-222] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-185] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-204] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-228] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-192] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-228] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-230] for track '51' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-195] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-239] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-201] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-236] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '55' has 1 frames without a visible bounding box.
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
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.