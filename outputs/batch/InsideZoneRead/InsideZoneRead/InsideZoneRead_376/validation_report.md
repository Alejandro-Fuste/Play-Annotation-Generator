# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_376`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_376/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 19 |
| Ball Tracks | 1 |
| CSV events parsed | 19 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_SnapReceive' for track '17' has invalid range: start=128, end=38. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '17' has invalid range: start=128, end=48. Clamping end to start.
> - Segment 'Action_Keep' for track '17' has invalid range: start=128, end=62. Clamping end to start.
> - Segment 'Action_BallSnap' for track '18' has invalid range: start=131, end=38. Clamping end to start.
> - Action 'Action_None' range [80-92] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-60] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-76] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-70] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-150] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [25-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-46] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-64] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [70-72] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-90] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-48] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-56] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-77] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-150] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-87] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-34] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-81] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [128-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '18' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_376'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.