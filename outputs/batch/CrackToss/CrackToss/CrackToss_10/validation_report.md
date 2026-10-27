# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_10`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_10/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 34 |
| Ball Tracks | 2 |
| CSV events parsed | 19 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 22: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '1' (LT) duration 105 frames exceeds threshold 90 frames [start=220, end=324].
> - Validation warning: Action 'Action_PullBlock' for track '5' (TE) duration 105 frames exceeds threshold 90 frames [start=220, end=324].
> - Action 'Action_None' range [217-300] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-322] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [329-333] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-383] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [220-305] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [255-272] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [274-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-246] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [220-324] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [220-271] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [277-324] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [325-335] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-287] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [289-346] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [348-389] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-259] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-306] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-312] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-316] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-264] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-292] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-317] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-283] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-337] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-267] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-287] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-294] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-259] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-279] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-318] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-226] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [227-254] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-272] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-277] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [220-268] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [274-282] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-99] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-216] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-287] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-216] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-276] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [286-306] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [308-319] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-353] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-311] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-389] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-389] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-351] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-389] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-376] for track '34' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.