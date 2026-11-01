# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_230`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_230/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_BallSnap' for track '6' has invalid range: start=110, end=4. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '6' has invalid range: start=113, end=4. Clamping end to start.
> - Segment 'Action_BallCarry' for track '9' has invalid range: start=156, end=150. Clamping end to start.
> - Segment 'Action_Handoff' for track '10' has invalid range: start=142, end=140. Clamping end to start.
> - Action 'Action_None' range [110-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-182] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-211] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-238] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-163] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-132] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-206] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-54] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-124] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-192] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-204] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [128-131] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [137-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-71] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-86] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-168] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-185] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-213] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-190] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-226] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-242] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-249] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-224] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-242] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [248-254] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-258] for track '27' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.