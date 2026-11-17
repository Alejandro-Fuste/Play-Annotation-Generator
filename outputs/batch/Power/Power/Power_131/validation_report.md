# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_131`
- **Input XML**: `outputs/batch/Power/Power/Power_131/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 264: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 264: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [15-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-221] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-234] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-269] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-100] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-157] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-250] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-104] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-165] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-169] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-225] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-230] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-259] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-226] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-232] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-248] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-253] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-264] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-169] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-140] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-148] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-220] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-254] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-264] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-148] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-242] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-258] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-264] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-226] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-230] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [71-87] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [94-98] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-88] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-194] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-203] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-176] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-226] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-231] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-151] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-194] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-201] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-218] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-238] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-251] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-267] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-194] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-203] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-215] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-236] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-262] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-215] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-213] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-225] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-259] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-251] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-257] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-265] for track '32' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.