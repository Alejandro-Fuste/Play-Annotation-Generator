# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_195`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_195/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 138 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 194 frames exceeds threshold 90 frames [start=291, end=484].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 130 frames exceeds threshold 90 frames [start=291, end=420].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [288–405], lower_priority='Action_ZoneBlock' annotated_start=291, effective_Action_ZoneBlock_start=406.
> - Segment 'Action_ZoneBlock' for track '18' has invalid range: start=291, end=149. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 194 frames exceeds threshold 90 frames [start=291, end=484].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 194 frames exceeds threshold 90 frames [start=291, end=484].
> - Action 'Action_None' range [288-411] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-469] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [471-622] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [624-625] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-462] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-465] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-488] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-493] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [495-586] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [291-416] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [421-462] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [469-471] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [473-478] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-569] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-412] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-430] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-608] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-460] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [303-453] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [456-476] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-629] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-456] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-538] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-621] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-593] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-498] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [504-513] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [406-408] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [411-420] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-418] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-476] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-417] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-422] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-462] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [465-586] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-37] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-188] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-413] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [417-446] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [453-458] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [462-474] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [476-480] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [482-601] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [291-478] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-562] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-286] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-629] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-151] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-165] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-218] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-264] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-288] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [306-313] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [315-349] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [351-352] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [354-358] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [360-361] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [379-380] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [382-387] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-566] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-424] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-549] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-556] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-411] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-488] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-533] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-542] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [545-577] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-465] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-503] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [505-515] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-526] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-457] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-473] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-486] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-492] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-504] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-513] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [531-533] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [470-471] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-478] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-482] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [479-482] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [488-588] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [498-507] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-511] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [515-516] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [518-563] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [507-509] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [512-555] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [563-588] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [518-558] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [563-570] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-577] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [595-596] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-542] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [544-545] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-545] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [561-588] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [594-596] for track '38' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.