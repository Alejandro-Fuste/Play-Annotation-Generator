# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_332`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_332/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '15' has invalid range: start=99, end=95. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '16' has invalid range: start=121, end=40. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '16' has invalid range: start=121, end=47. Clamping end to start.
> - Segment 'Action_Keep' for track '16' has invalid range: start=121, end=66. Clamping end to start.
> - Segment 'Action_BallSnap' for track '19' has invalid range: start=152, end=40. Clamping end to start.
> - Action 'Action_None' range [28-178] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-188] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-105] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-162] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-229] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [28-146] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [28-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-94] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-99] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-146] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-169] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-192] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-205] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-122] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-99] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-118] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-224] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-234] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '22' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_332'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.