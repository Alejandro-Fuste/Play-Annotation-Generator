# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_211`
- **Input XML**: `outputs/batch/Power/Power/Power_211/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 424: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [7-233] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-299] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-275] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-319] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-15] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-235] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-279] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-320] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-323] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-342] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-218] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-257] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-225] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-288] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-221] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-221] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-307] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-263] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-273] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [195-200] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [220-258] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [263-267] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-280] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-288] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-293] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-291] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-359] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-47] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-214] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-66] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-70] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-193] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-253] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-260] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-339] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-297] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-303] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-319] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-288] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-359] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-276] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-278] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-282] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-288] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-292] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-310] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-317] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-359] for track '30' has 3 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.