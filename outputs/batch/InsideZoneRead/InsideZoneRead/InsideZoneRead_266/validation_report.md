# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_266`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_266/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallSnap' for track '16' has invalid range: start=93, end=30. Clamping end to start.
> - Action 'Action_None' range [97-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-94] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-25] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-63] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-64] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-172] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-95] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-110] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-110] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-116] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-193] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-210] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [16-52] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-87] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-152] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-172] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-156] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-172] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [57-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [77-116] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [123-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [175-179] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-175] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-55] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-210] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [94-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-185] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-192] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-191] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_266'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.