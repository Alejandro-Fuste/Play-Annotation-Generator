# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_114`
- **Input XML**: `outputs/batch/Power/Power/Power_114/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_DownBlock' for track '11' has invalid range: start=199, end=56. Clamping end to start.
> - Action 'Action_PreSnap' range [22-236] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-246] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-359] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-219] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-258] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-256] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-206] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-274] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-214] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-313] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-214] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-258] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-307] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [199-241] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-305] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-348] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-101] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-142] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-359] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-198] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [199-203] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [212-217] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [230-238] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-280] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-359] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-200] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-212] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-286] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-221] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-349] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-221] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-300] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-312] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-331] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-259] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-246] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-250] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-292] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-305] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-352] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-359] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-287] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-290] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-292] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-315] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-320] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-327] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-332] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-340] for track '33' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.