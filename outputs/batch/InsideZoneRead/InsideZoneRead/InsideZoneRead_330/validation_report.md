# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_330`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_330/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_SnapReceive' for track '17' has invalid range: start=70, end=37. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '17' has invalid range: start=70, end=52. Clamping end to start.
> - Segment 'Action_Keep' for track '17' has invalid range: start=70, end=65. Clamping end to start.
> - Segment 'Action_BallSnap' for track '19' has invalid range: start=92, end=37. Clamping end to start.
> - Action 'Action_None' range [24-180] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [24-42] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-78] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-82] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-55] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-68] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-74] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-70] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-38] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-71] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-72] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-54] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-66] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-66] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [24-62] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-68] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [70-87] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-158] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-179] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '25' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_330'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.