# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_179`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_179/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 28 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 358: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 358: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '0' (RT) duration 98 frames exceeds threshold 90 frames [start=101, end=198].
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (RG) duration 98 frames exceeds threshold 90 frames [start=101, end=198].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 98 frames exceeds threshold 90 frames [start=101, end=198].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 98 frames exceeds threshold 90 frames [start=101, end=198].
> - Segment 'Action_SnapReceive' for track '18' has invalid range: start=198, end=112. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '18' has invalid range: start=198, end=133. Clamping end to start.
> - Segment 'Action_Handoff' for track '18' has invalid range: start=198, end=140. Clamping end to start.
> - Segment 'Action_BallSnap' for track '20' has invalid range: start=210, end=112. Clamping end to start.
> - Action 'Action_ZoneBlock' range [101-183] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-264] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-286] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-314] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-167] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [141-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-199] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-226] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-323] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-359] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-196] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-213] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-294] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-274] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-209] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-233] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-268] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-359] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-234] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-291] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-209] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-245] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-289] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-156] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-248] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-145] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-359] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-235] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-231] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-289] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-353] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-260] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-344] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-286] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '25' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_179'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.