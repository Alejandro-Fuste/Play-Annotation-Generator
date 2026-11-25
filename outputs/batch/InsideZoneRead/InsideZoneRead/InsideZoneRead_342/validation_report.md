# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_342`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_342/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_SnapReceive' for track '14' has invalid range: start=27, end=20. Clamping end to start.
> - Segment 'Action_BallSnap' for track '20' has invalid range: start=135, end=20. Clamping end to start.
> - Action 'Action_None' range [6-86] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-93] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [9-86] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-198] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-66] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-88] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [9-44] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-163] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [9-80] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [9-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-98] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 28, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [28-28] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [29-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [33-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [50-55] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [64-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-55] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-85] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [82-172] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [110-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-146] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-152] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-203] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-208] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-198] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '31' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_342'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.