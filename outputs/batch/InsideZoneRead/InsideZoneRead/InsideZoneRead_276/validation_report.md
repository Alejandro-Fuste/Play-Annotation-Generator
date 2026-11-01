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
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 101 frames exceeds threshold 90 frames [start=24, end=124].
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RG) duration 101 frames exceeds threshold 90 frames [start=24, end=124].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (LG) duration 101 frames exceeds threshold 90 frames [start=24, end=124].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 101 frames exceeds threshold 90 frames [start=24, end=124].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [21–34], lower_priority='Action_ZoneBlock' annotated_start=24, effective_Action_ZoneBlock_start=35.
> - Action 'Action_None' range [21-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-136] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-189] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-162] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-44] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-86] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-191] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-63] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-222] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-42] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [49-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-106] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-299] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-35] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-75] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [21-30] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-61] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-202] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-37] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-209] for track '22' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.