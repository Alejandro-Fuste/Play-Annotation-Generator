# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_163`
- **Input XML**: `outputs/batch/Power/Power/Power_163/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 117 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 327: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [10-216] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-217] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-317] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-215] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-243] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-285] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-308] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-359] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-287] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-295] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-339] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-343] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-359] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-230] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-216] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-255] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-274] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-283] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-301] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-316] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-347] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-278] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-357] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [213-216] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [241-244] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [248-249] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [251-253] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [256-257] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [260-278] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 285, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [285-285] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-307] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-350] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-222] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-246] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-253] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-267] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-278] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-216] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-246] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-282] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-300] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-216] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-253] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-316] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-278] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-281] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-337] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-341] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-346] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-356] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [213-215] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [213-216] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-19] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-22] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-42] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-246] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-250] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-278] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-283] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-295] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-326] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-244] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-249] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-257] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-277] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-267] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-278] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-283] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-337] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-278] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-283] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-359] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-278] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-283] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-314] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-309] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-331] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-351] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-355] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-323] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-348] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-339] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-351] for track '37' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.