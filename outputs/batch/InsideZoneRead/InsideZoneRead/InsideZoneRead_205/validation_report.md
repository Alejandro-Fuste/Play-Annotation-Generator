# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_205`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_205/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 410: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '0' has invalid range: start=463, end=123. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '5' has invalid range: start=463, end=126. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '11' has invalid range: start=463, end=182. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '15' has invalid range: start=463, end=70. Clamping end to start.
> - Segment 'Action_BallSnap' for track '17' has invalid range: start=460, end=239. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '17' has invalid range: start=460, end=239. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '17' has invalid range: start=484, end=239. Clamping end to start.
> - Segment 'Action_BallCarry' for track '17' has invalid range: start=514, end=239. Clamping end to start.
> - Action 'Action_PreSnap' range [0-123] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-194] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-226] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-178] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-226] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-182] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-89] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-104] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-96] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-153] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-168] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-182] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-183] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-67] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-184] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-194] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-32] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-162] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-198] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-203] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-214] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-223] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-233] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-192] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-213] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-193] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-227] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '27' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Action event 'Action_BallSnap' has invalid start frame 460. Video range is [0, 239].
> - Action event 'Action_ZoneBlock' has invalid start frame 463. Video range is [0, 239].
> - Action event 'Action_ZoneBlock' has invalid start frame 463. Video range is [0, 239].
> - Action event 'Action_ZoneBlock' has invalid start frame 463. Video range is [0, 239].
> - Action event 'Action_ZoneBlock' has invalid start frame 463. Video range is [0, 239].
> - Action event 'Action_SnapReceive' has invalid start frame 479. Video range is [0, 239].
> - Action event 'Action_ReadDefender' has invalid start frame 484. Video range is [0, 239].
> - Action event 'Action_BallCarry' has invalid start frame 514. Video range is [0, 239].
> - Action event 'Action_None' has invalid start frame 543. Video range is [0, 239].
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_205'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.