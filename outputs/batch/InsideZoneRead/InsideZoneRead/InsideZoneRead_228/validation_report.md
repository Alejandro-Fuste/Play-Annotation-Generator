# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_228`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_228/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallSnap' for track '19' has invalid range: start=137, end=105. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '22' has invalid range: start=165, end=105. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '22' has invalid range: start=165, end=121. Clamping end to start.
> - Segment 'Action_Handoff' for track '22' has invalid range: start=165, end=131. Clamping end to start.
> - Action 'Action_PreSnap' range [7-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-207] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-97] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-167] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-15] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-26] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-177] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-41] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-175] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-35] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [170-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [190-205] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-18] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-38] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-135] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-95] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-143] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [154-157] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-162] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-38] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [116-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [120-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 163, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [163-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-54] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '24' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_228'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.