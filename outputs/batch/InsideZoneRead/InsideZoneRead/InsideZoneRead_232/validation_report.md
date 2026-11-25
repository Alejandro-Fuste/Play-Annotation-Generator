# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_232`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_232/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 25 |
| Ball Tracks | 1 |
| CSV events parsed | 20 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '6' has invalid range: start=141, end=137. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '8' has invalid range: start=141, end=66. Clamping end to start.
> - Segment 'Action_BlockSecondLevel' for track '8' has invalid range: start=159, end=66. Clamping end to start.
> - Segment 'Action_BallSnap' for track '9' has invalid range: start=138, end=75. Clamping end to start.
> - Action 'Action_ZoneBlock' range [141-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-84] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [174-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [138-144] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [155-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-183] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-172] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-170] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-177] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-206] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-174] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '25' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_232'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.