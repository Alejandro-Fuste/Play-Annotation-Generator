# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_17`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 118 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 36: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_CrackBlock' range [174-189] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-331] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [334-335] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-359] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-188] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-218] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-189] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-221] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-189] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-200] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-188] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-201] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-219] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-253] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-213] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-359] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [171-283] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-189] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-188] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-277] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-291] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-359] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [207-217] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [220-299] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [306-319] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-300] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-308] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-322] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [174-189] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [214-256] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-316] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-188] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-288] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-297] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-359] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-213] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-235] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-319] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-331] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-359] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-246] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-284] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-256] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-293] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [251-263] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-359] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-258] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-272] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-346] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-359] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-280] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-327] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-359] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-337] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [350-354] for track '35' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.