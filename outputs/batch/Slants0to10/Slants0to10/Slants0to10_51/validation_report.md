# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_51`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 52 |
| Player Tracks | 52 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 131 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 51: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-12] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-19] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-28] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-36] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-68] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-20] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-39] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-69] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-44] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-266] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-270] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-282] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-287] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-256] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-220] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-81] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-133] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-214] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-63] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-123] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-19] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-69] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-148] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [84-124] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [131-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [150-246] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [256-261] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [264-290] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-12] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [2-5] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-13] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-19] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [33-34] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-42] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-29] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-12] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-18] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-22] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-31] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-76] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-8] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-20] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-37] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-68] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-74] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-114] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-168] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-68] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-72] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-114] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-54] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-58] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-67] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-163] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-198] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-205] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-73] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-93] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-112] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-90] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-92] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-114] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-129] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-116] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-132] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-201] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-140] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-211] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-243] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-270] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-194] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-259] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-290] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-299] for track '50' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.