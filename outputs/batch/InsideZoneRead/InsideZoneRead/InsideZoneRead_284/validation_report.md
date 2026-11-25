# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_284`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_284/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallSnap' for track '17' has invalid range: start=116, end=36. Clamping end to start.
> - Action 'Action_PreSnap' range [0-22] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-130] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-82] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-92] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-110] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-43] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-60] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-52] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-57] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-132] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-121] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [70-83] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-82] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-101] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-91] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-110] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-148] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-75] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [111-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-74] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-70] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-72] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-102] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-137] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 117, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [117-134] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-180] for track '21' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_284'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.