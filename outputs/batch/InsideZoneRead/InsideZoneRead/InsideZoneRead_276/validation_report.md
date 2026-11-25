# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_276`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_276/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_SnapReceive' for track '22' has invalid range: start=130, end=24. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '22' has invalid range: start=130, end=34. Clamping end to start.
> - Segment 'Action_Keep' for track '22' has invalid range: start=130, end=60. Clamping end to start.
> - Action 'Action_None' range [9-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-136] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-189] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-162] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [12-44] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-86] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-191] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [12-63] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-222] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-67] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [12-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-106] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-299] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-35] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-75] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [12-30] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-61] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-96] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-202] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-37] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-209] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-190] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-200] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-262] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-282] for track '31' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_276'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.