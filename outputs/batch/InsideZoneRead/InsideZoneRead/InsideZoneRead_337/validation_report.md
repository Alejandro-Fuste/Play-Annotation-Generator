# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_337`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_337/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [21–33], lower_priority='Action_ZoneBlock' annotated_start=24, effective_Action_ZoneBlock_start=34.
> - Action 'Action_None' range [21-65] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-182] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-65] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-73] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-78] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-91] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-71] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-44] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-49] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-210] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [69-163] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [165-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-65] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-65] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-65] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-65] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-78] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-113] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-126] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-68] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-199] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-185] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-41] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-94] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-187] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-167] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-182] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-142] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.