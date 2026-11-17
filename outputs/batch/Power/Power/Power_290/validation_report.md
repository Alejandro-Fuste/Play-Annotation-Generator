# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_290`
- **Input XML**: `outputs/batch/Power/Power/Power_290/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 31 |
| Ball Tracks | 1 |
| CSV events parsed | 12 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 580: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [0-316] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-376] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-252] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-325] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-276] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [217-228] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-139] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-287] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-290] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-261] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-323] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-389] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-246] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-262] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-286] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-301] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-242] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-329] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [217-269] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-278] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-353] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-270] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-276] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-15] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-267] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [217-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [231-235] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [240-258] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [262-266] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-288] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-369] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-380] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [217-244] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [248-254] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-245] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-380] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-375] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-304] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-298] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-302] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-309] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-378] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-385] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-303] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-330] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-309] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-366] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-372] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-386] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-343] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-389] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-341] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-350] for track '30' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.