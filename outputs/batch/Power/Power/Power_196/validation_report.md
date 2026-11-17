# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_196`
- **Input XML**: `outputs/batch/Power/Power/Power_196/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 38 |
| Ball Tracks | 1 |
| CSV events parsed | 10 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 394: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [20-43] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-226] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-318] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-350] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-218] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-267] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-274] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-224] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-300] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-342] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-355] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-238] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-247] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-226] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-42] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [182-218] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [226-251] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [182-254] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-209] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-225] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-231] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-260] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-200] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-259] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-275] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-291] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-138] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-252] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-256] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-254] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [182-262] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [182-194] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-24] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-250] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-324] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-336] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-188] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-229] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-240] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-178] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-184] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-231] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-260] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-389] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-256] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-298] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-275] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-287] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-314] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-319] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-362] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-384] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-347] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-350] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-386] for track '38' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.